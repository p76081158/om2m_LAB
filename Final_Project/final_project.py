import sys
import os
import psutil
import threading
import numpy as np
import scipy.stats
from numpy.random import uniform,randn,random
import matplotlib.pyplot as plt
import statsmodels.api as sm
import requests
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread
from final_gui import *

def create_uniform_particles(x_range, y_range, hdg_range, N):
    particles = np.empty((N, 3))
    particles[:, 0] = uniform(x_range[0], x_range[1], size=N)
    particles[:, 1] = uniform(y_range[0], y_range[1], size=N)
    particles[:, 2] = int(uniform(hdg_range[0],hdg_range[1]))
    return particles

    
def predict(particles, dist):
    """ move according to control input u (heading change, velocity)
    with noise Q (std heading change, std velocity)"""
    
    # move in the (noisy) commanded direction
    particles[:, 0] += np.random.uniform(-1, 1) * dist
    particles[:, 1] += np.random.uniform(-1, 1) * dist

        
    
def update(particles, weights, z, R, landmarks):
    weights.fill(1.)
    for i, landmark in enumerate(landmarks):
        distance = np.linalg.norm(particles[:, 0:2] - landmark, axis=1)
        weights *= scipy.stats.norm(distance, R).pdf(z[i])

    weights += 1.e-300      # avoid round-off to zero
    #print(weights)
    weights /= sum(weights) # normalize    
    
    
def estimate(particles, weights, l):
    """returns mean and variance of the weighted particles"""

    pos = particles[:, 0:2]
    mean = np.average(pos, weights=weights, axis=0)
    var  = np.average((pos - mean)**2, weights=weights, axis=0)
    N = len(particles)
    

    m = float('inf')
    state = 0;
    for i, p in enumerate(l):
        #print(n)
        #print(particles[n:, 0:2])
        dist = np.linalg.norm(mean - p)
        #print(i)
        #print("test")
        #print(dist)
        if (dist<m):
            m = dist
            state = i
    
    return mean, var, state
    
    
def neff(weights):
    return 1. / np.sum(np.square(weights))    
    
    
def simple_resample(particles, weights):
    N = len(particles)
    cumulative_sum = np.cumsum(weights)
    cumulative_sum[-1] = 1. # avoid round-off error
    indexes = np.searchsorted(cumulative_sum, random(N))

    # resample according to indexes
    particles[:] = particles[indexes]
    weights[:] = weights[indexes]
    weights /= np.sum(weights) # normalize    
    #print(weights)

def kde(situation, axis):
    r = requests.post(url = "http://140.116.247.67:1880/getvalue" + axis, data = {'situation' : situation})
    data = np.fromstring(r.text, dtype=float, sep=',')

    #print(np.average(data))
    kde = sm.nonparametric.KDEUnivariate(data)

    # Fit the model (estimate densities)
    kde.fit(kernel='gau', fft=False, gridsize=2**10)
    
    maxV = 0
    vl = 0
    for k in kde.support:
        i = kde.evaluate(k)
        if (i>maxV):
            maxV = i
            vl = k
    #print(vl)
    return vl;



class mainWin(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(mainWin, self).__init__(parent)
        self.setupUi(self)
        self.button_start.clicked.connect(self.OK)
        self.button_stop.clicked.connect(self.cancel)
        
    def run_pf(self, stop_event):    
        N=5000
        iters=18
        sensor_std_err=0.1
        r = requests.get(url = "http://140.116.247.67:1880/getSituation")
        situation = r.text.split(',')
        s_size = len(situation);
        landmarks = np.zeros((len(situation), 2))
        for i, s in enumerate(situation):
            #landmarks.
            landmarks[i][0] = kde(s,'X')
            landmarks[i][1] = kde(s,'Y')
            #print(s)
            #print(kde(s,'X'))
            #print(kde(s,'Y'))
        print(situation)
        print(landmarks)
        NL = len(landmarks)
        #self.c_value.setText("123")
        # create particles and weights
        particles = create_uniform_particles((-16,16), (-16,16), (0, s_size), N)
        weights = np.zeros(N)

        xs = []   # estimated values
        robot_pos = np.array([0., 0.])

        while(True):
            current_value = requests.get(url = "http://140.116.247.67:1880/getcurrentValue")
            x = float(current_value.text.split(',')[0])
            y = float(current_value.text.split(',')[1])
            robot_pos = (x,y)

            print(robot_pos)
            #self.c_value.setText("123")
            self.c_value.setText("(" + str(robot_pos[0]) + ", " + str(robot_pos[1]) + ")")

            particles = create_uniform_particles((-16,16), (-16,16), (0, s_size), N)
            weights = np.zeros(N)
            
            # distance from robot to each landmark >>> 取server中的pdf
            zs = np.linalg.norm(landmarks - robot_pos, axis=1) + (randn(NL) * sensor_std_err)

            # move particles forward to (+-dist)
            predict(particles, dist=0.2)

            # incorporate measurements
            update(particles, weights, z=zs, R=sensor_std_err, landmarks=landmarks)

            # resample if too few effective particles
            if neff(weights) < N/2:
                simple_resample(particles, weights)

            # Computing the State Estimate
            mu, var, pstate = estimate(particles, weights, l=landmarks)
            #xs.append(mu)

            #xs = np.array(xs)

            #print ('estimated position and variance:\n\t', mu, var)
            self.e_value.setText("(" + str(round(mu[0],3)) + ", " + str(round(mu[1],3)) + ")")
            #print(situation[pstate])
            self.c_situation.setText(situation[pstate])
            #print("")
            time.sleep(1)
            #QThread.sleep(1)

    def OK(self):
        self.stop_event=threading.Event()
        self.c_thread=threading.Thread(target=self.run_pf, args=(self.stop_event,))
        self.c_thread.start()
    
    def cancel(self):
        self.stop_event.set()
        self.close()
    
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = mainWin()
    main_win.show()
    app.exec_()

    
def kill_proc_tree(pid, including_parent=True):    
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()

me = os.getpid()
kill_proc_tree(me)
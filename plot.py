import matplotlib.pyplot as plt
import time

in_rate = [1, 2, 3, 4]
out_rate = [4, 3, 2, 1]

def plot():

    while(True):
        plt.subplot(2, 1, 1)
        plt.plot(in_rate)
        plt.title('in rate and out rate')
        plt.ylabel('in rate')

        plt.subplot(2, 1, 2)
        plt.plot(out_rate)
        plt.xlabel('time (s)')
        plt.ylabel('out rate')

        plt.draw()
        plt.pause(0.001)
        plt.clf()

        in_rate.append(1)

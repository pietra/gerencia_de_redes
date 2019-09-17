import matplotlib.pyplot as plt
import time

def plot_rate(rate_in, rate_out):

    plt.subplot(2, 1, 1)
    plt.plot(rate_in)
    plt.title('in rate and out rate')
    plt.ylabel('in rate')

    plt.subplot(2, 1, 2)
    plt.plot(rate_out)
    plt.xlabel('time (s)')
    plt.ylabel('out rate')

    plt.draw()
    plt.pause(0.001)
    plt.clf()

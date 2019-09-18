import matplotlib.pyplot as plt
import time

def plot_rate(rate_in, rate_out, err_rate_in, err_rate_out):

    plt.subplot(2, 2, 1)
    plt.plot(rate_in)
    plt.title('In and Out Traffic')
    plt.ylabel('Download (Mbps)')

    plt.subplot(2, 2, 3)
    plt.plot(rate_out)
    plt.xlabel('Time (s)')
    plt.ylabel('Upload (Mbps)')

    plt.subplot(2, 2, 2)
    plt.plot(err_rate_in)
    plt.title('Errors')
    plt.ylabel('In Packets with Error')

    plt.subplot(2, 2, 4)
    plt.plot(err_rate_out)
    plt.xlabel('time (s)')
    plt.ylabel('Out Packets with Error')

    plt.draw()
    plt.pause(0.001)
    plt.clf()

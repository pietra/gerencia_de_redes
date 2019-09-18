import matplotlib.pyplot as plt
import time

def plot_rate(times, rate_in, rate_out, err_rate_in, err_rate_out,
                multicast, unicast):

    plt.subplot(2, 3, 1)
    plt.plot(times, rate_in)
    plt.title('In and Out Traffic')
    plt.ylabel('Download (Mbps)')

    plt.subplot(2, 3, 4)
    plt.plot(times, rate_out)
    plt.xlabel('Time (s)')
    plt.ylabel('Upload (Mbps)')

    plt.subplot(2, 3, 2)
    plt.plot(times, err_rate_in)
    plt.title('Errors')
    plt.ylabel('In Packets with Error')

    plt.subplot(2, 3, 5)
    plt.plot(times, err_rate_out)
    plt.xlabel('time (s)')
    plt.ylabel('Out Packets with Error')

    plt.subplot(2, 3, 3)
    plt.plot(times, unicast)
    plt.title('Unicast/Multicast')
    plt.ylabel('Unicast Packets %')

    plt.subplot(2, 3, 6)
    plt.plot(times, multicast)
    plt.ylabel('Multicast Packets %')
    plt.xlabel('time (s)')

    plt.subplots_adjust(wspace=0.3)
    plt.draw()
    plt.pause(0.001)
    plt.clf()

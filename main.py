import time

from interface import interface
from rates import in_out_rates, in_out_error_rates, multicast_unicast_rates
from plot import plot_rate

class Agente:
    def __init__(self):
        self.ip = None
        self.usuario = None
        self.senha = None
        self.rate_in = []
        self.rate_out = []
        self.error_rate_in = []
        self.error_rate_out = []
        self.multicast = []
        self.unicast = []
        self.session = None

def main():
    agente = Agente()
    interface(agente)

    in_out_rates(agente)
    in_out_error_rates(agente)

    times = []
    start_time = time.time()
    while(True):
        rate_in, rate_out = in_out_rates(agente)
        err_rate_in, err_rate_out = in_out_error_rates(agente)
        m_cast, u_cast = multicast_unicast_rates(agente)

        times.append(time.time() - start_time)

        agente.rate_in.append(rate_in)
        agente.rate_out.append(rate_out)

        agente.error_rate_in.append(err_rate_in)
        agente.error_rate_out.append(err_rate_out)

        agente.multicast.append(m_cast)
        agente.unicast.append(u_cast)

        plot_rate(times, agente.rate_in, agente.rate_out,
                  agente.error_rate_in, agente.error_rate_out,
                  agente.multicast, agente.unicast
                  )

        time.sleep(5)

if __name__ == "__main__":
    main()

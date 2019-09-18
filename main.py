import time

from interface import interface
from rates import in_out_rates, in_out_error_rates
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
        self.session = None

def main():
    agente = Agente()
    interface(agente)

    in_out_rates(agente)
    in_out_error_rates(agente)

    while(True):
        rate_in, rate_out = in_out_rates(agente)
        err_rate_in, err_rate_out = in_out_error_rates(agente)

        agente.rate_in.append(rate_in)
        agente.rate_out.append(rate_out)

        agente.error_rate_in.append(err_rate_in)
        agente.error_rate_out.append(err_rate_out)

        plot_rate(agente.rate_in, agente.rate_out,
                  agente.error_rate_in, agente.error_rate_out)

        time.sleep(5)

if __name__ == "__main__":
    main()

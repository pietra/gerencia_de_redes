import time

from interface import interface
from rates import in_out_rates
from plot import plot_rate

class Agente:
    def __init__(self):
        self.ip = None
        self.usuario = None
        self.senha = None
        self.rate_in = []
        self.rate_out = []

def main():
    agente = Agente()
    interface(agente)


    while(True):
        rate_in, rate_out = in_out_rates(agente)

        agente.rate_in.append(rate_in)
        agente.rate_out.append(rate_out)

        plot_rate(agente.rate_in, agente.rate_out)

        time.sleep(1)

if __name__ == "__main__":
    main()

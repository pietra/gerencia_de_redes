from dataclasses import dataclass

from interface import interface
from plot import plot

@dataclass
class Agente:
    ip: str = None
    usuario: str = None
    senha: str = None

def main():
    agente = Agente()
    interface(agente)
    plot()

if __name__ == "__main__":
    main()
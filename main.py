from dataclasses import dataclass

from interface import interface

@dataclass
class Agente:
    ip: str = None
    usuario: str = None
    senha: str = None

def main():
    agente = Agente()
    interface(agente)
    print(agente)

if __name__ == "__main__":
    main()
import time
import sys

from easysnmp import Session, snmp_walk


class Agente:
    def __init__(self, ip):
        self.session = None
        self.ip = ip
        self.autenticacao = "SHA"
        self.criptografia = "AES"


MIB = 'sysUpTime'


def main():
    agente = Agente(sys.argv[1])
    agente.session = Session(hostname=agente.ip, community='public', version=2)

    while(True):
        result = agente.session.walk(MIB)
        print("----------------")
        print("MIB: ", result)
        print("----------------")
        time.sleep(5)


if __name__ == "__main__":
    main()

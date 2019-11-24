import time
import sys

from easysnmp import Session, snmp_walk


class Agente:
    def __init__(self, ip):
        self.session = None
        self.ip = ip
        self.autenticacao = "SHA"
        self.criptografia = "AES"


MIB = 'ifInOctets'


def main():
    agente = Agente(sys.argv[1])
    agente.session = Session(hostname=agente.ip, community='public', version=2,
                            security_level='auth_with_privacy',
                            privacy_protocol=agente.criptografia,
                            auth_protocol=agente.autenticacao)

    while(True):
        result = snmp_walk(MIB, hostname=agente.ip, community='public', version=3)
        print("----------------")
        print("MIB: ", result)
        print("----------------")
        time.sleep(5)


if __name__ == "__main__":
    main()

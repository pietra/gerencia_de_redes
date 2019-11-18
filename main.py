import time
from easysnmp import Session, snmp_walk


class Agente:
    def __init__(self):
        self.session = None

        self.ip = ""
        self.usuario = ""
        self.senha = ""

        self.autenticacao = "SHA"
        self.criptografia = "AES"


MIB = 'ifInOctets'


def main():
    agente = Agente()
    agente.session = Session(hostname=agente.ip, community='public', version=3,
                             security_level='auth_with_privacy',
                             security_username=agente.usuario,
                             privacy_protocol=agente.criptografia,
                             privacy_password=agente.senha,
                             auth_protocol=agente.autenticacao,
                             auth_password=agente.senha)

    while(True):
        snmp_walk(MIB, hostname=agente.ip, community='public', version=3)
        time.sleep(5)


if __name__ == "__main__":
    main()

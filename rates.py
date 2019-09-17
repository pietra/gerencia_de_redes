from easysnmp import Session, snmp_walk
import time

TIME_SLEEPING = 5

def values_of_list(list):
    values = []    
    for item in list:
        values.append(item.value)
    return values

# [1], pois fizemos apenas para a interface onde havia trafego.
def to_float(octets):
    return float(octets[1].encode('utf-8'))

def get_snap_walk(mib, agente):
    session = Session(hostname=agente.ip, community='public', version=3,
                security_level='auth_with_privacy',
                security_username=agente.usuario,
                privacy_protocol='DES',
                privacy_password=agente.senha,
                auth_protocol='MD5',
                auth_password=agente.senha)

    return values_of_list(session.walk(mib))


def in_out_rates(agente):
    if_in_octets = get_snap_walk('ifInOctets', agente)
    if_out_octets = get_snap_walk('ifOutOctets', agente)

    rate_in = to_float(if_in_octets)
    rate_out = to_float(if_out_octets)

    return rate_in, rate_out

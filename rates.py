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

def get_snap_walk(mib, ip):
    return values_of_list(snmp_walk(mib, hostname=ip, community='public', version=2))


def in_out_rates(agente):
    if_in_octets = get_snap_walk('ifInOctets', agente.ip)
    if_out_octets = get_snap_walk('ifOutOctets', agente.ip)

    rate_in = to_float(if_in_octets)
    rate_out = to_float(if_out_octets)

    return rate_in, rate_out

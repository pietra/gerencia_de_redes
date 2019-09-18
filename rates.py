from easysnmp import Session, snmp_walk
import time

TIME_SLEEPING = 5

in_err = 0
out_err = 0

in_total = 0
out_total = 0
last_time = time.time()

m_in_total = 0
m_out_total = 0
u_in_total = 0
u_out_total = 0

def values_of_list(list):
    values = []
    for item in list:
        values.append(item.value)
    return values

# [1], pois fizemos apenas para a interface onde havia trafego.
def to_float(octets):
    return to_float_sum(octets)

def to_float_sum(octets):
    result = 0

    #print("READ:")
    for i in range(len(octets)):
        #print(" - {}".format(octets[i]))
        result += float(octets[i])

    return result

def get_snap_walk(mib, agente):
    return values_of_list(agente.session.walk(mib))


def in_out_error_rates(agente):
    global in_err
    global out_err

    if_in_err_octets = get_snap_walk('ifInErrors', agente)
    if_out_err_octets = get_snap_walk('ifOutErrors', agente)

    rate_in = to_float_sum(if_in_err_octets)
    rate_out = to_float_sum(if_out_err_octets)

    err_rate_in = rate_in - in_err
    err_rate_out = rate_out - out_err

    in_err = rate_in
    out_err = rate_out
    return int(err_rate_in), int(err_rate_out)

def multicast_unicast_rates(agente):
    global m_in_total
    global m_out_total
    global u_in_total
    global u_out_total

    m_in = to_float(get_snap_walk('ifInNUcastPkts', agente))
    m_out = to_float(get_snap_walk('ifOutNUcastPkts', agente))
    u_in = to_float(get_snap_walk('ifInUcastPkts', agente))
    u_out = to_float(get_snap_walk('ifOutUcastPkts', agente))

    delta_m_in = m_in - m_in_total
    delta_m_out = m_out - m_out_total
    delta_u_in = u_in - u_in_total
    delta_u_out = u_out - u_out_total

    m_in_total = m_in
    m_out_total = m_out
    u_in_total = u_in
    u_out_total = u_out

    m = delta_m_in + delta_m_out
    u = delta_u_in + delta_u_out

    return (m * 100) / (m + u), (u * 100) / (m + u)

def in_out_rates(agente):
    global in_total
    global out_total
    global last_time

    if_in_octets = get_snap_walk('ifInOctets', agente)
    if_out_octets = get_snap_walk('ifOutOctets', agente)

    ctime = time.time()
    deltaTime = (ctime - last_time)
    last_time = ctime

    rate_in = to_float(if_in_octets)
    rate_out = to_float(if_out_octets)

    delta_in = rate_in - in_total
    delta_out = rate_out - out_total

    in_total = rate_in
    out_total = rate_out

    return (delta_in * 8) / (1024 * 1024 * deltaTime), (delta_out * 8) / (1024 * 1024 * deltaTime)

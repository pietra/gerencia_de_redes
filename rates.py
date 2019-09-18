from easysnmp import Session, snmp_walk
import time

TIME_SLEEPING = 5

in_err = 0
out_err = 0

in_total = 0
out_total = 0
last_time = time.time()

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

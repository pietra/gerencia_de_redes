from ErrorRateCalculator import *
from easysnmp import Session
from codecs import *
import time

#
# Author: Lucas Hagen 00274698
#

session = Session(hostname='192.168.0.21', community='public', version=3,
                security_level='auth_with_privacy',
                security_username='gerencia',
                privacy_protocol='DES',
                privacy_password='snmpehvida',
                auth_protocol='MD5',
                auth_password='snmpehvida')

print("==== {} ====".format(session.hostname))
print("")

interfaces = session.walk('ifPhysAddress')
errorRates = ErrorRateCalculator(session, 20)

errorRates.UpdateData()
time.sleep(3)

while True:

    errorRates.UpdateData()
    rate = errorRates.GetErrorPercentage()

    print("Interfaces:")
    for i in range(len(interfaces)):
        bmac = interfaces[i].value
        mac = ""
        if len(bmac) == 0:
            mac = "<<UNKNOWN>>"
        else:
            for c in bmac:
                if len(mac) > 0:
                    mac += ":"
                mac += "{:02x}".format(ord(c))

        print("    {}. {}:".format(i, mac))
        print("        - In Error Rate: {0:.2f} %".format(rate[i][0]))
        print("        - Out Error Rate: {0:.2f} %".format(rate[i][1]))

    time.sleep(3)


print("")
space = ""
for i in range(len(session.hostname)):
    space += "="
print("====={}=====".format(space))


















#

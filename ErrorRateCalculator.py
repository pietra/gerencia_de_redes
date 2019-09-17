from easysnmp import Session
import datetime

#
# Author: Lucas Hagen 00274698
#

def millis():
    return datetime.datetime.now()

class InterfaceData:

    def __init__(self, time, inTotal, outTotal, inError, outError):
        self.time = time
        self.inTotal = inTotal
        self.outTotal = outTotal
        self.inError = inError
        self.outError = outError

class ErrorRateCalculator:

    def __init__(self, session, maxCount=10):
        self.session = session
        self.queue = []
        self.maxCount = maxCount
        self.interfaces = 0

    def UpdateData(self):
        data = []
        time = millis()

        inCount = self.session.walk('ifInOctets')
        inError = self.session.walk('ifInErrors')
        outCount = self.session.walk('ifOutOctets')
        outError = self.session.walk('ifOutErrors')

        self.interfaces = len(inCount)

        for i in range(self.interfaces):
            data.append(InterfaceData(
                time,
                float(inCount[i].value),
                float(outCount[i].value),
                float(inError[i].value),
                float(outError[i].value)
            ))

        if len(self.queue) > self.maxCount:
            self.queue.pop(0)

        self.queue.append(data)

    def GetErrorPercentage(self):
        result = []

        for i in range(self.interfaces):
            a = self.queue[0][i]
            b = self.queue[len(self.queue) - 1][i]

            timeDelta = b.time - a.time
            inErrorRate = ((b.inError - a.inError) / max(b.inTotal - a.inTotal, 1)) * 100
            outErrorRate = ((b.outError - a.outError) / max(b.outTotal - a.outTotal, 1)) * 100
            result.append((inErrorRate, outErrorRate))

        return result

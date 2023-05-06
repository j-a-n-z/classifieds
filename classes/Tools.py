from datetime import datetime

class Tools:

    def generateId(self):
        dt = datetime.now()
        ts = datetime.timestamp(dt)

        return int(ts * 1000000)

from datetime import datetime

class Tools:

    @staticmethod
    def generateId():
        dt = datetime.now()
        ts = datetime.timestamp(dt)

        return int(ts * 1000000)

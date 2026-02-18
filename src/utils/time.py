import os
import time

class Time:

    # privates
    __startup_time = time.time()

    # publics
    deltaTime = 0


    def time_since_startup() -> float:
        return time.time() - Time.__startup_time

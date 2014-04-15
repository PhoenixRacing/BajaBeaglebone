
import IMU.lsm303
from termcolor import colored
from time import sleep
from Sensor import *


class Compass(Sensor):

        def __init__(self, name, delay=.05):
                super(self.__class__, self).__init__([],1, name)
                self.delay = delay
                self.bus = IMU.lsm303.setup_bus(1)                                      # bus: 3 indicates /dev/i2c-3
                self.Sm = IMU.lsm303.setup_mag(self.bus,IMU.lsm303.SCALE_M_81G)
               
        def run(self):
                while True:
                        m = IMU.lsm303.get_mag(self.bus,self.Sm)
                        
                        val = (m[0],m[1],m[2])
                        self.setSensorVal(str(val))
                        sleep(self.delay)
                        self.publish()


if __name__ == "__main__":
        C = Compass('Compass',.05)
        C.run()

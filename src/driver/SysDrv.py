#-*- coding:UTF-8 -*-

import ComDrv

class GPIO(ComDrv.ComDrv):
    def __init__(self, superUnit, name, pin):
        super().__init__(superUnit, name, "GPIO")
        self.HIGH = 1
        self.LOW = 0
        pass

    def get_input(self)
        val = self.LOW

        return val
        pass

    def output(self, level)

        pass


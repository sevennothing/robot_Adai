#-*- coding:UTF-8 -*-
#Author: caijun.Li <sevennothing@gmail.com>
#Date: 2019/01/20

#import SysDrv.GPIO as GPIO


class ServoControl(object):
    def __init__(self, config, superUnit=None):
        '''
        config: {
            "rsname": "resource name",
            "SignalPin": "GPIOx",
            "Power":"5V",
            "MaxAngle":"180",
            "limitAngle":"180"
        }

        '''
        self.config = config
        self.status = {}
        self.methods = {}

        if(superUnit != None):
            self._dump_info = superUnit['dump_info']
        else:
            self._dump_info = None

        ## 申请资源
        self.rs = []
        self.rs.append(GPIO(superUnit, config['rsname'] + ":" + config['SignalPin'], config['SignalPin']))

        pass

    def dump_info(self):

        if(self._dump_info != None):
            self._dump_info(self.config)
        else:
            print(self.config)
        
        pass

    def servo_pulse(self, angle):
        pulseWidth = (angle * 11) + 500
        pass

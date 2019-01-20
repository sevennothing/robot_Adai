#-*- coding:UTF-8 -*-

class ComDrv(object):
    def __init__(self,superUnit,name,drvType):
        '''
            通用驱动初始化，
            superUnit: 整体元素,提供给下层用于回调
            由它将整体联系在一起
            name: 驱动的命名
            driverType{
                GPIO
            }

        '''
        self.superUnit = superUnit
        self.name = name
        self.drvType = drvType;

        pass

    def set_input_param(self):
        pass
    def set_output_param(self):
        pass
    def check_param_valid(self):
        pass
    def check_drv_status(self):
        pass
    def destory_drv(self):
        pass
    def suspend_drv(self):
        pass
    def start_drv(self):
        pass
    def feedback(self):
        pass



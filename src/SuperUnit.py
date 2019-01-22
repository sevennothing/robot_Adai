#-*- coding:UTF-8 -*-
#Author: caijun.Li <sevennothing@gmail.com>
#Date: 2019/01/20
import os
import sys
import json
import component.ServoControl as ServoControl

class SuperUnit(object):
	def __init__(self, configCard, name='anonymous'):
		self.name = name
		self.my_writing("My name is " + name)

		if not os.path.exists(configCard):
			self.my_writing("I can't found my config Card, I'm dead, oh, I've never lived!")
			sys.exit(-1)

		with open(configCard) as json_file:
			self.configCard = json.load(json_file)
		json_file.close()

		self.debug = self.configCard['debug']
		self.my_debug(self.configCard, 10)
		self.register_resource()

		pass

	def my_speaking(self, msg):
		pass

	def my_writing(self, msg):
		print(msg)
		pass

	def my_debug(self,msg,level=1):
		if(level <= self.debug):
			print(msg)
		pass

	def register_resource_GPIO(self):
		if not "GPIO" in self.configCard['resource']:
			return
		for item in self.configCard['resource']['GPIO']:
			self.my_debug(item,10)
			rsname = item['rsname']
			self.rs[rsname] = {}
			self.rs[rsname]['used'] = 0
			self.rs[rsname]['share'] = 0
			self.rs[rsname]['user'] = []
			

		pass
	def register_resource_SPI(self):
		pass
	def register_resource_IIC(self):
		pass
	def register_resource_SERVO(self):
		if not "SERVOMOTOR" in self.configCard['resource']:
			return
		for item in self.configCard['resource']['SERVOMOTOR']:
			self.my_debug(item,10)
			rsname = item['rsname']
			self.rs[rsname] = {}
			self.rs[rsname]['used'] = 0
			self.rs[rsname]['share'] = 0
			self.rs[rsname]['user'] = []

		pass

	def register_resource(self):
		self.rs = {}
		self.register_resource_GPIO()
		self.register_resource_SPI()
		self.register_resource_IIC()
		self.register_resource_SERVO()

		self.my_debug("resource: " + str(self.rs), 3)
		pass


if __name__ == "__main__":
	adai = SuperUnit('./config.json','A Dai')

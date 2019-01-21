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
			slef.my_writing("I can't found my config Card, I'm dead, oh, I've never lived!")
			sys.exit(-1)

		with open(configCard) as json_file:
			self.configCard = json.load(json_file)
		json_file.close()

		#self.my_writing(self.configCard)

		pass

	def my_speaking(self, msg):
		pass

	def my_writing(self, msg):
		print(msg)
		pass


if __name__ == "__main__":
	adai = SuperUnit('./config.json','adai')

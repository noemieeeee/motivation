#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 小车跑起来
#
#

import RPi.GPIO as GPIO
import time


class stateCtrl(object):
	'''Motor Control Module'''

	def __init__(self):

		######## Motor Driver Interface Definition ##################
		self.ENA = 33  # //L298 enable A
		self.ENB = 35  # //L298 enable B
		self.IN1 = 11  # //Motor interface 1
		self.IN2 = 12  # //Motor interface 2
		self.IN3 = 13  # //Motor interface 3
		self.IN4 = 15  # //Motor interface 4
		self.setup()

	def setup(self):
		'''Pin initialization'''
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)

		GPIO.setup(self.IN1, GPIO.OUT)
		GPIO.setup(self.IN2, GPIO.OUT)
		GPIO.setup(self.IN3, GPIO.OUT)
		GPIO.setup(self.IN4, GPIO.OUT)

		GPIO.output(self.IN1, GPIO.LOW)
		GPIO.output(self.IN2, GPIO.LOW)
		GPIO.output(self.IN3, GPIO.LOW)
		GPIO.output(self.IN4, GPIO.LOW)
		print('car start')		

	def t_up(self, secondvalue=0):
		self.setup()
		GPIO.output(self.IN1, True)
		GPIO.output(self.IN2, False)
		GPIO.output(self.IN3, False)
		GPIO.output(self.IN4, True)

	def t_left(self, secondvalue=0):
		self.setup()
		GPIO.output(self.IN1, False)
		GPIO.output(self.IN2, True)
		GPIO.output(self.IN3, False)
		GPIO.output(self.IN4, True)

	def t_right(self, secondvalue=0):
		self.setup()
		GPIO.output(self.IN1, True)
		GPIO.output(self.IN2, False)
		GPIO.output(self.IN3, True)
		GPIO.output(self.IN4, False)

	def t_down(self, secondvalue=0):
		self.setup()
		GPIO.output(self.IN1, False)
		GPIO.output(self.IN2, True)
		GPIO.output(self.IN3, True)
		GPIO.output(self.IN4, False)

	def t_stop(self):
		self.setup()
		GPIO.output(self.IN1, False)
		GPIO.output(self.IN2, False)
		GPIO.output(self.IN3, False)
		GPIO.output(self.IN4, False)


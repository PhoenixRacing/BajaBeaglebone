#!/usr/bin/env python
from flask import Flask

class DashApp(Flask):

	def __init__(self):
		super(self.__class__, self).__init__(__name__)
		self.time = ""

	def timeCallback(self, data):
		self.time = str(data)

dashApp = DashApp()
from DashApp import controllers
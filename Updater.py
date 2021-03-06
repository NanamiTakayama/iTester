# -*- coding: utf-8 -*-

import datetime
import commands
import time
import subprocess

class Updater:

	def __init__(self, commitnumber ,updatecycle):
		self.commitnumber = commitnumber#コミットの回数を指定する
		self.updatecycle = updatecycle*60#updateのサイクルを分単位で指定する
		print("Updater Started")
		self.committime = str(datetime.datetime.today())#コミットメッセージとして入る時間
		print(self.committime)
		self.error ="""
		_______________________

		Something is Wrong 
		Please Check network or
		git setteings
		_______________________
		"""


	def newapp(self):
		print("generating new app")
		self.temporalyapp = str(commands.getoutput("cat template.py"))#app.pyを取得する
		self.temporalyapp = self.temporalyapp.replace("Hello", self.committime) #change time stamp
		self.chagedapp = open('./app.py','w')#nf for newfile
		self.chagedapp.write(self.temporalyapp)
		self.chagedapp.close()

	def addcommit(self):
		print("commit number is " + str(self.commitnumber))
		print("update cycle is " + str(self.updatecycle))

		for self.count in range(0,self.commitnumber):
			self.add = subprocess.call(["git","add","."])#git add .の実行
			print("sucessfully added")
			self.commit = str(subprocess.call(["git","commit","-m",self.committime]))#git commit の実行
				
			if self.commit == "0":
				print("sucessfully commited at" + self.committime)
				self.count += 1
				print(str(self.count) + "time sucessfully commited")

			else:
				print(self.error)
				break


	def push(self):
		self.push = str(subprocess.call(["git","push","origin","master"]))#git pushの実行
		if  self.push == "0":
			print("sucsesfully pushed")

		else:
			print(self.error)
			pass


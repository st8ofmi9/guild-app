import threading
import logging
from app.gw2data4 import *
from dateutil.parser import parse

class guildstats():


	def __init__(self):
		self.i=0
		self.withdrawal, self.deposit, self.invited = ([] for i in range(3))
		self.lst, self.kick, self.joined = ([] for i in range(3))
		self.itemcall = "items/{}"
		self.continueaction = 0
		self.entlistnum = 0
		self.guild = gw2data("ED17D35D-F092-0543-91BA-94FB4558C61AA1EDDD6E-1BBD-4776-80F7-FEABB4E41FC4")
		self.guild.guildinfo("Flash Bomb")
		self.called = {}

	def guildcall(self, call):
		self.gcall = "guild/{!s}/{!s}".format(self.guild.gid[0], call)
		self.grequest = requests.get(self.guild.url+self.gcall, headers=self.guild.auth)
		self.called[call] = self.grequest.json()
		logging.info(self.called)
		return self.called[call]
	
	def gthreads(self):
		threads = []
		gendpoint = ["members","ranks","log"]
		for calls in gendpoint:
			print("{}".format(calls))
			t = threading.Thread(name=calls, target=self.guildcall, args=[calls])
			threads.append(t)
			t.start()
		for thread in threads:
			thread.join()
			
	def unpack_and_org(self, *reqobj):
		for item in reqobj:
			if item['type']=='stash':
				if item['operation']=='withdraw': 
					self.withdrawal.append(item)
				elif item['operation']=='deposit': 
					self.deposit.append(item)
			if item['type']=='invited':
				self.invited.append(item)
			if item['type']=='kick':
				self.kick.append(item)
			if item['type']=='joined':
				self.joined.append(item)

	def withdrawal_stats(self, *withdrawal):
		self.lst = []
		self.i = 0
		for obj in withdrawal:
			wdStats = {}
			err_list = []
			try:
			  self.item = self.guild.apicall(self.itemcall.format(withdrawal[self.i]['item_id']),1)
			except(IndexError):
				logging.info(withdrawal[self.i]['item_id'])
				logging.info(withdrawal[self.i])
				pass

			try:
				entry = """
				User: {0!s}
				item id: {1!s}
				Date: {2!s}
				Coins: {3!s}
				""".format(withdrawal[self.i]['user'], self.item['name'], withdrawal[self.i]['time'], withdrawal[self.i]['coins'])
				wdStats['user'] = withdrawal[self.i]['user']
				wdStats['name'] = self.item['name']
				wdStats['time'] = withdrawal[self.i]['time']
				wdStats['coins'] = withdrawal[self.i]['coins']
				self.lst.append(wdStats)
			except(KeyError):
				print("Key: Name does not exist")
				wdStats['user'] = withdrawal[self.i]['user']
				wdStats['name'] = ""
				wdStats['time'] = withdrawal[self.i]['time']
				wdStats['coins'] = withdrawal[self.i]['coins']
				self.lst.append(wdStats)
			self.i = self.i + 1
		return self.lst
	
	def bombling(self, member_data, rank):
		bomblst = []
		for x,member in enumerate(member_data):
			if member['rank'] == rank:
				today = datetime.datetime.today()
				today = today.replace(tzinfo=None)
				delta = today - parse(member['joined']).replace(tzinfo=None)
				bomblinginfo = {}
				try:
					bomblinginfo['joined'] = member['joined']
					bomblinginfo['days_in_guild'] = delta.days
					bomblinginfo['name'] = member['name']
					bomblst.append(bomblinginfo)
				except(KeyError):
					pass
		return bomblst

	def member_rank(self, guildy):
		table = []
		for member in guildy:
			try:
				table.append("""<tr><td>{0!s}</td><td>{1!s}</td><td>{2!s}</td></tr>""".format(member['name'], member['joined'], member['days_in_guild']))
			except(KeyError):
				logging.info(a.called.keys())
		return table
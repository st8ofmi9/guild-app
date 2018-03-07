from app.guildstats import *
from threading import Thread, currentThread


class ItemThreads(Thread):
	
	def __init__(self,withdrawal): 
		self.sItem = []
		self.stats = guildstats()
		self.withdrawal = withdrawal
		super(ItemThreads, self).__init__()

	def run(self):
		print("Gathering Items")
		self.sItem.insert(0,(self.stats.guild.apicall(self.stats.itemcall.format(self.withdrawal['item_id']),1)))
		try:
			print("Processing Data for {}".format(currentThread().getName()))
		except(KeyError):
			print("Oops")
		return self.sItem
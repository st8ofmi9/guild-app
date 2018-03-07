from app.ItemThreads import *


class memberobj(guildstats):

    def __init__(self):
        #pass
        super(memberobj, self).__init__()
        self.threads = []
        self.thread_data = []

    def stat_threads(self, withdrawal):
        for i in range(len(withdrawal)):
            t = ItemThreads(withdrawal[i])
            self.threads.append(t)
            t.start()
            try:
                self.thread_data.insert(i, (t.sItem))
            except(IndexError):
                print("Index not found")
                pass
        for thread in self.threads:
            thread.join()
            print(t.sItem)
        return (self.thread_data)

    def member(self, *tdata, action=None):
        if action == 'withdraw':
            items = (obj[0] for obj in tdata)
            for i,obj in enumerate(items, start=0):
                try:
                    if self.withdrawal[i]['item_id'] in obj.values():
                        self.withdrawal[i]['item_name'] = obj['name']
                    elif 0 >= self.withdrawal[i]['item_id']:
                            self.withdrawal[i]['item_name'] = "GOLD"
                except(KeyError):
                        self.withdrawal[i]['item_name'] = "GOLD"
                except(IndexError):
                        pass
        elif action == 'deposit':
            items = (obj[0] for obj in tdata)
            for x,obj in enumerate(items, start=0):
                try:
                    if self.deposit[x]['item_id'] in obj.values():
                        self.deposit[x]['item_name'] = obj['name']
                    elif 0 >= self.deposit[x]['item_id']:
                            self.deposit[x]['item_name'] = "GOLD"
                except(KeyError):
                        self.deposit[x]['item_name'] = "GOLD"
                except(IndexError):
                        pass
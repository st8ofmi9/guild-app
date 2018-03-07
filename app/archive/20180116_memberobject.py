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
        for i,obj in enumerate(tdata, start=0):
            print(i, obj[0])
            if action == 'withdraw':
                try:
                    if self.withdrawal[i]['item_id'] in obj[0].values():
                        self.withdrawal[i]['item_name'] = obj[0]['name']
                    elif 0 >= self.withdrawal[i]['item_id']:
                        self.withdrawal[i]['item_name'] = "GOLD"
                except(KeyError):
                    self.withdrawal[i]['item_name'] = "GOLD"
                except(IndexError):
                    if self.withdrawal[i]['item_id'] in obj[0].values():
                        self.withdrawal[i]['item_name'] = obj['name']
                    elif 0 >= self.withdrawal[i]['item_id']:
                        self.withdrawal[i]['item_name'] = "GOLD"
                    pass
            elif action == 'deposit':
                try:
                    if self.deposit[i]['item_id'] in obj[0].values():
                        self.deposit[i]['item_name'] = obj[0]['name']
                    elif 0 >= self.deposit[i]['item_id']:
                        self.deposit[i]['item_name'] = "GOLD"
                except(KeyError):
                    self.deposit[i]['item_name'] = "GOLD"
                except(IndexError):
                    print("Index Name Error for {}".format(obj[0]))
                    print("Index Error for {}".format(i))
                    pass
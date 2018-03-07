from Cache import *
from time import time
from queue import Queue
from threading import Thread



class DownloadWorker(Thread):
    def __init__(self, inqueue, outqueue):
        Thread.__init__(self)
        self.inqueue = inqueue
        self.outqueue = outqueue
        self.sItem = []

    def run(self):
        while True:
        # Get the work from the queue and expand the tuple
            url = self.inqueue.get()
            #self.sItem.insert(0,)
            self.outqueue.put(get_content(url).json())
            self.inqueue.task_done()
        return self.queue

def main(endpoint, url=None):
    ts = time()
    if url == None:
        base_url = "http://api.guildwars2.com/v2/{}"
    else:
        base_url = url
    call = get_content(base_url.format(endpoint))
    if type(call.json()) is list:
        gen_link = [base_url.format(endpoint+"/{}".format(m)) for m in call.json()]
        print(gen_link)
        # Create a queue to communicate with the worker threads
        inqueue = Queue()
        outqueue = Queue() 
        # Create 4 worker threads
        for x in range(4):
            worker = DownloadWorker(inqueue, outqueue)
            # Setting daemon to True will let the main thread exit even though the workers are blocking
            worker.daemon = True
            worker.start()
        #c = (len(gen_link)+10) - len(gen_link)
        i = 0
        try:
            inqueue.put(gen_link[i])
            i = i+1
        except:
            inqueue.join()
        inqueue.join()
        #outqueue.join()
        qd = []
        while not outqueue.empty():
            qd.append(outqueue.get())
            outqueue.task_done()
    else: 
        qd = call.json()
    print("Task Completed in {} seconds".format(time() - ts))
    return qd

if __name__ == '__main__':
    main()
import eventlet.green.threading as threading
import eventlet.queue as Queue

class Producer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        for i in range(10):
            self.q.put(i)
        self.q.put(None)

class Consumer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            i = self.q.get()
            if i is None:
                return
            print i

def main():
    q = Queue.Queue()
    p = Producer(q)
    c = Consumer(q)
    c.start()
    p.start()
    p.join()
    c.join()

if __name__ == "__main__":
    main()

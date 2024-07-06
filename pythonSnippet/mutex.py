from threading import Thread, Lock
import time

class ProducerConsumer():
    def __init__(self, producerN, consumerN, bufferMaxSize):
        self.producerN = producerN
        self.consumerN = consumerN
        self.bufferMaxSize = bufferMaxSize
        self.count = 0
        self.mutex = Lock()
        for i in range(0, producerN):
            t = Thread(target = self.produce, args=(i,))
            t.start()
        for i in range(0, consumerN):
            t = Thread(target = self.consume, args=(i,))
            t.start()
        print("starting producer consumer problem")

    def produce(self, id):
        while True:
            self.mutex.acquire()
            if self.count < self.bufferMaxSize:
                self.count += 1
            print("Producer {0} - {1} items in buffer".format(id, self.count))
            self.mutex.release()
            time.sleep(2)

    def consume(self, id):
        while True:
            self.mutex.acquire()
            if self.count > 0:
                self.count -= 1
            print("Consumer {0} - {1} items in buffer".format(id, self.count))
            self.mutex.release()
            time.sleep(2)

ProducerConsumer(3, 5, 6)
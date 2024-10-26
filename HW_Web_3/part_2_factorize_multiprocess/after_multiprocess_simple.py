from multiprocessing import Queue, Process, Manager
from time import time
import sys

q = Queue()


def worker(queue: Queue, result: list):
    t1 = time()
    val = queue.get()
    i = 1
    result = [i for i in range(1, val + 1) if val % i == 0]
    print(f"Process with value: {val}, done in: {time() - t1} s, result: {result}")
    sys.exit(0)


def factorize(*number: tuple):
    t0 = time()
    with Manager() as m:
        result = m.list()
        processes = []
        for el in number:
            q.put(el)
        for i in range(len(number)):
            w = Process(target=worker, args=(q, result))
            w.start()
            processes.append(w)

        [w.join() for w in processes]

    print(f"All function done in: {time() - t0} s,")


if __name__ == '__main__':
    a = factorize(128, 255, 99999, 10651060)

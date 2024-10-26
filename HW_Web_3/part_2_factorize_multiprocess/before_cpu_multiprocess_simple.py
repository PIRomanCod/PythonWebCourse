import logging
from time import time


def factorize(*number: tuple) -> list:
    output = []
    t0 = time()
    for el in number:
        t1 = time()
        result = [i for i in range(1, el + 1) if el % i == 0]
        logging.debug(f"input element: {el}, time done: {time() - t1} s result: {result}")
        output.append(result)
    logging.debug(f"full time: {time() - t0} s")
    return output


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(funcName)s %(message)s")
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(1, 6):
            print("Hello:", i)
            sleep(0.2)


class Hi(Thread):
    def run(self):
        for i in range(1, 6):
            print("Hi:", i)
            sleep(0.2)


def main():
    t1 = Hello()
    t2 = Hi()

    t1.start()
    t2.start()


if __name__ == "__main__": main()

from threading import Thread
from time import sleep,time

# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello ",i+1)
#             sleep(0.2)
# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi ",i+1)
#             sleep(0.2)

def Download(file_name):
    print("Downloading file....",file_name)
    sleep(0.5)
    print("Download is completed",file_name)


if(__name__ == "__main__"):
    files = ['video.mp4' , 'image.png' , 'data.csv']
    start = time()

    for f in files:
        Download(f)

    end = time()
    print(f"Serial process time:{end-start:.2f} ")

    threads = []
    for f in files:
        t = Thread(target=Download,args=(f,))
        threads.append(t)

    start = time()

    for t in threads:
        t.start()
    # for t in threads:
    #     t.join()
    end = time()

    print(f"multiple process time:{end - start:.2f} ")

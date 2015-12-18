'''
Created on 2015-12-18

@author: dutao
'''
from time import ctime,sleep
import threading

def music(music_name):
    for i in range(2):
        print("I was listening to %s. %s" % (music_name,ctime()))
        sleep(1)

def move(movie_name):
    for i in range(2):
        print("I was at the %s! %s" % (movie_name,ctime()))
        sleep(5)
threads = []
thread1 = threading.Thread(target=music, args={'月亮之上'})
threads.append(thread1)
thread2 = threading.Thread(target=move, args={'火星救援'})
threads.append(thread2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        #把主线程A设置为守护线程，这时候，要是主线程A执行结束了，就不管子线程B是否完成,一并和主线程A退出
        t.start()
    t.join()#主线程A会在调用的地方等待，直到子线程完成操作后，才可以接着往下执行
    print("all over %s" %ctime())
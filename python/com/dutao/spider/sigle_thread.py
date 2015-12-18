'''
Created on 2015-12-18

@author: dutao
'''
from time import ctime,sleep

def music(music_name):
    for i in range(2):
        print("I was listening to %s. %s" % (music_name,ctime()))
        sleep(1)

def move(movie_name):
    for i in range(2):
        print("I was at the %s! %s" % (movie_name,ctime()))
        sleep(5)

if __name__ == '__main__':
    music('月亮之上')
    move('火星救援')
    print("all over %s" %ctime())
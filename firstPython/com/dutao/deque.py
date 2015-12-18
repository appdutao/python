'''
Created on 2015-12-15
在爬虫程序中, 用到了广度优先搜索(BFS)算法. 这个算法用到的数据结构就是队列.

Python的List功能已经足够完成队列的功能, 可以用 append() 来向队尾添加元素, 
可以用类似数组的方式来获取队首元素, 可以用 pop(0) 来弹出队首元素. 
但是List用来完成队列功能其实是低效率的, 因为List在队首使用 pop(0) 和 insert() 都是效率比较低的, 
Python官方建议使用collection.deque来高效的完成队列任务.

@author: dutao
'''
from collections import deque

queue = deque(['1','2','3'])
queue.append('4')
queue.append('5')
queue.popleft()#去除队首
queue.pop()
print(queue)
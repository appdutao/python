'''
Created on 2015-12-15
Python提供了set这种数据结构. set是一种无序的, 不包含重复元素的结构. 一般用来测试是否已经包含了某元素, 或者用来对众多元素们去重. 与数学中的集合论同样, 他支持的运算有交, 并, 差, 对称差.

创建一个set可以用 set() 函数或者花括号 {} . 但是创建一个空集是不能使用一个花括号的, 只能用 set() 函数. 因为一个空的花括号创建的是一个字典数据结构. 以下同样是Python官网提供的示例.
@author: dutao
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('orange' in basket)

a = set(['apple','pear','1'])
b = set(['apple','2','3'])
print(a - b)#a中独有
print(a | b)#ab所有
print(a ^ b)#去除共有
print(a & b)#大家公有
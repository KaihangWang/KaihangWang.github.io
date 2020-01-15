
# def print_info(*args, **kwargs):
#     name = kwargs['name']
#     age = kwargs['age']
#     sex = kwargs['sex']
#     # if 'hobbie' in kwargs:
#     #     hobbie = kwargs['hobbie']
#     # else:
#     #     hobbie = '大保健'
#     hobbie = kwargs['hobbie'] if 'hobbie' in kwargs else '大保健'
#     print('-------info--------')
#     print('Name: %s' % name)
#     print('Age: %s' % age)
#     print('Sex: %s' % sex)
#     print('Hobbie: %s' % hobbie)
#
#
# print_info(name='Alex', age=22, sex='M')
# print_info(name='Jack', age=26, sex='M', hobbie='学习')

# a = [1, 3, 4, 6, 7, 8, 9, 11, 15, 17, 19, 21, 22, 25, 29, 33, 38, 69, 107]
# def find(num,a):
#
#     b = int(len(a)//2)
#     if b != 0:
#         if a[b] > num:
#             a = a[0:b]
#             print(a)
#             find(num, a)
#         elif a[b] < num:
#             a = a[b:len(a)]
#             print(a)
#             find(num, a)
#         else:
#             print(a[b])
#     else:
#         print(None)
# find(33, a)

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield  # yield可以接收到外部send传过来的数据并赋值给baozi
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))
c = consumer('A')
c2 = consumer('B')
c.__next__() # 执行一下next可以使上面的函数走到yield那句。 这样后面的send语法才能生效
c2.__next__()
print("----老子开始准备做包子啦!----")
for i in range(10):
    time.sleep(1)
    print("做了2个包子!")
    c.send(i)  # send的作用=next, 同时还把数据传给了上面函数里的yield
    c2.send(i)

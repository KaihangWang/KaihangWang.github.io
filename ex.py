#
# num = 1
#
# while num < 4:
#
#     name = input("name:")
#     password = input("password:")
#
#     if name == "seven" or name == "alex" and password == '123':
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
#     num += 1

# num = 1
# while num < 13:
#     if num == 6:
#         num += 1
#         continue
#     elif num == 10:
#         num += 1
#         continue
#     else:
#         print(num)
#     num += 1

# num = 100
# while True:
#     if num > 50:
#         while num > 49:
#             print(num)
#             num -= 1
#     elif num < 50:
#         num = 0
#         while num < 50:
#             print(num)
#             num += 1
#     else:
#         print(num)
#         break

# name = input("name:")
# address = input("address:")
# love = input("love:")
# print('敬爱可爱的%s，最喜欢在%s, %s' % (name, address, love))

# a = "* "
# num = 2
# while True:
#     if num < 5 and num > 1:
#         print(a * 1)
#         while num < 6:
#             print(a * num)
#             num += 1
#     elif num > 5:
#         num = 4
#         while num > 1:
#             print(a * num)
#             num -= 1
#     else:
#         print(a)
#         break

#
# num = 1
# red_ball = []
# blue_ball = []
# print('Welcome to system')
# while True:
#     len_red = len(red_ball)
#     len_blue = len(blue_ball)
#     if len_red < 6 and len_blue == 0:
#         num_ball = int(input("[%s]select red ball:" % num))
#         if num_ball > 0 and num_ball < 33:
#             if num_ball in red_ball:
#                 print("number %s is already exist  in red ball list" % num_ball)
#             else:
#                 red_ball.append(num_ball)
#                 num += 1
#         else:
#             print("%s不在1到32之间！" % num_ball)
#     elif len_red == 6 and len_blue < 2:
#         num = 1
#         num_ball = int(input("[%s]select blue ball:" % num))
#         if num_ball > 0 and num_ball < 17:
#             if num_ball in blue_ball:
#                 print("number %s is already exist  in red ball list" % num_ball)
#             else:
#                 blue_ball.append(num_ball)
#                 num += 1
#         else:
#             print("%s不在1到16之间！" % num_ball)
#     else:
#         print("red ball is %s" % red_ball)
#         print("blue ball is %s" % blue_ball)
#         print("Good Luck.")
#         break

# a = range(0, 100)
# b = {}
# for i in a:
#     b[i] = i
# print(b)

#
# a = {'k0': 0, 'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5, 'k6': 6, 'k7': 7, 'k8': 8, 'k9': 9}
# # for i in a:
# #     if a[i] > 5:
# #         print(a[i])
# list1 = []
# for i in a:
#     list1.append(i)
#     list1.index()
# print(list1)
#
# names = ['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', 'eva', '鸡头']
#
# target = 'eva'
# b = []
# for index, nums in enumerate(names):
#     print(index)
#     if nums == target:
#         b.append(index)
# print(b)
#
# names[b[1]] = 'EVA'
# print(names)
#

# f = open('测试文件.txt', 'a')
# # data = f.read()
# # print(data)
# f.write('真的一样吗？')
# f.close()
# f = open('测试文件.txt')
# data = f.read()
# print(data)
# f.close()
#

# f = open('测试文件.txt')
# for line in f:
#     line = line.split()
#     print(line)
# f.close()

# import sys
# import os
# old_file, new_file = sys.argv[1], sys.argv[2]
# def change_file(old_file, new_file):
#     f_name = old_file
#     f_new_name = new_file
#
#     old_name = '岳妮妮'
#     new_name = 'huo ni ni'
#
#     f = open(f_name, 'r')
#     f_new = open(f_new_name, 'w')
#
#     for line in f:
#         if old_name in line:
#             new_lin = line.replace(old_name, new_name)
#             print(new_lin)
#         else:
#             new_lin = line
#         f_new.write(new_lin)
#     f.close()
#     f_new.close()
#     os.replace(new_file, old_file)
# if __name__ == '__main__':
#     change_file(old_file, new_file)
# #     os.replace('测试文件新.txt', '测试文件.txt')
# # if __name__ == '__main__':
# #     change_file('测试文件.txt', '测试文件新.txt')



# def print_info(*args,hobbie='大保健',**kwargs):
#     name = kwargs['name']
#     age = kwargs['age']
#     sex = kwargs['sex']
#     if 'hobbie' in kwargs:
#         hobbie = kwargs['hobbie']
#     else:
#             hobbie = '大保健'
#     print('-------info--------')
#     print('Name: %s' % name)
#     print('Age: %s' % age)
#     print('Sex: %s' % sex)
#     print('Hobbie: %s' % hobbie)
#
# print_info(name = 'Alex', age = 22, sex = 'M')
# print_info(name='Jack',age=26,sex='M',hobbie='学习')

# import my_module
# import sys
# print(sys.path)
# my_module.sayhi('kaihang')

import re
a = re.compile(r"""\d + # the integral part
                \. # the decimal point
                \d * # some fractional digits""",
                re.X)
b = re.compile(r"\d+\.\d*")
print(a, b)

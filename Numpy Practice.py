# number = int(input('enter a number: '))
# fact = 13
# for i in range(1, number):
#     fact *= i

# print(f'the fact of (number) is (fact)')  
#   
# ..........

# import random
# matrix = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(random.randint(1, 10))
#     matrix.append(row)
# for row in matrix:
#     for item in row:
#         print(f'{item:4}', end =' ')
#     print()
 
# .........

# data = []
# uniqui_data = []
# for item in data:
#     if item not in uniqui_data:
#         uniqui_data.append(item)
# print(f'uniqui data : {uniqui_data}')

# ................

# data = [5, 6, None, 10, None, 13, None]

# missing_count = 0
# for item in data:
#     if item is None:
#       missing_count += 1

# print(f'missings: {missing_count}')

# ...........

# data = {5, 10, 15, 20, 25}
# min_value = min(data)
# max_value = max(data)

# normal_data = []
# for item in data:
#     normal_val = (item-min_value) / (max_value-min_value)
#     normal_data.append(normal_val)
# print(f'normal data: {normal_data}')

# ..............

# data = [10, 11, 13, 15, 17, 19, 20]
# mean = sum(data) / len(data)
# sum_equard_diff = 0
# for item in data:
#     sum_equard_diff +


# ............

# def mean_and_std(data):
#     mean = sum(data) / len(data)
#     variance = sum((x - mean) ** 2 for x in data) / len(data)
#     std_dev = variance ** 0.5
#     return mean, std_dev

# data = [10, 12, 23, 23, 16, 23, 21, 16]
# mean, std_dev = mean_and_std(data)
# print('میانگین:', mean)
# print('انحراف معیار:', std_dev)

#  ...............

# # مقادیر پرت

# def detect_outliers(data):
#     mean, std_dev = mean_and_std(data)
#     outliers = [x for x in data if abs(x - mean > std_dev)]
#     return outliers
# data = [10, 12, 23, 23, 16, 23, 21, 16, 100]
# outliers = detect_outliers(data)
# print('مقادیر پرت:', outliers)

# [100] :مقادیر پرت

# def f2(arg1, arg2, *args, **kwargs):
#     print(arg1, arg2, args, kwargs)
# f2(arg1=1, arg2=2, c=3)

# ..............

# import numpy as np
# grade = np.array[ 16, 17, 13, 12, 10, 12, 10, 12, 15, 18, 20]
# change = 3
# print(grade + change)

# x = np.random.randint(0, 10, (3, 3))
# print (x)
# matrix = np.random.randint(20, 100, (6, 6))
# print (matrix)
# x = np.array([[2, 8, 9], [5, 9, 0]])
# y = np.array([[4, 6], [4, 7], [2, 3]])
# zarb = np.dot(y, x)
# print(zarb)

# ..............

# import numpy as np
# matrix = np.array([[1, 2, 3], [10, 11, 12]])
# vector = np.array([1, 3, 9])
# result = matrix + vector
# print(result)
# '..............'
# array = np.array  ([1, 2, 3, 4, 5])
# squared = array ** 2
# print(squared)
'...........'
# x = np.array([2, 3, 4, 5, 6])
# y = np.array([2, 3, 4, 5, 6])
# # print(x == y)
# import timeit
# x = np.arange(1000)
# timeit(x +1)
# num = int(input("Enter a positive integer: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial:", factorial)

# for i in range(1, 101):
#     if i%2 != 0:
#      print(i)

# numbers = [ 1, 2, 4, 5]
# total = sum(numbers)
# print('the sum:', total)

# text = input('enter str: ')
# new = text[::-1]
# print('reversted version:', new)

# num = int(input("Enter a positive integer: "))
# a = 1
# for i in range(1, num):
#     a = a + i
# print("Factorial:", a)
# num = int(input("Enter a positive integer: "))
# is_prime = True

# if num < 2:
#     is_prime = False
# else:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")
# s = input('sentence:')
# words = s.split()
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print('words frequency:')
# for word, count in word_count.items():
#     print(f'{word}, {count}')

# import numpy as np
        
# x = np.random.randint(1, 20, size=(2,3,5), dtype= 'int8')
# x.strides
# y=x.max(axis=2)
# print(x)
# print(y)
# z=x.flatten()
# print(z)
# t=np.range(24)
# g= t.shape=3, 4, -1
# print(g)

# ........

# a = np.random.randint(19, size=(3, 4))
# print(a)
# w=a[:, [True, False, True, False]]
# print(w)
# k=a[[True, False, True], :]
# print(k)

# .........

# f= np.array([[1., 2.,], [np.nan, 3.], [np.nan, np.nan]])
# print(f)
# o=np.isnan(f)
# print(o)
# l=f[~np.isnan(f)]
# print(l)

# ......

# numbers= np.linspace(5, 50, 24, dtype=int).reshape(4, -1)
# print(numbers)
# mask=numbers % 4 == 0 
# print(mask)
# h= numbers[mask]
# print(h)

# ......

# data= np.array([
#     ('joey', 32, 6),
#     ('rachel', 31, 8),
#     ('ross' , 33, 7),
# ], dtype=[('name', str, 10), ('age', int), ('power', int)])


# .....


          

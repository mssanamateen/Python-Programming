Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fruits=["apple","mango","apple"]
>>> print(fruits)
['apple', 'mango', 'apple']
>>> print(len(fruits))
3
>>> range(0,11)
range(0, 11)
>>> num=list(range(0,11))
>>> num
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> num2=list(range(0,11,2))
>>> num2
[0, 2, 4, 6, 8, 10]
>>> num2.append(12)
>>> num2
[0, 2, 4, 6, 8, 10, 12]
>>> num2.append(0)
>>> num2
[0, 2, 4, 6, 8, 10, 12, 0]
>>> num2.pop(0)
0
>>> num2
[2, 4, 6, 8, 10, 12, 0]
>>> num2.insert(1,'apple')
>>> num2
[2, 'apple', 4, 6, 8, 10, 12, 0]
>>> num2.remove(0)
>>> num2
[2, 'apple', 4, 6, 8, 10, 12]
>>> num2[3]
6
>>> num2[:5]
[2, 'apple', 4, 6, 8]
>>> num2[:,2]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    num2[:,2]
TypeError: list indices must be integers or slices, not tuple
>>> num2[::2]
[2, 4, 8, 12]

Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #slicing
>>> num=[1,2,3,4,5]
>>> print(num[1:4])
[2, 3, 4]
>>> print(num[-3:-1])
[3, 4]
>>> fruits=['apple','cherry','berry']
>>> count=[2,4,5]
>>> fruits.append(count)
>>> fruits
['apple', 'cherry', 'berry', [2, 4, 5]]
>>> fruits.index('berry')
2
>>> fruits.pop()
[2, 4, 5]
>>> fruits
['apple', 'cherry', 'berry']
>>> fruits.count('apple')
1
>>> fruits.reverse()
>>> fruits
['berry', 'cherry', 'apple']
>>> copyfruits=fruits.copy()
>>> copyfruits
['berry', 'cherry', 'apple']
>>> fruits.remove('berry')
>>> fruits
['cherry', 'apple']
>>> fruits.extend(count)
>>> fruits
['cherry', 'apple', 2, 4, 5]

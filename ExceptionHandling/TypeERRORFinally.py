try:
    a=2
    b='apple'
    c=a+b
except TypeError as te:
    print(te)
finally:
    print(b*a)

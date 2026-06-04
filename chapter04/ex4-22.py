try:
    10 /0
    c = "will never get defined."
except ZeroDivisionError:
    print(c)

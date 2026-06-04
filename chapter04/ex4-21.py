try:
    a = input("なにか数字を入力して")
    b = input("別の数字を入力して")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("正しい値でお願い")


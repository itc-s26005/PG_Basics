z = [1, 2, 3]

while True:
    a = input("数字を入れてください('qで終了')")

    if a == "q":
        break
    
    try:
        num = int(a)

        if num in z:
            print("正解")
        else:
            print("不正解")
    except ValueError:
        print("数字か'q'を入力してください")

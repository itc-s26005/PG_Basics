def ai_a(x):
    try:
       return float(x)
   #return floatじゃないとできない
   #float関数はオブジェクトを受け取り""オブジェクトに返す
    except (ValueError):
       print("数字じゃないので処理を中止")

a = ai_a("")
print(a)

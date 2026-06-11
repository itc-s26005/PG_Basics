def ai(x):
    return x //2

def ue(x):
    return x * 4

a =int(input("数字を入力してください"))

b = ai(a)
c = ue(b)

print(c)

"""
数字を聞く動作が起こって、その数字を a に入れる。
次に b = ai(a) が実行され、ai関数の中で aの値がxに渡されて2で割られる。
returnでその結果が返され、b に入る。
次に c = ue(b) が実行され、ue関数の中で bの値がxに渡されて4倍される。
returnでその結果が返され、c に入る。
最後に print(c) で結果を表示する。
"""

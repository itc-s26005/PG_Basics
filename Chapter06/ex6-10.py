what = input("何が:")
when = input("いつ:")
where = input("どこで:")
do = input("どうしてだ:")

r = "{}は{}に{}で{}。".format(what, when, where, do)
print(r)
#f文字列を使っての書式指定だとこうなる
print(f"{what}は{when}、{where}で{do}")

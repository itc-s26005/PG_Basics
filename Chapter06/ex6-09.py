#formatメソッドによる書式指定
print("こんにちは、{}".format("ウィリアム・フォークナー"))
name= "ウィリアム・フォークナー"
print("こんにちは、{}".format(name))
#formatメソッドには複数の値が設定できる
author = "ウィリアム・フォークナー"
year_born = "1897"
print("{}は{}年に生まれました。".format(author,year_born))
#こう書いたほうがスッキリかも？
print(f"{authon}は{year_born}年に生まれました。")

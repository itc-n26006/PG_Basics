number=[3,7,10,25,50]

while True:
    s=input("数字を入力してください('q'で終了):")
    if s =="q":
        print("終了します。")
        break
    try:
        num=int(s)
        if num in number:
            print("正解")
        else:
            print("不正解")
    except ValueError:
            print("数字か'q'を入力してください")

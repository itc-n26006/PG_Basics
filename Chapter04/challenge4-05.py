def decimal(a):

    try:
        print("入力された文字=",a)
        print("入力された文字を小数点化した結果=",float(a))
        return a
    except ValueError:
        print("整数、または、小数点数を入力してください。")

a=str("55")
decimal(a)

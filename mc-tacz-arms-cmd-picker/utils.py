def get_valuable_num(prompt): #判断输入为整数而非非法字符
    while True:
        num = input(prompt)
        if num == "q":
            print("欢迎下次使用本程序。")
            return None
        try:
            return int(num)
        except ValueError:
            print("请输入正确的数字。")
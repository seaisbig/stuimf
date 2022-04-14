if __name__ == '__main__':
    while True:
        menu()
        key=input("输入选项数字 查询/输入 信息：")
        if key=='1':
            lookup()
        elif key=='2':
            append()
        elif key=='3':
            delete()
        elif key=='4':
            allinformation()
        elif key=='5':
            revice()
        elif key=='6':
            save()
        elif key=='0':
            print("确认退出？")
            exit = input("输入yes确认")
            if exit == 'yes':
                break
            else:
                print("输入错误，返回")

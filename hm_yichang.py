#
# try:
#     pass
#
# except:
#     pass
#
# Exception  as  result:
#     print("未知的错误%s" % result)
def input_pwd():
    pwd = input("请输入密码：")
    if len(pwd) >= 8:
        return  pwd
    print("输出异常")
    a = Exception("密码长度不能小于8")
    raise a
try:
    input_pwd()
except:
    print("请输入正确密码")

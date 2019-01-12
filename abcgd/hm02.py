# file = open("ssdf","a")
#
#
#
# b = file.write("ruguo ddafasdf")
#
#
# file.close()
#
#
# bbb = open("ssdf")
#
# a = bbb.read()
# print(a)
# bbb.close()
# file = open("ssdf")
# file2 = open("ss","w")
#
# text = file.read()
# file2.write(text)
#
#
#
#
#
#
# file.close()
# file2.close()
file  = open("ssdf")
file2 = open("aaa","w")
while True:

    a = file.readline()

    if not a :
        break
    print(a,end="")

    file2.write(a)

# file2.close()
file.close()
file2.close()

hd = open()
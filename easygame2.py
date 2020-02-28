import os,sys,random
print("-----------start-------------")
sercet=random.randint(1,100)
num = input("请输入1到100 之间的数字：")
#print(type(num))
#限制只能输入数字字符
while not num.isdigit():
    num = input("输入不合法，请继续输入1到100 之间的数字：")
#强制转换
guess=int(num)
i=1
count=10
minnum=1
maxnum=100
while(guess!=sercet):
    if(guess>sercet):
        print("你猜错了，猜的数太大了")
        maxnum=guess
        if(i<count):
            print("你已经猜错"+str(i)+"次了,还有"+str(count-i)+"次机会")
        else:
            print("你5次机会都用完了，游戏结束，你输了")
            sys.exit(0)
        str1="请输入"+str(minnum)+"到"+str(maxnum)+"之间的数字："
        renum = input(str1)
        guess=int(renum)
    elif(guess<sercet):
        print("你猜错了，猜的数太小了")
        minnum=guess
        if(i<count):
            print("你已经猜错"+str(i)+"次了,还有"+str(count-i)+"次机会")
        else:
            print("你5次机会都用完了，游戏结束，你输了")
            sys.exit(0)
        str2="请输入"+str(minnum)+"到"+str(maxnum)+"之间的数字："
        renum = input(str2)
        guess=int(renum)
    else:
        break
    i=i+1
print("你猜对了,答案就是"+str(sercet)+"，你赢了，游戏结束")
        

import operator
from random import randint


#获取数据
f=open('d:\mystuff\guess_number.txt')
lines=f.readlines()
f.close()
data={}
for x in lines:
    s=x.split()
    data[s[0]]=s[1:]
print(data)
    

player=input('请输入用户名：')
player_score=data.get(player)
if player_score==None:
    data[player]=['0','0','0']
    player_score=data.get(player)
game_time=int(player_score[0])
min_time=int(player_score[1])
total_time=int(player_score[2])
print('之前玩了{:d}轮,最快{:d}次成功，一共玩了{:d}次。'.format(game_time,min_time,total_time))



print('猜猜数字是几？')
while True:
    rand_number=randint(1,100)
    print(rand_number)
    times=0
    while True:
        times+=1
        print('第 %d 次'%(times))
        while True:       
            try:
                guess_number=input()
                z=int(guess_number)+int(guess_number[0])+int(str(100-int(guess_number))[0])
                break
            except:
                print('请输入100以内的数字')
        if 100>int(guess_number)>rand_number:
            print('%s 太大了'%(guess_number))                      
        elif 0<=int(guess_number)<rand_number:
            print('%s 太小了'%(guess_number))
        elif int(guess_number)==rand_number:
            print('猜中了，答案就是%s'%(guess_number))
            break           

    m=input('输入go再玩一次，否则退出：')
    if m!='go':
        break

if game_time==0 or times<min_time:
    min_time=times
    total_time+=times
    game_time+=1


data[player]=[str(game_time),str(min_time),str(total_time)]

result=''
for x in data:
    line=x+' '+' '.join(data[x])+'\n'
    result+=line

f=open('d:\mystuff\guess_number.txt','w')
f.writelines(result)
f.close()

    

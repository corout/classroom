f=open('d:/mystuff/report.txt')
f1=f.readlines()
f.close()
m=[]

#1 生成原始总列表
for x in f1:
    m.append(x.split())

#2 插入学科平均分xkl一列,
xkl=['平均']
for i in range(1,10):
    z1=0
    for j in m[1:]:
        z1+=int(j[i])
    xkl.append(str(z1//30))
m.insert(1,xkl)

#3 计算所有列表的总分z，平均分z1
m[0].append('总分')
m[0].append('平均分')
for a in m[1:]:
    z=0
    for b in a[1:]:
        z+=int(b)
        z1=float(z/9)
    a.append(str(z))
    a.append('{:.2f}'.format(z1))


#4 开始排序,生成排序后的新列表m1
m1=sorted(m[2:],key=lambda x:float(x[-1]),reverse=True)
m1.insert(0,m[0])
m1.insert(1,m[1])
m1[0].insert(0,'名次')
for x in m1[1:]:
    x.insert(0,str(m1.index(x)-1))

#5 查找不及格课程，统一替换为“不及格”
for x in m1[2:]:
    for y in range(2,11):
        if int(x[y])<60:
            x[y]='不及格'

#6 生成新文件
f2=open('d:/mystuff/report2.txt','w')
for x in m1:
    x.append('\n')
    y=' '.join(x)
    f2.writelines(y)  
f2.close()

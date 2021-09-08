n = [1,1,2,2,3,3,4,5,5,5]

dic = {}
c = 0

for i in n:
      dic[i] = dic.get(i,0)+1

print(dic)

for i in dic:
      print(dic[i])
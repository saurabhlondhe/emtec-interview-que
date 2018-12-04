with open("demo.txt") as f:
    data=f.read().split()
data_s=set(data)
for i in data_s:
    print(i+"\t"+str(data.count(i)))
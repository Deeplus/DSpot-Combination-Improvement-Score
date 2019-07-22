import linecache

filename='score.txt'
num_1=""
num_2=""
num_3=""
num_4=""
num_5=""
num_6=""
num_7=""
num_8=""
num_9=""
num_10=""
num_11=""
num_combination=""

M=linecache.getline(r'score.txt',1)

for i in M:
    if i.isdigit():
        num_1+=i


M=linecache.getline(r'score.txt',2)

for i in M:
    if i.isdigit():
        num_2+=i


M=linecache.getline(r'score.txt',3)

for i in M:
    if i.isdigit():
        num_3+=i
TestDataMutator=int(num_3)

M=linecache.getline(r'score.txt',4)

for i in M:
    if i.isdigit():
        num_4+=i
MethodGeneratorAmplifier=int(num_4)

M=linecache.getline(r'score.txt',5)

for i in M:
    if i.isdigit():
        num_5+=i
ReturnValueAmplifier=int(num_5)

M=linecache.getline(r'score.txt',6)

for i in M:
    if i.isdigit():
        num_6+=i
StringLiteralAmplifier=int(num_6)

M=linecache.getline(r'score.txt',7)
for i in M:
    if i.isdigit():
        num_7+=i
NumberLiteralAmplifier=int(num_7)

M=linecache.getline(r'score.txt',8)

for i in M:
    if i.isdigit():
        num_8+=i
BooleanLiteralAmplifier=int(num_8)

M=linecache.getline(r'score.txt',9)

for i in M:
    if i.isdigit():
        num_9+=i
CharLiteralAmplifier =int(num_9)

M=linecache.getline(r'score.txt',10)

for i in M:
    if i.isdigit():
        num_10+=i
AllLiteralAmplifiers=int(num_10)

M=linecache.getline(r'score.txt',11)

for i in M:
    if i.isdigit():
        num_11+=i
NullifierAmplifier =int(num_11)

combination=linecache.getline(r'MethodAdd+MethodRemove.txt',4)
for i in combination:
    if i.isdigit():
        num_combination+=i
count=int(num_combination)

list={
    'MethodAdd' : int(num_1),
    'MethodRemove' : int(num_2),
    'count' : int(num_combination)
}


print(list)



comb_1=input("Combination_1: ")
comb_2=input("Combination_2: ")
count=input("count")
CIS_1=list.get(comb_1)
CIS_2=list.get(comb_2)
bis=list.get(count)

print("CIS is ",(CIS_1+CIS_2-bis)/2)
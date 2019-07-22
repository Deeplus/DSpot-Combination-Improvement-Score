import linecache

########## obtain individual score #########
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

M=linecache.getline(r'score.txt',4)
for i in M:
    if i.isdigit():
        num_4+=i

M=linecache.getline(r'score.txt',5)
for i in M:
    if i.isdigit():
        num_5+=i

M=linecache.getline(r'score.txt',6)
for i in M:
    if i.isdigit():
        num_6+=i

M=linecache.getline(r'score.txt',7)
for i in M:
    if i.isdigit():
        num_7+=i

M=linecache.getline(r'score.txt',8)
for i in M:
    if i.isdigit():
        num_8+=i

M=linecache.getline(r'score.txt',9)
for i in M:
    if i.isdigit():
        num_9+=i

M=linecache.getline(r'score.txt',10)
for i in M:
    if i.isdigit():
        num_10+=i

M=linecache.getline(r'score.txt',11)
for i in M:
    if i.isdigit():
        num_11+=i

########## obtain combination score #########
combination=linecache.getline(r'/Users/dongzm/PycharmProjects/DSpot_CIS/Combination/MethodAdd+MethodRemove.txt',4)
for i in combination:
    if i.isdigit():
        num_combination+=i
count=int(num_combination)

########## make list #########
list={
    'MethodAdd' : int(num_1),
    'MethodRemove' : int(num_2),
    'TestDataMutator' : int(num_3),
    'MethodGeneratorAmplifier' : int(num_4),
    'ReturnValueAmplifier' : int(num_5),
    'StringLiteralAmplifier' : int(num_6),
    'NumberLiteralAmplifier' : int(num_7),
    'BooleanLiteralAmplifier' : int(num_8),
    'CharLiteralAmplifier' : int(num_9),
    'AllLiteralAmplifiers' : int(num_10),
    'NullifierAmplifier' : int(num_11),
    'yes' : int(num_combination)
}

#print(list)

comb_1=input("Combination_1: ")
comb_2=input("Combination_2: ")
yes=input("Do you want to Calculate [yes/no]：")
CIS_1=list.get(comb_1)
CIS_2=list.get(comb_2)
bis=list.get(yes)

########## save the result.txt #########
doc = open("/Users/dongzm/PycharmProjects/DSpot_CIS/Result/result.txt",'w')
print("The Combination Improvement Score is ",((bis-(CIS_1+CIS_2)))/2,file=doc)

doc.close()
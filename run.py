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
num_combination_2=""
num_combination_3=""

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
combination=linecache.getline(r'./Combination/3 kinds combinations/AllLiteralAmplifiers+MethodAdd+MethodGenerator.txt',5)
for i in combination:
    if i.isdigit():
        num_combination+=i
Bis_1=int(num_combination)

combination=linecache.getline(r'./Combination/3 kinds combinations/AllLiteralAmplifiers+MethodRemove+MethodGenerator.txt',5)
for i in combination:
    if i.isdigit():
        num_combination+=i
Bis_2=int(num_combination)

combination=linecache.getline(r'./Combination/3 kinds combinations/AllLiteralAmplifiers+ReturnValueAmplifier+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_3+=i
Bis_3=int(num_combination_3)


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
}


########## 3 kinds of combinations, split the method amplifier name #########
with open("./Combination/3 kinds combinations/AllLiteralAmplifiers+MethodAdd+MethodGenerator.txt", "r") as f:
    data = f.readline()

Method_1,Method_2,Method_3=data.split()

CIS_1=list.get(Method_1)
CIS_2=list.get(Method_2)
CIS_3=list.get(Method_3)

with open("./Combination/3 kinds combinations/AllLiteralAmplifiers+MethodRemove+MethodGenerator_report.txt", "r") as f:
    data = f.readline()

Method_1,Method_2,Method_3=data.split()

CIS_4=list.get(Method_1)
CIS_5=list.get(Method_2)
CIS_6=list.get(Method_3)

with open("./Combination/3 kinds combinations/AllLiteralAmplifiers+ReturnValueAmplifier+NullifierAmplifier.txt", "r") as f:
    data = f.readline()

Method_11,Method_22,Method_33=data.split()

CIS_7=list.get(Method_11)
CIS_8=list.get(Method_22)
CIS_9=list.get(Method_33)


########## save the result.txt #########
doc = open("./Result/3 kinds combination/AllLiteralAmplifiers+MethodAdd+MethodGenerator_result.txt",'w')
print("AllLiteralAmplifiers+MethodAdd+MethodGenerator CIS Score is",((Bis_1-(CIS_1+CIS_2+CIS_3)))/3,file=doc)
doc.close()

doc = open("./Result/3 kinds combination/AllLiteralAmplifiers+MethodRemove+MethodGenerator_result.txt",'w')
print("AllLiteralAmplifiers+MethodAdd+MethodGenerator CIS Score is",((Bis_2-(CIS_4+CIS_5+CIS_6)))/3,file=doc)
doc.close()

doc = open("./Result/3 kinds combination/AllLiteralAmplifiers+ReturnValueAmplifier+NullifierAmplifier_result.txt",'w')
print("AllLiteralAmplifiers+ReturnValueAmplifier+NullifierAmplifier CIS Score is",((Bis_3-(CIS_7+CIS_8+CIS_9)))/3,file=doc)
doc.close()

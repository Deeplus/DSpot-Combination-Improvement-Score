#!/usr/bin/python3

import linecache
import glob
import time

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

########## obtain 2 kinds combination score #########
num_combination=""
num_combination_2=""
num_combination_3=""
num_combination_4=""
num_combination_5=""
num_combination_6=""
num_combination_7=""
num_combination_8=""
num_combination_9=""
num_combination_10=""
num_combination_11=""
num_combination_12=""
num_combination_13=""
num_combination_14=""
num_combination_15=""
num_combination_16=""
num_combination_17=""
num_combination_18=""
num_combination_19=""
num_combination_20=""
num_combination_21=""
num_combination_22=""
num_combination_23=""
num_combination_24=""
num_combination_25=""
num_combination_26=""
num_combination_27=""

########## obtain 3 kinds combination score #########
num_combination_301=""
num_combination_302=""
num_combination_303=""
num_combination_304=""
num_combination_305=""
num_combination_306=""
num_combination_307=""
num_combination_308=""
num_combination_309=""
num_combination_310=""
num_combination_311=""
num_combination_312=""
num_combination_313=""
num_combination_314=""
num_combination_315=""
num_combination_316=""
num_combination_317=""
num_combination_318=""
num_combination_319=""
num_combination_320=""
num_combination_321=""
num_combination_322=""

########## obtain 4 kinds combination score #########
num_combination_401=""
num_combination_402=""
num_combination_403=""
num_combination_404=""
num_combination_405=""
num_combination_406=""
num_combination_407=""
num_combination_408=""
num_combination_409=""

########## obtain 5 kinds combination score #########
num_combination_501=""
num_combination_502=""

########## obtain 6 kinds combination score #########
num_combination_600=""

########## make list_1 #########
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

########## make list_2 #########
list={
    'MethodAdd' : int(num_1),
    'MethodRemove' : int(num_2),
    'FastLiteralAmplifier' : int(num_3),
    'MethodGeneratorAmplifier' : int(num_4),
    'ReturnValueAmplifier' : int(num_5),
    'StringLiteralAmplifier' : int(num_6),
    'NumberLiteralAmplifier' : int(num_7),
    'BooleanLiteralAmplifier' : int(num_8),
    'CharLiteralAmplifier' : int(num_9),
    'AllLiteralAmplifiers' : int(num_10),
    'NullifierAmplifier' : int(num_11),
}


########## obtain the 2 kinds of combination score #########
combination=linecache.getline(r'./Combination/jsoup-AllLiteralAmplifiers+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination+=i
Bis_1=int(num_combination)

combination=linecache.getline(r'./Combination/jsoup-AllLiteralAmplifiers+ReturnValueAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_2+=i
Bis_2=int(num_combination_2)

combination=linecache.getline(r'./Combination/jsoup-BooleanLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_3+=i
Bis_3=int(num_combination_3)

combination=linecache.getline(r'./Combination/jsoup-MethodAdd+MethodGenerator.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_4+=i
Bis_4=int(num_combination_4)

combination=linecache.getline(r'./Combination/jsoup-MethodAdd+MethodRemove.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_5+=i
Bis_5=int(num_combination_5)

combination=linecache.getline(r'./Combination/jsoup-MethodGenerator+BooleanLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_6+=i
Bis_6=int(num_combination_6)

combination=linecache.getline(r'./Combination/jsoup-MethodGenerator+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_7+=i
Bis_7=int(num_combination_7)

combination=linecache.getline(r'./Combination/jsoup-MethodGenerator+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_8+=i
Bis_8=int(num_combination_8)

combination=linecache.getline(r'./Combination/jsoup-MethodGenerator+NumberLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_9+=i
Bis_9=int(num_combination_9)

combination=linecache.getline(r'./Combination/jsoup-MethodGenerator+ReturnValueAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_10+=i
Bis_10=int(num_combination_10)

combination=linecache.getline(r'./Combination/jsoup-MethodGenerator+StringLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_11+=i
Bis_11=int(num_combination_11)

combination=linecache.getline(r'./Combination/jsoup-MethodRemove+MethodGenerator.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_12+=i
Bis_12=int(num_combination_12)

combination=linecache.getline(r'./Combination/jsoup-MethodRemove+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_13+=i
Bis_13=int(num_combination_13)

combination=linecache.getline(r'./Combination/jsoup-MethodRemove+ReturnValueAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_14+=i
Bis_14=int(num_combination_14)

combination=linecache.getline(r'./Combination/jsoup-NumberLiteralAmplifier+BooleanLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_15+=i
Bis_15=int(num_combination_15)

combination=linecache.getline(r'./Combination/jsoup-NumberLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_16+=i
Bis_16=int(num_combination_16)

combination=linecache.getline(r'./Combination/jsoup-ReturnValueAmplifier+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_17+=i
Bis_17=int(num_combination_17)

combination=linecache.getline(r'./Combination/jsoup-StringLiteralAmplifier+BooleanLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_18+=i
Bis_18=int(num_combination_18)

combination=linecache.getline(r'./Combination/jsoup-StringLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_19+=i
Bis_19=int(num_combination_19)

combination=linecache.getline(r'./Combination/jsoup-StringLiteralAmplifier+NumberLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_20+=i
Bis_20=int(num_combination_20)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+AllLiteralAmplifiers.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_21+=i
Bis_21=int(num_combination_21)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+BooleanLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_22+=i
Bis_22=int(num_combination_22)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_23+=i
Bis_23=int(num_combination_23)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_24+=i
Bis_24=int(num_combination_24)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+NumberLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_25+=i
Bis_25=int(num_combination_25)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+ReturnValueAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_26+=i
Bis_26=int(num_combination_26)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_27+=i
Bis_27=int(num_combination_27)

########## obtain the 3 kinds of combination score #########
combination=linecache.getline(r'./Combination/jsoup-AllLiteralAmplifiers+MethodAdd+MethodGenerator.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_301+=i
Bis_301=int(num_combination_301)


combination=linecache.getline(r'./Combination/jsoup-AllLiteralAmplifiers+MethodRemove+MethodGenerator_report.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_302+=i
Bis_302=int(num_combination_302)

combination=linecache.getline(r'./Combination/jsoup-AllLiteralAmplifiers+ReturnValueAmplifier+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_303+=i
Bis_303=int(num_combination_303)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_304+=i
Bis_304=int(num_combination_304)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodGenerator.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_305+=i
Bis_305=int(num_combination_305)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_306+=i
Bis_306=int(num_combination_306)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+MethodRemove+MethodGenerator.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_307+=i
Bis_307=int(num_combination_307)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_308+=i
Bis_308=int(num_combination_308)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_309+=i
Bis_309=int(num_combination_309)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+ReturnValueAmplifier+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_310+=i
Bis_310=int(num_combination_310)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+BooleanLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_311+=i
Bis_311=int(num_combination_311)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_312+=i
Bis_312=int(num_combination_312)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_313+=i
Bis_313=int(num_combination_313)

combination=linecache.getline(r'./Combination/jsoup-MethodAdd+MethodRemove+MethodGenerator.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_314+=i
Bis_314=int(num_combination_314)

combination=linecache.getline(r'./Combination/jsoup-MethodRemove+FastLiteralAmplifier+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_315+=i
Bis_315=int(num_combination_315)

combination=linecache.getline(r'./Combination/jsoup-MethodRemove+FastLiteralAmplifier+ReturnValueAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_316+=i
Bis_316=int(num_combination_316)

combination=linecache.getline(r'./Combination/jsoup-MethodRemove+MethodGenerator+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_317+=i
Bis_317=int(num_combination_317)

combination=linecache.getline(r'./Combination/jsoup-MethodRemove+MethodGenerator+ReturnValueAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_318+=i
Bis_318=int(num_combination_318)

combination=linecache.getline(r'./Combination/jsoup-NumberLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_319+=i
Bis_319=int(num_combination_319)

combination=linecache.getline(r'./Combination/jsoup-StringLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_320+=i
Bis_320=int(num_combination_320)

combination=linecache.getline(r'./Combination/jsoup-StringLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_321+=i
Bis_321=int(num_combination_321)

combination=linecache.getline(r'./Combination/jsoup-StringLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_322+=i
Bis_322=int(num_combination_322)

########## obtain the 4 kinds of combination score #########
combination=linecache.getline(r'./Combination/jsoup-AllLiteralAmplifiers+MethodAdd+MethodRemove+MethodGenerator.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_401+=i
Bis_401=int(num_combination_401)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_402+=i
Bis_402=int(num_combination_402)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_403+=i
Bis_403=int(num_combination_403)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_404+=i
Bis_404=int(num_combination_404)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_405+=i
Bis_405=int(num_combination_405)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_406+=i
Bis_406=int(num_combination_406)

combination=linecache.getline(r'./Combination/jsoup-MethodRemove+MethodGenerator+FastLiteralAmplifier+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_407+=i
Bis_407=int(num_combination_407)

combination=linecache.getline(r'./Combination/jsoup-MethodRemove+MethodGenerator+FastLiteralAmplifier+ReturnValueAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_408+=i
Bis_408=int(num_combination_408)

combination=linecache.getline(r'./Combination/jsoup-MethodRemove+MethodGenerator+ReturnValueAmplifier+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_409+=i
Bis_409=int(num_combination_409)
########## obtain the 5 kinds of combination score #########
combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+NullifierAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_501+=i
Bis_501=int(num_combination_501)

combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+ReturnValueAmplifier.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_502+=i
Bis_502=int(num_combination_502)

########## obtain the 6 kinds of combination score #########
combination=linecache.getline(r'./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+NullifierAmplifier+ReturnValueAm.txt',5)
for i in combination:
    if i.isdigit():
        num_combination_600+=i
Bis_600=int(num_combination_600)



########## 2 kinds of combinations, split the method amplifier name #########
with open("./Combination/jsoup-AllLiteralAmplifiers+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_1,Method_2=data.split()
CIS_1=list.get(Method_1)
CIS_2=list.get(Method_2)

with open("./Combination/jsoup-AllLiteralAmplifiers+ReturnValueAmplifier.txt", "r") as f:
    data = f.readline()
Method_3,Method_4=data.split()
CIS_3=list.get(Method_3)
CIS_4=list.get(Method_4)

with open("./Combination/jsoup-BooleanLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_5,Method_6=data.split()
CIS_5=list.get(Method_5)
CIS_6=list.get(Method_6)

with open("./Combination/jsoup-MethodAdd+MethodGenerator.txt", "r") as f:
    data = f.readline()
Method_7,Method_8=data.split()
CIS_7=list.get(Method_7)
CIS_8=list.get(Method_8)

with open("./Combination/jsoup-MethodAdd+MethodRemove.txt", "r") as f:
    data = f.readline()
Method_9,Method_10=data.split()
CIS_9=list.get(Method_9)
CIS_10=list.get(Method_10)

with open("./Combination/jsoup-MethodGenerator+BooleanLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_11,Method_12=data.split()
CIS_11=list.get(Method_11)
CIS_12=list.get(Method_12)

with open("./Combination/jsoup-MethodGenerator+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_13,Method_14=data.split()
CIS_13=list.get(Method_13)
CIS_14=list.get(Method_14)

with open("./Combination/jsoup-MethodGenerator+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_15,Method_16=data.split()
CIS_15=list.get(Method_15)
CIS_16=list.get(Method_16)

with open("./Combination/jsoup-MethodGenerator+NumberLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_17,Method_18=data.split()
CIS_17=list.get(Method_17)
CIS_18=list.get(Method_18)

with open("./Combination/jsoup-MethodGenerator+ReturnValueAmplifier.txt", "r") as f:
    data = f.readline()
Method_19,Method_20=data.split()
CIS_19=list.get(Method_19)
CIS_20=list.get(Method_20)

with open("./Combination/jsoup-MethodGenerator+StringLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_21,Method_22=data.split()
CIS_21=list.get(Method_21)
CIS_22=list.get(Method_22)

with open("./Combination/jsoup-MethodRemove+MethodGenerator.txt", "r") as f:
    data = f.readline()
Method_23,Method_24=data.split()
CIS_23=list.get(Method_23)
CIS_24=list.get(Method_24)

with open("./Combination/jsoup-MethodRemove+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_25,Method_26=data.split()
CIS_25=list.get(Method_25)
CIS_26=list.get(Method_26)

with open("./Combination/jsoup-MethodRemove+ReturnValueAmplifier.txt", "r") as f:
    data = f.readline()
Method_27,Method_28=data.split()
CIS_27=list.get(Method_27)
CIS_28=list.get(Method_28)

with open("./Combination/jsoup-NumberLiteralAmplifier+BooleanLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_29,Method_30=data.split()
CIS_29=list.get(Method_29)
CIS_30=list.get(Method_30)

with open("./Combination/jsoup-NumberLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_31,Method_32=data.split()
CIS_31=list.get(Method_31)
CIS_32=list.get(Method_32)

with open("./Combination/jsoup-ReturnValueAmplifier+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_33,Method_34=data.split()
CIS_33=list.get(Method_33)
CIS_34=list.get(Method_34)

with open("./Combination/jsoup-StringLiteralAmplifier+BooleanLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_35,Method_36=data.split()
CIS_35=list.get(Method_35)
CIS_36=list.get(Method_36)

with open("./Combination/jsoup-StringLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_37,Method_38=data.split()
CIS_37=list.get(Method_27)
CIS_38=list.get(Method_28)

with open("./Combination/jsoup-StringLiteralAmplifier+NumberLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_39,Method_40=data.split()
CIS_39=list.get(Method_39)
CIS_40=list.get(Method_40)

with open("./Combination/jsoup-FastLiteralAmplifier+AllLiteralAmplifiers.txt", "r") as f:
    data = f.readline()
Method_41,Method_42=data.split()
CIS_41=list.get(Method_41)
CIS_42=list.get(Method_42)

with open("./Combination/jsoup-FastLiteralAmplifier+BooleanLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_43,Method_44=data.split()
CIS_43=list.get(Method_43)
CIS_44=list.get(Method_44)

with open("./Combination/jsoup-FastLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_45,Method_46=data.split()
CIS_45=list.get(Method_45)
CIS_46=list.get(Method_46)

with open("./Combination/jsoup-FastLiteralAmplifier+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_47,Method_48=data.split()
CIS_47=list.get(Method_47)
CIS_48=list.get(Method_48)

with open("./Combination/jsoup-FastLiteralAmplifier+NumberLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_49,Method_50=data.split()
CIS_49=list.get(Method_49)
CIS_50=list.get(Method_50)

with open("./Combination/jsoup-FastLiteralAmplifier+ReturnValueAmplifier.txt", "r") as f:
    data = f.readline()
Method_51,Method_52=data.split()
CIS_51=list.get(Method_51)
CIS_52=list.get(Method_52)

with open("./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_53,Method_54=data.split()
CIS_53=list.get(Method_53)
CIS_54=list.get(Method_54)

########## 3 kinds of combinations, split the method amplifier name #########
with open("./Combination/jsoup-AllLiteralAmplifiers+MethodAdd+MethodGenerator.txt", "r") as f:
    data = f.readline()
Method_3301,Method_301,Method_302=data.split()
CIS_3301=list.get(Method_3301)
CIS_301=list.get(Method_301)
CIS_302=list.get(Method_302)


with open("./Combination/jsoup-AllLiteralAmplifiers+MethodRemove+MethodGenerator_report.txt", "r") as f:
    data = f.readline()
Method_3303,Method_303,Method_304=data.split()
CIS_3303=list.get(Method_3303)
CIS_303=list.get(Method_303)
CIS_304=list.get(Method_304)

with open("./Combination/jsoup-AllLiteralAmplifiers+ReturnValueAmplifier+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_3305,Method_305,Method_306=data.split()
CIS_3305=list.get(Method_3305)
CIS_305=list.get(Method_305)
CIS_306=list.get(Method_306)

with open("./Combination/jsoup-FastLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_3307,Method_307,Method_308=data.split()
CIS_3307=list.get(Method_3307)
CIS_307=list.get(Method_307)
CIS_308=list.get(Method_308)

with open("./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodGenerator.txt", "r") as f:
    data = f.readline()
Method_3309,Method_309,Method_310=data.split()
CIS_3309=list.get(Method_3309)
CIS_309=list.get(Method_309)
CIS_310=list.get(Method_310)

with open("./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove.txt", "r") as f:
    data = f.readline()
Method_3311,Method_311,Method_312=data.split()
CIS_3311=list.get(Method_3311)
CIS_311=list.get(Method_311)
CIS_312=list.get(Method_312)

with open("./Combination/jsoup-FastLiteralAmplifier+MethodRemove+MethodGenerator.txt", "r") as f:
    data = f.readline()
Method_3313,Method_313,Method_314=data.split()
CIS_3313=list.get(Method_3313)
CIS_313=list.get(Method_313)
CIS_314=list.get(Method_314)

with open("./Combination/jsoup-FastLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_3315,Method_315,Method_316=data.split()
CIS_3315=list.get(Method_3315)
CIS_315=list.get(Method_315)
CIS_316=list.get(Method_316)

with open("./Combination/jsoup-FastLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_3317,Method_317,Method_318=data.split()
CIS_3317=list.get(Method_3317)
CIS_317=list.get(Method_317)
CIS_318=list.get(Method_318)

with open("./Combination/jsoup-FastLiteralAmplifier+ReturnValueAmplifier+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_3319,Method_319,Method_320=data.split()
CIS_3319=list.get(Method_3319)
CIS_319=list.get(Method_319)
CIS_320=list.get(Method_320)

with open("./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+BooleanLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_3321,Method_321,Method_322=data.split()
CIS_3321=list.get(Method_3321)
CIS_321=list.get(Method_321)
CIS_322=list.get(Method_322)

with open("./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_3323,Method_323,Method_324=data.split()
CIS_3323=list.get(Method_3323)
CIS_323=list.get(Method_323)
CIS_324=list.get(Method_324)

with open("./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_3325,Method_325,Method_326=data.split()
CIS_3325=list.get(Method_3325)
CIS_325=list.get(Method_325)
CIS_326=list.get(Method_326)

with open("./Combination/jsoup-MethodAdd+MethodRemove+MethodGenerator.txt", "r") as f:
    data = f.readline()
Method_3327,Method_327,Method_328=data.split()
CIS_3327=list.get(Method_3327)
CIS_327=list.get(Method_327)
CIS_328=list.get(Method_328)

with open("./Combination/jsoup-MethodRemove+FastLiteralAmplifier+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_3329,Method_329,Method_330=data.split()
CIS_3329=list.get(Method_3329)
CIS_329=list.get(Method_329)
CIS_330=list.get(Method_330)

with open("./Combination/jsoup-MethodRemove+FastLiteralAmplifier+ReturnValueAmplifier.txt", "r") as f:
    data = f.readline()
Method_3331,Method_331,Method_332=data.split()
CIS_3331=list.get(Method_3331)
CIS_331=list.get(Method_331)
CIS_332=list.get(Method_332)

with open("./Combination/jsoup-MethodRemove+MethodGenerator+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_3333,Method_333,Method_334=data.split()
CIS_3333=list.get(Method_3333)
CIS_333=list.get(Method_333)
CIS_334=list.get(Method_334)

with open("./Combination/jsoup-MethodRemove+MethodGenerator+ReturnValueAmplifier.txt", "r") as f:
    data = f.readline()
Method_3335,Method_335,Method_336=data.split()
CIS_3335=list.get(Method_3335)
CIS_335=list.get(Method_335)
CIS_336=list.get(Method_336)

with open("./Combination/jsoup-NumberLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_3337,Method_337,Method_338=data.split()
CIS_3337=list.get(Method_3337)
CIS_337=list.get(Method_337)
CIS_338=list.get(Method_338)

with open("./Combination/jsoup-StringLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_3339,Method_339,Method_340=data.split()
CIS_3339=list.get(Method_3339)
CIS_339=list.get(Method_339)
CIS_340=list.get(Method_340)

with open("./Combination/jsoup-StringLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_3341,Method_341,Method_342=data.split()
CIS_3341=list.get(Method_3341)
CIS_341=list.get(Method_341)
CIS_342=list.get(Method_342)

with open("./Combination/jsoup-StringLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_3343,Method_343,Method_344=data.split()
CIS_3343=list.get(Method_3343)
CIS_343=list.get(Method_343)
CIS_344=list.get(Method_344)

########## 4 kinds of combinations, split the method amplifier name #########
with open("./Combination/jsoup-AllLiteralAmplifiers+MethodAdd+MethodRemove+MethodGenerator.txt", "r") as f:
    data = f.readline()
Method_401,Method_402,Method_403,Method_404=data.split()
CIS_401=list.get(Method_401)
CIS_402=list.get(Method_402)
CIS_403=list.get(Method_403)
CIS_404=list.get(Method_404)

with open("./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator.txt", "r") as f:
    data = f.readline()
Method_405,Method_406,Method_407,Method_408=data.split()
CIS_405=list.get(Method_405)
CIS_406=list.get(Method_406)
CIS_407=list.get(Method_407)
CIS_408=list.get(Method_408)

with open("./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_409,Method_410,Method_411,Method_412=data.split()
CIS_409=list.get(Method_409)
CIS_410=list.get(Method_410)
CIS_411=list.get(Method_411)
CIS_412=list.get(Method_412)

with open("./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_413,Method_414,Method_415,Method_416=data.split()
CIS_413=list.get(Method_413)
CIS_414=list.get(Method_414)
CIS_415=list.get(Method_415)
CIS_416=list.get(Method_416)

with open("./Combination/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_417,Method_418,Method_419,Method_420=data.split()
CIS_417=list.get(Method_417)
CIS_418=list.get(Method_418)
CIS_419=list.get(Method_419)
CIS_420=list.get(Method_420)

with open("./Combination/jsoup-FastLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.txt", "r") as f:
    data = f.readline()
Method_421,Method_422,Method_423,Method_424=data.split()
CIS_421=list.get(Method_421)
CIS_422=list.get(Method_422)
CIS_423=list.get(Method_423)
CIS_424=list.get(Method_424)

with open("./Combination/jsoup-MethodRemove+MethodGenerator+FastLiteralAmplifier+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_425,Method_426,Method_427,Method_428=data.split()
CIS_425=list.get(Method_425)
CIS_426=list.get(Method_426)
CIS_427=list.get(Method_427)
CIS_428=list.get(Method_428)

with open("./Combination/jsoup-MethodRemove+MethodGenerator+FastLiteralAmplifier+ReturnValueAmplifier.txt", "r") as f:
    data = f.readline()
Method_429,Method_430,Method_431,Method_432=data.split()
CIS_429=list.get(Method_429)
CIS_430=list.get(Method_430)
CIS_431=list.get(Method_431)
CIS_432=list.get(Method_432)

with open("./Combination/jsoup-MethodRemove+MethodGenerator+ReturnValueAmplifier+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_433,Method_434,Method_435,Method_436=data.split()
CIS_433=list.get(Method_433)
CIS_434=list.get(Method_434)
CIS_435=list.get(Method_435)
CIS_436=list.get(Method_436)

########## 5 kinds of combinations, split the method amplifier name #########
with open("./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+NullifierAmplifier.txt", "r") as f:
    data = f.readline()
Method_501,Method_502,Method_503,Method_504,Method_505=data.split()
CIS_501=list.get(Method_501)
CIS_502=list.get(Method_502)
CIS_503=list.get(Method_503)
CIS_504=list.get(Method_504)
CIS_505=list.get(Method_505)

with open("./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+ReturnValueAmplifier.txt", "r") as f:
    data = f.readline()
Method_506,Method_507,Method_508,Method_509,Method_510=data.split()
CIS_506=list.get(Method_506)
CIS_507=list.get(Method_507)
CIS_508=list.get(Method_508)
CIS_509=list.get(Method_509)
CIS_510=list.get(Method_510)

########## 6 kinds of combinations, split the method amplifier name #########
with open("./Combination/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+NullifierAmplifier+ReturnValueAm.txt", "r") as f:
    data = f.readline()
Method_601,Method_602,Method_603,Method_604,Method_605,Method_606=data.split()
CIS_601=list.get(Method_601)
CIS_602=list.get(Method_602)
CIS_603=list.get(Method_603)
CIS_604=list.get(Method_604)
CIS_605=list.get(Method_605)
CIS_606=list.get(Method_606)


########## save the 2 kinds of combinations result.txt #########
doc = open("./Result/jsoup-AllLiteralAmplifiers+NullifierAmplifier.csv",'w')
print("jsoup-AllLiteralAmplifiers+NullifierAmplifier CIS Score is",((Bis_1-(CIS_1+CIS_2)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-AllLiteralAmplifiers+ReturnValueAmplifier.csv",'w')
print("jsoup-AllLiteralAmplifiers+ReturnValueAmplifier CIS Score is",((Bis_2-(CIS_3+CIS_4)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-BooleanLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-BooleanLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_3-(CIS_5+CIS_6)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodAdd+MethodGenerator.csv",'w')
print("jsoup-MethodAdd+MethodGenerator CIS Score is",((Bis_4-(CIS_7+CIS_8)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodAdd+MethodRemove.csv",'w')
print("jsoup-MethodAdd+MethodRemove CIS Score is",((Bis_5-(CIS_9+CIS_10)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodGenerator+BooleanLiteralAmplifier.csv",'w')
print("jsoup-MethodGenerator+BooleanLiteralAmplifier CIS Score is",((Bis_6-(CIS_11+CIS_12)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodGenerator+CharLiteralAmplifier.csv",'w')
print("jsoup-MethodGenerator+CharLiteralAmplifier CIS Score is",((Bis_7-(CIS_13+CIS_14)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodGenerator+NullifierAmplifier.csv",'w')
print("jsoup-MethodGenerator+NullifierAmplifier CIS Score is",((Bis_8-(CIS_15+CIS_16)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodGenerator+NumberLiteralAmplifier.csv",'w')
print("jsoup-MethodGenerator+NumberLiteralAmplifier CIS Score is",((Bis_9-(CIS_17+CIS_18)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodGenerator+ReturnValueAmplifier.csv",'w')
print("jsoup-MethodGenerator+ReturnValueAmplifier CIS Score is",((Bis_10-(CIS_19+CIS_20)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodGenerator+StringLiteralAmplifier.csv",'w')
print("jsoup-MethodGenerator+StringLiteralAmplifier CIS Score is",((Bis_11-(CIS_21+CIS_22)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodRemove+MethodGenerator.csv",'w')
print("jsoup-MethodRemove+MethodGenerator CIS Score is",((Bis_12-(CIS_23+CIS_24)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodRemove+NullifierAmplifier.csv",'w')
print("jsoup-MethodRemove+NullifierAmplifier CIS Score is",((Bis_13-(CIS_25+CIS_26)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodRemove+ReturnValueAmplifier.csv",'w')
print("jsoup-MethodRemove+ReturnValueAmplifier CIS Score is",((Bis_14-(CIS_27+CIS_28)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-NumberLiteralAmplifier+BooleanLiteralAmplifier.csv",'w')
print("jsoup-NumberLiteralAmplifier+BooleanLiteralAmplifier CIS Score is",((Bis_15-(CIS_29+CIS_30)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-NumberLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-NumberLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_16-(CIS_31+CIS_32)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-ReturnValueAmplifier+NullifierAmplifier.csv",'w')
print("jsoup-ReturnValueAmplifier+NullifierAmplifier CIS Score is",((Bis_17-(CIS_33+CIS_34)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-StringLiteralAmplifier+BooleanLiteralAmplifier.csv",'w')
print("jsoup-StringLiteralAmplifier+BooleanLiteralAmplifier CIS Score is",((Bis_18-(CIS_35+CIS_36)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-StringLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-StringLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_19-(CIS_37+CIS_38)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-StringLiteralAmplifier+NumberLiteralAmplifier.csv",'w')
print("jsoup-StringLiteralAmplifier+NumberLiteralAmplifier CIS Score is",((Bis_20-(CIS_39+CIS_40)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+AllLiteralAmplifiers.csv",'w')
print("jsoup-FastLiteralAmplifier+AllLiteralAmplifiers CIS Score is",((Bis_21-(CIS_41+CIS_42)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+BooleanLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+BooleanLiteralAmplifier CIS Score is",((Bis_22-(CIS_43+CIS_44)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_23-(CIS_45+CIS_46)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+NullifierAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+NullifierAmplifier CIS Score is",((Bis_24-(CIS_47+CIS_49)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+NumberLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+NumberLiteralAmplifier CIS Score is",((Bis_25-(CIS_49+CIS_50)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+ReturnValueAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+ReturnValueAmplifier CIS Score is",((Bis_26-(CIS_51+CIS_52)))/2,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+StringLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+StringLiteralAmplifier CIS Score is",((Bis_27-(CIS_53+CIS_54)))/2,file=doc)
doc.close()

########## save the 3 kinds of combinations result.txt #########
doc = open("./Result/jsoup-AllLiteralAmplifiers+MethodAdd+MethodGenerator.csv",'w')
print("jsoup-AllLiteralAmplifiers+MethodAdd+MethodGenerator CIS Score is",((Bis_301-(CIS_3301+CIS_301+CIS_302)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-AllLiteralAmplifiers+MethodRemove+MethodGenerator_report.csv",'w')
print("jsoup-AllLiteralAmplifiers+MethodRemove+MethodGenerator_report CIS Score is",((Bis_302-(CIS_3303+CIS_303+CIS_304)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-AllLiteralAmplifiers+ReturnValueAmplifier+NullifierAmplifier.csv",'w')
print("jsoup-AllLiteralAmplifiers+ReturnValueAmplifier+NullifierAmplifier CIS Score is",((Bis_303-(CIS_3305+CIS_305+CIS_306)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_304-(CIS_3307+CIS_307+CIS_308)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+MethodAdd+MethodGenerator.csv",'w')
print("jsoup-FastLiteralAmplifier+MethodAdd+MethodGenerator CIS Score is",((Bis_305-(CIS_3309+CIS_309+CIS_310)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove.csv",'w')
print("jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove CIS Score is",((Bis_306-(CIS_3311+CIS_311+CIS_312)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+MethodRemove+MethodGenerator.csv",'w')
print("jsoup-FastLiteralAmplifier+MethodRemove+MethodGenerator CIS Score is",((Bis_307-(CIS_3313+CIS_313+CIS_314)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier CIS Score is",((Bis_308-(CIS_3315+CIS_315+CIS_316)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_309-(CIS_3317+CIS_317+CIS_318)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+ReturnValueAmplifier+NullifierAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+ReturnValueAmplifier+NullifierAmplifier CIS Score is",((Bis_310-(CIS_3319+CIS_319+CIS_320)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+BooleanLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+StringLiteralAmplifier+BooleanLiteralAmplifier CIS Score is",((Bis_311-(CIS_3321+CIS_321+CIS_322)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+StringLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_312-(CIS_3323+CIS_323+CIS_324)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier CIS Score is",((Bis_313-(CIS_3325+CIS_325+CIS_326)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodAdd+MethodRemove+MethodGenerator.csv",'w')
print("jsoup-MethodAdd+MethodRemove+MethodGenerator CIS Score is",((Bis_314-(CIS_3327+CIS_327+CIS_328)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodRemove+FastLiteralAmplifier+NullifierAmplifier.csv",'w')
print("jsoup-MethodRemove+FastLiteralAmplifier+NullifierAmplifier CIS Score is",((Bis_315-(CIS_3329+CIS_329+CIS_330)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodRemove+FastLiteralAmplifier+ReturnValueAmplifier.csv",'w')
print("jsoup-MethodRemove+FastLiteralAmplifier+ReturnValueAmplifier CIS Score is",((Bis_316-(CIS_3331+CIS_331+CIS_332)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodRemove+MethodGenerator+NullifierAmplifier.csv",'w')
print("jsoup-MethodRemove+MethodGenerator+NullifierAmplifier CIS Score is",((Bis_317-(CIS_3333+CIS_333+CIS_334)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodRemove+MethodGenerator+ReturnValueAmplifier.csv",'w')
print("jsoup-MethodRemove+MethodGenerator+ReturnValueAmplifier CIS Score is",((Bis_318-(CIS_3335+CIS_335+CIS_336)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-NumberLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-NumberLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_319-(CIS_3337+CIS_337+CIS_338)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-StringLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-StringLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_320-(CIS_3339+CIS_339+CIS_340)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-StringLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier.csv",'w')
print("jsoup-StringLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier CIS Score is",((Bis_321-(CIS_3341+CIS_341+CIS_342)))/3,file=doc)
doc.close()

doc = open("./Result/jsoup-StringLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-StringLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_322-(CIS_3343+CIS_343+CIS_344)))/3,file=doc)
doc.close()

########## save the 4 kinds of combinations result.txt #########
doc = open("./Result/jsoup-AllLiteralAmplifiers+MethodAdd+MethodRemove+MethodGenerator.csv",'w')
print("jsoup-AllLiteralAmplifiers+MethodAdd+MethodRemove+MethodGenerator CIS Score is",((Bis_401-(CIS_401+CIS_402+CIS_403+CIS_404)))/4,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator.csv",'w')
print("jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator CIS Score is",((Bis_402-(CIS_405+CIS_406+CIS_407+CIS_408)))/4,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+StringLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_403-(CIS_409+CIS_410+CIS_411+CIS_412)))/4,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier+BooleanLiteralAmplifier CIS Score is",((Bis_404-(CIS_413+CIS_414+CIS_415+CIS_416)))/4,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+StringLiteralAmplifier+NumberLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_405-(CIS_417+CIS_418+CIS_419+CIS_420)))/4,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifierr+NumberLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifierr+NumberLiteralAmplifier+BooleanLiteralAmplifier+CharLiteralAmplifier CIS Score is",((Bis_406-(CIS_421+CIS_422+CIS_423+CIS_424)))/4,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodRemove+MethodGenerator+FastLiteralAmplifierr+NullifierAmplifier.csv",'w')
print("jsoup-MethodRemove+MethodGenerator+FastLiteralAmplifierr+NullifierAmplifier CIS Score is",((Bis_407-(CIS_425+CIS_426+CIS_427+CIS_428)))/4,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodRemove+MethodGenerator+FastLiteralAmplifierr+ReturnValueAmplifier.csv",'w')
print("jsoup-MethodRemove+MethodGenerator+FastLiteralAmplifierr+ReturnValueAmplifier CIS Score is",((Bis_408-(CIS_429+CIS_430+CIS_431+CIS_432)))/4,file=doc)
doc.close()

doc = open("./Result/jsoup-MethodRemove+MethodGenerator+ReturnValueAmplifier+NullifierAmplifier.csv",'w')
print("jsoup-MethodRemove+MethodGenerator+ReturnValueAmplifier+NullifierAmplifier CIS Score is",((Bis_409-(CIS_433+CIS_434+CIS_435+CIS_436)))/4,file=doc)
doc.close()

########## save the 5 kinds of combinations result.txt #########
doc = open("./Result/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+NullifierAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+NullifierAmplifier CIS Score is",((Bis_501-(CIS_501+CIS_502+CIS_503+CIS_504+CIS_505)))/5,file=doc)
doc.close()

doc = open("./Result/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+ReturnValueAmplifier.csv",'w')
print("jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+ReturnValueAmplifier CIS Score is",((Bis_502-(CIS_506+CIS_507+CIS_508+CIS_509+CIS_510)))/5,file=doc)
doc.close()
########## save the 6 kinds of combinations result.txt #########
doc = open("./Result/jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+NullifierAmplifier+ReturnValueAm.csv",'w')
print("jsoup-FastLiteralAmplifier+MethodAdd+MethodRemove+MethodGenerator+NullifierAmplifier+ReturnValueAm CIS Score is",((Bis_600-(CIS_601+CIS_602+CIS_603+CIS_604+CIS_605+CIS_606)))/6,file=doc)
doc.close()


##################### Generate the CSV file ###################################################
csvx_list = glob.glob('./Result/*.csv')
#print('Find %s CSV files'% len(csvx_list))

for i in csvx_list:
    fr = open(i,'r').read()
    with open('CIS.csv','a') as f:
        f.write(fr)

print('Finish the process！')
print('CIS data is saved in the CIS.csv file. ')
time.sleep(1)

import numpy as np

s=[["4x+3t=5q+o+j+40"],["4x+4z+2j=3q+4e+4t+2o+20"],["2t+9=5q+e+z+4o+3j"],["x+2e+2t+3z+o+4j=51"],["4q+73=5x+2e+3t+4o+3j"],["q+3z+2o+3j+19=5x+2e+t"],["2z+3j+1=3x+3q+2e+5o"]]
#ošetřit proti neznámým typu "1*q"
#s je testovací input
pocetRovnic=len(s)
listNeznamych = []
listLevychStran = []
listPravychStran = []
pocetNeznamych = 0
numbers = ["1","2","3","4","5","6","7","8","9","0"]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
found = 0
k = 0

#převod string -> int
def strint(list):
    l = list
    list = [[int(i) for i in list]for list in l]
    return list

# rovnaSeSplit rozdělení přes znak "="
def formatovaniRovnice(s):
    rovnaSeSplit=s.split("=") 
    levaStrana=rovnaSeSplit[0].split("+")
    pravaStrana=rovnaSeSplit[1].split("+")
    listLevychStran.append(levaStrana)
    listPravychStran.append(pravaStrana)
    for i in range(len(levaStrana)):
        x = levaStrana[i][-1]
        if x not in listNeznamych:
            if x in letters:
                listNeznamych.append(x)

    for i in range(len(pravaStrana)):
        x = pravaStrana[i][-1]
        if x not in listNeznamych:
            if x in letters:
                listNeznamych.append(x)

for i in range(pocetRovnic):
    formatovaniRovnice(s[i][0])
 
for i in range(len(listNeznamych)-1):
        if any(x in listNeznamych[i] for x in numbers):
            del listNeznamych[i]

pocetNeznamych = len(listNeznamych)
listNeznamych.sort()


for i in range(pocetRovnic):
    j=0
    while j<len(listPravychStran[i]):
        if not any(x in listPravychStran[i][j] for x in numbers):
            listPravychStran[i][j] = "1"+listPravychStran[i][j]
        if any(x in listPravychStran[i][j] for x in listNeznamych):
            listLevychStran[i].append("-"+listPravychStran[i][j])
            del listPravychStran[i][j]
        else:
            j+=1

for i in range(pocetRovnic):
    j=0        
    while j<len(listLevychStran[i]):
        if not any(x in listLevychStran[i][j] for x in numbers): #pokud mám vlevo něco jako "q" změním to na "1q"
            listLevychStran[i][j] = "1"+listLevychStran[i][j]
        if not any(x in listLevychStran[i][j] for x in listNeznamych):
            listPravychStran[i].append("-"+listLevychStran[i][j])
            del listLevychStran[i][j]
        else:
            j+=1

#vytvořím matici o [pocetRovnic] řádcích a [pocetNeznamých] sloupcích

matice = []

for i in range(len(listLevychStran)):
    matice.append([])
    for inzn in range(pocetNeznamych):
        for j in range(len(listLevychStran[i])):
            if listNeznamych[inzn] in listLevychStran[i][j]:
                listLevychStran[i][j] = listLevychStran[i][j][:-1]
                matice[k].append(listLevychStran[i][j])
                matice
                found = True
        if not found:
            matice[k].append(0)
        else:
            found = False
    k+=1

matice = strint(matice)
listPravychStran = strint(listPravychStran)
print(listPravychStran)

matice = np.array(matice)
listPravychStran = np.array(listPravychStran)

for i in range(len(s)):
    print(s[i])
print("listNeznamych:",listNeznamych)

print("matice")
for i in range(len(matice)):
    print(matice[i],listPravychStran[i])

x = np.linalg.solve(matice,listPravychStran)
print(x)

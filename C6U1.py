
s=[["4x+3t=5q+o+j+40"],["4x+4z+2j=3q+4e+4t+2o+20"],["2t+9=5q+e+z+4o+3j"],["x+2e+2t+3z+o+4j=51"],["4q+73=5x+2e+3t+4o+3j"],["q+3z+2o+3j+19=5x+2e+t"],["2z+3j+1=3x+3q+2e+5o]"]]

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
    l.clear
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
            listNeznamych.append(x)

    for i in range(len(pravaStrana)):
        x = pravaStrana[i][-1]
        if x not in listNeznamych:
            listNeznamych.append(x)

for i in range(pocetRovnic):
    formatovaniRovnice(s[i][0])
#

for i in range(len(listNeznamych)-2):
        if any(x in listNeznamych[i] for x in numbers):
            del listNeznamych[i]

pocetNeznamych = len(listNeznamych)
listNeznamych.sort()

for i in range(pocetRovnic):
    j=0
    while j<len(listPravychStran[i])-1:
        if any(x in listPravychStran[i][j] for x in listNeznamych):
            listLevychStran[i].append("-"+listPravychStran[i][j])
            del listPravychStran[i][j]
        else:
            j+=1

print(s)
print("listLevychStran:",listLevychStran)
print("listPravychStran:",listPravychStran)
print("listNeznamych:",listNeznamych)
print("pocetNeznamych:",pocetNeznamych)

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

print(strint(matice))
print(strint(listPravychStran))


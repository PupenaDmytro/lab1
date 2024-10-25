myfile0 = open(r'C:\Users\DmitroP\Downloads\Lab1 (1)\Lab1\student_marks\student_names.txt', 'r')
myfile1 = open(r'C:\Users\DmitroP\Downloads\Lab1 (1)\Lab1\student_marks\math.txt', 'r')
myfile2 = open(r'C:\Users\DmitroP\Downloads\Lab1 (1)\Lab1\student_marks\physics.txt', 'r')
myfile3 = open(r'C:\Users\DmitroP\Downloads\Lab1 (1)\Lab1\student_marks\statistics.txt', 'r')

names = myfile0.readlines()
math = myfile1.readlines()
physics = myfile2.readlines()
statistics = myfile3.readlines()
mathint = [int(item) for item in math]
physicsint = [int(item) for item in physics]
statisticsint = [int(item) for item in statistics]
i=0
avarage = []
best = [3,2,1]
bestnames = ["3","2","1"]
m=0
k=0
for element in names:
    libr = {names[i]:{"math" : math[i], "physics" : physics[i], "statistics" : statistics[i]}}
    print (names[i], "math", libr[names[i]]["math"],"physics" , libr[names[i]]["physics"], "statistics" , libr[names[i]]["statistics"],)
    avarage.append((mathint[i]+physicsint[i]+statisticsint[i])/3)
    print("середнє арифметичне =",avarage[i],"\n")
    i=i+1
print("усього студентів =",i)
i=0
for element in names:
    if best[0]<avarage[i]:
        del best[0]
        del bestnames[0]
        best.append(avarage[i])
        bestnames.append(names[i])
    i=i+1
print("найкращі студенти","\n",bestnames[0], best[0],"\n", bestnames[1], best[1],"\n", bestnames[2], best[2],"\n")
i=0
print ("math" ,"середнє", sum(mathint)/len(mathint),"макс", max(mathint),"мін", min(mathint))
print ("physics" ,"середнє", sum(physicsint)/len(physicsint),"макс",max(physicsint),"мін", min(physicsint))
print ("statistics" ,"середнє", sum(statisticsint)/len(statisticsint),"макс",max(statisticsint),"мін", min(statisticsint))
for element in names:
    if k<mathint[i]:
        k = mathint[i]
        name = (names[i])
    i=i+1
print("\n math", name, k)
i=0
for element in names:
    if k<physicsint[i]:
        k = physicsint[i]
        name = (names[i])
    i=i+1
print("\n physics", name, k)
i=0
for element in names:
    if k<statisticsint[i]:
        k = statisticsint[i]
        name = (names[i])
    i=i+1
print("\n statistics", name, k)
i=0
print("\n Учні у яких менше 50 балів")
for element in names:
    if 50>avarage[i]:
        print (names[i], avarage[i],"\n")
    i=i+1

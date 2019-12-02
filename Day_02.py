data = open("Day_02_input.txt", "r")  
for line in data :
    field = line.split(",")
data.close()  
 
for noun in range(100) :
    for verb in range(100) :
        liste=[ int(x) for x in field]
        liste[1] = noun
        liste[2] = verb 
        
        r = 0
        while liste[r] != 99 :
            if liste[r] == 1 :
                liste[liste[r+3]] = liste[liste[r+1]] + liste[liste[r+2]]
            if liste[r] == 2 :
                liste[liste[r+3]] = liste[liste[r+1]] * liste[liste[r+2]]
            r = r + 4
        if liste[0] == 19690720 :
            print(100*noun + verb)

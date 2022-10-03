import random
a = int(input("Input first number from 1 to 6: "))
b = int(input("Input first number from 1 to 6: "))
d = a, b
answer = list(d) #Convert d to a list
 
randList = []
for i in range(6) :
    randNumbers = random.randrange(0, 10)
    randList.append(randNumbers)
 
print ("The six random numbers are: ", randList)
print ("Your inputs are: ", answer)
 
#Now let's compare your inputs with the randomly generated number
 
compare = all(elem in randList for elem in answer)
if (compare) :
    print("Congratulation!!! You win...")
else :
    print ("Ooops!!! You lost...")

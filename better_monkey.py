L=[]
import math
R=3
C=7
for I in range(7):
    Row_E=[]
    for J in range(3):
        A=int(input(f"Enter the food Taken by monkey {int(J+1)} : "))
        Row_E.append(A)
    Row_E.append(int(sum(Row_E)/len(Row_E)))
    L.append(Row_E)
print(f"Monkey 1","\t","Monkey 2","\t""Monkey3","\t","Average",end="")
print()

for I in range(7):
    for J in range(4):
        print(L[I][J],"\t","\t",end="")
    print()
List_of_food_eaten_by_Monkey_1=[]
for I in range(7):
    for J in range(1):
        List_of_food_eaten_by_Monkey_1.append(L[I][J])
min_food=min(List_of_food_eaten_by_Monkey_1)
max_food=max(List_of_food_eaten_by_Monkey_1)
print()
print(f"The least amount of food eaten by monkey 1 is {min_food}")
print(f"The maximum amount of food eaten by monkey 1 is {max_food}")
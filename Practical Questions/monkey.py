#A local zoo..
L1=[]
L=['Monkey no.',"\t",'Sun',"\t"'Mon',"\t",'Tue',"\t",'Wed',"\t",'Thu',"\t",'Fri',"\t",'Sat']

for I in range(3):
    r_ele=[]
    print(f"This is for monkey no.  {I+1}")
    r_ele.append(int(I+1))
    for J in range(7):
        x=int(input("Please input the pounds of food eaten by the monkey"))
        if x>0:
            r_ele.append(x)
        else:
            print("please enter a positive value!")
            J-=1
    L1.append(r_ele)
print(L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7])
for row in L1:
    for item in row:
        print(item,"\t", end = " ")
           
    

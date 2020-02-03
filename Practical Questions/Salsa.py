#Write a python program that lets a maker of chips...
d={"mild":0,"medium":0,"sweet":0,"hot":0,"zesty":0}
d1={}
L=list(d)
for I in range(0,5,1):
    d1[L[I]]=int(input(f"Enter the number of sales for {L[I]}"))
for I in d1.values():
    ma=I
    mi=I
for I in d1.values():
    if I>ma:
        ma=I
    if I<mi:
        mi=I
print(f"The maximum sale is of {list(d1.keys())[list(d1.values()).index(ma)]} and the number of products sold are {int(ma)}")
print(f"The minimum sale is of {list(d1.keys())[list(d1.values()).index(mi)]} and the number of products sold are {int(mi)}")
print("The report of all the flavors is listed below: ")
for I in range(5):
    print(f"The sale of {L[I]} is {list(d1.values())[I]}" )

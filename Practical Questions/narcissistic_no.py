Range_ = int(input("Till what limit would you like the loop to continue?: "))
List_of_narcists = []
for I in range(Range_):
    string = str(I)
    sum = 0
    for J in string:
        sum+=int(J)**len(string)
    sum_ = int(sum)
    if sum_== I:
        List_of_narcists.append(I)
print(List_of_narcists)
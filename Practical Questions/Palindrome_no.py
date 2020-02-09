Range_ = int(input("Till what limit would you like the loop to continue?: "))
List_of_palindromes = []
for I in range(Range_):
    string_ = str(I)
    rev_ = string_[::-1]
    if string_==rev_:
        List_of_palindromes.append(I)
print(List_of_palindromes)
import sys
print("COWS N BULLS\n")

print("The rules are simple.Try to guess the secret word based on the clues")
print("Number of cows indicate the number of letters in your guess that are in the secret word but NOT in the right position")
print("Whereas Number of bulls indicate the number of letters in your guess that are in the secret word AND in the right position\n")

guesses=[ ]
guess=" "
Try=1
cows=bulls=0

answer=input("Enter the secret word(make sure the letters are not repeated,I'm not paid to do this):")
for I in range(1,100):#for hiding answer
    print()

while True:
    print("Try",Try)
    if Try==1:
        print("hint:the secret word has",len(answer),"letters\n")
    guess=input("Enter your guess:")
    if len(guess)!=len(answer):
        print("\nTry again. The secret word has",len(answer),"letters\n")
    else:
        if guess==answer:
            print("You have guessed the correct word!")
            sys.exit()
        else:
                #bulls=correct letter in correct place
                for J in range(0,len(answer)):
                    if guess[J]==answer[J]:
                        bulls+=1       
                    else:#cows=correct letter in wrong place
                        for x in answer:
                            if x==guess[J]:
                                cows+=1

        print("cows=",cows)                   
        print("bulls=",bulls)
        print()
        cows=bulls=0
        Try+=1

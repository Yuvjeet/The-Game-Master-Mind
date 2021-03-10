def Check(guess_no,key_no):
    Guess_list,Key_list=list(str(guess_no)),list(str(key_no))
    position=exist=0
    for i in Guess_list:
        if i in Key_list:
            exist+=1
            if Key_list.index(i)==Guess_list.index(i):
                position+=1
    return exist-position,position
def user_guess():
    while True:
        try:
            guess=int(input("Guess : "))
        except:
            print("***contain non number, try again")
        else:
            if len(str(guess))==4:
                if len(set(str(guess)))==4:
                    return guess
                else:
                    print("No repeted digits, try again")
            else:
                print("guess must have length of 4, try again")
key=int(input("What is the key: "))
for i in range(1,13):
    guess_a_no=user_guess()
    exist,position=Check(guess_a_no,key)
    if exist==0 and position==4:
        print(f"You Guessed The Key: {guess_a_no}\nIt took you {i} guesses")
        break
    else:
        print(f"{guess_a_no}: exist:{exist},position:{position}")
else:
    print("Sorry Your all chance are over")


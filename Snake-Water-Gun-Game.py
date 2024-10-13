#Creating a game of snake, water and gun
import sys
import random
name=input("Enter your name:")
try:
    t=int(input("How many turns you want to play: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.Rerun the program.")
    sys.exit()
if(t>50 and t):
    print("Limit Exceed!")
    sys.exit()
print("Let's Play:-)")
options=['S','W','G']
choice={
    'S':'Snake',
    'W':'Water',
    'G':'Gun'
}
cScore=uScore=0            
i=0
while(i<t):
    uChoice=input("Choose 'S' for snake, 'W' for water and 'G' for gun: ").upper()
    cChoice=random.choice(options)
    if(uChoice not in options):
        print("Invalid choice.")
        continue
    elif(uChoice==cChoice):
        print(f"You have chosen {choice[uChoice]} and Computer has chosen {choice[cChoice]}.")
        print("It's a draw")
    else:
        print(f"You have chosen {choice[uChoice]} and Computer has chosen {choice[cChoice]}.")
        if(cChoice=='S' and uChoice=='W'):
            cScore+=1
            print("Computer Won!")
        elif(cChoice=='S' and uChoice=='G'):
            uScore+=1
            print("You Won!")
        elif(cChoice=='W' and uChoice=='S'):
            uScore+=1
            print("You Won!")
        elif(cChoice=='W' and uChoice=='G'):
            cScore+=1
            print("Computer Won!")
        elif(cChoice=='G' and uChoice=='S'):
            cScore+=1
            print("Computer Won!")
        elif(cChoice=='G' and uChoice=='W'):
            uScore+=1
            print("You Won!")
    print(f"Computer Score\t|\t{name} Score")
    print(f"\t{cScore}\t|\t\t{uScore}")
    i+=1
if(uScore>cScore):
    print("Congratulations! You won this game.")        
elif(uScore<cScore):
    print("Computer won! Better luck next time.")
else:
    print("Match Tied!")
print("Game Over")

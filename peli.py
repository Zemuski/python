from random import randint
import webbrowser


peli = False 
print("I want to play a game")
kysy = input("Do you want too? (yes/no)")
if kysy == "yes":
    print("veri nice")
    k = True
    while k == True:
        try:
            x = int(input("Lowest number please: "))
        except ValueError:
            print("A NUMBER plese...")
        else:
            k = False
            s = True
            while s == True:
                try:
                    y = int(input("Biggest number please: "))
                except ValueError:
                    print("A NUMBER plese...")
                else:
                    if y <= x:
                        print("It has to be bigger than the first one...")
                    else:
                        s = False
                        peli = True 
                        vastaus = randint(x,y)
else:
    print("Your loss...")





while peli == True:
    try: 
        luku = int(input("Guess a number: "))
    except  ValueError:
        print("It's propably a number")
    if luku < vastaus:
        print("too small")
    elif luku > vastaus:
        print("too big, sorry")
    else:
        print("that's the number bro!!!")
        print("You did it!!!")
        #uncomment, if you really want to feel the victory
        #webbrowser.open('https://www.youtube.com/watch?v=DhlPAj38rHc')
        peli = False


import random
count1=0
count2=0
print("How many round do you want to play?") 
n=int(input("Number of Rounds:"))  
for i in range(n):
    print("*-----Computer's Turn ------*")
    RandNo=random.randint(1,3)
    if(RandNo==1):
        computer="r"
    elif(RandNo==2):
        computer="p"
    else:
        computer="s"
            

        
    print("*------Your Turn: Rock(r) , Paper(p), Scissor(s)------*")
    you=input("Rock(r) , Paper(p) or Scissor(s)?")
    
    print("\n\n\n*------RESULT------*")
    
    bool=True
    if(computer==you):
        bool= None
    else:    
        if(computer=="r"):
            if(you=="p" or you=="P"):
                bool= True
            else:
                bool= False


        if(computer=="p"):
            if(you=="r" or you=="R"):
                bool= False
            else:
                bool= True   

        if(computer=="s"):
            if(you=="r" or you=="R"):
               bool= True
            else:
                bool= False  

    if(bool==True):
        count1=count1+1
        print(f"Congratulations!! You are winner.  Time= {count1} ")
    elif(bool==False):
        count2=count2+1
        print(f"Computer is winner.  Time= {count2}  ")
    else:
        print(f"Tie ")
    print(f"*Computer Chose {computer}")
    print(f"*You Chose {you}")

print("\n\n\n*------FINAL RESULT------*")
print(f"you:", end="   ")
print(f"Win: {count1}")
print(f"Computer:" , end="   ")
print(f"Win: {count2}")


  



     

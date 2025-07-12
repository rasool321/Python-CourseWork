bullets=10
while bullets>0: 
    if bullets>83:  
        print ("User dead, Game over")
        break   #if break executes then else not working
    bullets-=1
    print (f"shoot (), {bullets} are left")
else:
    print ("Game over. You win the game") #if else executes then break not working
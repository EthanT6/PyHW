#Loops

def main():
    x=0

    print("----while loop----")
    #define a while loop
    while (x<5):
        print(x)
        x = x + 1
    print("---for loop----")
    #define a for loop
    for x in range(5,10):
        print(x)

    print("----days of the week *clap* *clap*")
    #use a for loop over a collection
    days =["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]    
    for d in days:
        print(d)
    
    print("----breaks and continues----")
    #use the break and continue statements
    for x in range(5,10):
        #if (x==7): break
        if (x % 2 == 0): continue
        print(x)

    print("----days of the week electric boogaloo----")
    #using the enumerate() function to get index
    days =["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]    
    for i,d in enumerate(days):
        print(i, d)

if __name__ == "__main__":
    main()


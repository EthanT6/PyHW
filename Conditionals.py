#Conditionals

def main():
    x,y = 100,100

    #condition flow uses if,elif,else
    if (x<y):
        st = "x is less than y"
    elif(x==y):
        st = "x is equal to y"    
    else:
        st = "x is greater than y"

    print (st)

    #conditionals allow you to use "a if c else b"
    st = "x is less than y"if (x<y) else "x is greater than or the same as"
    print(st)

if __name__ == "__main__":
    main()
    

n=6
for row in range(0,n,1):
    for col in range(0,row+1,1):
        if col==0 or col==row or row==n-1:
            print(chr(65+row),end="")
        else:
            print(" ", end="")
        
    print()
#if n is odd, print odd
#if n is even, print even

if __name__ == '__main__':
    n=int(input().strip())

    if(n==0):
        print("Zero")
    elif(n%2==0):
        print("Even")
    else:
        print("Odd")



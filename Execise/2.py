def term(n):
    if n==1:
        return 1/2
    else:
        if n%2==0:
            return term(n-1)-1/(n*(n+1))
        else:
            return term(n-1)+1/(n*(n+1))
n=int (input("give me a num:"))
print(term(n))
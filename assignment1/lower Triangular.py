n=6

# lower Triangular Pattern:
for i in range (1,n):
    print("*"*i)


# Upper Triangular Pattern:
for i in range (1,n):
    print(" "*(i-1),"*"*(n-1))
    n=n-1


# Pyramid Pattern:
for i in range (1,n):
    print(" "*(n-i),"* "*i)
print()
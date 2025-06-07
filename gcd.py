#Why we did the loop here in reverse its because the gcd of both the number is the maximum of the common factors in both it can also be one of the number it self
# Time Complecity o(min(n1,n2))
def gcd(n1, n2):
    for i in range(min(n1,n2), 0, -1):
        if(n1%i==0 and n2%i==0):
            print(i)
        


# Can also be done using euclidean algorithm i,e gcd(a,b)=gcd(a-b,b) where a>b:
# Can also stated as gcd(a,b)=gcd(a%b,b) where a>b  => this is much better for programming whatch striver 58 min Basic Math for DSA
# Time Complexity o(log(min(a,b)))
def gcd_eculidean(a,b):
    while a!=0 and b!=0:
        if a>b and b!=0 :
            a=a%b
        elif a<b and a!=0 :
            b=b%a
    if a == 0:
        print("GCD: ",b)
    else:
        print("GCD: ",a)
    
    
n1 = int(input("n1: "))
n2 = int(input("n2: "))
# gcd(n1,n2)
gcd_eculidean(n1,n2)
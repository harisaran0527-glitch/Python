'''#4).Alphabet letters from a to z

for ch in range(ord('a'),ord('z')+1):
    print(chr(ch),end=" ")

#5).Reverse alphabet letters from z to a 
for ch in range(ord('z'),ord('a')-1,-1):
    print(chr(ch),end=" ")

#6).ASCII values
for ch in range(1,256):
    print(chr(ch),ch)

'''
# WHILE LOOP

'''#10).
a=int(input("Enter a number: "))
temp=a
s=0
while temp>0:
    s+=temp%10
    temp//=10
print(s)
if a%s==0:
    print("It is Harshad Number")
else:
    print("It is not Harshad Number")
   '''
'''
#11).Sum of divisor
a=int(input("Enter a number: "))
s=0
for i in range(1,a+1):
    if a%i==0:
        s+=i
print("Sum of divisor:",s)
'''


'''#12).Palindrome Number
a=int(input("Enter a number: "))
temp=a
b=0
while a>0:
    c=a%10
    b=b*10+c
    a=a//10
    print(b)
if b==temp:
    print("It is palindrome number")
else:
    print("It is not palindrome number")
'''

#13).Armstrong Number
a=int(input("Enter a number: "))
x=a
y=a
Ccount=0
b=0
while a>0:
    count+=1
    a=a//10
print(count)
ans=0
while x>0:
        c=x%10
        ans=ans+c**count
        x=x//10
print(ans)
if ans==y:
        print("It is Armstrong number")
else:
        print("It is not Armstrong number")
        

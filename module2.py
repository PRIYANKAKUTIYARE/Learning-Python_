#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      priya
#
# Created:     13-09-2025
# Copyright:   (c) priya 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      priya
#
# Created:     20-12-2023
# Copyright:   (c) priya 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
'''text1 = 'Priyanka \
'
print(text1)
str2 ="""Hello priyanka
me your friend
priviya"""
print(str2)
a = 123
b = 125E01
c = 0o12
d = 0xC
e = 35.65
f = None
print(a,b,c,d,e,f)
add1 = a+4
print(add1)
# i am learning this only for you
def SeeYou():
    print("Mujhe ye to sikhna hi hoga kaise bhi karke")
    a= 15
    b = 10
    if a-10>=5:
       print("it is greater than 5 ")
    else:
       print("not greater than 5")
    if b>5:
        tmp = a
        a = b
        b = tmp
        print(a,b)
    else :
        print("okk donee")
SeeYou()
 Mujhe ye to sikhna hi hoga kaise bhi karke
    a= 15
    b = 10
    if a-10>=5:
      print it is greater than 5
'''
'''x=y=z=10
print(x,y,z)
x,y = 10,25
print(x,y)

x,y = y,x
print(x,y,y,x)
p,q,r = 6,7,8
q,r,p = p+1,q+2,r+4
print(p,q,r)

print(x)
x=25
type(x)
'''
#name1  = input("what is your name? : ")
'''name2  = input("what is your age? : ")
age  = int(name2)
name3  = input("what is your marks? : ")
ag1 = age + 1
print(ag1)
float1 = float(name3)
flo1   = float1 + 1
print(flo1)'''
#DAY02 DATA HANDLING
'''Age = int (input("what is your age? "))
type(Age)
Marks = float (input("what marks you got? "))
type(Marks)'''
#a = 10
#type(a)

#print("sum of 2+3 is ", 2+3)


'''W = weight_in_KG = float (input("Enter your weight in KG"))
H = height_in_METER = float (input("Enter your height in meter"))
BMI = W/(H*H)
print("BMI is :", BMI)'''
'''
subject = 'computer'
print(subject[-1] )'''

'''id(4)
print(id(4))
a= 4
print(id(4))
b = 5
print(id(b))
print(id(5))
b = b-1
print(id(b))'''

#print(5+4,7-9,4*5,5/4,8//5,4**3,7%3,-5**3,-8-9,-6*(-4))
'''a = 4
b = 5
c = 3.0
d = 'n'
e = 'g'
f = 'N'
g = 'god'
G = "GOD"
j = "GOD"
K = "GODhouse"
l = [1,2,3]
m = [2,3,4]
n = [1,2,3]
print(a==b,a<b,a==c, d==e, d!=f,d==f,d>f, g==G, g<G, G==K,l==m,l==n,l>m, l==n )
print(.5+.5+.5)
print(1.5)
print(0.5+0.5+0.5 == 1.50)
s1 = "abc"
#s2 = input("enter a string ")
s3 = "abc"
print(s1==s2, s1==s3, s1 is s2, s1 is s3)
l = 3.5
k = 3.5
K = float(input("enter a float number"))
print(l==k, l is k, l==K, l is K, l is not k, l is not K)
print(id(l),id(k),id(K))
print(4==4 or 4==5, 4==3 or 9==7)
print(4==4 and 4==4, 4==3 and 9==7, 4==7 and 3==3)
print( not 4==4,  not 9==7)
print(4==4 | 4==4, 4==5 | 9==7)
print(4==4 & 4==4, 4==3 & 9==7, 4==7 & 3==3)
print(bin(13))
print(bin(12))
print(13 ^ 12, 12|13, 13&12)
#print("and"*2, "and"+"then")
p= 7
q = 6
r = 13
print(p>q<r)
print(p<=q<r)
print(25/5 or 2.0+20/10)
print(25/5 and 2.0+20/10)
print(p or (q and (not r)))
print( (q and (not r)))
print(not r)
print((p and q) or (not r))
print((5>6) and (4<8))
print((5>6) or  (4<8))
a = 4
b = 9.0
print(int(b))
print(float(a))
print(complex(2), complex(2,6))
print(str(3))
print(bool(1), bool(0))
print(len(str(17<30)))
import math
print(math.ceil(2.67))
print(math.sqrt(4))
print(math.exp(3))
print(math.fabs(-1.0))
print(math.floor(-1.3))
print(math.floor(1.3))
print(math.log(1024, 2))
print(math.log10(10))
print(math.pow(4.0,3.0))
print(math.cos(30))
print(math.sin(60))
print(math.pi)
print(math.e)'''
# CONDITIONAL AND ITERATIVE STATEMENTS

#ODD-EVEN check
'''a = int(input("Enter any number "))
if (a%2) != 0 :
    print("the given number is an odd number")
if (a%2) == 0:
    print(a,"the given number is an even number")
else:
    print(a,"the given number is an odd number")
'''
#FIND THE LARGEST AMONG THREE NUM
'''p = float(input("Enter a number, N1 "))
q = float(input("Enter a number, N2 "))
r = float(input("Enter a number, N3 "))

Large = p
if q > Large:
    Large = q
if r > Large :
    Large = r
print("the largest number among three ",p,q,r,"is ", Large )'''

#CALCULATE SUM OF TWO NUMBERS
'''A = float(input("Enter number 1"))
B = float(input("Enter number 2"))
C = float(input("Enter number 3"))

print("The sum of the given three numbers",A,B,C ,"is", A+B+C)
Num = A
Sum1 = 0
if A == B:
   if C != A:
      Sum1 += C
else :
    if A == C :
        Sum1 += C
    else:
        if B == C:
            Sum1 += A
        else :
            Sum1 = A+B+C

print("sum of the non duplicate numbers are",Sum1)'''

# DIVISIBLITY TEST OF NUMBERS
'''num1 = float(input("Enter Number 1 "))
num2 = float(input("Enter Number 2 "))
if num1>=num2:
   if num1 % num2 == 0:
         print("the given number 1 is divisible by number 2")
   else:
         print("the given number 1 is  not divisible by number 2")
else :
    if num1< num2:
       if num2 % num1 == 0:
             print("the given number 2 is divisible by number 1 ")
       else :
             print("the given number 2 is  not divisible by number 1")'''

#FIND THE MULTIPLES OF THE NUMBER OUT OF 5
'''A = float(input("Enter number 1 "))
B = float(input("Enter number 2 "))
C = float(input("Enter number 3 "))
D = float(input("Enter number 4 "))
E = float(input("Enter number 5 "))
DI = float(input("Enter the divisor:"))
print("Multiples of Divisor",DI,"are :")
# remainder = R
Count = Ct = 0
R = A % DI
if R == 0:
    print(A, sep="")
    Ct +=1
R = B % DI
if R == 0:
    print(B, sep="")
    Ct +=1
R = C % DI
if R == 0:
    print(C, sep="")
    Ct +=1
R = D % DI
if R == 0:
    print(D, sep="")
    Ct +=1
R = E % DI
if R == 0:
    print(E, sep="")
    Ct +=1

print(Ct,"multiples of",DI,"are found")'''
#DATE 23-12-2023 OYOO BDAY
#RUNS SCORED BY A BATSMAN
'''Runs = int(input("Enter the runs scored by Batsman "))
if Runs>= 100:
    print("Batsman scored a cenetury")
elif Runs>= 50:
    print("Batsman scored a half-cenetury")
else:
    print("Batsman neither scored century not half-centuryry")'''

#TWO NUMBERS AND AN ARITHMATIC OPERATOR
'''Num1 = float(input("Enter Number 1 :"))
Num2 = float(input("Enter Number 2 :"))
Op = input("choose an arithmatic operator[+-/%*//**] :")
result = 0
if Op == '+':
    print("result = ",Num1+Num2)
if Op == '-':
    print("result = ",Num1-Num2)
if Op == '*':
    print("result = ",Num1*Num2)
if Op == '/':
    print("result = ",Num1/Num2)
if Op == '**':
    print("result = ",Num1**Num2)
if Op == '%':
    print("result = ",Num1%Num2)
if Op == '//':
    print("result = ",Num1//Num2)'''
#SORT THREE NUMBERS IN ASCENDING ORDER
'''X = int(input("Enter 1st Number: "))
Y = int(input("Enter 2nd Number: "))
Z = int(input("Enter 3rd Number: "))
Min = Max = Mid = None
if X < Y and X < Z:
    if Y < Z:
        Min,Mid,Max = X,Y,Z
    else:
        Min,Mid,Max = X,Z,Y
elif Z < Y and Z < X:
    if Y < X:
        Min,Mid,Max = Z,Y,X
    else:
        Min,Mid,Max = Z,X,Y
elif Y < Z and Y < X:
    if X < Z:
        Min,Mid,Max = Y,X,Z
    else:
        Min,Mid,Max = Y,Z,X
else :
    print()
print("Numbers in ascending order are", Min,Mid,Max)'''
24/12/23

#CHECK UPPERCASE LOWERCASE DIGIT OR SPECIAL CHARACTER
'''Ch = input("Enter a single Character: ")
if Ch >= 'a' and Ch <= 'z':
    print("you entere a lowercase character")
elif Ch >= 'A' and Ch <= 'Z':
    print("you entere a uppercase character")
elif Ch >= '0' and Ch <= '9':
    print("you entere a Digit character")
else :
    print("you entere a special character")'''
#TO FIND AREA OF A CIRCLE
'''import math
Rad = float(input("What is the radius of the circle"))
Area = math.pi *Rad*Rad
Crmf = 2 * math.pi*Rad
print("Area of the circle having radius ",Rad,"is",Area)
print("Perimeter of the circle having radius ",Rad,"is",Crmf)'''

#FIND ROOTS OF A QUADRATIC EQUATION
'''import math
print("Enter the coefficiants of the quadratic equation")
a = float(input("Enter coefficient of x^2: "))
b = float(input("Enter coefficient of x^1: "))
c = float(input("Enter coefficient of x^0: "))
if b*b - 4*a*c > 0:
    print("The one root of the equation is",(-b+math.sqrt(b*b - 4*a*c))/(2*a))
    print("The other root of the equation is",(-b-math.sqrt(b*b - 4*a*c))/(2*a))
elif b*b - 4*a*c == 0:
    print("The both root of the equation are same and the roots are",(-b/(2*a)))
else:
    print("no real root of the equation exist")'''

#ITERATION/LOOPING STATEMENT
'''for a in [1,2,3]:
    print(a, a*a)
for a in [1,2,3]:
    print(a, a*a*a)'''
# PROGRAM TO PRINT TABLE OF A NUMBER
'''Num = int(input("enter the number for which you want to print the table"))
for a in range(1,11):
    print(Num*a)'''
#PRINT SUM OF NANATURAL NUMBER
'''Num = int(input("enter the number upto you want sum"))
Sum = 0
for a in range(1,Num+1):
    Sum += a
print("the sum of ",Num,"integer number",Sum)'''
#FACTORIAL OF A NUMBER
'''Fact = int(input("enter the integer: "))
a = 1
Num = 1
while a <=Fact:
    Num *= a
    a += 1
print("Factorial of the given number is",Num)
'''
'''#SUM OF EVEN AND ODD OF N INTEGER
Num = int(input("Enter first N  Number upto which you want sum"))
Odd_sum = Even_sum = 0
a = 0
if Num%2 == 0:
    while a <= Num:
        Even_sum += a
        a += 2
    print("sum of first", Num, "Even integers",Even_sum)
else:
    while a <= Num:
        Odd_sum += a
        a += 2
    print("sum of first", Num, "Odd integers",Odd_sum)'''
    #i still have doubts for this
#TO USE BREAK
'''a = float(input("Enter divisor"))
b = float(input("Enter dividend"))
for s in range(1,):
    if b == 0:
        print(" Division by 0!!! Aborting!!")
        break
    else :
        print("answer is",a/b)'''
# use random and make a game
'''import random

Num = random.randint(71,111)
chance = 0
while chance < 4:
    Guess = int(input("Enter a digit between 71 to 111: "))
    if Guess == Num:
        print("Congratulations !!!You Won!!!")
        break
    else:
        chance +=1
if not chance<4:
    print("You Lost:( \n The number was", Num)'''
#CONTINUE STATEMENT
'''print("Enter two different Numbers")
a = float(input("Enter divisor"))
b = float(input("Enter dividend"))
for s in range(1,):
    if b == 0:
        print(" Division by 0!!! Aborting!!")
        continue
    else :
        print("answer is",a/b)'''
'''count = Sum = 0
ans = "y"
while ans == "y":
    num = int(input("Enter Number: "))
    if num < 0:
        print("number entered is below zero")
        break
    Sum = Sum + num
    count +=1
    ans = input("want to enter more numbeers? y/n  ")
else:
    print("you entered ",count,"numbers so far.")
    print("sum of enterd numbers is ",Sum)'''
#PROGRAM TO CHECK PRIME NUMBER ON NOT
'''num = int(input("Enter Number: "))
lim = int(num/2)+1
for i in range(2,lim):
    rem = num%i
    if rem == 0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")'''
#page number 225 doubt
'''a = int(input("enter upper range: "))
b = int(input("enter lower range: "))
for num in range(a,b):
    for i in range(2,num):
        if num%i == 0:
            j = num/i
    else :
        print(num)'''
#NEW CHAPTER STRING OPERATION
#25/12/23
'''name ="PYTHON"
for ch in name:
    print(ch,'-',end="")'''
'''String1 = input("Enter a string: ")
print("The string in forward and reverse order respectively: ")
length = len(String1)
for b in range(0,length,1):
    print(String1[b]," ",end="")
for a in range(-1,(-length-1),-1):
    print("  ",String1[a],end="")
string2 = input("Enter a string value")
lenght = len(string2)
i = 0
for a in range(-1,(-lenght-1),-1):
    print(string2[i],"\t",string2[a])
    i += 1'''
'''print("tea"+"pot")
print("8"+"3")
print("8"+"7")
print(10+9)
print("a" in "Pranav")
print("a" == "a")
print("ABC">"AB")
print("abc"<="ABCD[")
print("3"*4)
print("go!"*5)
print(ord("a"))
name1 = 'Siddhu'
lenght = len(name1)
i = 0
for i in range(0,lenght):
    print(name1[i])'''
'''Num = int(input("Enter a integer: "))
for a in range(1,10):
    print(a*Num)
    a +=1'''
'''word = 'amazing'
print(word[0:4])'''
'''word = 'siddharth'
print(word[6:])
print(word[:5])
print(word[:-9]+word[-9:])'''
#PRINT #HASH PATTERN
'''string = '#'
pattern = ""
for a in range(5):
    pattern += string
    print(pattern)'''
#PROGRAM TO BUILT IN STRING MANIPULATION
'''Line = input("Enter a line")
lowercount = uppercount = 0
digitcount = alphacount = 0
for a in Line:
    if a.islower():
        lowercount += 1
    elif a.isupper():
        uppercount += 1
    elif a.isdigit():
        digitcount += 1
    if a.isalpha():
        alphacount += 1
print("no of uppercase ",uppercount)
print("no of loeercase ",lowercount)
print("no of digit ",digitcount)
print("no of alpha ",alphacount)'''
#Doubt page number 284
'''b = 0
c = 0
for a in range(5):
    c = a + b
    print("c=",c)
    a = b
    b = c
    print("a=",a,end=" ")
    print("b=",b)'''
'''l1 = list('hello')
print(l1)
a = eval(input("Enter list: "))
print(a)'''
#List chapter
'''L = ['p','r','a','n','a','v']
length = len(L)
for a in range(length):
    print("Index ",a,"with element",L[a])'''

#27/12/23 LIST AND IT'S FUNCTIONS
'''L1 = [1,2,3,4,5]
print(L1)
L2 = list()
print(L2)
L3 = list('Priviya')
print(L3)
L4 = list(input("Enter a string "))
print("Entered List",L4)
list = eval(input("Enter a string "))
print("Entered List",list)
e = eval("3*10")
print(e)
print("Enter a list")
Lis1 = list(input("enter the elements of the list "))
print(Lis1)
vowels = ['a','e','i','o','u']
print(vowels[2])
vowels[0] = 'A'
print(vowels)
for i in range(0,5):
    print(vowels[i])
vowels[-4] = 'E'
print(vowels)
L1 = [1,3,5,7,9]
L2 = [2,4,6,8,10]
L3 = ['a','b','c']
print(L1+L2+L3)
print(L1*2)
L = L1 + L2 + L3
print(L[1:8])
print(L[1:6:2])
print(L[-1:-17])
print(L[15:20])
print(L[3:-8])
print(L[::2])
print(L[6::3])
print(L[::-1])
L1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sl1 = L1[4:14:3]
sl2 = L1[::4]
Sum = Avg = 0
print("Slice1")
for i in sl1:
    Sum += i
    print(i,end=" ")
print("Sum of elements in Slice",Sum)
print("Slice 2")
for i in sl2:
    Sum += i
    Avg = Sum/i
    print(i,end=" ")
print(Avg)
L = ["one","two","Three"]
L[0:2] = [1,2]
L[3:] = "124"
print(L)
L.append(7)
print(L)
L[4] = 5
print(L)
del L[2]
print(L)
L.pop(1)
print(L.pop(1))
print(L)
L.index(5)
L1 = [1,2,3,4]
L.extend(L1)
print(L)
L.extend([87,83])
print(L)
L.insert(3,9)
print(L)
L.insert(3,'a')
print(L)
L2 = L.pop(0)
print(L2)
print(L)
L3 = L.pop()
print(L3,"\n",L)
L.remove(1)
print(L)
L4 = ['i','l','u']
L4.clear()
print(L4)
print(L.count(2))
L4.reverse()
print(L1)
L5 = [12,23,1,4,5,98,87,83,19]
L5.sort()
print(L5)
L6 = ['a','b','e','t','w','c']
L6.sort()
print(L6)'''
#TO FIND MINIMUM NUMBER WITH INDEX
'''L1 = eval(input("Enter list: "))
length = len(L1)
minn_ele = L1[1]
minn_index = 0
for i in range(0,length):
    if L1[i] < minn_ele:
        minn_ele = L1[i]
        minn_index = i
print("Given list is:",L1)
print("Minimum element is ",minn_ele,"with index",minn_index)'''
#PROGRAM TO CLACULATE MEAN
'''L1 = eval(input("Enter list: "))
length = len(L1)
mean = Sum = 0
for i in range(0,length):
    Sum += L1[i]
mean = Sum/length
print("mean of the entered list is :",mean)'''
#PROGRAM TO SEARCH ELEMENT IN LIST
'''L1 = eval(input("Enter list: "))
length = len(L1)
Search = int(input("Enter the element you wanna search: "))
for i in range(0,length):
    if Search == L1[i]:
        print("We found it yayyyy!!!!",Search)
        break
else:
    print("Element not found")'''
#PROGRAM TO FIND FREQUENCY OF AN ELEMENT
'''L1 = eval(input("Enter list: "))
length = len(L1)
Search = int(input("Enter the element you wanna search: "))
count = 0
for i in range(0,length):
    if Search == L1[i]:
        count += 1
if count== 0:
    print("Element not found on the list!!!")
else:
    print(Search," Element having frequncy ",count)'''
#PROGRAM TO FIND FREQUENCY OF ELEMENTS OF THE LISTS
print("Hello World")

print("New Era of Me")


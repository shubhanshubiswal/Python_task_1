                                   ### PYTHON-TASK-1 ###

#Q1.Create an inner function to calculate the addition in the following way
#Create an outer function that will accept two parameters ‘a’ and ‘b’ 
#Create an inner function inside an outer function that will calculate the addition of ‘a’ and ‘b’ 
#At last, an outer function will add 5 into addition and return it

def outer(a,b):
    def inner(a,b):
        return a+b
    return inner(a,b)+5 
a,b=input("enter two digits (comma separated):\n").split(',')  
a=int(a)
b=int(b)
print(f"output : {outer(a,b)}")

#2. Given input String of combination of the lower and upper case ,arrange characters in such a way that all lowercase letters should come first.

inputStr = input("\nEnter string:\n")
lower = []
upper = []
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
String1 = ''.join(lower + upper)
print("\nArranging characters so that lowercase letters are coming first:")
print(String1)

#3. Given a Python list, remove all the even number from the list and save those even number in another list and print both the lists.
#For a given input list:  List1 = [1,2,3,4,5,6,7]
#Output : List1=[1,3,5,7]
#	List2 = [2,4,6]
def filter_odd_even(l):
    odd_num=[]
    even_num=[]
    for i in l:
        if i%2==0:
            even_num.append(i)
        else:
            odd_num.append(i)
    print(f"List1={odd_num}")
    print(f"List2={even_num}")
n=input("\nenter range of list:\n")
n=int(n)
List1=list(range(1,n+1))   
print(f"List1={List1}") 
filter_odd_even(List1)     


#4. Get the key corresponding to the minimum value from the following dictionary using appropriate python logic.
#sample={
#‘physics’, 88 ,  ‘maths’, 75,  ’chemistry’ , 72,’Basic electrical’ , 89 
#}

sample = {'physic': 88 ,  'maths': 75,  'chemistry' : 72,'Basic electrical' : 89 } 
temp = min(sample.values()) 
result = [key for key in sample if sample[key] == temp] 
print("\ndictionary--->sample : " + str(sample)) 
print("Key with minimum value : " + str(result)) 

#5.  Given two Python sets, update first set with items that exist only in the first set and not in the second set .
#S1={1,2,3,4,5,6,7,8,9}
#S2={1,3,4,6,8,11,22,34,51,67}

S1={1,2,3,4,5,6,7,8,9}
S2={1,3,4,6,8,11,22,34,51,67}
print(f"\nS1={S1}")
print(f"S2={S2}")
S1=S1-S2
print(f"updated S1={S1}")

#6. Program to create simple calculator in Python which on input of 1,2,3,4 should add , subtract , multiply and divide respectively.

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return(a/b)
a,b=input("\nEnter two numbers(comma separated):").split(',')             
a=int(a)
b=int(b)   
n=input("\nEnter:\n1(for addition)\n2(for subtraction)\n3(for multiply)\n4(for division)\n:")
n=int(n)
if n==1:
    print(f"addition of {a} and {b} : {add(a,b)}")
elif n==2:
    print(f"subtraction of {a} and {b} : {sub(a,b)}")
elif n==3:
    print(f"multiplication of {a} and {b} : {mul(a,b)}")
elif n==4:
    print(f"division of {a} and {b} : {div(a,b)}")
else:
    print("Invalid Option")        

                                            
                                                ### PANDAS ###
 
import pandas as pd
diamonds = pd.read_csv('diamonds.csv')

#7. Write a Pandas program to read a csv file from a specified source and print the first 5 rows

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
print("\nDiamond Dataframe:")
print("\nFirst 5 rows:")
print(f"{diamonds.head()}\n")

#8. Write a Pandas program to select a series from diamonds DataFrame. Print the content of the series.

n=input("Enter series name you want tp print\n(carat,cut,color,clarity,depth,table,price,x,y,z):\n")
print(f"contents of {n}:")
print(f"{diamonds[n]}\n")

#9. Write a Pandas program to calculate count, minimum, maximum price for each cut of diamonds DataFrame.

print("\nCount, minimum, maximum  price for each cut of diamonds DataFrame:\n")
print(diamonds.groupby('cut').price.agg(['count', 'min', 'max']))

#10. Write a Pandas program to check the number of rows and columns and drop those row if 'any' values are missing in a row of diamonds DataFrame.

print("\nNumber of rows and columns:")
print(diamonds.shape)
print("\nAfter droping those rows where values are missing:")
print(diamonds.dropna(how='any').shape)

#11.  Write a Pandas program to count the duplicate rows of diamonds DataFrame.

print("\nDiamonds Dataframe:")
print(diamonds.shape)
print("\nDuplicate rows of diamonds DataFrame:")
print(diamonds.duplicated().sum())

#12. Write a Pandas program to get sample 75% of the diamonds DataFrame's rows without replacement and store the remaining 25% of the rows in another DataFrame

print("\nSample 75% of diamonds DataFrame's rows without replacement:")
sample1 = diamonds.sample(frac=0.75, random_state=99)
print(sample1)
print("\nRemaining 25% of the rows:")
print(diamonds.loc[~diamonds.index.isin(sample1.index), :])    
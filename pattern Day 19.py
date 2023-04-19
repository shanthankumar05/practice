--Reverse
num =  int(input("Enter a number: ");
temp=num;
rev=0
while(num!=0):
  rem=num%10;
  rev=rev*10+rem;
  num=num/10
print("Reverse of a number: ",rev)

 --palindrome
 num =  int(input("Enter a number: ");
temp=num;
rev=0
while(num!=0):
  rem=num%10;
  rev=rev*10+rem;
  num=num/10
if(temp==num):
       print("Palindrome")
 else:
        printf("Not a palindrome")
            
 --- Armstrong number
  num=int(input("Enter a number: ");
          temp=num
   while(num>0):
          rem=num%10;
          sum=sum+rem*rem*rem;
          num=num/10;
    if(sum==temp):
          print("Armstrong number");
    else:
          print("Not an armstrong number")
          
 ---Areas
    
   base =int(input("Enter base : ");
   height =int(input("Enter height  : ");
   side = int(input("Enter side length: ");
   length= int(input("Enter length : ");
   breadth = int(input("Enter breadth: ");
   print("Area of triangle ",0.5*base*height)
   print("Area of sqaure is ",side*side)
   print("Area of rectangle ",length*breadth)
  ---swapping
   
   n1=int(input("Enter value: ")
n2=int(input("Enter value: ")
n3=int(input("Enter value: ")


if n1>n2 and n1>n3:
    if n2<n3:
         temp=n1
        n1=n2
        n2=n3
        n3=temp
    else:
        temp=n1;
        n1=n3
        n3=temp
elif n2>n1 and n2>n3:
    if n1<n3:
        temp=n2;
        n1=n3
        n3=temp
    else:
        temp=n2;
        n2=n1
        n3=temp
else:
    if n1>n2:
        temp=n2
        n2=n1
        n1=temp
print(n1,n2,n3)
          
    
         
        
  
             
           

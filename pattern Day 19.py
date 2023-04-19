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
           

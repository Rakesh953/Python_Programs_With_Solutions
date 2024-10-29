def PaliPrime(num,c_num,count=0,rev=0):
    for n in range(1,num+1):
        if num%n==0:
            count+=1
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    if count==2 and c_num==rev:
        print('PaliPrime')
    else:
        print("not")
num=int(input('Enter the number: '))
PaliPrime(num,c_num=num)





def PaliPrime(num, c_num, count=0, rev=0):
    # Reverse the number
    original_num = num  # Store original number for prime checking
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10

    # Check if the original number (before reversal) is prime
    for n in range(1, original_num + 1):
        if original_num % n == 0:
            count += 1

    # Check if the number is both prime and a palindrome
    if count == 2 and c_num == rev:
        print(c_num, 'is a PaliPrime Number')
    else:
        print(c_num, 'is not a PaliPrime Number')

# Input and function call
num = int(input('Enter the number: '))
PaliPrime(num, c_num=num)

def Armstrong(num,c_num,power,sum=0):
    while num!=0:
        rem=num%10
        sum+=rem**power
        num//=10
    return c_num==sum
num=int(input('Enter the Number: '))
print(Armstrong(num,c_num=num,power=(len(str(num)))))



# First N numbers
def N_Armstrong(N_arm, c_num=1, pwr=None):
    found = 0
    while found < N_arm:
        num = c_num
        res = 0
        pwr = len(str(num))  # Calculate the power for the current number
        temp = num  # Store the original number for comparison

        # Calculate the Armstrong sum
        while temp != 0:
            rem = temp % 10
            res += rem ** pwr
            temp //= 10

        # Check if the current number is an Armstrong number
        if num == res:
            print(num)
            found += 1

        c_num += 1  # Increment to check the next number

# Input for the first N Armstrong numbers
N_arm = int(input('Input the number of Armstrong numbers to generate: '))
N_Armstrong(N_arm)

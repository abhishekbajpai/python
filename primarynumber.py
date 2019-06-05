import math;

userNumber = input("Enter number to check if it's prime or now: \n");
numberSqrt = int(math.sqrt(int(userNumber)));
primeStatus = False;

for i in range(2, numberSqrt+1):
    if(int(userNumber) % i == 0):
        primeStatus = True;
        break;

if(primeStatus):
    print("Number entered is not prime");
else:
    print("Number entered is prime");
    
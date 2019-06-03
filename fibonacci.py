# Python program to find out the finonacci series.

fibonacciSeq = input("Enter number for which you want to print fibonacci: \n");
fibonnaciList= [];

for i in range(0, int(fibonacciSeq)):
    if(i==0 or i==1):
        fibonnaciList.append(1);
    else:
        fibonnaciList.append(fibonnaciList[len(fibonnaciList)-1] + fibonnaciList[len(fibonnaciList)-2]);

print(','.join(str(x) for x  in fibonnaciList));

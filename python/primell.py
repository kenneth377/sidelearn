import math
from sys import argv


if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        line = file.readline()

        while line != "":
            n = int(line.split('\n')[0])
            # found = False
            # for i in range(1,n):
            #     for j in range(i,n):
            #         if i*j == n:
            #             print(f"{i}*{j} = {n}")
            #             found =True
            #             break
            #     if found:
            #         break
            for i in range(2,int(math.sqrt(n))):
                isprime = True
                for j in range(2,int(math.sqrt(i))):
                   if i%j ==0:
                       isprime =False             
                if isprime and n%i==0:
                    print(f"{n}={int(n/i)}*{i}")
                    break
               

            line = file.readline()
except FileNotFoundError:
    print(f'File not found: {argv}')
except ValueError:
    print(f'Invalid input in the file: {argv}')
except Exception as e:
    print(f'An error occurred: {str(e)}')
    pass


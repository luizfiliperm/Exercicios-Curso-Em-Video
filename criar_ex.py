#import os
#for i in range(72, 96):

#    os.remove(f'mundo03/ex{i}.py')


num = int(input("Deseja criar até qual arquivo?")) + 1

for i in range(72, num):
    open(f'mundo03/ex0{i}.py', "a")
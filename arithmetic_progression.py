#Arithmetic Progression
from time import sleep

first_term = int(input('Enter the first term:\n'))
ratio = int(input('Enter the ratio:\n'))
term = 0

print('Printing the first 10 terms...')
sleep(1)

for terms in range (0, 10):
	term = first_term + terms * ratio
	print(term, end = '  ->  ')
	
print('Finished!')
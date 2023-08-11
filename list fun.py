#append
name=['Rutuja','Nikita','pradnya']
name.append('sakshi')
print(name)

#cont
numbers =[2,3,4,5,6,7,8]
count = numbers.count(2)
print('count of 2:,count')

#clear
numbers =[2,3,6,8,22]
numbers.clear()
print('list after clear():',numbers)

#pop
prime_numbers =[2,3,5,7]
removed_element = prime_numbers.pop(2)


print('Removed Element:',removed_element)
print('Updated List:',prime_numbers)

#remove
prime_number = [2,3,5,7,9,11]
prime_number.remove(9)
print('update list:',prime_numbers)

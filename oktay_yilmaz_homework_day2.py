#Question 1
mylist = list(range(10))
print(mylist)
#print(len(mylist))
first_half = [i for i in mylist if i < len(mylist)/2]
second_half = [i for i in mylist if i >= len(mylist)/2]
print(first_half)
print(second_half)
second_half.extend(first_half)
print(second_half)

#Question 2
n = int(input("Please enter a single digit integer: "))
list=list(range(n+1))
#print(list)
even_numbers = [i for i in list if i % 2 == 0]
print(even_numbers)
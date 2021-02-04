#Question 1: prime numbers between 0 and 100
def prime():
    upper_number = 100
    prime_numbers=[]
    for i in range(2,upper_number+1):
        if i==2:
            prime_numbers.append(i)
        elif i>2 and i % 2 !=0:
            title="True"
            for j in range(3,i-1): # "i" must be undividable by any integer (j) (except "1") which is smaller than itself
                if i % j == 0:
                    title = "False"
            if title=="True":
                prime_numbers.append(i)
    print(prime_numbers)
prime()

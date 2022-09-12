def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            #Not a prime
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

n = int(input("Check this number: "))

# call the function
prime_checker(number=n)
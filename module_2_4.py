numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []


for num in numbers:
    if num == 1:
       continue
    is_prime = True

    for j in range(2, num):

      if num % j == 0:
        is_prime = False
        break

    if is_prime is True:
       primes.append(num)

    else :
       not_primes.append(num)

print("This is primes: " , primes)
print("This is not primes : " , not_primes)

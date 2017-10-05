# DPC 20 [E]
# Prime Finder, less than 2000



primes = [3,5]

for k in range(7,2001,2):
  
  j = 0
  prime = True
  
  checking = True
  while (checking == True):
    if (k % primes[j] == 0):
      prime = False
      checking = False
    else:
      j += 1
      if (primes[j]*primes[j] == k):
        prime = False
        checking = False
      elif (primes[j]*primes[j] > k):
        checking = False
      else:
        checking = True
  if (prime == True):
    primes += [k]
    




    
primes = [2] + primes

print primes

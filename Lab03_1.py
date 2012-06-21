print "Ernest Pobee"

i = 0
prime = 2
while (i < 50):
     factor = 0
     if ((prime == 2) or (prime == 3)):
          num = prime
     else:
          for n in range(1,prime + 1):
               if (prime % n == 0):
                    factor += 1
          if factor == 2:
               num = prime
          else:
               num = 1
     if (num != 1):
          print num,
          i += 1
     if( (i % 10 == 0) and (num != 1)):
          print
     prime += 1 

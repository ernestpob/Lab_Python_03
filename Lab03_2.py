print "Ernest Pobee"

# Lab03_2a
for i in range(1,7):
     for j in range(1,i +1):
          print j,
     print

# Lab03_2b
for i in range(1,7):
     for j in range(1, 8 -i):
          print j,
     print

# Lab03_2c
for i in range(1,7):
     k = i
     for j in range(1, 7-i):
          print '  ',
     while(k > 0):
          print k,
          k -= 1
     print


#Lab03_2d
for i in range(1,7):
     j = i 
     while (j > 0):
          if (j == 1):
               j -= 1
               continue
          else:
               print  "  ",
               j -= 1
     for k in range(1,8 -i):
          print k,
     print

     
# Lab03_2e
for i in range(1,6):
     k = i
     l = 2
     for j in range(1, 7-i):
          print "  ",
     while (k > 0):
          print k,
          k -= 1
     while(l < (i+1)     ):
          print l,
          l += 1
     print

print "Ernest Pobee"

plaintext = raw_input("Enter plaintext")
shift_val  = input("Enter shift value")

plaintext2 = ''

for c in plaintext:
     plaintext2 += c

ciphertext = ''
for c in plaintext2:
     value = ord(c)
     if (value > 64 and value  < 91):
          value += shift_val
          if (value >90):
               value = 64 + (value % 90)
     elif(value > 96 and value < 123):
          value+=shift_val 
          if (value > 122):
               value = 96 + (value % 122)
     c = chr(value)
     ciphertext += c

print "Encrypted message : ",ciphertext
     

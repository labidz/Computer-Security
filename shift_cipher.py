def encrypt(text,s):
   result = ""
   for i in range(len(text)):
      char = text[i]
      if (char >= 'A' and char <= 'Z'):
         result += chr((ord(char) + s-65) % 26 + 65)
      elif(char >= 'a' and char <= 'z'):
         result += chr((ord(char) + s - 97) % 26 + 97)
      else:
         result += char
   return result

text = "Hello World!"
s = 4

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text,s))

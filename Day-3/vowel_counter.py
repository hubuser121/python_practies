word=input("enter your word")
vowel=['a','e','i','o','u','A','E','I','O','U']
count=0
found=[]
for letter in word:
    if letter in vowel:
        count += 1
        found.append(letter)
print("vowel found","".join(found))
print("the number of vowel found ", count )

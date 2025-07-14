sentence=input("enter your sentences")
count=0
found=[]
vowel=['a','e','i','o','u','A','E','I','O','U']

for letter in sentence:
    if letter in vowel:
        count+=1
        found.append(letter)
print("sentence tittle",sentence.title())
print("word length",len(sentence.split()))
print("vowel count us : ",count)
print("vowels are ","," .join(found))
print("reversed word is ", sentence[::-1])

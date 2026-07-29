print("=" * 35)
print("Count Vowels")
print("=" * 35)

sentence = input("Enter a sentence :")

count = 0

for ch in sentence.lower():
    if ch  in "aeiou":
        count +=1

print("\n Total Vowels :", count)
print("=" * 40)
print("Map Function")
print("=" * 40)

numbers=[5,10,15,20,25]

double=list(map(lambda x:x*2,numbers))
print("Original List :", numbers)
print("Doubled List  :", double)
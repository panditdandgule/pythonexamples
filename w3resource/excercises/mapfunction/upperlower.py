chars={'a','b','E','f','a','e','i','o','u','U'}

def change_case(s):
    return str(s).upper(),str(s).lower()

print("Original Characters:\n",chars)

result=map(change_case,chars)
print("\nAfter converting above characters in uppercase and lowercase")

print(set(result))
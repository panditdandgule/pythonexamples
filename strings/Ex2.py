s=input("Enter main string:")
sub=input("Enter sub string:")
try:
    n=s.index(sub)
except ValueError:
    print("Substring not found")
else:
    print("Substring found")
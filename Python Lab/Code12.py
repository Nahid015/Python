name = input("What is your name?")

name = name.upper()

if name.startswith("MR"):
    print("Hello Sir, how are you?")
elif name.startswith("MRS") or name.startswith("MS") or name.startswith("MISS"):
    print("Hello Madam, how are you?")
else:
    print("Hello",name,", how are you?")

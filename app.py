print("5"+str(3))

first = "Lucky"
course = "Software Engineering"

# Joining and inserting values (f-string: put f before the quotes)
print(first + " studies " + course)
print(f"{first} studies {course}")        # cleaner, preferred
print(f"2 + 3 = {2 + 3}")                 # any expression works inside {}

# Common methods
text = "  Hello, World  "
print(text.strip())            # "Hello, World"   (removes outer spaces)
print(text.upper())            # "  HELLO, WORLD  "
print(text.lower())            # "  hello, world  "
print(text.replace("World", "Nairobi"))
print("a,b,c".split(","))      # ['a', 'b', 'c']
print("-".join(["a", "b"]))    # "a-b"
print(len(first))              # 5

# Indexing and slicing work just like lists
print(first[0])       # "L"
print(first[-1])      # "y"
print(first[1:4])     # "uck"

# Strings are immutable: you can't change them in place
# first[0] = "l"      # TypeError
first = "l" + first[1:]   # build a new string instead
print(first)          # "lucky"


name = "lucky"
name = name.upper()
print(name)




score = 72

if score >= 80:
    print("Distinction")
elif score >= 60:
    print("Pass")
else:
    print("Fail")

# Combining conditions
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")

# Checking membership
role = "admin"
if role in ["admin", "editor"]:
    print("Can edit")

# One-line version (ternary)
status = "adult" if age >= 18 else "minor"
print(status)

# Truthy and falsy: these count as False
# 0, 0.0, "", None, [], {}
name = ""
if not name:
    print("Name is empty")
# for loop over a range of numbers
for i in range(5):            # 0, 1, 2, 3, 4  (end excluded)
    print(i)

for i in range(1, 6):         # 1 to 5
    print(i)

for i in range(0, 10, 2):     # start, stop, step -> 0, 2, 4, 6, 8
    print(i)

# for loop over a collection or a string
for letter in "Lucky":
    print(letter)

# while loop: runs as long as the condition is True
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1                # without this line, the loop never ends

# break (stop the loop) and continue (skip to the next round)
for n in range(1, 10):
    if n == 3:
        continue              # skip 3
    if n == 6:
        break                 # stop completely at 6
    print(n)                  # prints 1, 2, 4, 5

# Accumulator pattern: build up a result
total = 0
for n in range(1, 6):
    total += n                # same as total = total + n
print("Sum:", total)          # 15

# Nested loop: multiplication table
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end=" ")
    print()                   # new line after each row
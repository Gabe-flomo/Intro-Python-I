# Write a function is_even that will return true if the passed-in number is even.

def iseven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def isodd(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(iseven(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"
isodd(num)


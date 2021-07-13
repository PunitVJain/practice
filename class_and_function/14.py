#  python for the best of my knowledge.

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value 
# to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

def revse(num):
    return num[::-1]
num = input()
print(revse(num))


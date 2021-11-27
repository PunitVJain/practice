#  adding the element to the dictionary element of the list

mydict = {'start': ['India', 'UAE'],
          'Name': "Punit Jain"
            }

mydict['start'].append('USA')
mydict['start'].append('Maldives')
mydict['Name'] = "Rakhi Jain"

print(mydict)

# python practice 
print('Python is my life for sometime', end='\n')
#  python for learn python the hard way.
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    """
    Wromg Solution
    Needed to check the logic once again.
    """
    def reverse(self, x: int) -> int:
        num = list(str(x))
        if x in range(-2**31,2**31 - 1):
            if num[0] == '-':
                num.remove('-')
                nrevs = int(''.join(num[::-1])) * -1
                return nrevs
            nrevs = int(''.join(num[::-1]))
            return nrevs
        return 0

        
  
Sol = Solution()
print(Sol.reverse(321))

# --------------------------------------------------------------------------------

# stack data structure

class Stack(object):

    def __init__(self):
        self.iteam = []
    
    def push(self, *args, **kwargs):
        self.iteam.append(args)
        return None
    
    def size(self):
        return len(self.iteam)
    



Stack =  Stack()
print(Stack.push(1, 2, 3, 4))
print(Stack.size())
print(Stack.push(5))
print(Stack.size())
print(Stack.push(7))
print(Stack.size())
print(Stack)
        
# Write a function that reverses a string. 
# The input string is given as an array of characters s.

class RevString:

    def rev_string(self, onelist:str):        
        return onelist[::-1]
    
    def input_str(self):
        arr = input("Enter the string elements: ")
        onelist = list(map(str, arr.split(' ')))
        return onelist
    
if __name__ == "__main__":
    rs =  RevString()
    myarray = rs.input_str()
    revarr = rs.rev_string(myarray)
    print(revarr)

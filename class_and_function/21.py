#  python for Punit Jain.

class Sample:

    def __init__(self) -> None:
        pass

    def add(self, first_value, second_value):
        return first_value + second_value
    
    def reverse_string(self, mystr):
        index = len(mystr)
        mylist = []
        while index:
            index -= 1
            mylist.append(mystr[index])
        return ''.join(mylist) 

    def main(self):
        sam = Sample()
        first_value, second_value = int(input("Enter the First Number: ")), int(input("Enter the Second Number: "))
        print("The Summation of the two numbers: ", sam.add(first_value, second_value))
        mystr = input("Enter the input string: ")
        print("The reversed String is: ", sam.reverse_string(mystr))



if __name__ == "__main__":
    wam =  Sample()
    wam.main()

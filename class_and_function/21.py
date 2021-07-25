#  python for Punit Jain.

class Sample:

    def __init__(self) -> None:
        pass

    def add(self, first_value, second_value):
        return first_value + second_value
    def main(self):
        sam = Sample()
        first_value, second_value = int(input("Enter the First Number: ")), int(input("Enter the Second Number: "))
        print("The Summation of the two numbers: ", sam.add(first_value, second_value)) 
if __name__ == "__main__":
    wam =  Sample()
    wam.main()

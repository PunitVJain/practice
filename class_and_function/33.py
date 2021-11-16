#  python with the linux

class Sample(object):

    def __init__(self) -> None:
        super().__init__()
    
    def my_name(self):
        return "Punit Jain"

def main():
    sa_one = Sample()
    print(sa_one.my_name())

if __name__ == "__main__":
    main()

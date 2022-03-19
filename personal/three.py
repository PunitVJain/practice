#  python with Punit Jain
#  find the second largest number from the list in python

class SecondLargest:

    def __init__(self, lst:list) -> None:
        self.lst = lst
    
    @property
    def lst(self):
        return self._lst
    
    @lst.setter
    def lst(self, lst):
        for ele in lst:
            if type(ele) != int:
                raise "The list elements are not valid."
        self._lst = lst

    
    def __max_num(self):
        max_num = self.lst[0]
        for ele in self.lst:
            if ele >= max_num:
                max_num = ele
        return max_num
    
    def sec_lar(self):
        max_num = self.__max_num()
        mod_lst = self.lst.remove(max_num)
        return self.__max_num()
    
if __name__ == "__main__":
    sl = SecondLargest([9, 2, 3, 5, 7, 8, 10, 6, 28, 29, 20])
    print("The Second largest Number is: ", sl.sec_lar())


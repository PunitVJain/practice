# Bubble sort algorithm in python.

class BubbleSort:

    def __init__(self, lst:list) -> None:
        self.lst = lst
    
    def doit(self):
        for iteam in range(len(self.lst)):
            for value in range(len(self.lst)-iteam-1):
                if self.lst[value] > self.lst[value + 1]:
                    self.lst[value], self.lst[value + 1] = self.lst[value+1], self.lst[value]
        return self.lst



mylist = [2, 9, 1, 3, 5, 6, 4, 6, 4]
bs = BubbleSort(mylist)
print(bs.doit())
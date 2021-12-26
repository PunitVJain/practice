# Bubble sort algorithm in python.

class BubbleSort:
    
    def doit(self, lst):
        for iteam in range(len(lst)):
            for value in range(len(lst)-iteam-1):
                if lst[value] > lst[value + 1]:
                    lst[value], lst[value + 1] = lst[value+1], lst[value]
        return lst



mylist = [2, 9, 1, 3, 5, 6, 4, 6, 4]
bs = BubbleSort()
print(bs.doit(mylist))
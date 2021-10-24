# python developer role.


#Write an algorithm to determine if a number n is happy.

#A happy number is a number defined by the following process:

#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.
#Return true if n is a happy number, and false if not.
# 1. function to split the number
# 2. squares of the numbers
# 3. sum of squares of the numbers
# 4. repeat this process until sum of squares is 1

class Example:

    def split_num(self, num:int):
        num = list(map(int, str(num)))
        return num

    def sum_of_sqrs_ele(self, num:list):
        sum_of_ele = sum(list(map(lambda iteam: iteam * iteam, num)))
        return sum_of_ele

    def isHappy(self, num:int):
        loop_value = set()
        if num > 0:
            while True:
                value = self.split_num(num)
                num = self.sum_of_sqrs_ele(value)
                if num == 1:
                    return True
                elif num not in loop_value:
                    loop_value.add(num)
                else:
                    return False


            

if __name__=="__main__":
    ex = Example()
    try:
        num = int(input("Enter the Number: "))
        print(ex.isHappy(num))
    except:
        print("The I/P is not integer.")
    

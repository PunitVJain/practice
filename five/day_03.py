#  class in Punit Jain

class Solution:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self):
        return self.first_name + " " + self.last_name
if __name__ == "__main__":
    sol = Solution("Punit", "Jain")
    print(sol.full_name())
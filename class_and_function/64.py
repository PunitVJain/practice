#  Python leet code 
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.




def rom_to_num(rom:str):
    roman_nums = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    rom_list = list(rom)
    print(rom_list)
    nums = [roman_nums.get(n, n) for n in rom_list]
    print(nums)
    







rom_to_num("XIV")

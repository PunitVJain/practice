#  Python leet code 
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.




def rom_to_num(rom:str):
    roman_nums = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    result = 0
    for iteam in range(len(rom)):
        if iteam + 1 != len(rom) and roman_nums[rom[iteam]]< roman_nums[rom[iteam+1]]:
            result -= roman_nums[rom[iteam]]
        else:
            result += roman_nums[rom[iteam]]
    return result
    







print(rom_to_num("XXVIII"))

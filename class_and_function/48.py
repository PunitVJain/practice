def removeElement(nums, val) -> int:
    nums  = list(map(lambda iteam : iteam if iteam !=val else "_", nums))
    print(nums)
    number_of_elements_replaced = len(list(value for value in nums if isinstance(value, int)))
    return number_of_elements_replaced

print(removeElement([3,2,2,3], 3))

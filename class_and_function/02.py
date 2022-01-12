


num_one = [1, 2, 3]
num_two = [4, 5, 6]

mod_lst = list(map(lambda ele: sum(ele), zip(num_one, num_two)))
print(mod_lst)
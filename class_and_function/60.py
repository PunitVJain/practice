# leet code questions
# Febonici series in generator.

# febo




def febo(limit):
    val, ele = 0, 1
    while val < limit:
        yield val
        val, ele = ele, val + ele

value = febo(10)

print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())




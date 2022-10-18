# 1
print("#1")
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print('id of "int_a" is ', id(int_a))
print('id of "str_b" is ', id(str_b))
print('id of "set_c" is ', id(set_c))
print('id of "lst_d" is ', id(lst_d))
print('id of "dict_e" is ', id(dict_e))

# 2
print("#2")
lst_d.append(4)
lst_d.append(5)
print(lst_d)
print(id(lst_d))

# 3
print("#3")
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# 4
print("#4")
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

# 5
print("#5")
a = 5
p = 7
print(f"Anna has {a} apples and {p} peaches.".format(a, p))

# 6
print("#6")
print("Anna has {0} apples and {1} peaches.".format(5, 7))

# 7
print("#7")
print("Anna has {apples} apples and {peaches} peaches.".format(apples=a, peaches=p))

# 8
print("#8")
print("Anna has {0:5} apples and {1:3} peaches.".format(a, p))

# 9
print("#9")
print(f"Anna has {a} apples and {p} peaches.".format(a, p))

# 10
print("#10")
print("Anna has %d apples and %d peaches." % (a, p))

# 11
print("#11")
dct = {"apples": 5, "peaches": 7}
print("Anna has", dct['apples'], "apples and", dct['peaches'], "peaches.")

# 12
print("#12")
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)

lst_1 = []
lst_1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_1)

# 13
print("#13")
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
# print(list_comprehension)

lst_2 = []
for num in range(10):
    if num % 2 == 0:
        lst_2.append(num // 2)
    else:
        lst_2.append(num * 10)
print(lst_2)

# 14
print("#14")
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)

d_1 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d_1)

# 15
print("#15")
# d_3 = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d_3[num] = num ** 2
#     else:
#         d_3[num] = num // 0.5
# print(d_3)

d_4 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d_4)

# 16
print("#16")
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
# print(dict_comprehension)

dict_reg = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_reg[x] = x ** 3
print(dict_reg)

# 17
print("#17")
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
# print(dict_comprehension)

dict_reg_2 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_reg_2[x] = x ** 3
    else:
        dict_reg_2[x] = x
print(dict_reg_2)

# 18
print("#18")
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
# print (foo(1,3))

foo_1 = lambda x, y: x if x < y else y
print(foo_1(1, 3))

# 19
print("#19")


# foo = lambda x, y, z: z if y < x and x > z else y
# print(foo(3,5,7))

def foo_2(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo_2(3, 5, 7))
print()

# 20
print("#20")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(lst_to_sort)

lst_to_sort.sort()
print(lst_to_sort)

# 21
print("#21")
lst_to_sort.reverse()
print(lst_to_sort)

# 22
print("#22")
lst_to_sort = list(map(lambda elem: elem * 2, lst_to_sort))
print(lst_to_sort)

# 23
print("#23")
# list_A = [2, 3, 4]
# list_B = [5, 6, 7]
#
# list_A = list(map(lambda x: x + 3 , list_A))
# print(list_A)

# 24
print("#24")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_24 = list(filter(lambda elem: elem % 2 == 1, lst_to_sort))
print(lst_24)

# 25
print("#25")
b = range(-10, 10)
lst_25 = []
for num in b:
    if num < 0:
        lst_25.append(num)
print(lst_25)

# 26
print("#26")


def myfunc(lst_1, lst_2):
    temp_list = []
    for num in range(len(lst_1) - 1):
        for num2 in range(len(lst_1) - 1):
            if lst_1[num] == lst_2[num2]:
                temp_list.append(lst_1[num])
            else:
                pass
    return temp_list


list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print(myfunc(list_1, list_2))

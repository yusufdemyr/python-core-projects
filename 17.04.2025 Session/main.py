
# number = [1,2,3,4,5,6,7,8,9,10]
# evens = [even for even in number if even % 2 == 0]
# print(evens)

# # lambda
# squares = [list(map(lambda x: x**2, number))]
# print(squares)

# squares = [x**2 for x in number]
# print(squares)

# # filter
# squares = list(filter(lambda x: x % 2 == 0, number))
# print(squares)

names = ['Ali', 'Ayşe', 'Veli']

# 1 Ali 2 Ayşe 3 Veli
# for i in range(len(names)):
#     print(i + 1, names[i])

# for i, name in enumerate(names):
#     print(i + 1, name)

# Tek bir tane liste içinde yapılır mı?
# names = ['Ali', 'Ayşe', 'Veli']
# for i, name in enumerate(names, start=1):
#     print(i, name)

fruits = ['Elma', 'Armut', 'Muz']
prices = [10, 20, 30]

for i, (fruit, price) in enumerate(zip(fruits, prices), start=1):
    print(i, fruit, price)

fiyat_dict = {meyve: fiyat for meyve, fiyat in zip(fruits, prices)}
print(fiyat_dict)
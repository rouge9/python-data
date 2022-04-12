# # Squired number
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squired_number = [num ** 2 for num in numbers]
# print(squired_number)
#
# # even numbers
# even = [num for num in numbers if num % 2 == 0]
# print(even)
#
# # checking if number in both files
#
# with open("file_1.txt") as file1:
#     fiel_1_data = file1.readlines()
#
# with open("file_2.txt") as file2:
#     fiel_2_data = file2.readlines()
#
# result = [int(num) for num in fiel_1_data if num in fiel_2_data]
# print(result)

# dictionary comprehension
#
# sentence = "what is the airspeed velocity of an unladen swallow?"
# new_dict = {word: len(word) for word in sentence.split() }
# print(new_dict)

# infinite argument
def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)

add(3,6,7,3,6)


# use of **kwargs
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multi"]
    return n

print(calculate(2, add= 25, multi= 30))


class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.make = kwargs.get("make")



my_car = Car(make="toyota")
print(my_car.make)


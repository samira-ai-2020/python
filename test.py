import numbers


# numbers = [5, 2, 5, 2, 2] 
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

# numbers = [2, 8, 6, 3, 10, 3, 7, 2]
# sam = []
# for number in numbers:
#     if number not in sam:
#         sam.append(number)
# print(sam)

# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print( y )

# customer = {
#     "name" : "samira ghasemi",
#     "age" : 34,
#     "phone" : 9967,
#     "is_verified" : True
# }
# print(customer.get("email", "sami549967@gmail.com")) 

# phone =input("phone : ")
# digits_mapping ={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)

# message = input(">")  
# words = message.split(' ')
# emojis = {
#     ":(": "😢",
#     ":)": "😊"
# }
# outpot = " "
# for word in words:
#     outpot += emojis.get(word, word) + "  " (چرا اینجا دوتا word نوشته شده؟)
# print(outpot)    


# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!")
#     print("welcome dear")
# print("Start")
# greet_user("samira", "ghasemi")
# print("Finish")

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":(": "😢",
#         ":)": "😊"
#     }
#     outpot = " "
#     for word in words:
#         outpot += emojis.get(word, word) + "  " 
#     return outpot   
# message = input("!")
# print(emoji_converter(message))


# try:
#     Name = int(input('age: '))
# except ValueError:
#     print('invalid Value')

# class Point:
#     def __int__(self, x, y):
#          self.x = x
#          self.y = y

#     def move(self):
#         print("move")
         
#     def draw(self):
#         print("draw")   


# point = Point(10)   اینجا وقتی بهش مقدار میدم اجرا نمیشه؟
# print(point.x)

# class Person:
#     def __int__(self, name, family):
#         self.name = name
#         self.family = family
#
#
#     def talk(self):
#         print("hello", self.name)
#
#
# user = Person("samira")
# print(user.name)
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"Hi , i am {self.name}")
#
#
# samira = Person("Samira Ghasemi")
# samira.talk()

# import converters
#
# print(converters.kg_to_lbs(70))

from utils import find_max

numbers = [10, 3, 6, 2]
max = find_max(numbers)
print(max)

# def hello_world():
#    print("Hello World!")
# hello_world()


# def todays_mood():
#   mood = "happy"
#   print("Today I am feeling " + mood)
# todays_mood()


# def print_menu(menu):
#   return "lunch today is: "+ menu
# print(print_menu("Steak and corn"))

# def sum_of_two_numbers(a, b):
#   result = a + b
#   print(result * 2)
# sum_of_two_numbers(2, 3)

# def product(a, b):
#   return a * b
# print(product(22, 7))

# def classify_age(age):
#   if age < 18:
#     print("You are not an adult")
#   else:
#     print("You are an adult")
# classify_age(18)

# def classify_hour(hour):
#   if hour == 2:
#     return "It's taco time"
#   elif hour == 12:
#     return "It's peanut butter jelly time"
#   else:
#     return "It's nap time"
# print(classify_hour(2))
# print(classify_hour(12))
# print(classify_hour(15))



# def classify_score(score):
#   if score == 21:
#     return "Blackjack!"
#   elif score > 21:
#     return "Bust" 
#   elif score >= 17 and score < 21:
#     return "Nice Hand"
#   else:
#     return "Hit Me!"
# print(classify_score(21))
# print(classify_score(19))
# print(classify_score(12))
# print(classify_score(41))




# def get_first (lst):
#   length_of_lst = len(lst)
#   if length_of_lst // 2 == 0:
#     print("middle number cannot be found")
#   else:
#     (length_of_lst + 1) / 2
# print(get_first([3, 6, 1, 2, 5]))

def print_middle_integer(numbers):
    if len(numbers) % 2 == 0:
        print("There is no middle integer in the list since it has an even number of elements.")
    else:
        middle_index = len(numbers) // 2
        print("The middle integer is:", middle_index)

# Example usage:
numbers = [1, 2, 3, 4, 5]
print_middle_integer(numbers)

  



  
  



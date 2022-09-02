import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

person_who_will_pay = random.choice(names)
print(person_who_will_pay)
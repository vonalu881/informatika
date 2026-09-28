def century_message(name, age, current_year):
    x = (100 - age) + current_year
    return f'{name}, тебе исполнится 100 лет в {x} году'

if __name__ == "__main__":
    name = input("введите имя")

if __name__ == "__main__":
    age = int(input("введите возраст"))

if __name__ == "__main__":
    current_year = int(input("введите год"))

print(century_message(name, age, current_year))
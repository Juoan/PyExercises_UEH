from random import randint

# Ex1:
def vote_eligible():
    age = int(input("Your age: "))
    print("You can vote!") if age >= 18 else print(f"Wait for {18 - age} more years")

# Ex2:
def is_even():
    num = int(input("Enter a number: "))
    print("The number is even!") if num % 2== 0 else print("The number is odd!")

# Ex3:
def div_by_7():
    num = int(input("Enter a number: "))
    print(f"{num} is divisible by 7") if num % 7 == 0 else print(f"{num} is not divisible by 7")

# Ex4:
def div_by_3():
    num = input("Enter a number: ")
    print(f"{num[-1]} is divisible by 3") if int(num[-1]) % 3 == 0 else print(f"{num[-1]} is not divisible by 3")

# Ex5:
def guess_num():
    guess = input("Guess a number between 1 and 9: ")
    ran_num = randint(1,9)
    if guess == ran_num:
        print("You guessed it!")
    else:
        print("You didn't guess it! \n The number was: ", ran_num)

# Ex6:
def days():
    day = input("Enter a day of the week: ")
    day_map = {
        "1": "Sunday",
        "2": "Monday",
        "3": "Tuesday",
        "4": "Wednesday",
        "5": "Thursday",
        "6": "Friday",
        "7": "Saturday"
    }
    print(day_map.get(day, "Invalid input"))

if __name__ == '__main__':
    days()


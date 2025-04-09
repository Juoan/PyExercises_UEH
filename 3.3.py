import random

# Ex1:
def count_to_10():
    for i in range(1, 11):
        print(i)

# Ex2:
def count_sum():
    n = int(input("Enter a number: "))
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(f"The sum is {sum}")

# Ex3:
def count_sum_even_odd():
    n = int(input("Enter a number: "))
    sum_even = 0
    sum_odd = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    print(f"The sum of even numbers is {sum_even}")
    print(f"The sum of odd numbers is {sum_odd}")

# Ex4:
def is_vowels():

    word = input("Enter a word: ").lower()
    count = 0
    vowels = []

    for letter in word:
        if letter in "aeiou":
            vowels.append(letter)
            count += 1
    print(f"The word contains {count} vowels which are {''.join(vowels)}")

# Ex5:
def count_words_in_sentence():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print(f"The sentence contains {len(words)} words")

# Ex6:
def game_engine():
    game_mode = input("Choose a game mode (easy, medium, hard): ").lower()

    if game_mode == "easy":
        play_times = 10
    elif game_mode == "medium":
        play_times = 6
    else:
        play_times = 4

    num = random.randint(1, 100)

    for i in range(play_times):
        guess_num = int(input("Guess a number from 1 to 100: "))
        if num == guess_num:
            print(f"You are genius. After {i+1} time(s).")
            break
        elif num > guess_num:
            print(f"Wrong, your number {guess_num} is less than the computer's number.")
        else:
            print(f"Wrong, your number {guess_num} is greater than the computer's number.")
    else:
        print(f"Game over! The correct number was {num}.")

if __name__ == '__main__':
    game_engine()
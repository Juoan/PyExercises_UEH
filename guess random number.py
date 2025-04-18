"""
Viết 1 game chgo phép người dùng đoán số từ 1 đến 100.
Game có 3 cấp độ chơi:
    - dễ - đoán tối đa 9 lần
    - vừa - đoán tối đa 6 lần
    - khó - đoán tối đa 4 lần
Sau khi người dùng hoàn tất 1 lần chơi,
    chương trình sẽ hỏi người dùng có chơi nữa không.
    - Nếu người chơi đồng ý thì tiếp tục 1 lần chơi mới.
    - Nếu không thì kết thúc trò chơi, thống kê số lần chơi thắng/thua
"""

import random

# Thống kê toàn cục
player_wins = 0
player_loses = 0

def retry():
    while True:
        restart = input("\nDo you wish to try again? (y/n): ").lower()
        if restart == "y":
            return True
        elif restart == "n":
            return False
        else:
            print("Please enter y or n.")

def guess_the_number():
    global player_wins, player_loses

    is_restart = True

    while is_restart:
        print("1. Easy - with 9 guesses")
        print("2. Medium - with 6 guesses")
        print("3. Hard - with 4 guesses")

        while True:
            try:
                lvl = int(input("\nChoose your level [1 - 3]: "))
                if lvl == 1:
                    max_attempts = 9
                    break
                elif lvl == 2:
                    max_attempts = 6
                    break
                elif lvl == 3:
                    max_attempts = 4
                    break
                else:
                    print("Please, choose a number between 1 and 3.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        random_number = random.randint(1, 100)
        player_attempts = 0

        while player_attempts < max_attempts:
            try:
                player_guess = int(input("\nGuess the number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if player_guess == random_number:
                print(f"You guessed correctly! After {player_attempts+1} tries!")
                player_wins += 1
                break
            elif player_guess > random_number:
                print(f"Your guess was {player_guess} which is greater than the mystery number.")
            else:
                print(f"Your guess was {player_guess} which is lower than the mystery number.")

            player_attempts += 1

        if player_attempts >= max_attempts and player_guess != random_number:
            print(f"After {player_attempts+1} tries, You lose!")
            player_loses += 1

        is_restart = retry()

    total_games = player_wins + player_loses
    print(f"After {total_games} games, You won {player_wins} games and lose {player_loses} games")
    print("Thank you for playing!")

if __name__ == '__main__':
    guess_the_number()

"""
Viết 1 game Tài xỉu dưa trên nguyên tắc gieo 2 con xúc sắc ngẫu nhiên.
Nếu tổng giá trị của 2 con xúc sắc > 5, gọi là "Tài"
Còn không, gọi là "Xỉu"

Cho người dùng chọn 1 trong 2 trạng thái Tài hoặc Xỉu.
So sánh kết quả.
Hỏi người chơi có tiếp tục không? Nếu có thì chơi tiếp cho dến khi người dùng chọn không.

Mở rộng:
    1. Bắt đầu chơi, cho người dùng 1 số tiền là 100,000. Số tiền cược của mỗi lần chơi
        là 10,000. Sau khi người dùng chọn không chơi tiếp hoặc hết tiền thì ngưng. Sau đó thống kê
        tiền của người chơi, số ván thắng. (có thể cho người dùng chọn số tiền đặt cược)
    2. Cho phép người dùng cược vào số 5 (3 trạng thái thay vì 2 (Tài/Xỉu). Nếu người dùng cược đúng
        thì thắng được 3 lần số tiền cược.
"""
import random

player_money = 100000
player_wins = 0
player_loses = 0

def retry():
    while True:
        restart = input("\nDo you wish to try again? (y/n): ").lower()
        if restart == "y":
            return True
        elif restart == "n":
            print("Thank you for playing!")
            return False
        else:
            print("Invalid input. Please enter y or n.")

def TaiXiu():
    global player_money, player_wins, player_loses
    is_restart = True

    print("If you choose 'Tai', Enter 1, choose 'Xiu' Enter 2 or choose '5' Enter 5.")
    print("Each turn cost 10,000, however, you win 10,000 each time you win.")
    print("If you choose number 5 and won the game, you win 3 times of your money.")

    while is_restart and player_money > 0:
        player_input = input("\nEnter your choice [1, 2 or 5]: ")
        if player_input not in ["1", "2", "5"]:
            print("Invalid input. Please enter 1, 2 or 5.")
            is_restart = retry()
            continue

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total_dice = dice1 + dice2

        print(f"The total of the dice is {total_dice}. And you chose {player_input}")

        if player_input == "1":
            if total_dice > 5:
                player_money += 10000
                player_wins += 1
                print(f"You win! You now have ${player_money} in your account.")
            else:
                player_money -= 10000
                player_loses += 1
                print(f"You lose! You now have ${player_money} in your account.")
        elif player_input == "2":
            if total_dice > 5:
                player_money -= 10000
                player_loses += 1
                print(f"You lose! You now have ${player_money} in your account.")
            else:
                player_money += 10000
                player_wins += 1
                print(f"You win! You now have ${player_money} in your account.")
        elif player_input == "5":
            if total_dice == 5:
                player_money += 30000
                player_wins += 1
                print(f"You win! You now have ${player_money} in your account.")
            else:
                player_money -= 10000
                player_loses += 1
                print(f"You lose! You now have ${player_money} in your account.")

        if player_money > 0:
            is_restart = retry()

    if player_money == 0:
        print("Your balanced is 0. You lose!")
        print("Thank you for playing!")

if __name__ == '__main__':
    TaiXiu()

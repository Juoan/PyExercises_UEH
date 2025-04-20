import math
import random

def n_array(n):
    n_list = []
    for i in range(n):
        i = random.randint(1, 100)
        n_list.append(i)
    return n_list

def menu():
    n = int(input("Nhập số phần tử mong muốn: "))
    n_arr = n_array(n)

    print("""
    1. In ra danh sách vừa tạo.
    2. In đảo ngược danh sách.
    3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
    4. Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
    5. Đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
    6. In ra vị trí các phần tử là số nguyên tố.
    7. Tìm các số duy nhất (không trùng lặp) trong danh sách.
    8. Liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
    9. In ra các đoạn con trong danh sách giảm liên tiếp.
    10. Thoát!
    """)

    while True:

        respond = int(input("Lựa chọn của bạn [1...10]: "))

        if respond == 1:
            print(n_arr)

        elif respond == 2:
            print(n_arr[::-1])

        elif respond == 3:
            print(sorted(n_arr))

        elif respond == 4:
            max_value = n_arr[0]
            max_value_idx = 0

            for i in range(len(n_arr)):
                if n_arr[i] >= max_value:
                    max_value = n_arr[i]
                    max_value_idx = i
            print(f"Max value = {max_value} and located at position {max_value_idx}!")

        elif respond == 5:
            count = 0
            value_idx = []

            user_x = int(input("Enter a number: "))

            for i in range(len(n_arr)):
                if n_arr[i] == user_x:
                    count += 1
                    value_idx.append(i)

            print(f"The number {user_x} appears {count} times at positions {value_idx}")

        elif respond == 6:
            for i in range(len(n_arr)):
                number = n_arr[i]
                if number < 2:
                    continue
                is_prime = True
                for j in range(2, int(number ** 0.5) + 1):
                    if number % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(f" - Vị trí {i}: {number}")

        elif respond == 7:
            freq = {}
            for number in n_arr:
                if number in freq:
                    freq[number] += 1
                else:
                    freq[number] = 1

            new_n_arr = [num for num in freq if freq[num] == 1]
            print("Các số duy nhất (không trùng lặp):", new_n_arr)

        elif respond == 8:
            freq_dict = {}

            for number in n_arr:
                if number in freq_dict:
                    freq_dict[number] +=1
                else:
                    freq_dict[number] = 1
            for num in freq_dict:
                print(f"Giá trị {num} xuất hiện {freq_dict[num]} lần")

        elif respond == 9:
            temp = n_arr[0]
            desc_arr = [temp]

            for i in range(1, len(n_arr)):
                if n_arr[i] < temp:
                    desc_arr.append(n_arr[i])
                else:
                    if len(desc_arr) >= 2:
                        print("Đoạn giảm:", desc_arr)
                    desc_arr = [n_arr[i]]
                temp = n_arr[i]

            if len(desc_arr) >= 2:
                print("Đoạn giảm:", desc_arr)

        elif respond == 10:
            break
        else:
            print("Invalid input! Try again!")
            continue

if __name__ == '__main__':
    menu()
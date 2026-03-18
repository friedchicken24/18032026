import pandas as pd
import matplotlib.pyplot as plt

print("pandas đã được cài đặt thành công!")
print(f"Phiên bản pandas đang sử dụng: {pd.__version__}")

odd_numbers =[x for x in range(1, 21) if x % 2 != 0]
print("Danh sách số lẻ từ 1 đến 20:", odd_numbers)


hello_list = ["Hello" for _ in range(5)]
print("Danh sách chữ Hello:", hello_list)


gen_div_3 = (x for x in range(16) if x % 3 == 0)


print("Giá trị đầu tiên:", next(gen_div_3)) 
print("Giá trị thứ hai:", next(gen_div_3)) 

print("Đang vẽ đồ thị")

plt.plot([1, 2, 3, 4],[10, 20, 25, 30], color='blue', marker='o')
plt.title("Đồ thị đơn giản")
plt.xlabel("Trục X")
plt.ylabel("Trục Y")
plt.show()


div_3_and_5 =[x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print("\nCác số từ 1 đến 100 chia hết cho 3 và 5:", div_3_and_5)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_gen = (x for x in range(1, 21) if is_prime(x))

print("\nCác số nguyên tố từ 1 đến 20 :")

while True:
    try:
        print(next(prime_gen), end=" ")
    except StopIteration:
        print() 
        break
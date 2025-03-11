number = int(input("輸入一個0 到 255 之間的數字: "))

bit_0 = number % 2
bit_1 = (number // 2) % 2
bit_2 = (number // 4) % 2
bit_3 = (number // 8) % 2
bit_4 = (number // 16) % 2
bit_5 = (number // 32) % 2
bit_6 = (number // 64) % 2
bit_7 = (number // 128) % 2

binary_representation = f"{bit_7}{bit_6}{bit_5}{bit_4}{bit_3}{bit_2}{bit_1}{bit_0}"

hex_result = ""
for i in range(0, 8, 4):
    chunk = binary_representation[i:i+4]  
    decimal_value = int(chunk, 2)  
    if decimal_value < 10:
        hex_result += str(decimal_value)  
    else:
        hex_result += chr(decimal_value - 10 + ord('A'))  

print(f"輸入數字: {number}")
print(f"二進位: {binary_representation}")
print(f"十六進位: {hex_result}")

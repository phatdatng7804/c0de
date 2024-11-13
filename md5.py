# Hàm left rotate (xoay trái các bit)
def leftRotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

# Hàm tính toán sin(x) và chuyển đổi kết quả thành số nguyên 32-bit
def customSin(x):
    # Chuẩn bị hàm tính giá trị sin mà không dùng thư viện
    # Sử dụng công thức Taylor để tính gần đúng sin(x)
    # x là số nguyên và chúng ta tính sin(x) với đơn vị radian
    pi = 3.141592653589793
    rad = x * pi / 180  # chuyển độ sang radian
    sin_val = rad
    term = rad
    for i in range(1, 10):
        term *= -1 * rad**2 / ((2 * i) * (2 * i + 1))
        sin_val += term
    return sin_val

# Hàm tính hằng số T mà không dùng thư viện
def compute_T():
    T = []
    for i in range(64):
        # Lấy giá trị tuyệt đối của sin(i+1) và nhân với 2^32
        value = int((2**32) * abs(customSin(i + 1)))
        T.append(value)
    return T

# Hàm chuyển đổi một số nguyên 64-bit thành chuỗi 8 byte (độ dài)
def intTo8byte(n):
    result = []
    for _ in range(8):
        result.append(n & 0xFF)
        n >>= 8
    return bytes(result)

# Hàm chuyển chuỗi thành các khối 64 byte (512-bit)
def pad_message(input_string):
    original_length = len(input_string) * 8
    input_string += '\x80' #đệm độ dài của chuỗi dữ liệu là bôi số cụ thể 
    
    # Đệm thêm bit '0' sao cho độ dài chuỗi chia hết cho 512
    while (len(input_string) * 8) % 512 != 448:
        input_string += '\x00'

    # Thêm độ dài ban đầu (64-bit)
    length_bytes = intTo8byte(original_length)
    input_string += length_bytes.decode('latin1')
    return input_string

# Hàm chính để băm một chuỗi bằng MD5
def md5(input_string):
    # Các hằng số theo chuẩn MD5
    s = [
        7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
        5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
        4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
        6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
    ]

    # Bảng T tự tính toán
    T = compute_T()

    # Khởi tạo giá trị A, B, C, D theo chuẩn MD5
    A0 = 0x67452301 #4 biến này dùng để lưu trữ trạng thái trung gian của thuật toán
    B0 = 0xefcdab89
    C0 = 0x98badcfe
    D0 = 0x10325476

    # Xử lý chuỗi đầu vào
    input_string = pad_message(input_string)

    # Chia chuỗi thành các khối 512-bit (64 byte)
    for i in range(0, len(input_string), 64):
        M = [int.from_bytes(input_string[i + j:i + j + 4].encode('latin1'), byteorder='little') for j in range(0, 64, 4)]
        A, B, C, D = A0, B0, C0, D0

        for j in range(64):
            if 0 <= j <= 15:
                F = (B & C) | (~B & D)
                g = j
            elif 16 <= j <= 31:
                F = (D & B) | (~D & C)
                g = (5 * j + 1) % 16
            elif 32 <= j <= 47:
                F = B ^ C ^ D
                g = (3 * j + 5) % 16
            else:
                F = C ^ (B | ~D)
                g = (7 * j) % 16

            F = (F + A + T[j] + M[g]) & 0xFFFFFFFF
            A = D
            D = C
            C = B
            B = (B + leftRotate(F, s[j])) & 0xFFFFFFFF

        # Cộng với giá trị trước đó của A, B, C, D
        A0 = (A0 + A) & 0xFFFFFFFF
        B0 = (B0 + B) & 0xFFFFFFFF
        C0 = (C0 + C) & 0xFFFFFFFF
        D0 = (D0 + D) & 0xFFFFFFFF

    # Kết hợp A, B, C, D để tạo ra giá trị băm cuối cùng
    result = sum((x << (32 * i)) for i, x in enumerate([A0, B0, C0, D0]))
    return ''.join(f'{(result >> (8 * i)) & 0xFF:02x}' for i in range(16))

# Ví dụ sử dụng hàm
input_string = input("Nhập chuỗi bạn muốn mã hóa MD5: ")
hash_result = md5(input_string)
print(f"Giá trị băm MD5 của '{input_string}' là: {hash_result}")

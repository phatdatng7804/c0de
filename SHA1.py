# Hàm left rotate (xoay trái các bit)
def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

# Hàm chính để băm một chuỗi bằng SHA-1
def sha1(input_string):
    # Khởi tạo các hằng số 32-bit ban đầu
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Tiền xử lý: thêm một bit '1' và các bit '0'
    original_length = len(input_string) * 8  # Độ dài ban đầu (bit)
    input_string += '\x80'  # Thêm bit '1' (10000000 trong hệ nhị phân)

    # Đệm các bit '0' sao cho độ dài tổng cộng chia hết cho 512 trừ 64 bit
    while (len(input_string) * 8) % 512 != 448:
        input_string += '\x00'

    # Thêm độ dài ban đầu (64-bit) vào cuối chuỗi
    input_string += ''.join(chr((original_length >> (8 * i)) & 0xFF) for i in range(7, -1, -1))

    # Chia chuỗi đã tiền xử lý thành các khối 512-bit
    for i in range(0, len(input_string), 64):
        w = [0] * 80
        # Chia khối 512-bit thành 16 từ 32-bit
        for j in range(16):
            w[j] = (ord(input_string[i + j * 4]) << 24) | (ord(input_string[i + j * 4 + 1]) << 16) | \
                   (ord(input_string[i + j * 4 + 2]) << 8) | ord(input_string[i + j * 4 + 3])

        # Mở rộng thành 80 từ 32-bit
        for j in range(16, 80):
            w[j] = left_rotate(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1)

        # Khởi tạo các giá trị tạm thời
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Vòng lặp chính 80 bước
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= j <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Cộng giá trị của khối này vào giá trị tổng
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Kết hợp h0, h1, h2, h3, h4 để tạo ra giá trị băm cuối cùng
    hash_result = (h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4
    return ''.join(f'{(hash_result >> (8 * i)) & 0xFF:02x}' for i in range(19, -1, -1))

# Ví dụ sử dụng hàm
input_string = input("Nhap chuoi ban muon ma hoa : ")
hash_result = sha1(input_string)
print(f"Gia tri cua '{input_string}' la: {hash_result}")

def get_digit(num):
    return num%10

num = 10123421

while(num):
    print(get_digit(num), end=' ')
    num //= 10



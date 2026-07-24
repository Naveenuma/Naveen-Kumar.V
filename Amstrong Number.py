n = int(input())

temp = n
digits = 0

while temp > 0:
    digits += 1
    temp //= 10

temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total += digit**digits
    temp //= 10
if total == n:
    print("Amstrong Number")
else:
    print("Not a Amstrong Number")

a = int(input())
a ^= 0x68747541 ^ 0x69746E65 ^ 0x444D4163
a ^= 0x756E6547 ^ 0x49656E69 ^ 0x6C65746E
print(a)
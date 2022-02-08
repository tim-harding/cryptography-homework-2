def main():
    p = 229
    count = 0
    for i in range(0, p):
        g = i
        is_primitive_root = True
        for i in range(0, p - 1):
            if g == 1:
                is_primitive_root = False
                break
            g = (g * g) % p
        if is_primitive_root:
            count += 1
    print(count)

main()
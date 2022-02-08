def main():
    p = 229
    count = 0
    for g in range(2, p):
        power = g
        is_primitive_root = True
        for i in range(0, p - 2):
            if power == 1:
                is_primitive_root = False
                break
            power = (power * g) % p
        if is_primitive_root:
            print(g)
            count += 1
    print(count)

main()
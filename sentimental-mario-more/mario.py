# TODO
while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            for i in range(1, height + 1):
                print(" " * (height - i) + i * "#" + 2 * " " + i * "#")
            break
        else:
            continue
    except ValueError:
        continue

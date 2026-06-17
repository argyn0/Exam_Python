def showEven(a, b):
    for x in range(a, b+1):
        if x % 2 == 0:
            print(x)


def draw_line(distance, direction, symbol):
    if direction == "vertical":
        for _ in range(distance):
            print(symbol)
    elif direction == "horizontal":
        for _ in range(distance):
            print(symbol, end="")

draw_line(5, "horizontal", "*")
draw_line(5, "vertical", "*")
showEven(1, 10)
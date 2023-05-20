def rectangle(length: int, width: int):
    def ract_area():
        return width * length

    def rect_perim():
        return width * 2 + length * 2

    if type(length) != int or type(width) != int:
        return "Enter valid values!"
    else:
        return f"Rectangle area: {ract_area()}" \
               f"\nRectangle perimeter: {rect_perim()}"


print(rectangle(2, 10))

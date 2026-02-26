def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
  
length = float(input("Enter the length:"))
width = float(input("Enter the width:"))

area = calc_rectangle(length, width)[0]
perimeter = calc_rectangle(length, width)[1]

print(f"Area: {area}, Perimeter: {perimeter}")
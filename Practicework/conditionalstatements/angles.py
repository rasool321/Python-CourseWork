angle = int(input("Enter an angle: "))
if angle > 90 and angle<180:
    print("Obtuse angle")
elif angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
else:
    print("Invalid angle ")

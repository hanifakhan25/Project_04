def main():
    print("Triangle Perimeter")
    side1: float = float(input("What's The Length Of The Side 1?"))
    side2: float = float(input("What's The Length Of The Side 2?"))
    side3: float = float(input("What's The Length Of The Side 3?"))
    Parameter = side1 + side2 + side3
    # Determine The Type Of The Triangle 
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

        # check if it's a right angle triangle (pythagoras theorm)
    sides = sorted([side1, side2, side3])  # Sort sides to identify hypotenuse
    if round(sides[0]**2 + sides[1]**2, 5) == round(sides[2]**2, 5):
        triangle_type += " and Right-angled"
        # result

    print("The Perimeter Of The Triangle Is " + str(Parameter))
    print(f"The Triangle Is {triangle_type}")
if __name__ == '__main__':
    main()
# Dictionary storing the gravity ratio of each planet relative to Earth
PLANET_GRAVITIES = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    """
    Prompts the user for their weight on Earth and a planet name,
    then calculates and displays their equivalent weight on that planet.
    """
    while True:
        try:
            earth_weight = float(input("Enter a weight on Earth: ").strip())
            if earth_weight <= 0:
                print("⚠️ Please enter a valid positive number for weight.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid input. Please enter a numeric value.")

    planet = input("Enter a planet: ").strip()

    if planet in PLANET_GRAVITIES:
        equivalent_weight = round(earth_weight * PLANET_GRAVITIES[planet], 2)
        print(f"The equivalent weight on {planet}: {equivalent_weight}")
    else:
        print("⚠️ Invalid planet name. Please enter a valid planet from the solar system.")

if __name__ == '__main__':
    main()

# Define speed of light as constant
C = 299792458  # Speed of light in meters per second (m/s)

def main():
    while True:  # Keeps asking for mass input (Ctrl+C to stop)
        try:
            # Prompt user for mass input
            mass_in_kg = float(input("Enter kilos of mass: "))

            # Calculate energy using Einstein's formula
            energy_in_joules = mass_in_kg * (C ** 2)

            # Display the breakdown
            print("\ne = m * C^2...")
            print(f"m = {mass_in_kg} kg")
            print(f"C = {C} m/s")
            print(f"{energy_in_joules} joules of energy!\n")

        except ValueError:
            print("Invalid input! Please enter a valid number.")


if __name__ == '__main__':
    main()

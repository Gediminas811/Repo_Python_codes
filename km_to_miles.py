# Program that asks the user for a distance in kilometers and converts it to miles.
# 1 mile ~ 1.60934 km

print("Hello !")

def convert_km_to_miles():
    try:
        # Ask the user for a distance in kilometers
        km_input = input("Enter a distance in kilometers: ")

        # Convert the input to a float
        kilometers = float(km_input)

        # Conversion factor
        miles_per_km = 1 / 1.60934
        
        # Calculate miles
        miles = kilometers * miles_per_km 

        # Print result in a user-friendly format
        # \033[1m -> BOLD, \033[1m -> unBOLD
        print(f"\033[1m{kilometers}\033[0m kilometers is ~ \033[1m{miles:.2f}\033[0m miles.")

    except ValueError:
        # Handle the case where input is not a valid number
        print("Invalid input! Please enter a numeric value for kilometers.")

# Run the conversion function
convert_km_to_miles()

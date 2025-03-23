def main():
    anthon:int = 21 #Anthon age is given as 2 year old 
    beth:int = 6 + anthon # 6year older than anthon
    chen:int = 20 + beth #20 years older than beth
    drew:int = chen + anthon # drew's age is chen plus anthon ages
    ethan:int = chen # same age as chen 

    # derermine Age catogrie (Additional Feature )
    def age_category(age):
        if 13 <= age <= 19:
            return "Teenager"
        elif 20 <= age <= 35:
            return "Young"
        else:
            return "Middle-aged"

    # Print each person's age and category
    print(f"Anthon is {anthon} ({age_category(anthon)})")
    print(f"Beth is {beth} ({age_category(beth)})")
    print(f"Chen is {chen} ({age_category(chen)})")
    print(f"Drew is {drew} ({age_category(drew)})")
    print(f"Ethan is {ethan} ({age_category(ethan)})")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()

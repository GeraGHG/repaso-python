"""
I have a cat and a dog.
I got them at the same time as kitten/puppy. That was humanYears years ago.
Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only

Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that

Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
"""
"""
def first_year():
    return 15

def second_year():
    return 9

def cat(human_years: int) -> int:
    if human_years > 2:
        total_years_cat = first_year() + second_year()
        while human_years > 2:
            total_years_cat += 4
            human_years -= 1
        return total_years_cat
    elif human_years == 2:
        return second_year()
    elif human_years == 1:
        return first_year()
    
def dog(human_years: int) -> int:
    if human_years > 2:
        total_years_dog = first_year() + second_year()
        while human_years > 2:
            total_years_dog += 5
            human_years -= 1
        return total_years_dog
    elif human_years == 2:
        return first_year() + second_year()
    elif human_years == 1:
        return first_year()




def human_cat_dog(human_years: int) -> list:
    cat_years = cat(human_years)
    dog_years = dog(human_years)
    return [human_years, cat_years, dog_years]

def main():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Calculator to decipher the age of your pets (cat and dog)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("If you want to closed write the letter \"q\"")
    print()
    out_flag = False
    while not out_flag:
        while True:
            years = input("How many years have your pets been living with you? ")
            if years == "q": 
                print("Have a nice day!! :)")
                out_flag = True
                break
            if years.isdigit() and int(years) > 0:
                years = int(years) 
                break
            else: print("Enter years above zero")     
        answer = human_cat_dog(years)
        for object, years in zip(["Human", "Cat", "Dog"], answer):
            print(f"{object}: {years}")

if __name__ == '__main__':
    main()
"""

def calculate_pet_ages(human_years):
    cat_years = 15
    dog_years = 15
    if human_years < 1:
        return "Years positive in human years"
    
    if human_years >= 2:
        cat_years += 9
        dog_years += 9 

    if human_years > 2:
        cat_years += 4 * (human_years - 2)
        dog_years += 5 * (human_years - 2)
    return [human_years, cat_years, dog_years]


def main():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Calculator to decipher the age of your pets (cat and dog)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("If you want to quit, type \"q\"\n")
    
    while True:
        years = input("How many years have your pets been living with you? ")
        if years == "q":
            print("Have a nice day!! :)")
            break

        if years.isdigit() and int(years) > 0:
            years = int(years)
            answer = calculate_pet_ages(years)
            for pet, age in zip(["Human", "Cat", "Dog"], answer):
                print(f"{pet}: {age}")
        else:
            print("Please enter a valid number of years.")

if __name__ == '__main__':
    main()
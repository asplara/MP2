import my_mod #this module is where we'll perform all our data handling
    
# PART ONE - main menu and user interaction 

# main
print("\nHellloooo, Metalheads!!!")
print("Let's learn a little bit about your favorite Metal artists. \nPick an option below. (Enter Quit to leave)\n")

# We'll want our program to be able to run until the user tell us they want to quit,
# so you'll need to alter this structure as necessary
# Our main loop will present the user with a menu of options, display a table to them based on
# their choices, and present the main menu to them again to let them keep exploring or allow them to quit
print()
print("A: Bands per country")
print("B: Bands formed in year")
print("C: Bands with keyword")
print("D: Longest rocking bands\n")

# get user's choice 
user_choice = input()
while user_choice:
# make sure we give the user the opportunity to quit the program
    if user_choice == "Quit":
        print("Good Bye!")
        break

# If the user selects A, call the appropriate functions from your data module to print out a table,
# with countries in the first column and the number of bands formed in that country in the second column
    if user_choice == "A":
        z=my_mod.get_bands_per_country() 
        my_mod.print_table(z, "Country", "Num of Bands")
        print()
        print("A: Bands per country")
        print("B: Bands formed in year")
        print("C: Bands with keyword")
        print("D: Longest rocking bands\n")
        user_choice=input()

# If the user selects B, ask them to enter a year
    elif user_choice == "B":
        print("Want to see how Metal a given year was? \nEnter a year and check out which bands formed that year: ")
        year= input()
        m= my_mod.get_bands_formed_in_year(year) 
        my_mod.print_table(m , "Bands", "Country") 
        print()
        print("A: Bands per country")
        print("B: Bands formed in year")
        print("C: Bands with keyword")
        print("D: Longest rocking bands\n")
        user_choice=input()
        

# If the user enters C, we'll let them enter a keyword and print out a table showing them the bands
# who play that musical style
    elif user_choice == "C":
        print("Looking for a specific flavor of Metal? Enter a keyword: ")
        keyword= input().lower()
        x=my_mod.get_bands_with_style(keyword) 
        my_mod.print_table(x, "Bands", "Style") 
        print()
        print("A: Bands per country")
        print("B: Bands formed in year")
        print("C: Bands with keyword")
        print("D: Longest rocking bands\n")
        user_choice=input()
    
# If the user enters D, ask them how many bands they want to see. Then we'll show them a table
# of bands and the number of years they've been active
    elif user_choice == "D":
        print("How many bands do you want to see? ")
        try: num= int(input())
        except ValueError:
            print("Invalid Input")
            print("How many bands do you want to see? ")
            num= int(input())
        n= my_mod.get_longest_lived_bands(num)
        my_mod.print_table(n, "Bands", "Years")
        print()
        print("A: Bands per country")
        print("B: Bands formed in year")
        print("C: Bands with keyword")
        print("D: Longest rocking bands\n")
        user_choice=input()

    else:
        print("Invalid Input, Try Again")
        print()
        print("A: Bands per country")
        print("B: Bands formed in year")
        print("C: Bands with keyword")
        print("D: Longest rocking bands\n")
        user_choice=input()
        
    


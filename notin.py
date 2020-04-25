activity = input("What would you like to do today: ")

if "cinema" not in activity.casefold(): # use the casefold() to avoid confusion with other languages (German) when using lowercase
    print("But I want to go to the cinema")

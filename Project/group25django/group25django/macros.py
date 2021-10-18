weight = input("Enter weight: ")
height = input("Enter height: ")

ideal = input("Is your goal to maintain, lose fat, or gain muscle: ")

if (ideal == "maintain"):
    print("You should eat", 0.7 * float(weight), "to", float(weight), "g of protein a day.")
    print("You should eat", 0.3 * float(weight), "to", 0.5 * float(weight), "g of fat a day.")
    print("The rest of your calories should be from carbohydrates.")
elif (ideal == "lose fat"):
    print("You should eat", 1 * float(weight), "to", 1.2 * float(weight), "g of protein a day.")
    print("You should eat", 0.25 * float(weight), "to", 0.4 * float(weight), "g of fat a day.")
    print("The rest of your calories should be from carbohydrates.")
elif (ideal == "gain muscle"):
    print("You should eat", 1 * float(weight), "to", 1.5 * float(weight), "g of protein a day.")
    print("You should eat", 0.25 * float(weight), "to", 0.4 * float(weight), "g of fat a day.")
    print("The rest of your calories should be from carbohydrates.")

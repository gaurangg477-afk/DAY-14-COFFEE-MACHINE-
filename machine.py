import data
from data import Resources

machine_on = True

while machine_on:
    user_choice = input(
        "What is the drink you want to order (espresso/latte/cappuccino): "
    ).lower()

    # Show resources
    if user_choice == "resources":
        print(f"Water: {Resources['water']}ml")
        print(f"Milk: {Resources['milk']}ml")
        print(f"Coffee: {Resources['coffee']}g")

    # Turn off machine
    elif user_choice == "off":
        machine_on = False
        print("Coffee machine turned off.")

    # Check if drink exists
    elif user_choice in data.Menue:
        drink = data.Menue[user_choice]
        can_make = True

        # Check resources
        for item in drink["ingredient"]:
            if drink["ingredient"][item] > Resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False

        if can_make:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickels = int(input("How many nickels?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01

            total_inserted = quarters + dimes + nickels + pennies

            if total_inserted >= drink["cost"]:
                change = round(total_inserted - drink["cost"], 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_choice}. Enjoy ☕")

                # Deduct resources
                for item in drink["ingredient"]:
                    Resources[item] -= drink["ingredient"][item]

            else:
                print("Sorry that's not enough money. Money refunded.")

    else:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")
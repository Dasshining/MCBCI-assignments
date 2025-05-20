import SGP


def main():
    sgp = SGP.SGP()

    while True:
        print("-----------------------------GALLERY DATA BASE------------------------------------")
        print("General Menu")
        print("1. Register")
        print("2. Remove")
        print("3. Modify")
        print("4. Show")
        print("\n")

        gen_menu_choice = input("Choose an option: ")
        if gen_menu_choice == "1":
            print("-----------------------------REGISTER MENU------------------------------------")
            print("What do you want to register?")
            print("1. Gallery")
            print("2. Painter")
            print("3. Painting")
            print("4. Patron")
            print("5. School")
            print("6. Client")
            print("7. Sale")
            print("8. Back to General Menu")
            print("\n")

            gen_menu_choice_1 = input("Choose an option: ")
            if gen_menu_choice_1 == "1":
                sgp.register_gallery()

            if gen_menu_choice_1 == "2":
                sgp.register_painter()

            if gen_menu_choice_1 == "3":
                sgp.register_painting()

            if gen_menu_choice_1 == "4":
                sgp.register_patron()

            if gen_menu_choice_1 == "5":
                sgp.register_school()

            if gen_menu_choice_1 == "6":
                sgp.register_client()

            if gen_menu_choice_1 == "7":
                sgp.register_sale()

            if gen_menu_choice_1 == "8":
                continue

        if gen_menu_choice == "2":
            print("-----------------------------REMOVE MENU------------------------------------")
            print("What do you want to remove?")
            print("1. Gallery")
            print("2. Painter")
            print("3. Painting")
            print("4. Patron")
            print("5. School")
            print("6. Client")
            print("7. Sale")
            print("8. Back to General Menu")
            print("\n")

            gen_menu_choice_2 = input("Choose an option: ")
            if gen_menu_choice_2 == "1":
                sgp.erase_gallery()

            if gen_menu_choice_2 == "2":
                sgp.erase_painter()

            if gen_menu_choice_2 == "3":
                sgp.erase_painting()

            if gen_menu_choice_2 == "4":
                sgp.erase_patron()

            if gen_menu_choice_2 == "5":
                sgp.erase_school()

            if gen_menu_choice_2 == "6":
                sgp.erase_client()

            if gen_menu_choice_2 == "7":
                sgp.erase_sale()

            if gen_menu_choice_2 == "8":
                continue

        if gen_menu_choice == "3":
            print("-----------------------------MODIFY MENU------------------------------------")
            print("What do you want to modify?")
            print("1. Gallery")
            print("2. Painter")
            print("3. Painting")
            print("4. Patron")
            print("5. School")
            print("6. Client")
            print("7. Sale")
            print("8. Back to General Menu")
            print("\n")

            gen_menu_choice_3 = input("Choose an option: ")
            if gen_menu_choice_3 == "1":
                sgp.modify_gallery()

            if gen_menu_choice_3 == "2":
                sgp.modify_painter()

            if gen_menu_choice_3 == "3":
                sgp.modify_painting()

            if gen_menu_choice_3 == "4":
                sgp.modify_patron()

            if gen_menu_choice_3 == "5":
                sgp.modify_school()

            if gen_menu_choice_3 == "6":
                sgp.modify_client()

            if gen_menu_choice_3 == "7":
                sgp.modify_sale()

            if gen_menu_choice_3 == "8":
                continue

        if gen_menu_choice == "4":
            print("-----------------------------SHOW MENU------------------------------------")
            print("What do you want to Show?")
            print("1. Gallery")
            print("2. Painter")
            print("3. Painting")
            print("4. Patron")
            print("5. School")
            print("6. Client")
            print("7. Sale")
            print("8. Everything")
            print("9. Back to General Menu")
            print("\n")

            gen_menu_choice_4 = input("Choose an option: ")
            if gen_menu_choice_4 == "1":
                sgp.show_gallery()

            if gen_menu_choice_4 == "2":
                sgp.show_painter()

            if gen_menu_choice_4 == "3":
                sgp.show_painting()

            if gen_menu_choice_4 == "4":
                sgp.show_patron()

            if gen_menu_choice_4 == "5":
                sgp.show_school()

            if gen_menu_choice_4 == "6":
                sgp.show_client()

            if gen_menu_choice_4 == "7":
                sgp.show_sale()

            if gen_menu_choice_4 == "8":
                print("Paintings")
                sgp.show_painting()
                print("\n")
                print("Galleries")
                sgp.show_gallery()
                print("\n")
                print("Clients")
                sgp.show_client()
                print("\n")
                print("Sales")
                sgp.show_sale()
                print("\n")
                print("Schools")
                sgp.show_school()
                print("\n")
                print("Patrons")
                sgp.show_patron()
                print("\n")
                print("Painters")
                sgp.show_painter()

            if gen_menu_choice_4 == "9":
                continue

        sol = str(input("\nAnother action? (yes/no): "))
        if sol == "yes":
            pass
        if sol != "yes":
            break


if __name__ == "__main__":
    main()

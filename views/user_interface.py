def greeting():
    print("*" * 50)
    print(f"WELCOME TO THE NOTES APP!")
    print("*" * 50)
    print()


def main_menu():
    print("=" * 50)
    print("Please, choose the action you want to do:")
    print("=" * 50)
    print("\t1. Add note\n"
          "\t2. Search note\n"
          "\t3. Change / delete note\n"
          "\t4. Show all notes\n"
          "\t5. Save notes\n"
          "\t0. EXIT")
    print()


def note_actions():
    print("=" * 50)
    print("Please, choose the action you want to do:")
    print("=" * 50)
    print("\t1. Change note by ID\n"
          "\t2. Delete note by ID\n"
          "\t3. Return to the Main menu")
    print()


def search_note():
    print("=" * 50)
    print("Please, choose the action you want to do:")
    print("=" * 50)
    print("\t1. Searching by ID\n"
          "\t2. Searching by TITLE\n"
          "\t3. Searching by DATE\n"
          "\t4. Return to the previous menu")
    print()


def incorrect_input():
    print("=" * 50)
    print("Incorrect input! Please, choose something from the list!")
    print("=" * 50)
    print()


def search_by_date():
    print("=" * 50)
    print("Choose the period you want looking for:")
    print("=" * 50)
    print("\t1. Month\n"
          "\t2. Day and month\n"
          "\t0. Cancel")
    print()


def search_by_month():
    print("=" * 50)
    print("Choose the month:")
    print("=" * 50)
    print("\t1. January\n"
          "\t2. February\n"
          "\t3. March\n"
          "\t4. April\n"
          "\t5. May\n"
          "\t6. June\n"
          "\t7. July\n"
          "\t8. August\n"
          "\t9. September\n"
          "\t10. October\n"
          "\t11. November\n"
          "\t12. December\n"
          "\t0. Return to the previous menu")
    print()

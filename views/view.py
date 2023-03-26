from controller.note_controller import NoteController
import views.user_interface as u_i
import exceptions as ex
import log


class View:
    __n_c = NoteController()

    def run(self):
        u_i.greeting()

        while True:
            u_i.main_menu()
            op = ex.check_input("Enter the number from the list")

            if op == 1:
                print("You've chosen to add note.\n")
                res = self.__n_c.create_note()
                log.logg("1. Add note", res)
                print(res)
                print()

            elif op == 2:
                print("You've chosen to search note.\n")
                self.__menu_search_note()

            elif op == 3:
                print("You've chosen to change or delete note.\n")

                while True:
                    u_i.note_actions()
                    ad_op = ex.check_input("Enter the number from the list")

                    if ad_op == 1:
                        print("You've chosen to change note by ID.\n")
                        res = self.__n_c.change_note()
                        log.logg("3. Change / delete note -> 1. Change note by ID", res)
                        print(res)
                        print()

                    elif ad_op == 2:
                        print("You've chosen to delete note by ID.\n")
                        res = self.__n_c.delete_note()
                        log.logg("3. Change / delete note -> 2. Delete note by ID", res)
                        print(res)
                        print()

                    elif ad_op == 3:
                        print()
                        break

                    else:
                        u_i.incorrect_input()

            elif op == 4:
                print("You've chosen to show all notes.\n")
                print(self.__n_c.read_all())
                print()

            elif op == 5:
                print("Sorry! This function is not available yet! :(\n")

            elif op == 0:
                print("The program has finished working.")
                break

            else:
                u_i.incorrect_input()

    def __menu_search_note(self):
        while True:
            u_i.search_note()
            ad_op1 = ex.check_input("Enter the number from the list")

            if ad_op1 == 1:
                print("You've chosen to search note by ID.\n")
                print(self.__n_c.search_note_by_id())

            elif ad_op1 == 2:
                print("You've chosen to search note by TITLE.\n")
                print(self.__n_c.search_note_by_title())

            elif ad_op1 == 3:
                print("You've chosen to search note by DATE.\n")
                self.__menu_search_by_date()

            elif ad_op1 == 4:
                print()
                break

            else:
                u_i.incorrect_input()

    def __menu_search_by_date(self):
        while True:
            u_i.search_by_date()
            ad_op2 = ex.check_input("Enter the number from the list")

            if ad_op2 == 1:
                print("You've chosen to search note by Month.\n")
                self.__menu_search_by_month_day(ad_op2)

            elif ad_op2 == 2:
                print("You've chosen to search note by Month and Day.\n")
                self.__menu_search_by_month_day(ad_op2)

            elif ad_op2 == 0:
                print()
                break

            else:
                u_i.incorrect_input()

    def __menu_search_by_month_day(self, operation: int):
        while True:
            u_i.search_by_month()
            month = ex.check_input("Enter the month number")

            if 1 <= month <= 12:
                if operation == 1:
                    print(self.__n_c.search_note_by_date(month))
                    break
                elif operation == 2:
                    day = ex.check_day()
                    print(self.__n_c.search_note_by_date(month, day))
                    break
            elif month == 0:
                print()
                break
            else:
                u_i.incorrect_input()

from controller.note_controller import NoteController
import views.user_interface as u_i
import exceptions as ex


class View:
    __n_c = NoteController()

    def run(self):
        u_i.greeting()

        while True:
            u_i.main_menu()
            op = ex.check_input("Enter the number from the list")

            if op == 1:
                print("You've chosen to add note.\n")
                print(self.__n_c.create_note())

            elif op == 2:
                print("You've chosen to search note.\n")

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

                        while True:
                            u_i.search_by_date()
                            ad_op2 = ex.check_input("Enter the number from the list")

                            if ad_op2 == 1:
                                print("You've chosen to search note by Month.\n")

                                while True:
                                    u_i.search_by_month()
                                    month = ex.check_input("Enter the month number")

                                    if 1 <= month <= 12:
                                        print(self.__n_c.search_note_by_month(month))
                                        break
                                    elif month == 0:
                                        print()
                                        break
                                    else:
                                        u_i.incorrect_input()

                            elif ad_op2 == 2:
                                print("Sorry! This function is not available yet! :(\n")

                            elif ad_op2 == 0:
                                print()
                                break

                            else:
                                u_i.incorrect_input()

                    elif ad_op1 == 4:
                        print()
                        break

                    else:
                        u_i.incorrect_input()

            elif op == 3:
                print("You've chosen to change or delete note.\n")

                while True:
                    u_i.note_actions()
                    ad_op = ex.check_input("Enter the number from the list")

                    if ad_op == 1:
                        print("You've chosen to change note by ID.\n")
                        print(self.__n_c.change_note())

                    elif ad_op == 2:
                        print("You've chosen to delete note by ID.\n")
                        print(self.__n_c.delete_note())

                    elif ad_op == 3:
                        print()
                        break

                    else:
                        u_i.incorrect_input()

            elif op == 4:
                print("You've chosen to show all notes.\n")
                print(self.__n_c.read_all())

            elif op == 5:
                print("Sorry! This function is not available yet! :(\n")

            elif op == 0:
                print("The program has finished working.")
                break

            else:
                u_i.incorrect_input()

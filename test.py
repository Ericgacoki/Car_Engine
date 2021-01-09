
class Car_Engine:
    def player_message(self):
        print("|**************************************|")
        print("please follow the instructions carefully")

    def game_(self):
        started = False  # initially the car is stopped.
        for chance in range(1):
            # you are given only one chance to set your name.
            name = input("\n Set name before you start: ")  # input your name (player's name)
            car = input(
                "\n select car: >> {v8, H5racer or marcedes} :").upper()  # select one of the given cars. input converted to uppercase for later use

            if (car == 'V8' or car == 'H5RACER' or car == 'MARCEDES'):  # checks if the car selected is in the list
                print("Your", car, " is ready. !Fully fueled of course. \n")  # opening statement
                for trial in range(0, 7):  # player is given 15 chances to enter an action /command
                    command = input(
                        "Enter car action: -->> ").upper()  # player enters command and it's converted to uppercase
                    if command == 'HELP':  # help prints out the available car actions
                        print("start - to start the car")
                        print("stop _ to stop the car")
                        print("quit - to exit")
                        print("NB: ", name, "You have been  given up to 15 Actions ! \n")  # reminder
                    elif command == 'START':  # this is executed if player enters 'START'
                        if started:  # checks if started=True ie if the car is not stopped
                            print("Hey ", name,
                                  " The Car is already started ! \n")  # notifies the player that the car is already started

                        else:  # executed if started=False
                            started = True  # since the player entered 'START' and the car is stopped, we need to convert "started" bool to True
                            print("Car started... too smoky anyway. go! \n")  # car is now started

                        ''' This is where I'll write the code to be executed when the car engine is started '''
                    elif command == "STOP":  # checks if player enters 'STOP'
                        if not started:  # executed when the car is stopped. ie started=False
                            print("Hey ", name,
                                  " what are you doing ?.The Car is already stopped.\n")  # player is reminded that the car is stopped
                        else:  # gets executed when started=True. ie when the engine is started
                            started = False  # since the player entered 'STOP' and the car is started, we need to convert "started" bool to False
                            print("Car stopped. \n")  # car is now stopped
                    elif command == 'QUIT':  # checks is the player entered 'QUIT' and is so
                        print("Thanks ", name, "for trying this game ")  # prints "thank you message" to player and then
                        break  # the game exits
                    else:  # this is executed when the player enters un understood action. ie action that is not accepted
                        print(
                            "Sorry Boss, I don't understand that...\n")  # the car doesn't know what you mean. At this point,you can ask for help
                else:  # when the 15 chances are depleted
                    print("GAME COMPLETED !.")  # game is over
                    print(name + "'s",
                          "score = $ 150.21 .Congrats !! ")  # this is just to entertain the player and to prompt him/her to play again. This value is fixed
            else:  # if player selects a car from nowhere. ie car not in the list of available cars.
                print("INVALID CAR SELECTION. ", name, " PLEASE TRY AGAIN")  # alert for an invalid selection and
                break  # the game automatically exits.
# create instance of car engine
player = Car_Engine()
player.player_message()
player.game_()

command = ""
started = False

while command != "quit":
    command = input("> ").lower()

    if command == "start":
        if started:
            print("the car is already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print("the car is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
start - to start the car
stop  - to stop the car
quit  - to quit
""")
    elif command == "quit":
        print("game exited")
    else:
        print("sorry, we can't understand")
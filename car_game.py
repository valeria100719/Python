command=""
started=False
while True:
    command=input(">").lower()
    if command == "start":
        if started:
            print("the car is already started")
        else:
            started = True
            print("car start")
    elif command == "stop":
        if not started:
            print("the car is already stopped")
        else:
            started = False
            print("Car stop")
    elif command == "quit":
        break
    elif command == "help":
        print("""
             Start- car start
             Stop-car stop
             Quit-exit""")
    else:
        print("  Sorry, I did not understand")
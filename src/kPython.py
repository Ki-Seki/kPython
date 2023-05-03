from core.engine import command_handler


header = """kPython 1.1
Solve a problem within one single-line Python command. (c) Ki Seki.
Type 'help' for more information; type 'quit' to end the program
"""

if __name__ == "__main__":
    # Print the header information for kPython.
    print(header)

    # Main loop.
    command = input("$ ")
    while command != "quit":
        command_handler(command)
        command = input("$ ")

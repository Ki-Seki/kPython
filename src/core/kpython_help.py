import json

commands_json_path = "commands.json"
help_txt = """kPython is a single-line Python command processor, which is 
very easy to extend itself and to use. In kPython, you can either 
use builtin functions and class methods in those packages:

{}

or use those plugin functions:

{}

Currently, you can use `help(plugin_keyword)` to see a specific help.
"""


def kpython_help():
    """
    Print help information for kPython.
    """
    # Load commands.json
    with open(commands_json_path, "r") as f:
        command = json.load(f)
    # Print help
    print(help_txt.format(command["core"], command["plugin"]))


if __name__ == "__main__":
    kpython_help()

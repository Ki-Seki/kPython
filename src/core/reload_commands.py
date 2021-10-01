import json

command_handler_path = "./core/command_handler.py"
commands_json_path = "commands.json"


def reload_commands():
    """
    Reload all commands in commands.json: add import statements
    of all commands to the header of command_handler.py
    """
    with open(command_handler_path, "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            if lines[i].startswith("#"):  # Find the first comment line
                del lines[0: i]  # delete all lines before the comment line
                break
    with open(commands_json_path, "r") as f:
        commands = json.load(f)
        header = ["import " + ", ".join(commands["builtin"]) + "\n"]  # Deal with builtin commands.
        for item in commands["plugin"]:  # Deal with plugin commands.
            header.append(f"from plugin.{item} import {item}\n")
    with open(command_handler_path, "w") as f:
        f.writelines(header + ["\n"] + lines)
    return True


if __name__ == "__main__":
    command_handler_path = "test.py"
    commands_json_path = "../commands.json"
    if reload_commands():
        print("Successfully reloaded all commands!")

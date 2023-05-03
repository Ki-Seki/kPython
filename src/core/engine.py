import random, sys, os, time # Some useful libraries users might call.

import core.plugin as plugin
from core.plugin import *

def kpython_help():
    """
    Print help information for kPython.
    """
    help_txt = f"""kPython is a single-line Python command processor, which is 
        very easy to extend itself and to use. Currently, you can use 
        `help(plugin_keyword)` to see a specific help. Those keywords are
        {plugin.__all__}
        """
    print(help_txt)


def command_handler(command):
    """
    This is the engine to process a command.
    """
    if command == "help":
        kpython_help()
    else:
        try:
            ans = eval(command)
            if ans is not None:
                print(ans)
        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    command_handler("help")

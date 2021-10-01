import os


def gen_shortcut(dst="."):
    """
    Create a shortcut for kPython in directory, dst.
    """
    with open(dst + "/kPython.cmd", "w") as f:
        f.write("cd " + os.getcwd() + "\nkPython.py")

# Register new plugin here. One line for each plugin.
__all__ = [
    'gen_shortcut', 
    'focus',
    'chat'
    ]

def gen_shortcut(dst="."):
    """
    Create a shortcut for kPython in directory `dst`.
    """

    import os

    dst_path = f"{dst}/kPython" + (".cmd" if os.system == 'nt' else ".sh")
    with open(dst_path, "w") as f:
        f.write(f"cd {os.getcwd()}/src/\n")
        f.write("python kPython.py")


def focus(m=45, r=15):
    """
    Focus on working for m minutes, and then rest for r minutes.
    By default, m=45, r=15.
    """

    from time import sleep
    import winsound

    while True:
        sleep(m * 60)
        winsound.Beep(1000, 3000)
        sleep(r * 60)
        winsound.Beep(1000, 3000)


def chat(prompt):
    """
    ChatGPT in terminal.
    """

    import os
    import openai

    openai.api_key = os.getenv('OPENAI_API_KEY')
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=1000,
    )
    return completion.choices[0].text
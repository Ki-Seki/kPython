"""
This file store all plugins.
"""



# Register new plugin here. One line for each plugin.
__all__ = [
    'gen_shortcut', 
    'focus',
    'chat',
    'arxiv_today'
    ]

def gen_shortcut(dst="."):
    """
    Create a shortcut for kPython in directory `dst`.

    If `dst` is in the system PATH, then you can 
    use kPython by typing `kPython` instead of 
    changing directory and typing `python kPython.py`.
    """

    import os

    dst_path = f"{dst}/kPython" + (".cmd" if os.system == 'nt' else ".sh")
    with open(dst_path, "w") as f:
        f.write(f"cd {os.getcwd()}/src/\n")
        f.write("python kPython.py")


def focus(m=45, r=15):
    """
    Focus on working for `m` minutes, and then rest for `r` minutes.

    Requirements:
    * Windows platform only
    * `pip install winsound`
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

    Requirements:
    * Add your own OPENAI_API_KEY to the OS environment variables.
    * `pip install openai`

    More:
    * Visit: https://platform.openai.com/docs/api-reference/authentication
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

def arxiv_today(kw, max_results=float('inf'), show_abstract=True, download=True, path='.'):
    """
    Fetch the arXiv paper whose title or abstract contains `kw`.

    * Only fetched papers submitted today.
    * Paper abstract will be printed if `show_results=True`
    * Papers will be downloaded if `download=True`
    * Downloaded papers will be saved in `path`.

    Requirements:
    * `pip install arxiv`
    """

    import os
    import arxiv

    search = arxiv.Search(
    query = kw,
    max_results = max_results,
    sort_by = arxiv.SortCriterion.SubmittedDate
    )
    papers = list(search.results())
    cnt = len(papers)

    for i, paper in enumerate(papers):
        print(f'TITLE: {paper.title}')
        print(f'LINK: {paper.links[0]}')
        if show_abstract:
            print(f'ABSTRACT: {paper.summary}')
        if download:
            if not os.path.exists(path):
                os.mkdir(path)
            paper.download_pdf(dirpath=path, filename=f'{paper.get_short_id()}.pdf')
            print(f'Paper downloaded {i+1}/{cnt}.')
        print()
    return 

        

if __name__ == '__main__':
    arxiv_today('LLM', 5, path='./papers/')
    # print(arxiv_today.__doc__)
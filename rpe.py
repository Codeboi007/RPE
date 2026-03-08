from retrieval.search import search_papers
from reasoning.engine import reasoning_engine

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
import time
import sys

console = Console()

# CLI styling
style = Style.from_dict({
    "prompt": "bold cyan",
})

commands = ["exit", "quit", "help", "clear"]

completer = WordCompleter(commands)

session = PromptSession(
    history=FileHistory(".rpe_history")
)


def agent(query):

    with console.status("[yellow]Searching research papers...[/yellow]"):
        docs, meta, dist = search_papers(query)

    with console.status("[yellow]Running reasoning engine...[/yellow]"):
        answer = reasoning_engine(query, docs, meta, dist)

    papers = list({m["paper"] for m in meta[:5]})

    return answer, papers


def show_sources(papers):

    table = Table(title="Sources Used")

    table.add_column("Paper", style="cyan")

    for p in papers:
        table.add_row(p)

    console.print(table)


def show_help():

    console.print(
        Panel(
            """
Commands

help    Show this help menu
clear   Clear the screen
exit    Quit the application
            """,
            title="Help",
            border_style="cyan"
        )
    )


def main():

    console.print(
        Panel.fit(
            "[bold green]Research Paper Engine[/bold green]",
            border_style="cyan"
        )
    )

    while True:

        try:

            query = session.prompt(
                [("class:prompt", "Ask a research question ➜ ")],
                style=style,
                completer=completer
            )

            cmd = query.lower().strip()

            if cmd in ["exit", "quit"]:
                console.print("[bold red]Goodbye.[/bold red]")
                break

            if cmd == "help":
                show_help()
                continue

            if cmd == "clear":
                console.clear()
                continue

            console.print()

            answer, papers = agent(query)

            console.print("\n[bold green]Answer[/bold green]\n")

            stream_text(answer)

            show_sources(papers)

        except KeyboardInterrupt:
            continue

        except EOFError:
            break

def stream_text(text, delay=0.01):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        

    print()

if __name__ == "__main__":
    main()
from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule

console = Console()

default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)
    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return default_message

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file("events.txt")

    title_text = Text("The Dark Forest Adventure", style="bold gradient(purple,cyan)")
    console.print(title_text, justify="center")
    console.print(Panel.fit(
        "[italic bright_white]A chill wind brushes past you...[/italic bright_white]\n"
        "Paths diverge into [green]left[/green] and [cyan]right[/cyan].\n"
        "Type [yellow]exit[/yellow] if you wish to leave this place.",
        border_style="purple",
        subtitle="[dim]Choose wisely[/dim]",
        padding=(1, 2)
    ))
    console.print(Rule(style="bright_black"))

    while True:
        # PR feedback
        choice = Prompt.ask(
            "[bold]Which direction do you choose?[/bold]",
            choices=["left", "right", "exit"],
            show_choices=False
        )
        if choice == "exit":
            console.print("[bold red]You turn away as the forest fades into silence...[/bold red]")
            break
        console.print(Panel(step(choice, events), border_style="cyan", expand=False))

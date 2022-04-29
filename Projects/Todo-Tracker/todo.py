import typer

from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()


@app.command(short_help="Add a new task")
def add(task: str, category: str):
    """
    Add a new task
    """
    typer.echo(f"Adding task {task} in category {category}")


@app.command()
def delete(position: int):
    """
    Delete a task
    """
    typer.echo(f"Deleting task at position {position}")


@app.command()
def update(position: int, task: str = None, category: str = None):
    """
    Update a task
    """
    typer.echo(f"Updating task at position {position} with {task} and category of : {category}")

@app.command()
def show():

    tasks = [("Task 1", "Category 1"), ("Task 2", "Category 2"), ("Task 3", "Category 3")]
    console.print("[bold magenta]Todo List:[/bold magenta] !  " , "👷🏻‍")
    table = Table(show_header=True)



if __name__ == "__main__":
    app()

import typer

from src.lottery_post.command import Command

app = typer.Typer()

@app.command()
def results():
    pass # @todo: implement

def predictions():
    pass # @todo: implement

def get_command_handler(command: str):
    return type(command)

def route(command: str):
    """
    Routes the given command to its corresponding handler class and method.

    This method takes a command string, fetches the corresponding command
    handler class using the `get_command_handler` method, and then retrieves
    the method named 'run' from the handler class.

    Parameters:
    command (str): The command to be routed.

    Returns:
    object: The method object corresponding to the 'run' method
            of the command handler class.

    Raises:
    AttributeError: If the 'run' method is not found in the command handler class.
    """
    command_class = get_command_handler(command)
    return getattr(command_class, Command.RUN_METHOD)

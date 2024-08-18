from typing import Annotated

import src.dispatcher as dispatcher
import typer


app = typer.Typer(no_args_is_help=True)


@app.command()
def predictions():
    pass  # @todo: implement


@app.command()
def pull():
    pass  # @todo: implement


@app.command()
def results():
    pass  # @todo: implement


# https://typer.tiangolo.com/tutorial/printing/
# https://typer.tiangolo.com/tutorial/progressbar/#progress-bar_1
# Progress Bar for large results
# CLI Options / Arguments
# def main(command: Annotated[str, typer.Argument(help="The command to run.")] = "pull"):
# dispatcher.route(command)

if __name__ == "__main__":
    app()

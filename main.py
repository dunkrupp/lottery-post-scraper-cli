import src.dispatcher as dispatcher
import typer

# https://typer.tiangolo.com/tutorial/printing/
# https://typer.tiangolo.com/tutorial/progressbar/#progress-bar_1
# Progress Bar for large results
# CLI Options / Arguments
def main(command: str = typer.Argument(None)):
    dispatcher.route(command)


if __name__ == "__main__":
    typer.run(main)

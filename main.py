import typer


app = typer.Typer(
    no_args_is_help=True,
    pretty_exceptions_enable=True,
    rich_markup_mode='rich'
)


@app.command()
def predictions():
    return 'predictions data'


@app.command()
def pull():
    return 'pull data'


@app.command()
def results():
    return 'results data'


# https://typer.tiangolo.com/tutorial/printing/
# https://typer.tiangolo.com/tutorial/progressbar/#progress-bar_1
# Progress Bar for large results
# CLI Options / Arguments
# def main(command: Annotated[str, typer.Argument(help="The command to run.")] = "pull"):
# dispatcher.route(command)

if __name__ == "__main__":
    app()

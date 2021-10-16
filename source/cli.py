import typer
from loguru import logger
from source.main import hello_world


app = typer.Typer()


@app.command("hello")
def hello():
    hello_world()

if __name__ == "__main__":
    logger.info("Starting CLI application")
    app()
    logger.info("Ending CLI application")
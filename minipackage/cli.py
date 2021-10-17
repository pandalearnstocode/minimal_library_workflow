import typer
from loguru import logger
from minipackage.main import hello_world, hello_mcu, hello_dc


app = typer.Typer()


@app.command("hello")
def hw():
    hello_world()


@app.command("mcu")
def hm():
    hello_mcu()

@app.command("dc")
def hd():
    hello_dc()

if __name__ == "__main__":
    logger.info("Starting CLI application")
    app()
    logger.info("Ending CLI application")

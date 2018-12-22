import romanconverter
import click

@click.command()
@click.argument("value")
def cli(value):
    """Convert from decimal number to Roman numeral."""
    click.echo(romanconverter.convert(int(value), direction="roman"))

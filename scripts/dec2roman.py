import romanconverter
import click

@click.command()
@click.argument("value", type=int)
def cli(value):
    """Convert from decimal number to Roman numeral."""
    click.echo(romanconverter.convert(value, direction="roman"))

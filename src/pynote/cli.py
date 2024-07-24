from datetime import datetime

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--title", default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), help="Note title"
)
@click.option("--body", prompt="Note body", help="Body of your note")
def new(title, body):
    click.echo(f"{title}, {body}")


@cli.command()
def show():
    click.echo("list notes")


@cli.command()
@click.option("--id", help="note id")
@click.option("--title", help="New note title")
@click.option("--body", prompt="New body", help="new body of your note")
def edit(id, title, body):
    click.echo(f"Updated note with id:{id}, title:{title}, body:{body}")


@cli.command()
@click.option("--id", help="note id")
def delete(id):
    click.echo(f"Deleted note with id:{id}")

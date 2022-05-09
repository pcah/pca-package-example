"""Console script for pca-package-example."""

import click


@click.command()
def main():
    """Run the main entrypoint."""
    click.echo("pca-package-example")
    click.echo("=" * len("pca-package-example"))
    click.echo("Example & reference build of pca-scaffold")


if __name__ == "__main__":
    main()  # pragma: no cover

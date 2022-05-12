from click.testing import CliRunner

from pca.packages.package_example import cli


def test_command_line_interface():
    """Test the CLI"""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "pca-package-example" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help" in help_result.output

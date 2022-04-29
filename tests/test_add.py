
import pytest

from click.testing import CliRunner

from cli_tools.calculator import add


def test_add():
    runnner = CliRunner()
    result = runnner.invoke(add, ['10', '20'])
    assert result.exit_code == 0
    assert result.output == '30\n'


def test_add_verbose():
    runnner = CliRunner()
    result = runnner.invoke(add, ['10', '20', '-v'])
    assert result.exit_code == 0
    assert result.output == '10 + 20 = 30\n'


def test_add_multiple():
    runnner = CliRunner()
    result = runnner.invoke(add, ['10', '20', '30', '-v'])
    assert result.exit_code == 0
    assert result.output == '10 + 20 + 30 = 60\n'


def test_add_multiple():
    runnner = CliRunner()
    result = runnner.invoke(add, ['10', '20', '30', '-vv'])
    assert result.exit_code == 0

    expected_output = ''.join([
      '10 + 20 = 30\n',
      '10 + 20 + 30 = 60\n'
    ])
    assert result.output == expected_output

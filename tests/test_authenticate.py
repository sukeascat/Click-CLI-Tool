import pytest


from click.testing import CliRunner

from cli_tools.authenticate import auth


def test_non_admin_auth():
    # arrange
    runner = CliRunner()
    prompt_inputs = '\n'.join([
      'adam',
      'test',
      'test',
      'N'
    ])

    # act
    result = runner.invoke(auth, input=prompt_inputs)

    # asserts
    assert result.exit_code == 0

    expected_output = '\n'.join([
      'username: adam',
      'password: ',
      'Repeat for confirmation: ',
      'Are you and admin? [y/N]: N',
      'Logging in adam',
      ''
    ])
    assert result.output == expected_output


def test_admin_auth():
    # arrange
    runner = CliRunner()
    prompt_inputs = '\n'.join([
      'adam',
      'test',
      'test',
      'y',
      '207'
    ])

    # act
    result = runner.invoke(auth, input=prompt_inputs)

    # asserts
    assert result.exit_code == 0
    expected_output = '\n'.join([
      'username: adam',
      'password: ',
      'Repeat for confirmation: ',
      'Are you and admin? [y/N]: y',
      'Admin ID> 207',
      'Logging in admin adam (ID = 207)',
      ''
    ])
    assert result.output == expected_output

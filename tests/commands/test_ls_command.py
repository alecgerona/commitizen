import pytest
import sys
from commitizen import cli, commands

from pytest_mock import MockerFixture


def test_list_cz(config, mocker: MockerFixture):
    write_mock = mocker.patch("commitizen.out.write")
    commands.ListCz(config)()
    write_mock.assert_called_once()


def test_ls_command_shows_description_when_use_help_option(
    mocker: MockerFixture, capsys, file_regression
):
    testargs = ["cz", "ls", "--help"]
    mocker.patch.object(sys, "argv", testargs)
    with pytest.raises(SystemExit):
        cli.main()

    out, _ = capsys.readouterr()
    file_regression.check(out, extension=".txt")
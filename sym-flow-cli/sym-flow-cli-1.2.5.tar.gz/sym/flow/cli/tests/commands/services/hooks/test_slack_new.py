import uuid
from unittest.mock import patch

import pytest

from sym.flow.cli.commands.services.hooks.slack_new import get_magic_url, slack_new
from sym.flow.cli.errors import NotAuthorizedError
from sym.flow.cli.helpers.constants import DEFAULT_API_URL
from sym.flow.cli.tests.conftest import get_mock_response


class TestSlackNewCreateHook:
    """Suite for testing Slack installation."""

    MOCK_MAGIC_URL = "http://fake-test.symops.com"

    @patch("sym.flow.cli.commands.services.hooks.slack_new.webbrowser.open")
    @patch(
        "sym.flow.cli.commands.services.hooks.slack_new.click.confirm",
        return_value=True,
    )
    @patch(
        "sym.flow.cli.commands.services.hooks.slack_new.get_magic_url",
        return_value=MOCK_MAGIC_URL,
    )
    def test_slack_install_open_browser(
        self, mock_get_magic_url, mock_click_confirm, mock_webbrowser_open
    ):
        fake_service_id = str(uuid.uuid4())
        slack_new(DEFAULT_API_URL, fake_service_id)
        mock_get_magic_url.assert_called_once_with(
            api_url=DEFAULT_API_URL, service_id=fake_service_id
        )
        mock_click_confirm.assert_called_once()
        mock_webbrowser_open.assert_called_once_with(self.MOCK_MAGIC_URL)

    @patch("sym.flow.cli.commands.services.hooks.slack_new.webbrowser.open")
    @patch(
        "sym.flow.cli.commands.services.hooks.slack_new.click.confirm",
        return_value=False,
    )
    @patch("sym.flow.cli.commands.services.hooks.slack_new.click.secho")
    @patch(
        "sym.flow.cli.commands.services.hooks.slack_new.get_magic_url",
        return_value=MOCK_MAGIC_URL,
    )
    def test_click_command_no_browser(
        self,
        mock_get_magic_url,
        mock_click_secho,
        mock_click_confirm,
        mock_webbrowser_open,
    ):
        fake_service_id = str(uuid.uuid4())
        slack_new(DEFAULT_API_URL, fake_service_id)

        assert self.MOCK_MAGIC_URL in mock_click_secho.call_args.args[0]

        mock_get_magic_url.assert_called_once_with(
            api_url=DEFAULT_API_URL, service_id=fake_service_id
        )
        mock_click_confirm.assert_called_once()
        mock_webbrowser_open.assert_not_called()

    @patch(
        "sym.flow.cli.commands.services.hooks.slack_new.get_magic_url",
        side_effect=ValueError("random error"),
    )
    def test_click_call_catches_unknown_error(self, mock_get_magic_url, click_setup):
        with pytest.raises(ValueError, match="random error"):
            fake_service_id = str(uuid.uuid4())
            slack_new(DEFAULT_API_URL, fake_service_id)

            mock_get_magic_url.assert_called_once_with(
                api_url="https://api.symops.com/api/v1"
            )

    def test_initialize_slack_install_not_authorized_fails(self, sandbox):
        with pytest.raises(NotAuthorizedError, match="symflow login"):
            with sandbox.push_xdg_config_home():
                get_magic_url("http://afakeurl.symops.io/", "uuid")

    @patch(
        "sym.flow.cli.helpers.api.SymRESTClient.get",
        return_value=(get_mock_response(200, data={"url": "http://test.symops.io"})),
    )
    def test_get_magic_url(self, mock_api_get, sandbox):
        with sandbox.push_xdg_config_home():
            assert (
                get_magic_url("http://afakeurl.symops.io/", str(uuid.uuid4()))
                == "http://test.symops.io"
            )

        mock_api_get.assert_called_once()

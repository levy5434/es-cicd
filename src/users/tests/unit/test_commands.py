from io import StringIO
from unittest.mock import patch

import pytest
from django.core.management import call_command
from django.core.management.base import CommandError
from psycopg2 import OperationalError


@pytest.mark.django_db
class TestWaitForDBCommand:

    def test_successful_connection(self, monkeypatch) -> None:
        # Mock psycopg2.connect
        with patch("psycopg2.connect") as mock_connect:
            mock_connect.return_value.__enter__.return_value = True

            out = StringIO()
            call_command("wait_for_db", stdout=out)

            assert "Database is ready!" in out.getvalue()

    def test_failed_connection(self, monkeypatch) -> None:
        # Mock psycopg2.connect to raise error
        with patch("psycopg2.connect") as mock_connect:
            mock_connect.side_effect = OperationalError("Connection failed")

            out = StringIO()
            with pytest.raises(CommandError):
                call_command("wait_for_db", max_retries=1, stdout=out)

    def test_custom_parameters(self) -> None:
        with patch("psycopg2.connect") as mock_connect:
            mock_connect.return_value.__enter__.return_value = True

            out = StringIO()
            call_command("wait_for_db", max_retries=5, wait_seconds=0.1, stdout=out)

            assert "Database is ready!" in out.getvalue()

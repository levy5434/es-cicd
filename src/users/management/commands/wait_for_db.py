import os
import time

import psycopg2
from django.core.management.base import BaseCommand, CommandError
from psycopg2 import OperationalError


class Command(BaseCommand):
    help = "Waits for database connection."

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--max-retries",
            type=int,
            default=30,
            help="Maximum number of connection attempts",
        )
        parser.add_argument(
            "--wait-seconds",
            type=float,
            default=1.0,
            help="Delay between retries in seconds",
        )

    def handle(self, *args, **options) -> None:
        max_retries = options["max_retries"]
        wait_seconds = options["wait_seconds"]

        for i in range(max_retries):
            try:
                conn = psycopg2.connect(
                    dbname=os.getenv("DATABASE_NAME"),
                    user=os.getenv("DATABASE_USERNAME"),
                    password=os.getenv("DATABASE_PASSWORD"),
                    host=os.getenv("DATABASE_HOST"),
                    port=os.getenv("DATABASE_PORT"),
                )
                conn.close()
                self.stdout.write(self.style.SUCCESS("Database is ready!"))
                return
            except OperationalError as e:
                time.sleep(wait_seconds)
                if i == max_retries - 1:
                    raise CommandError(f"Failed to connect to database: {str(e)}")

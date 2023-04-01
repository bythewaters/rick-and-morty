from characters.scraper import sync_characters_with_api

from celery import shared_task


@shared_task
def sync_characters() -> None:
    sync_characters_with_api()

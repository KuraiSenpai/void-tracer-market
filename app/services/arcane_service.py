import requests

from app.config import settings
from app.models import Arcane, ArcaneStats

HEADERS = {"Language": "en"}


def fetch_arcanes() -> list[Arcane]:
    """Fetches items from Warframe Market and filters for Arcanes using requests."""
    url = f"{(settings.items_endpoint())}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

        items = response.json().get("data", [])

        # Filter for arcanes
        arcanes = []
        for item in items:
            tags = item.get("tags", [])
            if settings.ARCANE_TAG_NAME in tags and settings.MOD_TAG_NAME not in tags:
                arcanes.append(Arcane.model_validate(item))

        return arcanes

    except requests.exceptions.RequestException as err:
        print(f"Failed to fetch Arcanes: {err}")
        return []


def get_arcane_medians(arcane: Arcane) -> dict:
    url = f"{settings.statistics_endpoint(arcane.slug)}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        stats = response.json()["payload"]["statistics_closed"]
        stats_48h = stats.get("48hours", [])
        stats_90d = stats.get("90days", [])

        # Ignore unranked (rank 0) arcanes -> Arcane rank can be either 3 or 5
        valid_48h = [item for item in stats_48h if item.get("mod_rank", 0) > 0]
        valid_90d = [item for item in stats_90d if item.get("mod_rank", 0) > 0]

        med_48h = int(valid_48h[-1]["median"]) if valid_48h else None
        med_90d = int(valid_90d[-1]["median"]) if valid_90d else None

        return ArcaneStats(arcane=arcane, med_48h=med_48h, med_90d=med_90d)
    else:
        print(
            f"FAILED: {arcane.name} | URL: {url} | Code: {response.status_code} | Text: {response.text}"
        )
        return ArcaneStats(arcane=arcane, med_48h=None, med_90d=None)

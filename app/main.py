import time

from .core.exporters import ExcelExporter
from .models.arcane import ArcaneStats
from .services import fetch_arcanes, get_arcane_medians
from .utils import sort_arcanes_by_highest_median

SLEEP = 0.35


def main():
    print("Fetching Arcanes...")
    sorted_arcanes: list[ArcaneStats] = sort_arcanes_by_highest_median(get_arcanes())
    print("Exporting to excel...")
    file_path = ExcelExporter.export_stats(sorted_arcanes)
    print(f"Successfully exported stats to: {file_path}")


def get_arcanes() -> list:
    arcanes = fetch_arcanes()
    arcane_stats_list = []

    for arcane in arcanes:
        arcane_stats = get_arcane_medians(arcane)
        arcane_stats_list.append(arcane_stats)
        time.sleep(SLEEP)

    return arcane_stats_list


def print_arcanes(sorted_arcanes: list[ArcaneStats]):
    for arcane_stats in sorted_arcanes:
        print(
            f"{arcane_stats.arcane.name}: "
            f"48h Median = {f'{int(arcane_stats.med_48h)}p' if arcane_stats.med_48h is not None else 'N/A'} | "
            f"90d Median = {f'{int(arcane_stats.med_90d)}p' if arcane_stats.med_90d is not None else 'N/A'}"
        )


if __name__ == "__main__":
    main()

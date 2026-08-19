import time

from .models.arcane import ArcaneStats
from .services import fetch_arcanes, get_arcane_medians
from .utils import sort_arcanes_by_highest_median


def main():
    print("Fetching Arcanes...")
    arcanes = fetch_arcanes()

    arcane_stats_list = []

    for arcane in arcanes:
        arcane_stats = get_arcane_medians(arcane)
        arcane_stats_list.append(arcane_stats)
        time.sleep(0.35)

    sorted_arcanes: list[ArcaneStats] = sort_arcanes_by_highest_median(
        arcane_stats_list
    )

    for arcane_stats in sorted_arcanes:
        print(
            f"{arcane_stats.arcane.name}: "
            f"48h Median = {f'{int(arcane_stats.med_48h)}p' if arcane_stats.med_48h is not None else 'N/A'} | "
            f"90d Median = {f'{int(arcane_stats.med_90d)}p' if arcane_stats.med_90d is not None else 'N/A'}"
        )


if __name__ == "__main__":
    main()

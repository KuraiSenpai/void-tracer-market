from app.models.arcane import ArcaneStats


def sort_arcanes_by_highest_median(stats_list: list[ArcaneStats]) -> list[ArcaneStats]:
    """Sorts ArcaneStats objects by whichever median is higher (48h or 90d)."""
    return sorted(
        stats_list,
        key=lambda item: max(
            [m for m in (item.med_48h, item.med_90d) if m is not None] or [-1]
        ),
        reverse=True,
    )

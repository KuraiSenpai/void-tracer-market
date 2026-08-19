from .services import fetch_arcanes, get_arcane_medians


def main():
    print("Fetching Arcanes...")
    arcanes = fetch_arcanes()

    for arcane in arcanes:
        stats = get_arcane_medians(arcane.slug)

        med_48h = stats["48h"]
        med_90d = stats["90d"]

        print(
            f"{arcane.name}: "
            f"48h Median = {f'{int(med_48h)}p' if med_48h is not None else 'N/A'} | "
            f"90d Median = {f'{int(med_90d)}p' if med_90d is not None else 'N/A'}"
        )


if __name__ == "__main__":
    main()

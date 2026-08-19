import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    # .env
    BASE_URL: str = os.getenv("WF_MARKET_BASE_URL", "")
    ASSETS_URL: str = os.getenv("WF_MARKET_ASSETS_URL", "")
    RATELIMIT_PER_SECOND: int = os.getenv("WF_MARKET_RATELIMIT_PER_SECOND", int("3"))

    ARCANE_TAG_NAME: str = os.getenv("ARCANE_TAG_NAME", "arcane_enhancement")
    MOD_TAG_NAME: str = os.getenv("MOD_TAG_NAME", "mod")

    # API Versions
    API_V1: str = "v1"
    API_V2: str = "v2"

    @property
    def base_url_v1(self) -> str:
        return f"{self.BASE_URL}/{self.API_V1}"

    @property
    def base_url_v2(self) -> str:
        return f"{self.BASE_URL}/{self.API_V2}"

    # Derived
    def items_endpoint(self) -> str:
        return f"{self.base_url_v2}/items"

    def statistics_endpoint(self, slug: str) -> str:
        return f"{self.base_url_v1}/items/{slug}/statistics"


settings = Settings()

from typing import Optional

from pydantic import AliasPath, BaseModel, Field


class Arcane(BaseModel):
    id: str
    name: str = Field(validation_alias=AliasPath("i18n", "en", "name"))
    slug: str
    tags: list[str] = []
    max_rank: Optional[int] = Field(default=0, alias="maxRank")

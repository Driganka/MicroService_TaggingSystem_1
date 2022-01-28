from pydantic import BaseModel
from typing import List

class Tags(BaseModel):
    entity_id: str
    entity_name: str
    tags: List[str]
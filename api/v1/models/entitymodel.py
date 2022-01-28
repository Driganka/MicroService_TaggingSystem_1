from pydantic import BaseModel
from typing import List

class Entities(BaseModel):
    entity_id: str
    entity_name: str
    webhook_url: str
    valid_tags: List[str]
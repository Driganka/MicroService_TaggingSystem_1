from pydantic import BaseModel
from typing import List

class Microservices(BaseModel):
    id: str
    webhook: str

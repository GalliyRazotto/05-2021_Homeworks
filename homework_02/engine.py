"""
create dataclass `Engine`
"""
from pydantic import BaseModel


class Engine(BaseModel):
    volume: int
    pistons: int

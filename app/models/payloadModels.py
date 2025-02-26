from pydantic import BaseModel
from typing import List

class IntegrationJSONSettings(BaseModel):
    label: str
    type: str
    required: bool
    default: str

class TickRequest(BaseModel):
    channel_id: str
    return_url: str
    settings: List[IntegrationJSONSettings]
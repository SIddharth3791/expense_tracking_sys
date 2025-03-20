from pydantic import BaseModel, ConfigDict
from typing import List
from backend.model import category_summary

class ExpenseSummary(BaseModel):
    summary: List[category_summary]
    model_config = ConfigDict(arbitrary_types_allowed=True)
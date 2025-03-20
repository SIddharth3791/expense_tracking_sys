from typing import Optional
from pydantic import BaseModel

class CategorySummary(BaseModel):
    category: str
    total: float
    percentage: Optional[float] = 0.0

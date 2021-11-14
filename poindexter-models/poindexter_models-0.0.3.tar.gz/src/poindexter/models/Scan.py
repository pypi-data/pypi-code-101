from typing import List
from pydantic import BaseModel 


class ScanCreate(BaseModel):
  job_id: int
  report_id: int
  links: List[str]
  plugins: List[str]

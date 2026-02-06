from pydantic import BaseModel

class DashboardStats(BaseModel):
    total_cases: int
    flagged_cases: int
    cleared_cases: int
    pending_cases: int
    high_risk_cases: int
    medium_risk_cases: int
    low_risk_cases: int

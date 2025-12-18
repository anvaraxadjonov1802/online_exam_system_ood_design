from ..enums.violation_type import ViolationType
from datetime import datetime


class Violation:
    def __init__(self, violation_type: ViolationType):
        self.type = violation_type
        self.occurred_at = datetime.utcnow()

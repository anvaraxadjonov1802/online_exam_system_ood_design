from enum import Enum


class AttemptStatus(Enum):
    IN_PROGRESS = "InProgress"
    SUBMITTED = "Submitted"
    AUTO_SUBMITTED = "AutoSubmitted"

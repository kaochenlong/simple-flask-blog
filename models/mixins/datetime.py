from sqlalchemy import DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func


class TimeTrackable:
    created_at = mapped_column(DateTime, server_default=func.now())
    updated_at = mapped_column(
        DateTime, server_default=func.now(), server_onupdate=func.now()
    )

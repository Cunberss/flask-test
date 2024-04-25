from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Float
from src.db.base import Base


class CPUMetrics(Base):
    __tablename__ = 'cpu_metrics'

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.now)
    cpu_percent = Column(Float)

    def to_dict(self):
        return {'id': self.id,
                'timestamp': self.timestamp,
                'cpu_percent': self.cpu_percent}

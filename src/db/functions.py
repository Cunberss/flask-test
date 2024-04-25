from typing import List, Union, Dict

from sqlalchemy import insert, select, desc, func

from src.db.base import get_session
from src.db.models import CPUMetrics


def db_add_record(cpu_percent):
    with get_session() as session:
        stmt = insert(CPUMetrics).values(cpu_percent=cpu_percent)
        session.execute(stmt)
        session.commit()


def db_get_record(sort='default') -> List[CPUMetrics]:
    with get_session() as session:
        stmt = select(CPUMetrics).order_by(desc(CPUMetrics.id)).limit(100)
        results = session.execute(stmt)
        answer = results.all()
        if answer:
            records = [el[0].to_dict() for el in answer]
        else:
            records = []
        if sort == 'default':
            return records
        elif sort == 'min':
            return sorted(records, key=lambda record: record['cpu_percent'])
        elif sort == 'max':
            return sorted(records, key=lambda record: record['cpu_percent'], reverse=True)


def db_get_aggregation_data() -> Union[Dict, None]:
    with get_session() as session:
        stmt = select(CPUMetrics).order_by(desc(CPUMetrics.id)).limit(100)
        results = session.execute(stmt)
        answer = results.all()
        if answer:
            cpu_percent_data = [el[0].to_dict()['cpu_percent'] for el in answer]
            response = {'avg': round(sum(cpu_percent_data) / len(cpu_percent_data), 2),
                        'max': round(max(cpu_percent_data), 2),
                        'min': round(min(cpu_percent_data), 2)}
            return response
        else:
            return None

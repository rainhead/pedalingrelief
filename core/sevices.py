import logging
from datetime import datetime
from typing import Optional

from core.models import *

logger = logging.getLogger(__name__)


def score_to_pct(score: int) -> float:
    return score / 6.0


def receive_restock_post(
    *,
    cleanliness_score: int,
    comment: str,
    fullness_on_arrival: int,
    fullness_on_departure: int,
    needs: list[str],
    pantry: int,
    photo: Optional[str],
    restock_date: datetime,
    reporter_email: Optional[str],
    reporter_name: str,
    submitted_at: datetime,
) -> None:
    reporter = Person.upsert_by_email(reporter_email, name=reporter_name) if reporter_email else None
    restock = Restock(
        cleanliness_pct=score_to_pct(cleanliness_score),
        comment=comment,
        pantry=Pantry.objects.get(id=pantry),
        pct_full_on_arrival=score_to_pct(fullness_on_arrival),
        pct_full_on_departure=score_to_pct(fullness_on_departure),
        photo=photo,
        reporter=reporter,
        restock_date=restock_date,
        submitted_at=submitted_at,
    )
    restock.save()
    restock.needs.set(Item.upsert(*needs))
    pass

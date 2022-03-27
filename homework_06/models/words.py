from homework_06.models.database import db
from sqlalchemy import Column, Integer, String, DateTime, func


class Words(db.Model):
    id = Column(Integer, primary_key=True)
    eng_word = Column(String(120), unique=False, nullable=False)
    rus_word = Column(String(120), unique=False, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<{self.eng_word!r} - {self.rus_word!r}>"

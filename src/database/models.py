from sqlalchemy import column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine  = create_engine('sqlite:///database.db', echo = True)
Base = declarative_base()

class Challenge(Base):
    __tablename__ = 'challenges'

    id = column(Integer,primary_key = True)
    difficulty = column(String, nullable = False)
    date_created = column(datetime, default = datetime.now)
    created_by = column(String, nullable = False)
    title = column(String,nullable = False)
    options = column(String, nullable = False)
    correct_answer_id = column(String, nullable = False)


class ChallengeQuota(Base):
    __tablename__ = 'challenge_quota'

    id = column(Integer, primary_key = True)
    user_id = column(String, nullable = False, unique = True)
    quota_remaining = column(Integer, nullable = False, default = 50)
    last_reset_date = column(DateTime, default = datetime.now)

Base.metadate.create_all(engine)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()
        





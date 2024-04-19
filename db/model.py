from sqlalchemy import create_engine, Column, String, Float, Boolean, INTEGER
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import Session

Base = declarative_base()

class Token(Base):
    __tablename__ = "tokens"
    tok_address = Column(String, primary_key=True)

class User(Base):
    __tablename__ = "user"
    user_address = Column(String, primary_key=True)
    user_balance = Column(Float)
    user_announcement = Column(Boolean)
    user_auto_buy = Column(Boolean)
    min_pos_value = Column(Float)
    slippage_buy = Column(INTEGER)
    slippage_sell = Column(INTEGER)

DATABASE_URL = 'sqlite:///user_record.db'
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
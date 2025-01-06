from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class BaseTest(Base):
    """
    BaseTest model represents the base test entity in the database.

    Attributes:
        id (int): Primary key.
        test_type (str): Type of the test.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
        deleted_at (datetime, optional): Timestamp when the record was deleted.
        data (relationship): Relationship to the TestData model.
    """
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(255),nullable=True)
    goal_metric=Column(String(50))
    desired_outcome=Column(String(50),nullable=True)
    null_hypothesis=Column(String(50),nullable=True)
    alternative_hypothesis=Column(String(50),nullable=True)
    sample_size_group_a=Column(Integer,nullable=True)
    sample_size_group_b=Column(Integer,nullable=True)
    significance_level=Column(Float,default=0.05)
    power=Column(Float,default=0.80)
    bias_control_method=Column(String(50),nullable=True)
    identified_confounders=Column(String(50),nullable=True)
    success_metrics=Column(String(50),nullable=True)
    test_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime, nullable=True)
    data = relationship("TestData", back_populates='test')


class TestData(Base):
    """
    TestData model represents the test data entity in the database.

    Attributes:
        id (int): Primary key.
        test_id (int): Foreign key referencing the BaseTest model.
        variant (str): Variant of the test.
        timestamp (datetime): Timestamp of the test data.
        conversion (bool): Indicates if the conversion happened.
        revenue (float): Revenue generated.
        engagement_minutes (float): Minutes of engagement.
        additional_data (JSONB): Additional data in JSONB format.
        created_at (datetime): Timestamp when the record was created.
        updated_at (datetime): Timestamp when the record was last updated.
        test (relationship): Relationship to the BaseTest model.
    """
    __tablename__ = 'test_data'
    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey('test.id'))
    variant = Column(String(50), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    conversion = Column(Boolean, nullable=False)
    revenue = Column(Float, default=0.0)
    engagement_minutes = Column(Float, default=0.0)
    additional_data = Column(JSONB)
    user_id=Column(String(50),nullable=True)
    session_id=Column(String(50),nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    test = relationship("BaseTest", back_populates="data")


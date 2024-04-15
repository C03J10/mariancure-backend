from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from database import Base

class Role(Base):
    __tablename__ = "role"

    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String, unique=True, index=True)

    users = relationship("User", back_populates="role_assigned")

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role_id = Column(Integer, ForeignKey(Role.role_id))

    role_assigned = relationship("Role", back_populates="users")
    pharmacist_details = relationship("Pharmacist", back_populates="user_account")
    concern_form = relationship("Concern", back_populates="patient_details")


class Pharmacist(Base):
    __tablename__ = "pharmacist"

    pharmacist_id = Column(Integer, primary_key=True, autoincrement=True)
    pharmacist_name = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey(User.user_id))

    user_account = relationship("User", back_populates="pharmacist_details")
    feedback_form = relationship("Feedback", back_populates="pharmacist")


class Concern(Base):
    __tablename__ = "concern"

    concern_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.user_id))
    name = Column(String)
    contact_number = Column(String)
    gender = Column(String)
    height = Column(Float)
    weight = Column(Float)
    age = Column(Integer)
    is_pregnant = Column(Boolean)
    does_breastfeed = Column(Boolean)
    does_drink_alcohol = Column(Boolean)
    does_smoke = Column(Boolean)
    number_of_packs_yearly = Column(Integer)
    chief_complaint_content = Column(String)
    family_history_content = Column(String)
    allergy_history_content = Column(String)
    previous_medication = Column(String)
    current_medication = Column(String)
    date_concern_submitted = Column(DateTime)

    patient_details = relationship("User", back_populates="concern_form")
    feedback_added = relationship("Feedback", back_populates="concern_based_on")


class Feedback(Base):
    __tablename__ = "feedback"

    feedback_id = Column(Integer, primary_key=True, autoincrement=True)
    concern_id = Column(Integer, ForeignKey(Concern.concern_id))
    pharmacist_id = Column(Integer, ForeignKey(Pharmacist.pharmacist_id))
    assessment_content = Column(String)
    plan_content = Column(String)
    date_feedback_submitted = Column(DateTime)

    concern_based_on = relationship("Concern", back_populates="feedback_added")
    pharmacist = relationship("Pharmacist", back_populates="feedback_form")


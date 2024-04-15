from typing import Union, Optional

from pydantic import BaseModel
import datetime

class RoleBase(BaseModel):
    role_name: str

class RoleCreate(RoleBase):
    pass

class RoleGet(RoleBase):
    role_id: int

class PharmacistBase(BaseModel):
    pharmacist_name: str

class PharmacistGet(PharmacistBase):
    pharmacist_id: int

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    full_name: str
    role_name: str
    password: str

class UserGet(UserBase):
    user_id: int
    role_id: int
    role_name: str 
    pharmacist_id: Optional[int]
    pharmacist_name: Optional[str]

class ConcernBase(BaseModel):
    name: str
    contact_number: str
    gender: str
    height: float
    weight: float
    age: int
    is_pregnant: bool
    does_breastfeed: bool
    does_drink_alcohol: bool
    does_smoke: bool
    number_of_packs_yearly: Optional[int]
    chief_complaint_content: str
    family_history_content: str
    allergy_history_content:str
    previous_medication: Optional[str]
    current_medication: str

class ConcernCreate(ConcernBase):
    user_id: int

class ConcernGet(ConcernCreate):
    concern_id: int
    date_concern_submitted: datetime.datetime
    feedback_id: Optional[int]
    pharmacist_id: Optional[int]
    pharmacist_name: Optional[str]
    assessment_content: Optional[str]
    plan_content: Optional[str]
    date_feedback_submitted: Optional[datetime.datetime]

class FeedbackBase(BaseModel):
    assessment_content: str
    plan_content: str

class FeedbackCreate(FeedbackBase):
    concern_id: int
    pharmacist_id: int

class FeedbackGet(FeedbackBase):
    feedback_id: int
    pharmacist: PharmacistGet

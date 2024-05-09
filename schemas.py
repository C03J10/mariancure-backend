from typing import Union, Optional

from pydantic import BaseModel
import datetime

class RoleBase(BaseModel):
    role_name: str

class RoleGet(RoleBase):
    role_id: int

class UserBase(BaseModel):
    username: str
    full_name: str
    email_address: str

class UserCreate(UserBase):
    role_name: str
    password: str

class UserGet(UserBase):
    user_id: int
    role_id: int
    role_name: str 

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
    patient_history_content: str
    previous_medication: Optional[str]
    current_medication: str
    user_id: int

class ConcernGet(BaseModel):
    concern_id: int
    user_id: int
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
    patient_history_content: str
    previous_medication: Optional[str]
    current_medication: str
    date_concern_submitted: datetime.datetime
    assessment_id: Optional[int]
    pharmacist_id: Optional[int]
    pharmacist_full_name: Optional[str]
    assessment_content: Optional[str]
    plan_content: Optional[str]
    date_assessment_submitted: Optional[datetime.datetime]

class FeedbackBase(BaseModel):
    assessment_content: str
    plan_content: str

class FeedbackCreate(FeedbackBase):
    concern_id: int
    user_id: int

class NotificationBase(BaseModel):
    notification_id: int
    role_id: int
    concern_id: int
    notification_type: str
    notification_content: str
    is_seen: bool
    date_notification_created: datetime.datetime

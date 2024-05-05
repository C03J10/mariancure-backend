from sqlalchemy.orm import Session
import bcrypt
from datetime import datetime

import models, schemas

def get_role(db:Session, role_id: int):
    return db.query(models.Role).filter(models.Role.role_id== role_id).first()

def get_role_by_name(db:Session, role_name: str):
    return db.query(models.Role).filter(models.Role.role_name== role_name).first()


def get_all_users(db:Session):
    return db.query(models.User.full_name,
        models.User.username,
        models.User.email_address,
        models.User.user_id,        
        models.Role.role_id,
        models.Role.role_name
        ).join(
        models.User.role_assigned, isouter=True).all()

def get_user(db:Session, user_id: int):
    return db.query(
        models.User.full_name,
        models.User.username,
        models.User.email_address,
        models.User.user_id,        
        models.Role.role_id,
        models.Role.role_name).join(
        models.User.role_assigned, isouter=True).filter(
        models.User.user_id == user_id).first()

def get_user_by_email_address(db:Session, email_address: str):
    return db.query(
        models.User.full_name,
        models.User.username,
        models.User.email_address,
        models.User.user_id,        
        models.Role.role_id,
        models.Role.role_name).join(
        models.User.role_assigned, isouter=True).filter(
        models.User.email_address == email_address).first()
    
def get_user_by_login(db:Session, username: str, password: str):
    user = db.query(models.User).filter(
        models.User.username == username).first()
 
    if(compare_password(password, user.password )):
        return get_user(db, user_id=user.user_id)
    return None

def create_user(db:Session, user:schemas.UserCreate):

    role_id = get_role_by_name(db, user.role_name)
    add_user = models.User (
        full_name = user.full_name,
        username = user.username,
        email_address = user.email_address,
        password = hash_password(user.password),
        role_id = role_id.role_id
    )

    db.add(add_user)
    db.commit()

    return get_user(db, add_user.user_id)

def update_password(db:Session, username:str, password: str):
    user = db.query(models.User).filter(models.User.email_address == username).first()

    setattr(user, "password", hash_password(password))

    db.commit()

    return get_user(db, user.user_id)
    

def get_all_concerns(db:Session):
     return db.query(
        models.Concern.name,
        models.Concern.contact_number,
        models.Concern.gender,
        models.Concern.height,
        models.Concern.weight,
        models.Concern.age,
        models.Concern.is_pregnant,
        models.Concern.does_breastfeed,
        models.Concern.does_drink_alcohol,
        models.Concern.does_smoke,
        models.Concern.number_of_packs_yearly,
        models.Concern.chief_complaint_content,
        models.Concern.family_history_content,
        models.Concern.allergy_history_content,
        models.Concern.patient_history_content,
        models.Concern.previous_medication,
        models.Concern.current_medication,
        models.Concern.user_id,
        models.Concern.concern_id,
        models.Concern.date_concern_submitted,
        models.Assessment.assessment_id,
        models.User.user_id,
        models.User.full_name,
        models.Assessment.assessment_content,
        models.Assessment.plan_content,
        models.Assessment.date_assessment_submitted
        ).join(
        models.Concern.assessment_added, isouter=True).join(
        models.Assessment.pharmacist, isouter=True).all()

def get_concerns_with_feedback(db:Session):
     return db.query(
        models.Concern.name,
        models.Concern.contact_number,
        models.Concern.gender,
        models.Concern.height,
        models.Concern.weight,
        models.Concern.age,
        models.Concern.is_pregnant,
        models.Concern.does_breastfeed,
        models.Concern.does_drink_alcohol,
        models.Concern.does_smoke,
        models.Concern.number_of_packs_yearly,
        models.Concern.chief_complaint_content,
        models.Concern.family_history_content,
        models.Concern.allergy_history_content,
        models.Concern.patient_history_content,
        models.Concern.previous_medication,
        models.Concern.current_medication,
        models.Concern.user_id,
        models.Concern.concern_id,
        models.Concern.date_concern_submitted,
        models.Assessment.assessment_id,
        models.User.user_id,
        models.User.full_name,
        models.Assessment.assessment_content,
        models.Assessment.plan_content,
        models.Assessment.date_assessment_submitted
        ).join(
        models.Concern.assessment_added).join(
        models.Assessment.pharmacist).all()
    
def get_concern(db:Session, concern_id: int):
    return db.query(
         models.Concern.name,
        models.Concern.contact_number,
        models.Concern.gender,
        models.Concern.height,
        models.Concern.weight,
        models.Concern.age,
        models.Concern.is_pregnant,
        models.Concern.does_breastfeed,
        models.Concern.does_drink_alcohol,
        models.Concern.does_smoke,
        models.Concern.number_of_packs_yearly,
        models.Concern.chief_complaint_content,
        models.Concern.family_history_content,
        models.Concern.allergy_history_content,
        models.Concern.patient_history_content,
        models.Concern.previous_medication,
        models.Concern.current_medication,
        models.Concern.user_id,
        models.Concern.concern_id,
        models.Concern.date_concern_submitted,
        models.Assessment.assessment_id,
        models.User.user_id,
        models.User.full_name,
        models.Assessment.assessment_content,
        models.Assessment.plan_content,
        models.Assessment.date_assessment_submitted
        ).join(
        models.Concern.assessment_added, isouter=True).join(
        models.Assessment.pharmacist, isouter=True).filter(
        models.Concern.concern_id == concern_id
        ).first()
        
def get_concern_by_user(db:Session, user_id: int):
    return db.query(
         models.Concern.name,
        models.Concern.contact_number,
        models.Concern.gender,
        models.Concern.height,
        models.Concern.weight,
        models.Concern.age,
        models.Concern.is_pregnant,
        models.Concern.does_breastfeed,
        models.Concern.does_drink_alcohol,
        models.Concern.does_smoke,
        models.Concern.number_of_packs_yearly,
        models.Concern.chief_complaint_content,
        models.Concern.family_history_content,
        models.Concern.allergy_history_content,
        models.Concern.patient_history_content,
        models.Concern.previous_medication,
        models.Concern.current_medication,
        models.Concern.user_id,
        models.Concern.concern_id,
        models.Concern.date_concern_submitted,
        models.Assessment.assessment_id,
        models.User.user_id,
        models.User.full_name,
        models.Assessment.assessment_content,
        models.Assessment.plan_content,
        models.Assessment.date_assessment_submitted
        ).join(
        models.Concern.assessment_added, isouter=True).join(
        models.Assessment.pharmacist, isouter=True).filter(
        models.Concern.user_id == user_id
        ).first()
        
def create_concern(db:Session, concern: schemas.ConcernCreate):

    add_concern = models.Concern (
        user_id = concern.user_id,
        name = concern.name,
        contact_number = concern.contact_number,
        gender = concern.gender,
        height = concern.height,
        weight = concern.weight,
        age = concern.age,
        is_pregnant = concern.is_pregnant,
        does_breastfeed = concern.does_breastfeed,
        does_drink_alcohol = concern.does_drink_alcohol,
        does_smoke = concern.does_smoke,
        number_of_packs_yearly = concern.number_of_packs_yearly,
        chief_complaint_content = concern.chief_complaint_content,
        family_history_content = concern.family_history_content,
        allergy_history_content = concern.allergy_history_content,
        patient_history_content = concern.patient_history_content,
        previous_medication = concern.previous_medication,
        current_medication = concern.current_medication,
        date_concern_submitted = datetime.now()
    )

    db.add(add_concern)
    db.commit()

    return get_concern(db, add_concern.concern_id)


def create_feedback(db:Session, feedback: schemas.FeedbackCreate):

    add_feedback = models.Assessment(
        concern_id = feedback.concern_id,
        user_id = feedback.user_id,
        assessment_content = feedback.assessment_content,
        plan_content = feedback.plan_content,
        date_assessment_submitted = datetime.today()
    )

    db.add(add_feedback)
    db.commit()
    
    return get_concern(db, add_feedback.concern_id)


def hash_password(password: str):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def compare_password(password: str, comp_password: str):
    return bcrypt.checkpw(password.encode('utf-8'), comp_password.encode('utf-8'))


from sqlalchemy.orm import Session
import bcrypt
from datetime import datetime

import models, schemas

def get_all_roles(db:Session):
    return db.query(models.Role).all()

def get_role(db:Session, role_id: int):
    return db.query(models.Role).filter(models.Role.role_id== role_id).first()

def get_role_by_name(db:Session, role_name: str):
    return db.query(models.Role).filter(models.Role.role_name== role_name).first()

def create_role(db:Session, role: schemas.RoleCreate):
    add_role = models.Role(role_name = role.role_name)
    db.add(add_role)
    db.commit()
    db.refresh(add_role)
    return add_role

def get_all_users(db:Session):
    return db.query(models.User.username,
        models.User.user_id,        
        models.Role.role_id,
        models.Role.role_name,
        models.Pharmacist.pharmacist_id,
        models.Pharmacist.pharmacist_name,
        ).join(
        models.User.role_assigned, isouter=True).join(
        models.User.pharmacist_details, isouter=True).all()

def get_user(db:Session, user_id: int):
    return db.query(
        models.User.username,
        models.User.user_id,        
        models.Role.role_id,
        models.Role.role_name,
        models.Pharmacist.pharmacist_id,
        models.Pharmacist.pharmacist_name,).join(
        models.User.role_assigned, isouter=True).join(
        models.User.pharmacist_details, isouter=True).filter(
        models.User.user_id == user_id).first()

def get_user_by_login(db:Session, username: str, password: str):
    user = db.query(models.User).filter(
        models.User.username == username).first()
 
    if(compare_password(password, user.password )):
        return get_user(db, user_id=user.user_id)
    return None

def create_user(db:Session, user:schemas.UserCreate):

    role_id = get_role_by_name(db, user.role_name)
    add_user = models.User (
        username = user.username,
        password = hash_password(user.password),
        role_id = role_id.role_id
    )

    db.add(add_user)
    db.commit()

    if (user.role_name == "Pharmacist"):
        add_pharmacist = models.Pharmacist (
            pharmacist_name = user.full_name,
            user_id = add_user.user_id
        )

        db.add(add_pharmacist)
        db.commit()

    return get_user(db, add_user.user_id)

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
        models.Concern.previous_medication,
        models.Concern.current_medication,
        models.Concern.user_id,
        models.Concern.concern_id,
        models.Concern.date_concern_submitted,
        models.Feedback.feedback_id,
        models.Pharmacist.pharmacist_id,
        models.Pharmacist.pharmacist_name,
        models.Feedback.assessment_content,
        models.Feedback.plan_content,
        models.Feedback.date_feedback_submitted
        ).join(
        models.Concern.feedback_added, isouter=True).join(
        models.Feedback.pharmacist, isouter=True).all()

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
        models.Concern.previous_medication,
        models.Concern.current_medication,
        models.Concern.user_id,
        models.Concern.concern_id,
        models.Concern.date_concern_submitted,
        models.Feedback.feedback_id,
        models.Pharmacist.pharmacist_id,
        models.Pharmacist.pharmacist_name,
        models.Feedback.assessment_content,
        models.Feedback.plan_content,
        models.Feedback.date_feedback_submitted
        ).join(
        models.Concern.feedback_added, isouter=True).join(
        models.Feedback.pharmacist, isouter=True).filter(
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
        models.Concern.previous_medication,
        models.Concern.current_medication,
        models.Concern.user_id,
        models.Concern.concern_id,
        models.Concern.date_concern_submitted,
        models.Feedback.feedback_id,
        models.Pharmacist.pharmacist_id,
        models.Pharmacist.pharmacist_name,
        models.Feedback.assessment_content,
        models.Feedback.plan_content,
        models.Feedback.date_feedback_submitted
        ).join(
        models.Concern.feedback_added, isouter=True).join(
        models.Feedback.pharmacist, isouter=True).filter(
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
        previous_medication = concern.previous_medication,
        current_medication = concern.current_medication,
        date_concern_submitted = datetime.now()
    )

    db.add(add_concern)
    db.commit()

    return get_concern(db, add_concern.concern_id)

def create_feedback(db:Session, feedback: schemas.FeedbackCreate):

    add_feedback = models.Feedback(
        concern_id = feedback.concern_id,
        pharmacist_id = feedback.pharmacist_id,
        assessment_content = feedback.assessment_content,
        plan_content = feedback.plan_content,
        date_feedback_submitted = datetime.today()
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


#return db.query(
# models.Concern.name,
# models.Concern.contact_number,
# models.Concern.gender,
# models.Concern.height,
# models.Concern.weight,
# models.Concern.age,
# models.Concern.is_pregnant,
# models.Concern.does_breastfeed,
# models.Concern.does_drink_alcohol,
# models.Concern.does_smoke,
# models.Concern.number_of_packs_yearly,
# models.Concern.chief_complaint_content,
# models.Concern.family_history_content,
# models.Concern.allergy_history_content,
# models.Concern.previous_medication,
# models.Concern.current_medication,
# models.Concern.user_id,
# models.Concern.concern_id,
# models.Concern.date_submitted, 
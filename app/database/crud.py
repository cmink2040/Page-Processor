from app import fmodels
from sqlalchemy.orm import Session
import app.database.models as models

def create_user(user: fmodels.SaltedUser, session: Session):
    if session:
        if not session.query(models.User).filter_by(username=user.username).first():
            user = models.User(username=user.username, password=user.password, salt=user.salt,
                                session="", session_exp=0)
            session.add(user)
            session.commit()
            session.refresh(user)
            return True
    return False


# Retrieves a user. Returns either a user 
def get_user_data(username: str, session: Session) -> fmodels.SaltedUser | None:
    if session:
        user = session.query(models.User).filter_by(username=username).first()
        if user:
            return user
    return None


# Function to update user.
# Returns False if failed, and True if success.
def update_user(user: models.User, session: Session):
    if session:
        target_user = session.query(models.User).filter_by(username=user.username).first()

        if user:
            target_user = user
            session.commit()
            return True
    return False

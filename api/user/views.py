from typing import List, Tuple, Optional

from molten import (
    HTTP_404, HTTPError, schema, Field, HTTP_201, HTTP_204
)
from molten.contrib.sqlalchemy import (
    Session
)

from .models import User


@schema
class UserSchema:
    id: int = Field(response_only=True)
    email_address: Optional[str]
    display_name: Optional[str]
    title: Optional[str]


def list_users(session: Session) -> List[UserSchema]:
    user_obs = session.query(User).all()
    return [
        UserSchema(
            id=ob.id,
            email_address=ob.email_address,
            display_name=ob.display_name,
            title=ob.title
        ) for ob in user_obs
    ]


def create_user(user: UserSchema, session: Session) -> Tuple[str, UserSchema]:
    user_ob = User(
        email_address=user.email_address,
        display_name=user.display_name,
        title=user.title
    )
    session.add(user_ob)
    session.flush()

    user.id = user_ob.id
    return HTTP_201, user


def delete_user(user_id: str, session: Session) -> Tuple[str, None]:
    session.query(User).filter(User.id == user_id).delete()
    return HTTP_204, None


def get_user(user_id: int, session: Session) -> UserSchema:
    ob = session.query(User).get(user_id)
    if ob is None:
        raise HTTPError(HTTP_404, {"error": f"user {user_id} not found"})

    return UserSchema(
        id=ob.id,
        email_address=ob.email_address,
        display_name=ob.display_name,
        title=ob.title
    )

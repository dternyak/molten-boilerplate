from datetime import datetime
from typing import List, Tuple, Optional

from molten import (
    HTTP_404, HTTPError, schema, Field, HTTP_201, HTTP_204, field
)
from molten.contrib.sqlalchemy import (
    Session
)
import datetime

from .models import Comment


@schema
class CommentSchema:
    content: str
    user_id: int
    id: int = Field(response_only=True)
    date_created: datetime = Field(response_only=True)


def list_comments(session: Session) -> List[CommentSchema]:
    comments = session.query(Comment).all()
    return [
        CommentSchema(
            id=ob.id,
            content=ob.content,
            user_id=ob.user_id,
            date_created=ob.date_created
        ) for ob in comments
    ]


def create_comment(comment: CommentSchema, session: Session) -> Tuple[str, CommentSchema]:
    comment_ob = Comment(
        user_id=comment.user_id,
        content=comment.content,
    )
    session.add(comment_ob)
    session.flush()

    comment.id = comment_ob.id
    comment.date_created = comment_ob.date_created
    return HTTP_201, comment


def delete_comment(comment_id: int, session: Session) -> Tuple[str, None]:
    session.query(Comment).filter(Comment.id == comment_id).delete()
    return HTTP_204, None


def get_comment(comment_id: int, session: Session) -> CommentSchema:
    ob = session.query(Comment).get(comment_id)
    # print(str(ob.date_created))
    if ob is None:
        raise HTTPError(HTTP_404, {"error": f"comment {comment_id} not found"})

    return CommentSchema(
        id=ob.id,
        content=ob.content,
        user_id=ob.user_id,
        date_created=ob.date_created
    )

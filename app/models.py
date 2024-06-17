from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from app.extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, autoincrement=True, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def json(self):
        items = self.__dict__
        if "_sa_instance_state" in items:
            del items["_sa_instance_state"]
        if "updated_at" in items:
            items.update({"updated_at": items.get("updated_at").isoformat()})
        if "created_at" in items:
            items.update({"created_at": items.get("created_at").isoformat()})
        if "deleted_at" in items:
            items.update({"deleted_at": items.get("deleted_at").isoformat()})
        return items


class UserModel(BaseModel):
    __tablename__ = "user"

    username = Column(String(255), nullable=False, unique=False)
    password = Column(String(255), nullable=False)

from dataclasses import dataclass, field
from typing import Literal, Optional
from bson import ObjectId

from .config import MongoDB

mongo = MongoDB()
db = mongo.db


@dataclass
class Message:
    role: Literal["system", "assistant", "user"]
    content: str


@dataclass
class Conversation:
    user_id: str
    messages: list[Message] = field(default_factory=list)
    limited_messages: list[Message] = field(default_factory=list)
    _id: Optional[ObjectId] = None

    def _to_dict(self):
        return {
            "user_id": self.user_id,
            "messages": [m.__dict__ for m in self.messages],
            "limited_messages": [m.__dict__ for m in self.limited_messages],
        }

    def save(self):
        if self._id:
            db.conversations.update_one({"_id": self._id}, {"$set": self._to_dict()})
        else:
            result = db.conversations.insert_one(self._to_dict())
            self._id = result.inserted_id

    @staticmethod
    def get_by_user_id(user_id: str):
        data = db.conversations.find_one({"user_id": user_id})
        if data:
            data["messages"] = [Message(**m) for m in data.pop("messages")]
            data["limited_messages"] = [
                Message(**m) for m in data.pop("limited_messages")
            ]
            return Conversation(**data)
        return None

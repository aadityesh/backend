from mongoengine import Document, StringField, ReferenceField
from .users import User


class Posts(Document):
    username = ReferenceField(User, required=True)
    post_content = StringField(required=True)

from mongoengine import connect, Document, StringField, BooleanField

connect(db="hw8", host="mongodb://localhost:27017")


class Contact(Document):
    full_name = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    message_sent = BooleanField(default=False)
    phone = StringField()
    preferred_contact_method = StringField(choices=["email", "sms"], default="email")

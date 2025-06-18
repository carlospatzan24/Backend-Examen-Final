from flask_marshmallow import Marshmallow
from .models import Contact, ContactReason

ma = Marshmallow()

class ContactReasonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContactReason
        load_instance = True

class ContactSchema(ma.SQLAlchemyAutoSchema):
    reason_info = ma.Nested(ContactReasonSchema) # pylint: disable=no-member
    
    class Meta:
        model = Contact
        load_instance = True
        include_fk = True

contact_reason_schema = ContactReasonSchema()
contact_reasons_schema = ContactReasonSchema(many=True)
contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)
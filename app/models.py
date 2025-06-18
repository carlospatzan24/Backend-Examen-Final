from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ContactReason(db.Model):
    __tablename__ = "contact_reasons"
    id =            db.Column(db.Integer, primary_key=True)
    reason =        db.Column(db.String(50), unique=True, nullable=False)
    description =   db.Column(db.String(255))
    contacts =      db.relationship("Contact", backref="reason_info", lazy=True)

    def __repr__(self):
        return f"<ContactReason {self.id}: {self.reason}>"

class Contact(db.Model):
    __tablename__ = "contacts"
    id =                db.Column(db.Integer, primary_key=True)
    first_name =        db.Column(db.String(80), nullable=False)
    last_name =         db.Column(db.String(80), nullable=False)
    email =             db.Column(db.String(120), nullable=False)
    contact_reason_id = db.Column(db.Integer, db.ForeignKey("contact_reasons.id"), nullable=False)
    message =           db.Column(db.Text, nullable=False)
    created_at =        db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<Contact {self.id}: {self.first_name} {self.last_name}>"
from flask import Blueprint, request, jsonify
from .models import db, Contact, ContactReason
from .schemas import (
    contact_schema, contacts_schema,
    contact_reason_schema, contact_reasons_schema
)

contact_bp = Blueprint("contacts", __name__, url_prefix="/contacts")
reasons_bp = Blueprint("reasons", __name__, url_prefix="/contact-reasons")

# Endpoints para Contactos
@contact_bp.route("/", methods=["POST"])
def add_contact():
    new_contact = contact_schema.load(request.json)
    db.session.add(new_contact)
    db.session.commit()
    return contact_schema.dump(new_contact), 201

@contact_bp.route("/", methods=["GET"])
def get_contacts():
    all_contacts = Contact.query.all()
    return contacts_schema.dump(all_contacts), 200

@contact_bp.route("/<int:contact_id>", methods=["GET"])
def get_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return contact_schema.dump(contact), 200

# Endpoints para Razones de Contacto (solo GET para el frontend)
@reasons_bp.route("/", methods=["GET"])
def get_reasons():
    all_reasons = ContactReason.query.all()
    return contact_reasons_schema.dump(all_reasons), 200
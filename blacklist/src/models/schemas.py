from marshmallow import Schema, fields, validate, validates

class CreateBlacklistInputSchema(Schema):
    email = fields.Email(required=True)
    app_uuid = fields.Str(required=True, validate=validate.Length(equal=36))
    blocked_reason = fields.Str(required=False)
    ip_address = fields.Str(required=True, validate=validate.Length(max=45))

class GetBlacklistInfoInputSchema(Schema):
    email = fields.Email(required=True)

    @validates('email')
    def validate_email(self, value):
        # Puedes agregar validaciones adicionales aquí si es necesario
        pass

class GetBlacklistInfoOutputSchema(Schema):
    found = fields.Bool(required=True)
    reason = fields.Str(required=True)
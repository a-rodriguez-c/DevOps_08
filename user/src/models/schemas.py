from marshmallow import Schema, fields, ValidationError, validate

class CreateUserInputSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=1))
    password = fields.Str(required=True, validate=validate.Length(min=8))
    email = fields.Email(required=True)
    dni = fields.Str()
    fullName = fields.Str()
    phoneNumber = fields.Str()


class ResponseJsonUserSchema(Schema):
    id = fields.UUID()
    createdAt = fields.DateTime(format="iso")


class UpdateUserSchema(Schema):
    status = fields.Str(required=False)
    dni = fields.Str(required=False)
    fullName = fields.Str(required=False)
    phoneNumber = fields.Str(required=False)


class CreateBlacklistInputSchema(Schema):
    email = fields.Email(required=True)
    app_uuid = fields.Str(required=True, validate=validate.Length(equal=36))
    blocked_reason = fields.Str(required=False)
    ip_address = fields.Str(required=True, validate=validate.Length(max=45))


class ResponseJsonBlacklistSchema(Schema):
    id = fields.UUID()
    email = fields.Email()
    app_uuid = fields.Str()
    blocked_reason = fields.Str()
    ip_address = fields.Str()
    created_at = fields.DateTime(format="iso")

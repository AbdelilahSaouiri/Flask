from marshmallow import Schema, fields, validate, ValidationError

class UserSchema(Schema):
    firstName = fields.String(
        required=True,
        validate=[
            validate.Length(max=100),
            validate.Regexp(r'\S', error="firstName cannot be blank")
        ]
    )
    lastName = fields.String(
        required=True,
        validate=[
            validate.Length(max=100),
            validate.Regexp(r'\S', error="lastName cannot be blank")
        ]
    )
    email = fields.Email(required=True)
    password = fields.String(
        required=True,
        validate=[
            validate.Length(min=6, max=100),
            validate.Regexp(r'\S', error="password cannot be blank")
        ]
    ) 

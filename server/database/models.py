from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

class owner(models.Model):
    id = fields.IntField(pk=True)
    document_type = fields.CharField(max_length=50)
    full_name = fields.CharField(max_length=50, null=True)
    address = fields.CharField(max_length=50, null=True)
    phone = fields.CharField(max_length=50, null=True)
    email = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

class vehicles(models.Model):
    id = fields.IntField(pk=True)
    plate = fields.CharField(max_length=50)
    brand = fields.CharField(max_length=50, null=True)
    model = fields.CharField(max_length=50, null=True)
    year = fields.IntField(null=True)
    color = fields.CharField(max_length=50, null=True)
    owner = fields.ForeignKeyField('models.owner')
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
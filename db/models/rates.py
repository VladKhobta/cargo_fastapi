from tortoise.models import Model
from tortoise import fields


class Rate(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    cargo_type = fields.CharField(max_length=254)
    rate = fields.CharField(max_length=254)

    def __str__(self):
        return self.cargo_type

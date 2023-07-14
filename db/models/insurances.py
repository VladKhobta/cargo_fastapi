from tortoise.models import Model
from tortoise import fields


class Insurance(Model):
    date = fields.DateField()
    cargo_type = fields.CharField(max_length=254)
    declared_value = fields.FloatField()
    rate = fields.FloatField()
    value = fields.FloatField()

    def __str__(self):
        return self.value

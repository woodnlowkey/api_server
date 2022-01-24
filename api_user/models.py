from django.db import models

class Bread(models.Model):
    name = models.CharField(max_length=64)
    stock = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField(default=50)
    class Meta:
        db_table = "Bread"

class Topping(models.Model):
    name = models.CharField(max_length=64)
    stock = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField(default=50)
    class Meta:
        db_table = "Topping"

class Cheese(models.Model):
    name = models.CharField(max_length=64)
    stock = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField(default=50)
    class Meta:
        db_table = "Cheese"

class Sauce(models.Model):
    name = models.CharField(max_length=64)
    stock = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField(default=50)
    class Meta:
        db_table = "Sauce"

class Sandwich(models.Model):
    bread = models.ForeignKey(Bread, on_delete=models.DO_NOTHING, db_constraint=False)
    topping = models.ForeignKey(Topping, on_delete=models.DO_NOTHING, db_constraint=False)
    cheese = models.ForeignKey(Cheese, on_delete=models.DO_NOTHING, db_constraint=False)
    sauce = models.ForeignKey(Sauce, on_delete=models.DO_NOTHING, db_constraint=False)
    class Meta:
        db_table = "Sandwich"
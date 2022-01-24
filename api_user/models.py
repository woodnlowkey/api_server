from django.db import models

class Bread(models.Model):
    name = models.CharField(max_length=64)
    stock = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField()
    # 기본값이 적용되지 않는 이슈?
    existence = models.BooleanField(default=True)
    class Meta:
        db_table = "Bread"

class Topping(models.Model):
    name = models.CharField(max_length=64)
    stock = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField()
    existence = models.BooleanField(default=True)
    class Meta:
        db_table = "Topping"

class Cheese(models.Model):
    name = models.CharField(max_length=64)
    stock = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField()
    existence = models.BooleanField(default=True)
    class Meta:
        db_table = "Cheese"

class Sauce(models.Model):
    name = models.CharField(max_length=64)
    stock = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField()
    existence = models.BooleanField(default=True)
    class Meta:
        db_table = "Sauce"

class Sandwich(models.Model):
    bread = models.ForeignKey(Bread, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    existence = models.BooleanField(default=True)
    class Meta:
        db_table = "Sandwich"
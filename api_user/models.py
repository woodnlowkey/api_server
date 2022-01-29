from django.db import models

class Ingredient(models.Model):
    category = models.CharField(
        max_length=32, choices=(
            ('bread', 'bread'), ('topping', 'topping'), 
            ('cheese', 'cheese'), ('sauce', 'sauce')
        ))
    name = models.CharField(max_length=64)
    stock = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    deleted_data = models.BooleanField(default=False)
    class Meta:
        db_table = 'Ingredient'

class Sandwich(models.Model):
    bread = models.ForeignKey(
        'Ingredient', on_delete=models.CASCADE, 
        related_name='bread')
    topping = models.ForeignKey(
        'Ingredient', on_delete=models.CASCADE,
        related_name='topping')
    topping2 = models.ForeignKey(
        'Ingredient', on_delete=models.CASCADE, 
        related_name='topping2', null=True)
    cheese = models.ForeignKey(
        'Ingredient', on_delete=models.CASCADE,
        related_name='cheese')
    sauce = models.ForeignKey(
        'Ingredient', on_delete=models.CASCADE, 
        related_name='sauce')
    sauce2 = models.ForeignKey(
        'Ingredient', on_delete=models.CASCADE,
        related_name='sauce2', null=True)
    price = models.PositiveIntegerField(default=0)
    deleted_data = models.BooleanField(default=False)
    class Meta:
        db_table = "Sandwich"
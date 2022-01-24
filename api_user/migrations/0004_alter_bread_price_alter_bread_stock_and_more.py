# Generated by Django 4.0.1 on 2022-01-24 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0003_cheese_sauce_topping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bread',
            name='price',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='bread',
            name='stock',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='cheese',
            name='price',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='cheese',
            name='stock',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='sauce',
            name='price',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='sauce',
            name='stock',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='topping',
            name='price',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='topping',
            name='stock',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.CreateModel(
            name='Sandwich',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sauce', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='api_user.sauce')),
                ('bread', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='api_user.bread')),
                ('cheese', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='api_user.cheese')),
                ('topping', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='api_user.topping')),
            ],
            options={
                'db_table': 'Sandwich',
            },
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-19 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_pantry_options_alter_person_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

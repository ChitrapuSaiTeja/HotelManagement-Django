# Generated by Django 4.1.5 on 2023-03-31 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broomk', '0003_alter_hotels_name_alter_hotels_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='payprice',
            field=models.IntegerField(default=0),
        ),
    ]

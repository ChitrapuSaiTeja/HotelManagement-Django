# Generated by Django 5.0.6 on 2024-07-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broomk', '0010_alter_hotels_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

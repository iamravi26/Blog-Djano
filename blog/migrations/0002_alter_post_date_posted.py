# Generated by Django 4.1.1 on 2022-09-17 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date_posted",
            field=models.DateTimeField(auto_now=True),
        ),
    ]

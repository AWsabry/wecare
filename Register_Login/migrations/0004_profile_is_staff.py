# Generated by Django 4.1.2 on 2023-10-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Register_Login", "0003_rename_is_staff_profile_is_nurse"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]

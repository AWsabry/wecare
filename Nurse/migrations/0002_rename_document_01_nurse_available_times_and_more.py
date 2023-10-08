# Generated by Django 4.1.2 on 2023-10-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Nurse", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="nurse",
            old_name="document_01",
            new_name="available_times",
        ),
        migrations.RenameField(
            model_name="nurse",
            old_name="document_02",
            new_name="cv",
        ),
        migrations.RenameField(
            model_name="nurse",
            old_name="document_03",
            new_name="proof_of_experience",
        ),
        migrations.AddField(
            model_name="nurse",
            name="years_of_experience",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="nurse",
            name="national_id",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

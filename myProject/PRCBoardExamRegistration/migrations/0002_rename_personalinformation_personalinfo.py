# Generated by Django 4.2.3 on 2023-07-10 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("PRCBoardExamRegistration", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PersonalInformation",
            new_name="PersonalInfo",
        ),
    ]

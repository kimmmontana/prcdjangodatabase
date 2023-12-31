# Generated by Django 4.2.3 on 2023-07-10 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PRCBoardExamRegistration", "0005_educationinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="educationinfo",
            name="PRC_bc",
            field=models.CharField(max_length=4, verbose_name="PRC Course Code"),
        ),
        migrations.AlterField(
            model_name="educationinfo",
            name="PRC_cc",
            field=models.CharField(max_length=4, verbose_name="PRC Course Code"),
        ),
        migrations.AlterField(
            model_name="educationinfo",
            name="PRC_sc",
            field=models.CharField(max_length=4, verbose_name="PRC School Code"),
        ),
    ]

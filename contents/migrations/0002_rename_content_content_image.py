# Generated by Django 4.1.1 on 2022-09-30 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contents", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="content", old_name="content", new_name="image",
        ),
    ]

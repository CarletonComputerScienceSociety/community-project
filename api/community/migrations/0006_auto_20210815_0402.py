# Generated by Django 3.2 on 2021-08-15 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0005_alter_newsitem_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="announcement",
            name="link",
        ),
        migrations.AddField(
            model_name="newsitem",
            name="external_link",
            field=models.CharField(blank=True, max_length=300),
        ),
    ]

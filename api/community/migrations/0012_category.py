# Generated by Django 3.2 on 2021-09-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0011_alter_newsitem_organizations"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
            ],
        ),
    ]

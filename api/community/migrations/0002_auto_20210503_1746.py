# Generated by Django 3.2 on 2021-05-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
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
                ("title", models.CharField(max_length=150)),
                ("description", models.TextField(blank=True, null=True)),
                ("website", models.CharField(max_length=300)),
                ("facebook", models.CharField(max_length=250)),
                ("instagram", models.CharField(max_length=250)),
                ("discord", models.CharField(max_length=250)),
                ("slack", models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="end_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="link",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="start_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

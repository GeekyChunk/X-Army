# Generated by Django 3.2.4 on 2021-06-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

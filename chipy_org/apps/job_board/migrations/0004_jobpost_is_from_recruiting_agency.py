# Generated by Django 2.2.12 on 2020-07-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0003_auto_20200730_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='is_from_recruiting_agency',
            field=models.BooleanField(default=False, verbose_name='Is this posting from a recruiting agency?'),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-12 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_experience_title_alter_project_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='image',
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]

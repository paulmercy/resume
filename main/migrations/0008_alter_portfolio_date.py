# Generated by Django 4.1.1 on 2022-09-11 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_portfolio_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

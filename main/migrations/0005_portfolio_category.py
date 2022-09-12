# Generated by Django 4.1.1 on 2022-09-10 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='name', to='main.category'),
            preserve_default=False,
        ),
    ]
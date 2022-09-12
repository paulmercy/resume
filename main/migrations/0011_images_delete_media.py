# Generated by Django 4.1.1 on 2022-09-12 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_portfolio_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.portfolio')),
            ],
        ),
        migrations.DeleteModel(
            name='Media',
        ),
    ]
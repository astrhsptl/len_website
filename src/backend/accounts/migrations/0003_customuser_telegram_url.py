# Generated by Django 4.2 on 2023-07-14 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_avatar_alter_customuser_taxpayer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telegram_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
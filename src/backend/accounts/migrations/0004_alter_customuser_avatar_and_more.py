# Generated by Django 4.2 on 2023-08-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_telegram_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='profile/avatar/avatar.webp', null=True, upload_to='profile/avatar/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telegram_url',
            field=models.URLField(blank=True, default='https://t.me', null=True),
        ),
    ]

# Generated by Django 3.2 on 2023-05-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserCenter', '0002_alter_worker_wid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='wid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

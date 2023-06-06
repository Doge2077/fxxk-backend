# Generated by Django 3.2 on 2023-06-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('hash_code', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'user',
                'ordering': ['uid'],
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('wid', models.AutoField(primary_key=True, serialize=False)),
                ('worker_name', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255, null=True)),
                ('age', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('e_mail', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('edu_school', models.CharField(max_length=255, null=True)),
                ('edu_level', models.CharField(max_length=255, null=True)),
                ('work_year', models.IntegerField(null=True)),
                ('statue', models.CharField(max_length=255, null=True)),
                ('urls', models.URLField(max_length=255, null=True)),
                ('url_format', models.CharField(max_length=255, null=True)),
                ('hash_code', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'worker',
                'ordering': ['wid'],
            },
        ),
        migrations.AddIndex(
            model_name='worker',
            index=models.Index(fields=['wid'], name='worker_wid_20c430_idx'),
        ),
        migrations.AddIndex(
            model_name='worker',
            index=models.Index(fields=['worker_name'], name='worker_worker__60a34a_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='worker',
            unique_together={('hash_code',)},
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['uid'], name='user_uid_8f8462_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['hash_code'], name='user_hash_co_1ccebb_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('hash_code',)},
        ),
    ]

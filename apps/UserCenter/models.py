from django.db import models


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    hash_code = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'UserCenter'
        db_table = 'user'
        ordering = ['uid']
        unique_together = ('hash_code',)
        indexes = [
            models.Index(fields=['uid']),
            models.Index(fields=['hash_code']),
        ]

    def __str__(self):
        return self.hash_code


class Worker(models.Model):
    wid = models.AutoField(primary_key=True)
    worker_name = models.CharField(max_length=255, null=False)
    sex = models.CharField(max_length=255, null=True)
    age = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    e_mail = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    edu_school = models.CharField(max_length=255, null=True)
    edu_level = models.CharField(max_length=255, null=True)
    work_year = models.IntegerField(null=True)
    statue = models.CharField(max_length=255, null=True)
    urls = models.URLField(max_length=255, null=True)
    url_format = models.CharField(max_length=255, null=True)
    hash_code = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'UserCenter'
        db_table = 'worker'  # 指定数据库中的表名
        ordering = ['wid']  # 排序方式按照 wid 正序
        unique_together = ('hash_code',)  # 设置 hash_code 字段的值必须唯一
        indexes = [  # 设置 wid 和 worker_name 两个字段在数据库中创建索引
            models.Index(fields=['wid']),
            models.Index(fields=['worker_name']),
        ]

    def __str__(self):
        return self.worker_name


class Have(models.Model):
    hid = models.AutoField(primary_key=True)
    uid = models.IntegerField(null=False)
    wid = models.IntegerField(null=False)

    class Meta:
        app_label = 'UserCenter'
        db_table = 'have'
        ordering = ['hid']
        indexes = [
            models.Index(fields=['hid']),
            models.Index(fields=['uid']),
        ]


class Job(models.Model):
    jid = models.AutoField(primary_key=True)
    jname = models.CharField(max_length=255, null=True)
    jneed_age = models.IntegerField(null=True)
    jneed_edu = models.CharField(max_length=255, null=True)
    jneed_year = models.CharField(max_length=255, null=True)
    jneed_other = models.TextField(null=True)

    class Meta:
        app_label = 'UserCenter'
        db_table = 'job'
        ordering = ['jid']
        indexes = [
            models.Index(fields=['jid']),
            models.Index(fields=['jname']),
        ]

    def __str__(self):
        return self.jname


class Matchwork(models.Model):
    minfo = models.AutoField(primary_key=True)
    wid = models.IntegerField(null=False)
    jid = models.IntegerField(null=False)
    match = models.FloatField(null=False)

    class Meta:
        app_label = 'UserCenter'
        db_table = 'matchwork'
        ordering = ['minfo']
        indexes = [
            models.Index(fields=['minfo']),
            models.Index(fields=['wid']),
        ]

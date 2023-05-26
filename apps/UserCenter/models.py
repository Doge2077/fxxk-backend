from django.db import models


class Worker(models.Model):
    view = models.IntegerField(null=False)
    worker_name = models.CharField(max_length=255, null=False)
    sex = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    e_mail = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    edu_school = models.CharField(max_length=255)
    edu_level = models.CharField(max_length=255)
    work_year = models.IntegerField()
    statue = models.CharField(max_length=255)
    urls = models.URLField(max_length=255)
    url_format = models.CharField(max_length=255)
    hash_code = models.CharField(max_length=255)

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

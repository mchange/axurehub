from django.db import models
from django.utils.safestring import mark_safe
from datetime import datetime

# Create your models here.

class Prototype(models.Model):
    name = models.CharField(verbose_name='原型名称', max_length=50)
    BU_OPTION = (
        ('0', '趣生财'),
        ('1', '信汇通'),
        ('2', '收单协作'),
        ('3', '收单传统'),
        ('4', '互联网支付'),
        ('5', '其他'),
    )
    bu = models.CharField(
        verbose_name='业务线',
        max_length=1,
        choices=BU_OPTION,
        default=0
    )

    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now, blank=False)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = u'原型'
        verbose_name_plural = u'原型'
        ordering = ['-update_time', ]
    
    def get_view_url(self):
        if self.resource_set.all():
            resource = self.resource_set.all()[0:1][0]
            return resource.get_view_url()
        else:
            return '暂无原型'
    
    get_view_url.short_description = u'预览'
        
    def __str__(self):
        return self.name


class Resource(models.Model):
    no = models.BigAutoField(verbose_name='编号', primary_key=True)
    path = models.FileField(verbose_name='存储路径', upload_to='file')
    prototype = models.ForeignKey(Prototype, on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    
    STATUS = (
        ('0', '正常'),
        ('1', '删除')
    )
    status = models.CharField(
        verbose_name='状态',
        max_length=1,
        choices=STATUS,
        default=0,
    )

    def __str__(self):
        return ''
    
    def get_view_url(self):
        href = '/www/' + str(self.no) + '/' + self.path.name.split("/")[1].split(".")[0] + "/start.html"
        return mark_safe('<a href="' + href + '" target="_blank">预览</a>')

    get_view_url.short_description = u'预览'
    
    class Meta:
        verbose_name = u'资源'
        verbose_name_plural = u'资源'
        ordering = ['-no', ]

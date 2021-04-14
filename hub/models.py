from django.db import models
from django.utils.safestring import mark_safe
from datetime import datetime
from django.utils.html import format_html_join
# Create your models here.

# 原型托管资源
class Resource(models.Model):
    no = models.BigAutoField(verbose_name='编号', primary_key=True)
    path = models.FileField(verbose_name='存储路径', upload_to='file')
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
        return str(self.no)
    
    def get_view_url(self):
        href = '/www/' + str(self.no) + '/' + self.path.name.split("/")[1].split(".")[0] + "/index.html"
        return mark_safe('<a href="' + href + '" target="_blank">预览</a>')

    get_view_url.short_description = u'预览'
    
    class Meta:
        verbose_name = u'资源'
        verbose_name_plural = u'资源'
        ordering = ['-no', ]

# 标签
class Tag(models.Model):
    name = models.CharField(verbose_name='标签', max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签'

# 业务线
class Bu(models.Model):
    name = models.CharField(verbose_name='名称', max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'业务线'
        verbose_name_plural = u'业务线'

# 需求原型
class Prototype(models.Model):
    name = models.CharField(verbose_name='原型名称', max_length=50)
    bu = models.ForeignKey(Bu, on_delete=models.DO_NOTHING, verbose_name="业务线")
    resource = models.ForeignKey(Resource, on_delete=models.DO_NOTHING, verbose_name="资源")
    tags = models.ManyToManyField(Tag, verbose_name="标签", blank = True, null = True)

    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now, blank=False)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    remark = models.TextField(verbose_name='备注', blank = True)

    class Meta:
        verbose_name = u'需求原型'
        verbose_name_plural = u'需求原型'
        ordering = ['-update_time', ]
    
    def get_view_url(self):
        return self.resource.get_view_url()
    
    get_view_url.short_description = u'预览'

    def get_tags(self):
        return format_html_join(
            mark_safe('<br/>'),
            "{}",
            ((tag,) for tag in self.tags.all()),
        )

    get_tags.short_description = u'标签'    

    def get_resource_no(self):
        return self.resource.no

    get_resource_no.short_description = u'资源ID'  

    def __str__(self):
        return self.name


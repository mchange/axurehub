from django.contrib import admin
from . import models
# creating django file objects
from django.core.files import File

# zipprocessing
import zipfile
from django.conf import settings
import os
import shutil

import time

# Register your models here.

class PrototypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'bu', 'create_time', 'update_time', 'get_view_url')

    search_fields = ['name', 'bu']

    list_filter = [ 'bu']


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('no', 'path', 'status', 'create_time', 'update_time', 'get_view_url')

    list_filter = ['status', 'prototype__name' ]

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            # 设置默认no值
            timestamp = int(round(time.time() * 1000))
            obj.no = timestamp
            if form.cleaned_data['path'] is not None:
                no = str(timestamp)
                zip = zipfile.ZipFile(form.cleaned_data['path'])
                www_dir = os.path.join(settings.WWW_ROOT, no)
                os.makedirs(www_dir)
                if zip:
                    for file in zip.namelist():
                        zip.extract(file, settings.MEDIA_ROOT)
                        # 处理加压后中文乱码
                        right_file = file.encode('cp437').decode('utf-8')
                        shutil.move(os.path.join(settings.MEDIA_ROOT, file), os.path.join(www_dir, right_file))
                zip.close()
            super().save_model(request, obj, form, change)
            shutil.rmtree(settings.MEDIA_ROOT)




admin.site.register(models.Prototype, PrototypeAdmin)

admin.site.register(models.Resource, ResourceAdmin)

admin.site.disable_action('delete_selected')
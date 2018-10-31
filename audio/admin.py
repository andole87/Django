from django.contrib import admin
from .models import Audio,Audio_Detail
# Register your models here.

# admin.site.register(Audio)
# admin.site.register(Audio_Detail)

class DetailInline(admin.TabularInline):
    model=Audio_Detail

class AudioInline(admin.ModelAdmin):
    inlines=[
        DetailInline,
    ]

admin.site.register(Audio,AudioInline)
admin.site.site_header = "내맘대로 오디오북"
admin.site.site_title = "관리페이지"
admin.site.index_title = "관리페이지"
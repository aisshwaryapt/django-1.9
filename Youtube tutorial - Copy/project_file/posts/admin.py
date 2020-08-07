from django.contrib import admin

from .models import postspage

class PostModelAdmin(admin.ModelAdmin):
    list_display= ["title","update","timestamp"]
    list_filter=["update","timestamp"]
    search_fields=["title","content"]
    class Meta:
        model=postspage


admin.site.register(postspage,PostModelAdmin)
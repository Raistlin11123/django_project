from django.contrib import admin
from .models import Profil, Post, CommentPost


class ProfilAdmin(admin.ModelAdmin):
    pass
    #prepopulated_fields = {'slug': ('titre', )}
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'date', 'is_visible',)
    list_filter = ('is_visible',)
    search_fields = ('pseudo', )
    
class CommentPostAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'date', 'is_visible',)
    list_filter = ('is_visible',)
    search_fields = ('pseudo', )

admin.site.register(Profil, ProfilAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(CommentPost, CommentPostAdmin)


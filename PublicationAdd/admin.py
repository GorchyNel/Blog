from django.contrib import admin
from .models import Tag, Publication, Rubric


class TagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]

    class Meta:
        model = Tag


class RubricAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rubric._meta.fields]
    
    class Meta:
        model = Rubric

class PublicationAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Publication._meta.fields if field.name != "Text"]
    
    class Meta:
        model = Publication

admin.site.register(Tag, TagAdmin)
admin.site.register(Rubric, RubricAdmin)
admin.site.register(Publication, PublicationAdmin)

from artifacts.models import Artifact
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
class ArtifactAdmin(admin.ModelAdmin):
   fields  = ['url', 'description']
   formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
   }

admin.site.register(Artifact,ArtifactAdmin)

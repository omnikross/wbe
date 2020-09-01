from django.contrib import admin
from .models import Director, Genre, Film, FilmInstance
# Register your models here.
# admin.site.register(Film)
#admin.site.register(Director)
admin.site.register(Genre)
# admin.site.register(FilmInstance)

class FilmsInstanceInline(admin.TabularInline):
    model = FilmInstance

# Define the admin class
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
# Register the admin class with the associated model
admin.site.register(Director, DirectorAdmin)

# Register the Admin classes for Film using the decorator

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'display_genre')
    
    @staticmethod
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'
    inlines = [FilmsInstanceInline]

# Register the Admin classes for FilmInstance using the decorator

@admin.register(FilmInstance) 
class FilmInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'session_time')
    fieldsets = (
        ('Film Data', {
            'fields': ('film','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'session_time')
        }),
    )
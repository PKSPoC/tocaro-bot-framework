from django.contrib import admin
from .models import User, Quote


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Quote)
class Quote(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import User, Quote, Command


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Quote)
class Quote(admin.ModelAdmin):
    pass


@admin.register(Command)
class Command(admin.ModelAdmin):
    pass

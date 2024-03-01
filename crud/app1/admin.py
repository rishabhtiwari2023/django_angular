from django.contrib import admin

# Register your models here.
# class ApiapplicationConfig(AppConfig):
#     name = 'app1'
from .models import BookList
from .models import User1
# Register your models here.
admin.site.register(BookList)
admin.site.register(User1)
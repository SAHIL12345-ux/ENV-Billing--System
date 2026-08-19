from django.contrib import admin # pyright: ignore[reportMissingModuleSource]
from .models import Invoice
# Register your models here.




admin.site.register(Invoice)
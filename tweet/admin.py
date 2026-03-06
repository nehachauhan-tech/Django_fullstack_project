from django.contrib import admin
from .models import Tweet

# Register Tweet model to make it visible in Django admin panel
admin.site.register(Tweet)

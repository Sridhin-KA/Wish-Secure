from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Wish)
admin.site.register(WishComment)

admin.site.register(Activity)
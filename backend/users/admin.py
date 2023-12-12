from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # UserAdmin의 필드셋을 확장하여 phone_number를 포함시킵니다.
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )

# 새로운 UserAdmin 클래스로 User 모델을 등록합니다.
admin.site.register(User, UserAdmin)

from django.contrib import admin
from .models import MenuItem, SiteSettings


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name']


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['cafe_name', 'background_opacity']
    fieldsets = [
        ('Kafe nomi', {'fields': ['cafe_name']}),
        ('TV fon rasmi', {
            'fields': ['background_image', 'background_opacity'],
            'description': 'Smart TV ekrani orqa foniga rasm qo\'yish uchun. '
                           'Qorayish darajasi yuqori bo\'lsa matn yaxshi o\'qiladi (masalan 55-70).',
        }),
    ]

    def has_add_permission(self, request):
        # Faqat bitta sozlamalar yozuvi bo'lishi kerak
        return not SiteSettings.objects.exists()

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

from rest_framework import serializers
from .models import MenuItem, SiteSettings


class SiteSettingsSerializer(serializers.ModelSerializer):
    """TV ekran sozlamalari: kafe nomi va fon rasmi"""

    class Meta:
        model = SiteSettings
        fields = ['cafe_name', 'background_image', 'background_opacity']


class MenuItemPublicSerializer(serializers.ModelSerializer):
    """TV ekran uchun — faqat kerakli maydonlar"""

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'image', 'order']


class MenuItemAdminSerializer(serializers.ModelSerializer):
    """Mobil panel API uchun (agar kelajakda mobil ilova qilsangiz kerak bo'ladi)"""

    class Meta:
        model = MenuItem
        fields = '__all__'
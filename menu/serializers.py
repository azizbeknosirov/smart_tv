from rest_framework import serializers
from .models import MenuItem


class MenuItemPublicSerializer(serializers.ModelSerializer):
    """TV ekran uchun — faqat kerakli maydonlar"""

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'image', 'order']


class MenuItemAdminSerializer(serializers.ModelSerializer):
    """Mobil panel API uchun (agar kelajakda mobil ilova qilsangiz kerak bo'ladi)"""

    class Meta:
        model = MenuItem
        fields = '__all__'

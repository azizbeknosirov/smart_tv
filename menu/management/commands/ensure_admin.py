from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = "Admin foydalanuvchini kafolatlaydi (har deployda DB tozalangani uchun)"

    def handle(self, *args, **options):
        username = os.environ.get('ADMIN_USERNAME', 'admin')
        password = os.environ.get('ADMIN_PASSWORD', '1234')

        user, created = User.objects.get_or_create(
            username=username,
            defaults={'is_staff': True, 'is_superuser': True},
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'"{username}" foydalanuvchisi yaratildi'))
        else:
            self.stdout.write(f'"{username}" allaqachon mavjud')

        # Parolni har doim env dagi qiymatga moslaydi (env yo'q bo'lsa 1234)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS('Parol yangilandi'))

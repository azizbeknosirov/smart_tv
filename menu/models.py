from django.db import models


class SiteSettings(models.Model):
    """Sayt sozlamalari: TV ekran fon rasmi va kafe nomi (bitta yozuv)"""
    cafe_name = models.CharField(
        'Kafe nomi', max_length=200, default='SUSAMBIL', blank=True
    )
    background_image = models.ImageField(
        'Fon rasmi',
        upload_to='bg/bg.jpg',  # barqaror qisqa nom — DB yo'l uzunligi muammosi oldini oladi
        blank=True,
        null=True,
    )
    background_opacity = models.PositiveIntegerField(
        "Fon qorayish darajasi (0-80)", default=55
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sayt sozlamalari'
        verbose_name_plural = 'Sayt sozlamalari'

    def __str__(self):
        return self.cafe_name or 'Kafe'

    def save(self, *args, **kwargs):
        # Faqat bitta yozuv bo'lishi kerak (id=1)
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class MenuItem(models.Model):
    name = models.CharField('Nomi', max_length=200)
    description = models.CharField('Tavsif', max_length=255, blank=True, default='')
    price = models.DecimalField('Narxi (so\'m)', max_digits=10, decimal_places=0)
    image = models.ImageField('Rasm', upload_to='menu_images/')
    is_active = models.BooleanField('Ko\'rinadimi', default=True)
    order = models.PositiveIntegerField('Tartib', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Taom'
        verbose_name_plural = 'Taomlar'

    def __str__(self):
        return self.name
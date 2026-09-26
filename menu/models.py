from django.db import models


class MenuItem(models.Model):
    name = models.CharField('Nomi', max_length=200)
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

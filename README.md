# Kafe menyu tizimi (Smart TV + Telefon paneli)

## 1. Lokalda ishga tushirish

```bash
cd cafe_menu
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # telefon panelga kirish uchun login/parol shu bo'ladi

python manage.py runserver 0.0.0.0:8000
```

## 2. Sahifalar

- **Smart TV uchun**: `http://<kompyuter-ip>:8000/tv/`
  TV brauzerida shu manzilni oching va **fullscreen** qiling.
  Taomlar 10 soniyada bir yangilanib turadi — sahifani qayta yuklash shart emas.

- **Telefon boshqaruv paneli**: `http://<kompyuter-ip>:8000/panel/`
  `createsuperuser` bilan yaratgan login/parol orqali kiring.
  Har bir taom yonida yashirish/ko'rsatish tugmasi (switch), "Tahrirlash" tugmasi
  orqali nomi, narxi va rasmini o'zgartirishingiz mumkin.

- Panelni telefon ekraningizga qo'shib qo'yish uchun: brauzerda "Add to Home Screen"
  (Bosh ekranga qo'shish) — shunda alohida ilova belgisi kabi ochiladi.

- **Django admin** (`/admin/`) orqali ham taomlarni boshqarish, boshqa xodimlarga
  login yaratish mumkin.

## 3. Railway'ga chiqarish

1. Bu papkani GitHub repo qilib push qiling.
2. Railway'da "New Project" → "Deploy from GitHub repo".
3. PostgreSQL qo'shing (Railway avtomatik `DATABASE_URL` beradi).
4. Environment Variables'ga qo'shing:
   - `SECRET_KEY` — o'zingiz tasodifiy uzun matn yozing
   - `DEBUG` = `False`
5. Deploy bo'lgandan keyin: Railway console orqali
   `python manage.py createsuperuser` ishga tushiring.

### ⚠️ Muhim: rasm fayllari haqida

Railway'ning fayl tizimi **vaqtinchalik** — har yangi deploy qilganingizda
yuklangan rasmlar o'chib ketishi mumkin. Ishlab chiqarishga chiqarganda:

- Railway'da **Volume** ulab, `MEDIA_ROOT`ni o'sha volume'ga ko'rsating, YOKI
- Rasmlarni **Cloudinary** yoki **AWS S3** kabi tashqi xizmatga saqlang
  (`django-storages` kutubxonasi orqali).

Development bosqichida hozircha shart emas — sizga qulay bo'lgani uchun
oddiy `MEDIA_ROOT` qoldirilgan.

## 4. TV'ni brauzer bilan avtomatik ochish

Ko'p Smart TV'larda (Tizen, webOS, Android TV) brauzerni "kiosk mode"da,
qurilma yoqilganda avtomatik ochiladigan qilib sozlash mumkin — bu TV
modelingizga bog'liq, agar kerak bo'lsa, TV modelini ayting, o'sha bo'yicha
ham yordam beraman.

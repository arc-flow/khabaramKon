# Dockerfile

# استفاده از تصویر رسمی Python
FROM python:3.12-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌های مورد نیاز
COPY requirements.txt /app/requirements.txt

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کد پروژه
COPY . /app

# باز کردن پورت ۸۰۰۰ برای Django
EXPOSE 80

# دستور پیش‌فرض برای اجرای سرور Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

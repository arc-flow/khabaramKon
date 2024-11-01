# Dockerfile

# استفاده از تصویر رسمی Python
FROM python:3.12-alpine

# تنظیم دایرکتوری کاری
RUN apk add --no-cache redis gcc musl-dev libffi-dev

WORKDIR /app
# کپی کردن فایل‌های مورد نیاز
COPY requirements.txt /app/requirements.txt

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کد پروژه
COPY . /app

# باز کردن پورت ۸۰۰۰ برای Django
EXPOSE 80 6379

# دستور پیش‌فرض برای اجرای سرور Django
CMD redis-server --daemonize yes && celery -A khabaramKon worker --loglevel=info --detach && python3 manage.py runserver 0.0.0.0:80

# ☀️ Solar Panel Fire & Environment Monitoring System

این پروژه یک سیستم مانیتورینگ هوشمند برای پنل‌های خورشیدی است که داده‌های دما، رطوبت و دود را از طریق آردوئینو جمع‌آوری کرده و در یک داشبورد گرافیکی نمایش می‌دهد.

## 🛠 تکنولوژی‌های استفاده شده
- **Hardware:** Arduino UNO R4 WiFi, SHT20 Sensor, MQ Smoke Sensor
- **Database:** InfluxDB 2.7 (Time-series)
- **Visualization:** Grafana
- **Backend:** Python (Ingestion Service)
- **Deployment:** Docker & Docker Compose

## 🚀 راهنمای نصب و اجرا

برای اجرای پروژه در شبکه داخلی دانشگاه، مراحل زیر را دنبال کنید:

### ۱. تنظیمات سخت‌افزار
مطمئن شوید آردوئینو به وای‌فای متصل است و یک IP ثابت (Static IP) در شبکه دارد.

### ۲. تنظیمات نرم‌افزار
ابتدا مخزن را کلون کنید:
```bash
git clone https://github.com/YOUR_USERNAME/solar-monitoring-system.git
cd solar-monitoring-system

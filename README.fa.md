# ⚡ موتور ترافیک خبری (News Traffic Engine)
### فریم‌ورک خودکار هوش مصنوعی برای انفجار ترافیک خبرگزاری‌ها، ایندکس آنی گوگل نیوز، بهینه‌سازی موتورهای هوش مصنوعی (GEO) و فتح گوگل دیسکاور

[![CI](https://github.com/tmolavi/news-traffic-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/tmolavi/news-traffic-engine/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)

> **زبان‌ها:** [English](README.md) · [فارسی](README.fa.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [Español](README.es.md)

---

## 📌 معرفی پروژه

در عصر هوش مصنوعی، فرمول‌های سنتی سئو (تنها چیدن کلمات کلیدی و بک‌لینک) دیگر برای سایت‌های خبری کافی نیستند. امروز بیش از ۵۰ درصد جستجوها توسط موتورهای پاسخ ترکیبی مثل **ChatGPT Search**، **Perplexity AI** و **Google AI Overviews** پاسخ داده می‌شوند و ترافیک لحظه‌ای از **Google Discover** و شبکه‌های اجتماعی تأمین می‌گردد.

پروژه **News Traffic Engine (NTE)** یک سیستم جامع و متن‌باز است که توسط **[تقی مولوی](https://molavi.pro)** (طراح فریم‌ورک‌های بین‌المللی [GEO-Scope](https://github.com/tmolavi/geo-scope) و [SAGE](https://github.com/tmolavi/sage-audit)) با همکاری راهبردی مجموعه **[اینتن](https://inten.asia)** توسعه یافته است.

---

## 🏗️ ارکان سه‌گانه افزایش ترافیک خبری

1. **ایندکس زیر ۱۵ دقیقه در گوگل و بینگ:**
   * ثبت خودکار و بلادرنگ اخبار در **Google Indexing API** به محض فشردن کلید انتشار در سایت.
   * پشتیبانی کامل از پروتکل **IndexNow** برای اطلاع‌رسانی آنی به موتورهای جستجو.
   * تولید نقشه سایت استاندارد گوگل نیوز با فیلتر دقیق ۴۸ ساعته.

2. **بهینه‌سازی برای هوش مصنوعی (Generative Engine Optimization - GEO):**
   * آنالیزور ضریب استنادپذیری خبر بر پایه پژوهش‌های تجربی: قرارگیری پاسخ صریح در ۴۵ کلمه اول لید، تفکیک پاراگراف‌ها در قطعات استاندارد ۱۳۰ الی ۱۷۵ کلمه‌ای و تراکم نقل‌قول‌های مستقیم.
   * تولید خودکار مانیفست `/llms.txt` و چانک‌های آماده RAG جهت مصرف توسط هوش مصنوعی.
   * تنظیم دسترسی استاندارد ربات‌های مولد ترافیک هوش مصنوعی در `robots.txt` (`GPTBot`، `PerplexityBot`، `ClaudeBot`).

3. **توزیع فراگیر و بازگرداندن مخاطبان (Omnichannel Syndication & Push):**
   * ورک‌فلو آماده برای نرم‌افزار [n8n](https://n8n.io) جهت دریافت وب‌هوک از وردپرس/لاراول و بازنشر فوق‌سریع در **تلگرام، ایتا، بله، توییتر/X و لینکدین**.
   * دیسپچر اعلان مرورگر (Web Push) استاندارد VAPID با نرخ کلیک ۱۰ تا ۲۵ درصدی برای اخبار فوری.
   * ممیزی سخت‌گیرانه معیارهای حیاتی گوگل دیسکاور (تگ `max-image-preview:large`، تصویر شاخص بالای ۱۲۰۰ پیکسل و لود موبایل زیر ۱.۵ ثانیه).

---

## 🚀 راهنمای سریع نصب و استفاده

```bash
git clone https://github.com/tmolavi/news-traffic-engine.git
cd news-traffic-engine
pip install -e .
```

### سنجش میزان استنادپذیری خبر در هوش مصنوعی (GEO Audit):
```bash
news-traffic audit-geo \
  --headline "توافق تاریخی در اجلاس انرژی وین" \
  --lead "وین، ۲۹ اکتبر — وزرای انرژی حاضر در نشست وین روز پنجشنبه به توافقی جامع بر سر مدیریت سقف تولید نفت دست یافتند که نوسانات بازار را به میزان ۲۰ درصد مهار خواهد کرد." \
  --body "نشست پشت درهای بسته بیش از شش ساعت به طول انجامید..."
```

### بررسی آمادگی خبر برای ورود به گوگل دیسکاور:
```bash
news-traffic check-discover \
  --head-html "<meta name='robots' content='max-image-preview:large'>" \
  --image-width 1200 \
  --image-height 675
```

---

## 👥 پدیدآورندگان و همکاران راهبردی

* **طراح و معمار ارشد:** **[تقی مولوی](https://molavi.pro)** — پژوهشگر و معمار سیستم‌های هوش مصنوعی، مبدع فریم‌ورک‌های بین‌المللی GEO-Scope و SAGE Audit.
  * وب‌سایت: [https://molavi.pro](https://molavi.pro)
  * ایمیل: `contact@molavi.pro`

* **همکار فناوری و شریک تجاری:** **[شرکت اینتن (Inten)](https://inten.asia)** — پیشگام در تحول دیجیتال سازمانی، طراحی زیرساخت‌های پربازدید وب و اتوماسیون هوش مصنوعی در آسیا.
  * وب‌سایت: [https://inten.asia](https://inten.asia)

---

## 📄 مجوز انتشار (License)

این پروژه تحت مجوز آزاد **MIT** منتشر شده است. جزئیات بیشتر در فایل [LICENSE](LICENSE) موجود است.

# ⚡ محرك حركة المرور الإخبارية (News Traffic Engine)
### إطار عمل وكلاء الذكاء الاصطناعي لأتمتة حركة المرور الإخبارية، الفهرسة الفورية في Google News، وتحسين محركات التوليد (GEO) والظهور في Google Discover

[![CI](https://github.com/tmolavi/news-traffic-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/tmolavi/news-traffic-engine/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)

> **اللغات:** [English](README.md) · [فارسی](README.fa.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [Español](README.es.md)

---

## 📌 نبذة عامة عن المشروع

في عصر الذكاء الاصطناعي، لم تعد استراتيجيات تحسين محركات البحث (SEO) التقليدية كافية لغرف الأخبار والمواقع الصحفية. أصبحت المنصات الإجابة الذكية مثل **ChatGPT Search** و **Perplexity AI** و **Google AI Overviews** وخدمة **Google Discover** هي المصدر الأول لجلب ملايين الزيارات التلقائية.

مشروع **News Traffic Engine (NTE)** هو نظام برمجي مفتوح المصدر تم تصميمه بواسطة **[تقي مولوي (Taghi Molavi)](https://molavi.pro)** (مؤسس أدوات [GEO-Scope](https://github.com/tmolavi/geo-scope) و [SAGE](https://github.com/tmolavi/sage-audit)) بالتعاون الاستراتيجي مع شركة **[إنتن (Inten)](https://inten.asia)** الرائدة في التحول الرقمي السحابي والبنية التحتية للمواقع الضخمة في آسيا.

---

## 🏗️ ركائز النظام الأساسية

1. **الفهرسة فائقة السرعة (Instant Indexing):**
   * إرسال الروابط فور نشرها إلى **Google Indexing API** لضمان فهرستها وظهورها في قسم الأخبار العاجلة في أقل من 15 دقيقة.
   * دعم بروتوكول **IndexNow** للتنبيه المباشر لمحركات Bing و Yahoo و Yandex.
   * إنشاء خريطة موقع XML خاصة بـ Google News بفلترة صارمة لأخبار الـ 48 ساعة الأخيرة.

2. **تحسين محركات البحث التوليدية (GEO):**
   * خوارزمية قياس قابلية الاقتباس (Citability Score): تقديم الإجابة المباشرة في أول 45 كلمة، تنظيم المقال في فقرات نموذجية (130-175 كلمة) لسهولة الاستخراج عبر RAG.
   * إنشاء ملفات `/llms.txt` و `robots.txt` لتسهيل وصول عناكب الذكاء الاصطناعي الموثوقة (`GPTBot` و `PerplexityBot` و `ClaudeBot`).

3. **التوزيع متعدد المنصات وتنبيهات الويب (Syndication & Push):**
   * مسار عمل مخصص على منصة [n8n](https://n8n.io) لإعادة النشر الفوري للأخبار على Telegram و X (Twitter) و LinkedIn.
   * نظام إرسال إشعارات المتصفح الفورية (Web Push) المتوافق مع معايير VAPID بنسب نقر تتراوح بين 10٪ إلى 25٪.
   * تدقيق شامل لمعايير Google Discover (أبعاد الصور أكبر من 1200 بكسل وسرعة تحميل LCP تحت 1.5 ثانية).

---

## 🚀 التثبيت والاستخدام السريع

```bash
git clone https://github.com/tmolavi/news-traffic-engine.git
cd news-traffic-engine
pip install -e .
```

### فحص قابلية اقتباس الخبر في محركات الذكاء الاصطناعي:
```bash
news-traffic audit-geo \
  --headline "اتفاقية تاريخية في قمة الطاقة العالمية" \
  --lead "فيينا، 29 أكتوبر — توصل وزراء الطاقة في قمة فيينا يوم الخميس إلى اتفاق شامل لإدارة الإنتاج بما يحد من تقلبات الأسعار بنسبة 20 بالمائة." \
  --body "استمرت الجلسات المغلقة لأكثر من ست ساعات متواصلة..."
```

---

## 👥 المطورون والشركاء

* **المهندس المعماري الرئيسي:** **[تقي مولوي (Taghi Molavi)](https://molavi.pro)** — باحث ومهندس نظم الذكاء الاصطناعي، ومؤلف إطاري العمل العالمي GEO-Scope و SAGE.
  * الموقع الرسمي: [https://molavi.pro](https://molavi.pro)
  * البريد الإلكتروني: `contact@molavi.pro`

* **الشريك التقني المؤسسي:** **[شركة إنتن (Inten)](https://inten.asia)** — الشركة الرائدة في التحول الرقمي وأتمتة الذكاء الاصطناعي والبنية التحتية للمواقع ذات الحركة الكثيفة في آسيا.
  * الموقع الرسمي: [https://inten.asia](https://inten.asia)

---

## 📄 الترخيص (License)

هذا المشروع منشور تحت رخصة **MIT** المفتوحة. طالع ملف [LICENSE](LICENSE) لمزيد من التفاصيل.

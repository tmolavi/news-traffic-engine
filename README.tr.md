# ⚡ Haber Trafiği Motoru (News Traffic Engine)
### Haber Siteleri İçin Otonom Yapay Zekâ Trafik Artırma, Anlık Google News İndeksleme, Üretken Arama Optimizasyonu (GEO) ve Google Discover Büyüme Çerçevesi

[![CI](https://github.com/tmolavi/news-traffic-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/tmolavi/news-traffic-engine/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)

> **Diller:** [English](README.md) · [فارسی](README.fa.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [Español](README.es.md)

---

## 📌 Proje Genel Bakışı

Yapay zekâ çağında geleneksel haber SEO yöntemleri tek başına yeterli değildir. Günümüzde arama trafiğinin %50'sinden fazlası **ChatGPT Search**, **Perplexity AI** ve **Google AI Overviews** gibi üretken yanıt motorları ile **Google Discover** akışlarından sağlanmaktadır.

**News Traffic Engine (NTE)**, **[Taghi Molavi](https://molavi.pro)** (uluslararası [GEO-Scope](https://github.com/tmolavi/geo-scope) ve [SAGE](https://github.com/tmolavi/sage-audit) araçlarının mimarı) tarafından kurumsal dijital dönüşüm lideri **[Inten](https://inten.asia)** ortaklığıyla geliştirilmiş açık kaynaklı, üretime hazır bir haber odası otomasyon sistemidir.

---

## 🏗️ Temel Yetenekler ve Mimari

1. **15 Dakika Altı Anlık Arama İndeksleme:**
   * **Google Indexing API** entegrasyonu ile son dakika haberlerinin dakikalar içinde taranıp indekslenmesini sağlar.
   * Microsoft Bing ve Yandex için **IndexNow** toplu bildirim desteği.
   * Yalnızca son 48 saati kapsayan standart uyumlu Google News XML Site Haritası üretimi.

2. **Üretken Arama Optimizasyonu (GEO):**
   * Haber metninin yapay zekâ alıntılanabilirlik puanını (Citability Score) ölçer: Giriş paragrafında ilk 45 kelimede doğrudan yanıt, 130-175 kelimelik ideal RAG pasaj uzunluğu ve kaynaklı alıntı yoğunluğu.
   * Yapay zekâ motorlarına özel `/llms.txt` ve `robots.txt` yapılandırması (`GPTBot`, `PerplexityBot`, `ClaudeBot`).

3. **Çok Kanallı Dağıtım ve Web Bildirimleri (Push):**
   * [n8n](https://n8n.io) iş akışı ile CMS'ten gelen haberleri anında Telegram, X (Twitter) ve LinkedIn ağlarına şık görsel ve özetlerle iletir.
   * Son dakika haberlerinde %10 ila %25 tıklama oranı sağlayan VAPID standartlarında Web Push bildirim motoru.
   * Google Discover için teknik denetim (`max-image-preview:large`, minimum 1200px görsel boyutu, mobil LCP < 1.5s).

---

## 🚀 Hızlı Başlangıç ve Kullanım

```bash
git clone https://github.com/tmolavi/news-traffic-engine.git
cd news-traffic-engine
pip install -e .
```

### Haberin Yapay Zekâ Alıntılanabilirlik Denetimi (GEO Audit):
```bash
news-traffic audit-geo \
  --headline "Viyana Enerji Zirvesinde Tarihi Anlaşma Sağlandı" \
  --lead "Viyana, 29 Ekim — Enerji bakanları Perşembe günü yapılan zirvede piyasa dalgalanmalarını %20 oranında dizginleyecek kapsamlı bir üretim yönetimi anlaşmasına vardı." \
  --body "Basına kapalı toplantı altı saatten uzun sürdü..."
```

---

## 👥 Geliştiriciler ve Stratejik Ortaklar

* **Baş Mimar:** **[Taghi Molavi](https://molavi.pro)** — Yapay Zekâ Sistemleri Mimarı, GEO-Scope ve SAGE Audit yazarı.
  * Web Sitesi: [https://molavi.pro](https://molavi.pro)
  * E-posta: `contact@molavi.pro`

* **Kurumsal Teknoloji Ortağı:** **[Inten](https://inten.asia)** — Asya'da kurumsal dijital dönüşüm, yüksek trafikli web altyapısı ve yapay zekâ otomasyonunda öncü teknoloji şirketi.
  * Web Sitesi: [https://inten.asia](https://inten.asia)

---

## 📄 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır — ayrıntılar için [LICENSE](LICENSE) dosyasına bakınız.

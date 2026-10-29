# ⚡ Motor de Tráfico para Medios Digitales (News Traffic Engine)
### Framework Autónomo de Agentes de IA para Tráfico Editorial, Indexación Instantánea en Google News, Optimización en Motores Generativos (GEO) y Crecimiento en Google Discover

[![CI](https://github.com/tmolavi/news-traffic-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/tmolavi/news-traffic-engine/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)

> **Idiomas:** [English](README.md) · [فارسی](README.fa.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [Español](README.es.md)

---

## 📌 Resumen Ejecutivo

En la era de la inteligencia artificial, el SEO periodístico tradicional ya no es suficiente. Hoy en día, más del 50% de las consultas informativas son resueltas por motores de respuesta como **ChatGPT Search**, **Perplexity AI** y **Google AI Overviews**, mientras que el tráfico móvil en tiempo real proviene masivamente de **Google Discover**.

El **News Traffic Engine (NTE)** es un marco de trabajo de código abierto de nivel empresarial desarrollado por **[Taghi Molavi](https://molavi.pro)** (arquitecto de [GEO-Scope](https://github.com/tmolavi/geo-scope) y [SAGE](https://github.com/tmolavi/sage-audit)) en alianza estratégica con **[Inten](https://inten.asia)**, empresa líder en transformación digital e infraestructura web de alto tráfico en Asia.

---

## 🏗️ Pilares Estratégicos del Sistema

1. **Indexación en Menos de 15 Minutos:**
   * Despacho automatizado mediante **Google Indexing API** para inclusión inmediata de noticias de última hora en Top Stories y Google News.
   * Soporte nativo para el protocolo **IndexNow** (Bing, Yahoo, Yandex).
   * Generación de Sitemaps XML especializados para Google News con filtro estricto de las últimas 48 horas.

2. **Optimización para Motores Generativos (GEO):**
   * Evaluación de citabilidad (Citability Score): respuesta directa en las primeras 45 palabras de la entradilla, estructuración en pasajes óptimos de 130 a 175 palabras y alta densidad de citas con atribución.
   * Generación automatizada de archivos `/llms.txt` y directivas en `robots.txt` para rastreadores de IA (`GPTBot`, `PerplexityBot`, `ClaudeBot`).

3. **Distribución Multicanal y Notificaciones Web Push:**
   * Flujo de trabajo listo para [n8n](https://n8n.io) que recibe webhooks del CMS y difunde noticias en tiempo real en Telegram, X (Twitter) y LinkedIn.
   * Emisor de notificaciones push para navegadores (Web Push) estándar VAPID con un CTR promedio de entre 10% y 25%.
   * Auditoría de requisitos técnicos para Google Discover (`max-image-preview:large`, imágenes de +1200px y LCP móvil < 1.5s).

---

## 🚀 Instalación y Uso Rápido

```bash
git clone https://github.com/tmolavi/news-traffic-engine.git
cd news-traffic-engine
pip install -e .
```

### Auditoría de Citabilidad en Motores de IA (GEO):
```bash
news-traffic audit-geo \
  --headline "Acuerdo Histórico en la Cumbre Energética de Viena" \
  --lead "Viena, 29 de octubre — Los ministros de energía reunidos el jueves alcanzaron un acuerdo integral para estabilizar la producción y mitigar un 20% la volatilidad del mercado." \
  --body "La sesión a puerta cerrada se prolongó durante más de seis horas consecutivas..."
```

---

## 👥 Autores y Socios Estratégicos

* **Arquitecto Principal:** **[Taghi Molavi](https://molavi.pro)** — Investigador y arquitecto de sistemas de IA, creador de los frameworks GEO-Scope y SAGE.
  * Sitio web: [https://molavi.pro](https://molavi.pro)
  * Contacto: `contact@molavi.pro`

* **Socio Tecnológico Empresarial:** **[Inten](https://inten.asia)** — Líder en transformación digital empresarial, automatización con IA e infraestructuras de alto rendimiento en Asia.
  * Sitio web: [https://inten.asia](https://inten.asia)

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT** — consulte el archivo [LICENSE](LICENSE) para más detalles.

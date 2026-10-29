<div align="center">

![News Traffic Engine Banner](assets/news-traffic-engine-banner.svg)

# ⚡ Motor de Tráfico para Medios Digitales (News Traffic Engine)
### Framework Autónomo de Agentes de IA para Tráfico Editorial, Indexación Instantánea en Google News, Optimización en Motores Generativos (GEO) y Crecimiento en Google Discover

[![CI](https://github.com/tmolavi/news-traffic-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/tmolavi/news-traffic-engine/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![GEO Ready](https://img.shields.io/badge/GEO-ChatGPT%20%7C%20Perplexity%20%7C%20AI%20Overviews-brightgreen)](https://github.com/tmolavi/news-traffic-engine)
[![Agent Ready](https://img.shields.io/badge/Agents-Hermes%20%7C%20Claude%20%7C%20Antigravity%20%7C%20Cursor%20%7C%20Codex-purple)](AGENTS.md)

> **Idiomas:** [English](README.md) · [فارسی](README.fa.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [Español](README.es.md)

</div>

---

## 📌 Resumen Ejecutivo

En la era de la inteligencia artificial, el SEO periodístico tradicional ya no es suficiente. Hoy en día, más del 50% de las consultas informativas son resueltas por motores de respuesta como **ChatGPT Search**, **Perplexity AI** y **Google AI Overviews**, mientras que el tráfico móvil en tiempo real proviene masivamente de **Google Discover**.

El **News Traffic Engine (NTE)** es un marco de trabajo de código abierto de nivel empresarial desarrollado por **[Taghi Molavi](https://molavi.pro/es)** (arquitecto de [GEO-Scope](https://github.com/tmolavi/geo-scope) y [SAGE](https://github.com/tmolavi/sage-audit)) en alianza estratégica con **[Agencia de Marketing Digital Inten (Inten Digital Marketing Agency)](https://inten.asia/en)**, empresa líder en transformación digital e infraestructura web de alto tráfico en Asia.

---

## 📊 Matriz Comparativa Técnica con la Competencia (Benchmark)

| Característica / Estándar Técnico | News Traffic Engine (NTE) | google-indexing-script | newspaper4k | Postiz | Plugins Yoast / RankMath | claude-seo |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Indexación Google API (<15 min)** | ✅ Integrado y por lotes | ✅ Nativo | ❌ No | ❌ No | ⚠️ Plugin limitado | ❌ No |
| **Protocolo IndexNow (Bing, Yandex)** | ✅ Cliente Nativo | ❌ No | ❌ No | ❌ No | ⚠️ Básico | ❌ No |
| **Auditoría de Citabilidad GEO (0-100)** | ✅ Puntuación y Guía | ❌ No | ❌ No | ❌ No | ❌ No | ⚠️ Solo Prompts |
| **Generador Automático de `/llms.txt`** | ✅ Estandarizado | ❌ No | ❌ No | ❌ No | ❌ No | ⚠️ Genérico |
| **Esquema NewsArticle y LiveBlog** | ✅ Grafo con sameAs | ❌ No | ❌ No | ❌ No | ✅ Básico | ⚠️ Estático |
| **Auditoría Técnica Google Discover** | ✅ Dimensiones + Vitals | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Distribución Multicanal con n8n** | ✅ Flujo Listo | ❌ No | ❌ No | ⚠️ Panel Manual | ❌ No | ❌ No |
| **Notificaciones Web Push (VAPID)** | ✅ Integrado nativo | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Integración con Agentes de IA** | ✅ Estándar multi-agente | ❌ No | ❌ No | ❌ No | ❌ No | ⚠️ Solo Claude |

---

## 🤖 Integración con Agentes de Programación con IA

News Traffic Engine está concebido para ser orquestado autónomamente por agentes inteligentes:
* **[Hermes Agent](HERMES.md):** Automatiza el ciclo de captura de noticias, reescritura de titulares y publicación inmediata.
* **[Claude Code & Claude AI](CLAUDE.md):** Supervisa los estándares de código y pruebas automatizadas.
* **[Google Antigravity & Gemini](AGENTS.md):** Totalmente compatible con las habilidades del ecosistema Antigravity.
* **[Cursor](.cursorrules):** Supervisa en tiempo real la regla de respuesta en 45 palabras y pasajes de 130-175 palabras.
* **[OpenAI Codex y Kimi Code](AGENTS.md):** Ejecución fluida mediante CLI y API de Python.

---

## ❓ Preguntas Frecuentes (FAQ) — Crecimiento Editorial y GEO

### P1: ¿Cómo logra la Google Indexing API reducir el tiempo de indexación a menos de 15 minutos?
La API de indexación de Google omite las colas tradicionales de rastreo al permitir al editor notificar directamente las nuevas URL. El Googlebot programa una visita de máxima prioridad en un plazo de 5 a 15 minutos, permitiendo que la noticia compita en **Google Top Stories**.

### P2: ¿Qué es la Optimización para Motores Generativos (GEO) y por qué es crucial?
GEO es la ingeniería de redacción estructurada para que los motores de IA (ChatGPT Search, Perplexity) citen tu medio como fuente primordial. El 92% de las citas provienen de noticias con respuestas directas en las primeras 45 palabras del primer párrafo y pasajes modulares de entre 130 y 175 palabras.

### P3: ¿Cuáles son los requisitos técnicos obligatorios para aparecer en Google Discover?
Google Discover exige tres factores indispensables: 1. La directiva `<meta name="robots" content="max-image-preview:large">`. 2. Imagen principal de alta resolución con al menos 1200px de ancho y proporción 16:9. 3. Rendimiento web móvil con LCP inferior a 1.5 segundos y estabilidad visual CLS inferior a 0.05.

### P4: ¿Por qué la difusión inmediata en Telegram, X y redes sociales multiplica el tráfico?
El 60% del impacto de una noticia de última hora se concentra en las dos primeras horas. El envío automático genera un pico instantáneo de lectores que envía a los algoritmos de búsqueda la señal de viralidad y relevancia.

### P5: ¿Cómo ayuda el estándar `/llms.txt` a ganar visibilidad en modelos como ChatGPT y Claude?
El archivo `/llms.txt` ofrece a los rastreadores de IA un resumen en Markdown limpio y sin código residual, facilitando su indexación en sistemas RAG con un consumo óptimo de tokens.

### P6: ¿Se puede integrar en WordPress o Laravel?
Sí; a través de webhooks conectados a n8n o ejecutando directamente el CLI en Python desde eventos del CMS.

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

* **Arquitecto Principal:** **[Taghi Molavi](https://molavi.pro/es)** — Investigador y arquitecto de sistemas de IA, creador de los frameworks GEO-Scope y SAGE.
  * Sitio web: [https://molavi.pro/es](https://molavi.pro/es)
  * Contacto: `contact@molavi.pro`

* **Socio Tecnológico Empresarial:** **[Agencia de Marketing Digital Inten (Inten Digital Marketing Agency)](https://inten.asia/en)** — Líder en transformación digital empresarial, automatización con IA e infraestructuras de alto rendimiento en Asia.
  * Sitio web: [https://inten.asia/en](https://inten.asia/en)

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT** — consulte el archivo [LICENSE](LICENSE) para más detalles.

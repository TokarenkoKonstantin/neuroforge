# 🤖 Neuroforge

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-latest-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

> Портфолио AI-архитектора | Модули и примеры для разработки AI-систем

## 👨‍💻 О себе

AI-архитектор, специализирующийся на разработке интеллектуальных систем, чат-ботов и AI-приложений. Опыт работы с современными LLM, RAG-системами, multi-agent архитектурами и голосовыми интерфейсами.

## 🚀 Навыки и Технологии

### AI & Machine Learning
- 🧠 **LLM Integration** - GPT-4, Claude, Llama, Groq
- 🔍 **RAG Systems** - Vector databases, semantic search
- 🎯 **Prompt Engineering** - Оптимизация промптов, few-shot learning
- 🤝 **Multi-Agent Systems** - Координация нескольких AI-агентов
- 🎤 **Voice AI** - Speech-to-text, text-to-speech (Deepgram, ElevenLabs)
- 🖼️ **Multi-modal AI** - Работа с текстом, изображениями, голосом

### Backend & Infrastructure
- 🐍 **Python** - FastAPI, aiogram, LangChain
- 🗄️ **Databases** - PostgreSQL, SQLite, Vector DBs (Pinecone, Chroma)
- 🐳 **DevOps** - Docker, nginx, systemd
- ☁️ **Cloud** - AWS, VPS deployment
- 🔐 **Security** - API authentication, rate limiting

### Chatbot Development
- 💬 **Telegram Bots** - aiogram, webhooks, inline keyboards
- 🎨 **UI/UX** - Conversational design, user flows
- 💳 **Payments** - Stripe, YooKassa integration
- 📊 **Analytics** - User tracking, metrics

## 📦 Модули для Чат-Ботов

Коллекция готовых модулей для быстрой разработки AI-чат-ботов:

### 1. 🔍 RAG Module (Retrieval Augmented Generation)
Модуль для создания чат-ботов с доступом к базе знаний.

**Возможности:**
- Semantic search по документам
- Vector embeddings (OpenAI, Cohere)
- Интеграция с vector databases
- Контекстные ответы на основе документов

**Технологии:** LangChain, Pinecone/Chroma, OpenAI Embeddings

[→ Подробнее](./chatbot-modules/rag-module/)

### 2. 🛠️ Function Calling Module
Модуль для интеграции внешних инструментов и API.

**Возможности:**
- Автоматический вызов функций
- Интеграция с внешними API
- Tool use (поиск, калькуляции, API запросы)
- Structured outputs

**Технологии:** OpenAI Function Calling, LangChain Tools

[→ Подробнее](./chatbot-modules/function-calling/)

### 3. 🧠 Memory System Module
Система памяти для долгосрочных диалогов.

**Возможности:**
- Short-term memory (контекст диалога)
- Long-term memory (история пользователя)
- Semantic memory (важные факты)
- Персонализация ответов

**Технологии:** Redis, PostgreSQL, Vector DB

[→ Подробнее](./chatbot-modules/memory-system/)

### 4. 🎤 Voice Integration Module
Голосовой интерфейс для чат-ботов.

**Возможности:**
- Speech-to-text (Deepgram, Whisper)
- Text-to-speech (ElevenLabs, Google TTS)
- Голосовые команды
- Потоковая обработка аудио

**Технологии:** Deepgram, Whisper, ElevenLabs

[→ Подробнее](./chatbot-modules/voice-integration/)

### 5. 🤝 Multi-Agent System
Система из нескольких специализированных агентов.

**Возможности:**
- Координация нескольких AI-агентов
- Специализированные агенты (поиск, анализ, генерация)
- Автоматическое делегирование задач
- Параллельная обработка

**Технологии:** LangChain Agents, AutoGPT patterns

[→ Подробнее](./chatbot-modules/multi-agent/)

### 6. 📊 Analytics & Monitoring Module
Аналитика и мониторинг чат-ботов.

**Возможности:**
- User tracking
- Conversation analytics
- Performance metrics
- Error monitoring
- A/B testing

**Технологии:** PostgreSQL, Grafana, Custom dashboards

[→ Подробнее](./chatbot-modules/analytics/)

### 7. 🔄 Streaming Responses Module
Потоковая генерация ответов.

**Возможности:**
- Real-time streaming
- Partial responses
- Better UX (пользователь видит ответ сразу)
- Поддержка SSE и WebSockets

**Технологии:** FastAPI, SSE, WebSockets

[→ Подробнее](./chatbot-modules/streaming/)

### 8. 🖼️ Multi-Modal Module
Работа с разными типами контента.

**Возможности:**
- Обработка изображений (GPT-4 Vision, DALL-E)
- Генерация изображений
- Анализ документов
- OCR (распознавание текста)

**Технологии:** GPT-4 Vision, DALL-E, Tesseract

[→ Подробнее](./chatbot-modules/multi-modal/)

## 🎯 Проекты

### [Второй Мозг (vtoroi-mozg)](https://github.com/TokarenkoKonstantin/vtoroi-mozg)
Telegram бот для управления задачами с AI.

**Технологии:** Python, aiogram, Deepgram, Groq, Todoist API, YooKassa, Stripe

**Возможности:**
- Голосовые сообщения → текст → задачи
- AI классификация (задача/заметка/идея)
- Интеграция с Todoist и Obsidian
- Платёжная система (подписки)
- Dashboard команды

### [OpenClaw Demo](https://github.com/TokarenkoKonstantin/openclaw-demo)
Демонстрационные материалы для продажи AI-услуг.

**Включает:**
- Портфолио проектов
- Сценарии демонстрации
- Скрипты продаж
- Гайд по установке

### [Obsidian Produkt](https://github.com/TokarenkoKonstantin/obsidian-produkt)
Готовая система продуктивности с ПАРА и Кайдзен.

**Технологии:** Obsidian, Markdown, PARA methodology

### [Frilans Materialy](https://github.com/TokarenkoKonstantin/frilans-materialy)
Материалы для запуска фриланс-карьеры.

**Включает:**
- Профили для Upwork/Fiverr
- Шаблоны предложений
- Пакеты услуг

## 📚 Примеры Использования

### Быстрый старт: RAG Chatbot
```python
from chatbot_modules import RAGModule

# Инициализация
rag = RAGModule(
    vector_db="pinecone",
    embeddings="openai",
    llm="gpt-4"
)

# Загрузка документов
rag.load_documents("./docs")

# Запрос
response = rag.query("Как настроить бота?")
print(response)
```

### Быстрый старт: Function Calling Bot
```python
from chatbot_modules import FunctionCallingBot

# Определение функций
tools = [
    {
        "name": "search_web",
        "description": "Поиск в интернете",
        "parameters": {"query": "string"}
    }
]

# Инициализация
bot = FunctionCallingBot(tools=tools)

# Обработка запроса
response = bot.process("Найди информацию о Python")
```

### Быстрый старт: Voice Bot
```python
from chatbot_modules import VoiceBot

# Инициализация
bot = VoiceBot(
    stt_provider="deepgram",
    tts_provider="elevenlabs"
)

# Обработка голосового сообщения
audio_file = "voice_message.ogg"
text = bot.transcribe(audio_file)
response = bot.generate_response(text)
audio_response = bot.synthesize(response)
```

## 🏗️ Архитектурные Паттерны

### 1. Модульная Архитектура
```
Bot Application
├── Core (routing, middleware)
├── Modules (RAG, functions, memory)
├── Integrations (APIs, databases)
└── UI (handlers, keyboards)
```

### 2. Event-Driven Architecture
```
User Input → Event Bus → Handlers → AI Processing → Response
```

### 3. Microservices Architecture
```
API Gateway → [Bot Service, AI Service, DB Service] → Response
```

## 📈 Статус проекта

- 📚 **3 модуля** с полной документацией (RAG, Function Calling, Memory)
- 💻 **5 модулей** в разработке (Voice, Multi-Agent, Analytics, Streaming, Multi-Modal)
- 🔧 **Примеры кода** для быстрого старта
- 🔒 **Security-first** подход во всех решениях

## 🛠️ Инструменты и Сервисы

### AI & LLM
- OpenAI (GPT-4, GPT-3.5, Embeddings)
- Anthropic (Claude)
- Groq (Llama, Mixtral)
- Deepgram (Speech-to-text)
- ElevenLabs (Text-to-speech)

### Frameworks & Libraries
- LangChain (LLM orchestration)
- aiogram (Telegram bots)
- FastAPI (REST APIs)
- Pydantic (Data validation)

### Databases
- PostgreSQL (Relational data)
- Redis (Caching, sessions)
- Pinecone/Chroma (Vector search)
- SQLite (Lightweight storage)

### DevOps
- Docker (Containerization)
- nginx (Reverse proxy)
- systemd (Service management)
- GitHub Actions (CI/CD)

## 📞 Контакты

Свяжитесь со мной для обсуждения проектов и сотрудничества:

- 💬 **Telegram:** [@KonstantinTokar](https://t.me/KonstantinTokar)
- 📧 **Email:** konstantin.tokarenko@gmail.com
- 🐙 **GitHub:** [TokarenkoKonstantin](https://github.com/TokarenkoKonstantin)

**Открыт для:**
- 🚀 Фриланс проектов (AI/ML, чат-боты)
- 💼 Консультаций по архитектуре AI-систем
- 🤝 Технического партнёрства
- 📚 Менторства и code review

## 📄 Лицензия

Все модули и примеры предоставляются "как есть" для образовательных целей.

---

**Создано с ❤️ AI-архитектором | 2026**

*Постоянно обновляется новыми модулями и проектами*
---

**Создано с ❤️ AI-архитектором | 2026**

*Постоянно обновляется новыми модулями и проектами*

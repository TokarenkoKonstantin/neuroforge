# 📦 Модули для Чат-Ботов

Коллекция готовых модулей для быстрой разработки AI-чат-ботов.

## 🎯 Философия

Каждый модуль:
- ✅ **Независимый** - работает автономно
- ✅ **Переиспользуемый** - легко интегрируется в любой проект
- ✅ **Документированный** - полная документация и примеры
- ✅ **Тестированный** - покрыт тестами
- ✅ **Production-ready** - готов к использованию в production

## 📚 Доступные Модули

### 1. RAG Module
**Retrieval Augmented Generation** - чат-бот с доступом к базе знаний.

[→ Документация](./rag-module/)

### 2. Function Calling Module
**Tool Use** - интеграция внешних инструментов и API.

[→ Документация](./function-calling/)

### 3. Memory System Module
**Conversation Memory** - система памяти для долгосрочных диалогов.

[→ Документация](./memory-system/)

### 4. Voice Integration Module
**Speech Interface** - голосовой интерфейс для чат-ботов.

[→ Документация](./voice-integration/)

### 5. Multi-Agent System
**Agent Coordination** - система из нескольких специализированных агентов.

[→ Документация](./multi-agent/)

### 6. Analytics Module
**Monitoring & Analytics** - аналитика и мониторинг чат-ботов.

[→ Документация](./analytics/)

### 7. Streaming Module
**Real-time Responses** - потоковая генерация ответов.

[→ Документация](./streaming/)

### 8. Multi-Modal Module
**Multi-format Content** - работа с текстом, изображениями, голосом.

[→ Документация](./multi-modal/)

## 🚀 Быстрый Старт

### Установка
```bash
pip install -r requirements.txt
```

### Использование
```python
from chatbot_modules import RAGModule, VoiceBot, FunctionCallingBot

# Инициализация модулей
rag = RAGModule(vector_db="pinecone")
voice = VoiceBot(stt_provider="deepgram")
functions = FunctionCallingBot(tools=my_tools)

# Использование
response = rag.query("Как настроить бота?")
text = voice.transcribe(audio_file)
result = functions.process(user_message)
```

## 🏗️ Архитектура

```
chatbot-modules/
├── rag-module/
│   ├── __init__.py
│   ├── rag.py
│   ├── embeddings.py
│   └── README.md
├── function-calling/
│   ├── __init__.py
│   ├── functions.py
│   └── README.md
├── memory-system/
│   ├── __init__.py
│   ├── memory.py
│   └── README.md
└── ...
```

## 📖 Документация

Каждый модуль имеет:
- 📄 **README.md** - описание и примеры
- 🔧 **API Reference** - полное описание API
- 💡 **Examples** - примеры использования
- 🧪 **Tests** - unit и integration тесты

## 🤝 Вклад

Приветствуются:
- 🐛 Bug reports
- 💡 Feature requests
- 📝 Documentation improvements
- 🔧 Code contributions

## 📄 Лицензия

MIT License - свободное использование в коммерческих и некоммерческих проектах.

# 🧠 Memory System Module

Система памяти для долгосрочных диалогов и персонализации чат-бота.

## 🎯 Что это?

Memory System - модуль для хранения и использования информации о пользователе и истории диалогов. Позволяет боту "помнить" предыдущие разговоры, предпочтения пользователя и важные факты.

## ✨ Типы памяти

### 1. Short-term Memory (Краткосрочная)
- Контекст текущего диалога
- Последние N сообщений
- Временные данные сессии

### 2. Long-term Memory (Долгосрочная)
- История всех диалогов
- Персональные данные пользователя
- Предпочтения и настройки

### 3. Semantic Memory (Семантическая)
- Важные факты о пользователе
- Извлечённые из диалогов знания
- Структурированная информация

## 🚀 Быстрый старт

```python
from chatbot_modules.memory import MemorySystem

# Инициализация
memory = MemorySystem(
    storage="redis",  # или "postgresql", "sqlite"
    short_term_size=10,  # последние 10 сообщений
    semantic_search=True
)

# Сохранение сообщения
memory.add_message(
    user_id=12345,
    role="user",
    content="Меня зовут Константин"
)

memory.add_message(
    user_id=12345,
    role="assistant",
    content="Приятно познакомиться, Константин!"
)

# Получение контекста
context = memory.get_context(user_id=12345)
print(context)  # Последние N сообщений

# Поиск по истории
results = memory.search(
    user_id=12345,
    query="Как меня зовут?"
)
```

## 📦 Установка

```bash
pip install redis postgresql-client langchain
```

## 🔧 Конфигурация

```python
config = {
    "storage": {
        "type": "redis",
        "host": "localhost",
        "port": 6379,
        "db": 0
    },
    "short_term": {
        "size": 10,  # количество сообщений
        "ttl": 3600  # время жизни в секундах
    },
    "long_term": {
        "enabled": True,
        "compression": True  # сжатие старых сообщений
    },
    "semantic": {
        "enabled": True,
        "embeddings": "openai",
        "vector_db": "pinecone"
    }
}

memory = MemorySystem(config)
```

## 💡 Примеры использования

### Базовая память
```python
# Добавление сообщения
memory.add_message(user_id, "user", "Я люблю Python")

# Получение истории
history = memory.get_history(user_id, limit=20)

# Очистка истории
memory.clear_history(user_id)
```

### Семантический поиск
```python
# Поиск релевантных сообщений
results = memory.semantic_search(
    user_id=12345,
    query="Какие языки программирования я изучаю?",
    top_k=5
)

for msg in results:
    print(f"{msg.role}: {msg.content}")
```

### Извлечение фактов
```python
# Автоматическое извлечение важных фактов
facts = memory.extract_facts(user_id=12345)
# Результат: {"name": "Константин", "interests": ["Python", "AI"]}

# Сохранение факта
memory.save_fact(user_id=12345, "favorite_language", "Python")

# Получение факта
lang = memory.get_fact(user_id=12345, "favorite_language")
```

### Персонализация
```python
# Получение профиля пользователя
profile = memory.get_user_profile(user_id=12345)

# Генерация персонализированного ответа
response = llm.generate(
    prompt=f"Пользователь {profile['name']} спрашивает...",
    context=memory.get_context(user_id=12345)
)
```

## 🏗️ Архитектура

```
Message Input
    ↓
Short-term Storage (Redis)
    ↓
Long-term Storage (PostgreSQL)
    ↓
Semantic Indexing (Vector DB)
    ↓
Fact Extraction (LLM)
    ↓
User Profile Update
```

## 📊 Структура данных

### Message
```python
{
    "id": "msg_123",
    "user_id": 12345,
    "role": "user",  # или "assistant"
    "content": "Текст сообщения",
    "timestamp": "2026-03-23T17:00:00Z",
    "metadata": {
        "tokens": 15,
        "language": "ru"
    }
}
```

### User Profile
```python
{
    "user_id": 12345,
    "name": "Константин",
    "facts": {
        "favorite_language": "Python",
        "interests": ["AI", "ML", "Chatbots"]
    },
    "preferences": {
        "language": "ru",
        "tone": "friendly"
    },
    "stats": {
        "total_messages": 150,
        "first_seen": "2026-03-01",
        "last_seen": "2026-03-23"
    }
}
```

## 🔗 Интеграция с Telegram

```python
from aiogram import Router, F
from aiogram.types import Message

router = Router()
memory = MemorySystem(config)

@router.message(F.text)
async def handle_message(message: Message):
    user_id = message.from_user.id
    
    # Сохранение сообщения пользователя
    memory.add_message(user_id, "user", message.text)
    
    # Получение контекста
    context = memory.get_context(user_id)
    
    # Генерация ответа с учётом контекста
    response = llm.generate(message.text, context=context)
    
    # Сохранение ответа бота
    memory.add_message(user_id, "assistant", response)
    
    await message.answer(response)
```

## 🎓 Best Practices

1. **TTL для short-term** - устанавливайте время жизни для краткосрочной памяти
2. **Compression** - сжимайте старые сообщения для экономии места
3. **Indexing** - индексируйте часто используемые поля
4. **Privacy** - шифруйте персональные данные
5. **GDPR** - предоставляйте возможность удаления данных
6. **Summarization** - суммаризируйте длинные истории
7. **Fact Verification** - проверяйте извлечённые факты

## 🔒 Приватность

```python
# Шифрование данных
memory = MemorySystem(
    encryption_key=os.getenv("ENCRYPTION_KEY"),
    encrypt_content=True
)

# Удаление данных пользователя (GDPR)
memory.delete_user_data(user_id=12345)

# Экспорт данных пользователя
data = memory.export_user_data(user_id=12345)
```

## 📚 Ресурсы

- [LangChain Memory Documentation](https://python.langchain.com/docs/modules/memory/)
- [Redis Documentation](https://redis.io/docs/)

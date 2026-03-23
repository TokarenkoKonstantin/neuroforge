# 📚 Примеры кода

Рабочие примеры использования модулей для чат-ботов.

## 🚀 Быстрый старт

### Установка зависимостей

```bash
pip install langchain openai chromadb
```

### Настройка API ключей

```bash
export OPENAI_API_KEY="your-api-key-here"
```

## 📝 Доступные примеры

### 1. RAG (Retrieval Augmented Generation)

**Файл:** `rag_simple_example.py`

Простой пример RAG системы с использованием LangChain и Chroma.

```bash
python examples/rag_simple_example.py
```

**Что демонстрирует:**
- Создание embeddings из документов
- Поиск релевантных фрагментов
- Генерация ответов на основе контекста
- Работа с vector store (Chroma)

**Требования:**
- OpenAI API ключ
- Python 3.12+
- langchain, openai, chromadb

### 2. Function Calling (в разработке)

Пример интеграции внешних функций и API.

### 3. Memory System (в разработке)

Пример системы памяти для долгосрочных диалогов.

## 💡 Примечания

- Все примеры используют реальные библиотеки (LangChain, OpenAI)
- Код упрощён для демонстрации концепций
- Для production нужно добавить обработку ошибок и конфигурацию
- Требуются API ключи для работы

## 🔗 Полезные ссылки

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Chroma Documentation](https://docs.trychroma.com/)

## 📞 Вопросы?

Если у вас есть вопросы или предложения по примерам:
- Telegram: [@KonstantinTokar](https://t.me/KonstantinTokar)
- GitHub Issues: [neuroforge/issues](https://github.com/TokarenkoKonstantin/neuroforge/issues)

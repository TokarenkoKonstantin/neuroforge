# 🔍 RAG Module (Retrieval Augmented Generation)

Модуль для создания чат-ботов с доступом к базе знаний через семантический поиск.

## 🎯 Что это?

RAG (Retrieval Augmented Generation) - техника, которая позволяет LLM получать доступ к внешним документам и базам знаний. Вместо того чтобы полагаться только на знания, заложенные в модель, бот может искать релевантную информацию в ваших документах и использовать её для ответа.

## ✨ Возможности

- 📚 **Semantic Search** - поиск по смыслу, а не по ключевым словам
- 🔢 **Vector Embeddings** - преобразование текста в векторы для поиска
- 🗄️ **Multiple Vector DBs** - поддержка Pinecone, Chroma, Weaviate
- 📄 **Document Processing** - загрузка PDF, DOCX, TXT, Markdown
- 🎯 **Context Ranking** - ранжирование найденных документов по релевантности
- 💬 **Conversational RAG** - учёт истории диалога

## 🚀 Быстрый старт

```python
from chatbot_modules.rag import RAGModule

# Инициализация
rag = RAGModule(
    vector_db="pinecone",
    embeddings_model="openai",
    llm="gpt-4",
    chunk_size=1000,
    chunk_overlap=200
)

# Загрузка документов
rag.load_documents("./knowledge_base/")

# Запрос
response = rag.query(
    question="Как настроить Telegram бота?",
    top_k=3  # количество релевантных документов
)

print(response.answer)
print(response.sources)  # источники информации
```

## 📦 Установка

```bash
pip install langchain openai pinecone-client chromadb
```

## 🔧 Конфигурация

```python
config = {
    "vector_db": {
        "provider": "pinecone",  # или "chroma", "weaviate"
        "index_name": "my-knowledge-base",
        "dimension": 1536  # для OpenAI embeddings
    },
    "embeddings": {
        "provider": "openai",  # или "cohere", "huggingface"
        "model": "text-embedding-ada-002"
    },
    "llm": {
        "provider": "openai",
        "model": "gpt-4",
        "temperature": 0.7
    },
    "chunking": {
        "chunk_size": 1000,
        "chunk_overlap": 200,
        "separator": "\n\n"
    }
}

rag = RAGModule(config)
```

## 💡 Примеры использования

### Базовый RAG
```python
# Простой вопрос-ответ
answer = rag.query("Что такое Python?")
```

### RAG с историей диалога
```python
# Учёт контекста диалога
conversation = []
conversation.append({"role": "user", "content": "Расскажи о Python"})
conversation.append({"role": "assistant", "content": "Python - язык программирования..."})

answer = rag.query(
    question="А какие у него преимущества?",
    conversation_history=conversation
)
```

### RAG с фильтрацией
```python
# Поиск только в определённых документах
answer = rag.query(
    question="Как установить библиотеку?",
    filters={"category": "installation", "language": "ru"}
)
```

## 🏗️ Архитектура

```
User Query
    ↓
Embedding (преобразование в вектор)
    ↓
Vector Search (поиск похожих документов)
    ↓
Context Retrieval (получение текста документов)
    ↓
Prompt Construction (формирование промпта с контекстом)
    ↓
LLM Generation (генерация ответа)
    ↓
Response
```

## 📊 Метрики качества

- **Retrieval Precision** - точность поиска релевантных документов
- **Answer Relevance** - релевантность ответа вопросу
- **Faithfulness** - соответствие ответа найденным документам
- **Context Recall** - полнота найденного контекста

## 🎓 Best Practices

1. **Chunking Strategy** - разбивайте документы на смысловые части (500-1500 токенов)
2. **Metadata** - добавляйте метаданные к документам (дата, категория, автор)
3. **Hybrid Search** - комбинируйте semantic и keyword search
4. **Reranking** - используйте reranker для улучшения качества
5. **Caching** - кешируйте embeddings для ускорения

## 🔗 Интеграция с Telegram

```python
from aiogram import Router, F
from aiogram.types import Message

router = Router()
rag = RAGModule(config)

@router.message(F.text)
async def handle_question(message: Message):
    answer = rag.query(message.text)
    await message.answer(
        f"{answer.answer}\n\n📚 Источники: {', '.join(answer.sources)}"
    )
```

## 📚 Ресурсы

- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [Pinecone Documentation](https://docs.pinecone.io/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)

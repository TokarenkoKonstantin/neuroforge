"""
Простой пример RAG (Retrieval Augmented Generation)

Этот пример показывает базовую концепцию RAG:
1. Загрузка документов
2. Создание embeddings
3. Поиск релевантных фрагментов
4. Генерация ответа на основе найденного контекста

Для production использования нужно добавить:
- Обработку ошибок
- Конфигурацию
- Кеширование
- Мониторинг
"""

from typing import List
import os

# Требуется: pip install langchain openai chromadb

def simple_rag_example():
    """
    Минимальный пример RAG системы
    """
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.vectorstores import Chroma
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.llms import OpenAI
    from langchain.chains import RetrievalQA
    from langchain.docstore.document import Document
    
    # Проверка API ключа
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Установите OPENAI_API_KEY в переменные окружения")
        return
    
    # Пример документов (в реальности загружаются из файлов)
    documents = [
        Document(
            page_content="Python - высокоуровневый язык программирования. "
                        "Он поддерживает множественные парадигмы программирования.",
            metadata={"source": "python_intro.txt"}
        ),
        Document(
            page_content="LangChain - это фреймворк для разработки приложений с LLM. "
                        "Он упрощает создание RAG систем и агентов.",
            metadata={"source": "langchain_intro.txt"}
        ),
        Document(
            page_content="RAG (Retrieval Augmented Generation) - техника, которая "
                        "позволяет LLM использовать внешние документы для ответов.",
            metadata={"source": "rag_intro.txt"}
        )
    ]
    
    print("📚 Создание RAG системы...")
    
    # Разбиение на чанки
    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    texts = text_splitter.split_documents(documents)
    print(f"✅ Создано {len(texts)} текстовых фрагментов")
    
    # Создание embeddings и vector store
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=texts,
        embedding=embeddings
    )
    print("✅ Vector store создан")
    
    # Создание QA цепочки
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 2})
    )
    print("✅ QA система готова\n")
    
    # Примеры запросов
    questions = [
        "Что такое Python?",
        "Для чего используется LangChain?",
        "Объясни что такое RAG"
    ]
    
    for question in questions:
        print(f"❓ Вопрос: {question}")
        answer = qa_chain.run(question)
        print(f"💡 Ответ: {answer}\n")


def rag_with_custom_documents(file_paths: List[str]):
    """
    RAG система с загрузкой документов из файлов
    
    Args:
        file_paths: Список путей к текстовым файлам
    """
    from langchain.document_loaders import TextLoader
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.vectorstores import Chroma
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain.chains import RetrievalQA
    from langchain.llms import OpenAI
    
    # Загрузка документов
    documents = []
    for file_path in file_paths:
        loader = TextLoader(file_path, encoding='utf-8')
        documents.extend(loader.load())
    
    # Разбиение на чанки
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    texts = text_splitter.split_documents(documents)
    
    # Создание vector store
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(texts, embeddings)
    
    # Создание QA системы
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    
    return qa


if __name__ == "__main__":
    print("🚀 Запуск простого примера RAG\n")
    simple_rag_example()
    
    print("\n" + "="*50)
    print("💡 Для использования с вашими документами:")
    print("   qa = rag_with_custom_documents(['doc1.txt', 'doc2.txt'])")
    print("   answer = qa.run('Ваш вопрос')")

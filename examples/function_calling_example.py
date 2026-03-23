"""
Простой пример Function Calling (Tool Use)

Этот пример показывает как LLM может вызывать внешние функции:
1. Определение функций с описаниями
2. LLM анализирует запрос и выбирает нужную функцию
3. Выполнение функции с параметрами
4. Генерация ответа на основе результата

Для production использования нужно добавить:
- Обработку ошибок
- Валидацию параметров
- Rate limiting
- Логирование
"""

import json
import os
from typing import Any, Dict, List

# Требуется: pip install openai

def get_weather(city: str) -> Dict[str, Any]:
    """
    Получение погоды для города (упрощённая версия)
    В реальности здесь был бы API запрос к сервису погоды
    """
    # Симуляция API ответа
    weather_data = {
        "Москва": {"temp": -5, "condition": "Снег", "humidity": 80},
        "Санкт-Петербург": {"temp": -3, "condition": "Облачно", "humidity": 85},
        "Сочи": {"temp": 12, "condition": "Солнечно", "humidity": 60},
    }
    
    return weather_data.get(city, {"temp": 0, "condition": "Неизвестно", "humidity": 0})


def calculate(expression: str) -> float:
    """
    Вычисление математического выражения
    ВНИМАНИЕ: В production использовать безопасный парсер!
    """
    try:
        # В реальности использовать ast.literal_eval или безопасный парсер
        result = eval(expression)
        return float(result)
    except Exception as e:
        return f"Ошибка: {str(e)}"


def search_database(query: str) -> List[Dict[str, str]]:
    """
    Поиск в базе данных (упрощённая версия)
    В реальности здесь был бы SQL запрос
    """
    # Симуляция результатов поиска
    mock_data = [
        {"id": "1", "title": "Python Tutorial", "content": "Основы Python"},
        {"id": "2", "title": "AI Guide", "content": "Введение в AI"},
        {"id": "3", "title": "LangChain Docs", "content": "Документация LangChain"},
    ]
    
    # Простой поиск по вхождению
    results = [item for item in mock_data if query.lower() in item["title"].lower()]
    return results


# Определение функций для OpenAI
FUNCTIONS = [
    {
        "name": "get_weather",
        "description": "Получить текущую погоду для указанного города",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Название города, например 'Москва'"
                }
            },
            "required": ["city"]
        }
    },
    {
        "name": "calculate",
        "description": "Вычислить математическое выражение",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Математическое выражение, например '2 + 2' или '10 * 5'"
                }
            },
            "required": ["expression"]
        }
    },
    {
        "name": "search_database",
        "description": "Поиск информации в базе данных",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Поисковый запрос"
                }
            },
            "required": ["query"]
        }
    }
]


def execute_function(function_name: str, arguments: Dict[str, Any]) -> Any:
    """
    Выполнение функции по имени
    """
    functions_map = {
        "get_weather": get_weather,
        "calculate": calculate,
        "search_database": search_database
    }
    
    if function_name not in functions_map:
        return f"Функция {function_name} не найдена"
    
    try:
        return functions_map[function_name](**arguments)
    except Exception as e:
        return f"Ошибка выполнения: {str(e)}"


def simple_function_calling_example():
    """
    Простой пример использования function calling
    """
    from openai import OpenAI
    
    # Проверка API ключа
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Установите OPENAI_API_KEY в переменные окружения")
        return
    
    client = OpenAI()
    
    # Примеры запросов
    queries = [
        "Какая погода в Москве?",
        "Вычисли 25 * 4 + 10",
        "Найди информацию о Python"
    ]
    
    print("🚀 Запуск примера Function Calling\n")
    
    for query in queries:
        print(f"❓ Запрос: {query}")
        
        # Первый запрос к LLM
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": query}],
            functions=FUNCTIONS,
            function_call="auto"
        )
        
        message = response.choices[0].message
        
        # Проверяем, хочет ли LLM вызвать функцию
        if message.function_call:
            function_name = message.function_call.name
            arguments = json.loads(message.function_call.arguments)
            
            print(f"🔧 Вызов функции: {function_name}")
            print(f"📝 Параметры: {arguments}")
            
            # Выполняем функцию
            function_result = execute_function(function_name, arguments)
            print(f"✅ Результат: {function_result}")
            
            # Второй запрос к LLM с результатом функции
            second_response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": query},
                    {
                        "role": "function",
                        "name": function_name,
                        "content": json.dumps(function_result)
                    }
                ]
            )
            
            final_answer = second_response.choices[0].message.content
            print(f"💡 Ответ: {final_answer}\n")
        else:
            # LLM ответил без вызова функции
            print(f"💡 Ответ: {message.content}\n")


def manual_function_calling_demo():
    """
    Демонстрация работы функций без OpenAI (для тестирования)
    """
    print("🧪 Демонстрация функций (без OpenAI API)\n")
    
    # Тест погоды
    print("1️⃣ Тест функции get_weather:")
    weather = get_weather("Москва")
    print(f"   Москва: {weather['temp']}°C, {weather['condition']}\n")
    
    # Тест калькулятора
    print("2️⃣ Тест функции calculate:")
    result = calculate("25 * 4 + 10")
    print(f"   25 * 4 + 10 = {result}\n")
    
    # Тест поиска
    print("3️⃣ Тест функции search_database:")
    results = search_database("Python")
    print(f"   Найдено результатов: {len(results)}")
    for item in results:
        print(f"   - {item['title']}: {item['content']}\n")


if __name__ == "__main__":
    print("="*60)
    print("Function Calling Example")
    print("="*60 + "\n")
    
    # Сначала демонстрация функций
    manual_function_calling_demo()
    
    print("="*60)
    print("Для полного примера с OpenAI установите OPENAI_API_KEY")
    print("="*60 + "\n")
    
    # Если есть API ключ, запускаем полный пример
    if os.getenv("OPENAI_API_KEY"):
        simple_function_calling_example()
    else:
        print("💡 Установите OPENAI_API_KEY для запуска полного примера:")
        print("   export OPENAI_API_KEY='your-api-key-here'")
        print("   python examples/function_calling_example.py")

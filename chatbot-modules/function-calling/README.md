# 🛠️ Function Calling Module

Модуль для интеграции внешних инструментов и API в чат-бота через function calling.

## 🎯 Что это?

Function Calling (Tool Use) - возможность LLM вызывать внешние функции и API. Вместо того чтобы просто генерировать текст, бот может выполнять действия: искать информацию, делать расчёты, обращаться к базам данных, вызывать API.

## ✨ Возможности

- 🔧 **Automatic Function Detection** - LLM сам определяет когда нужно вызвать функцию
- 📝 **Structured Outputs** - получение структурированных данных
- 🌐 **API Integration** - интеграция с любыми API
- 🔄 **Multi-step Reasoning** - цепочки вызовов функций
- ✅ **Validation** - валидация параметров функций
- 🎯 **Error Handling** - обработка ошибок вызовов

## 🚀 Быстрый старт

```python
from chatbot_modules.function_calling import FunctionCallingBot

# Определение функций
def search_web(query: str) -> str:
    """Поиск информации в интернете"""
    # Реализация поиска
    return f"Результаты поиска для: {query}"

def calculate(expression: str) -> float:
    """Вычисление математического выражения"""
    return eval(expression)

# Регистрация функций
tools = [
    {
        "name": "search_web",
        "description": "Поиск информации в интернете",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Поисковый запрос"
                }
            },
            "required": ["query"]
        },
        "function": search_web
    },
    {
        "name": "calculate",
        "description": "Вычисление математических выражений",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Математическое выражение"
                }
            },
            "required": ["expression"]
        },
        "function": calculate
    }
]

# Инициализация бота
bot = FunctionCallingBot(
    tools=tools,
    llm="gpt-4",
    max_iterations=5
)

# Использование
response = bot.process("Найди информацию о Python и вычисли 25 * 4")
print(response)
```

## 📦 Установка

```bash
pip install openai langchain pydantic
```

## 🔧 Примеры функций

### Поиск в интернете
```python
import requests

def search_web(query: str, num_results: int = 5) -> list:
    """Поиск в интернете через API"""
    api_key = os.getenv("SEARCH_API_KEY")
    response = requests.get(
        "https://api.search.com/search",
        params={"q": query, "num": num_results},
        headers={"Authorization": f"Bearer {api_key}"}
    )
    return response.json()["results"]
```

### Работа с базой данных
```python
def get_user_info(user_id: int) -> dict:
    """Получение информации о пользователе из БД"""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return {"id": result[0], "name": result[1], "email": result[2]}
```

### Отправка email
```python
def send_email(to: str, subject: str, body: str) -> bool:
    """Отправка email"""
    import smtplib
    from email.mime.text import MIMEText
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['To'] = to
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        server.send_message(msg)
    
    return True
```

### API запросы
```python
def get_weather(city: str) -> dict:
    """Получение погоды"""
    api_key = os.getenv("WEATHER_API_KEY")
    response = requests.get(
        f"https://api.weather.com/v1/current?city={city}&key={api_key}"
    )
    return response.json()
```

## 🏗️ Архитектура

```
User Message
    ↓
LLM Analysis (нужна ли функция?)
    ↓
Function Selection (какую функцию вызвать?)
    ↓
Parameter Extraction (извлечение параметров)
    ↓
Function Execution (выполнение функции)
    ↓
Result Processing (обработка результата)
    ↓
Response Generation (генерация ответа)
```

## 💡 Продвинутые примеры

### Цепочка вызовов
```python
# Бот может вызывать несколько функций последовательно
response = bot.process(
    "Найди погоду в Москве и отправь результат на email@example.com"
)
# 1. Вызовет get_weather("Москва")
# 2. Вызовет send_email("email@example.com", "Погода", результат)
```

### Условные вызовы
```python
# Бот может принимать решения на основе результатов
response = bot.process(
    "Если температура в Москве ниже 0, отправь мне уведомление"
)
```

## 🔗 Интеграция с Telegram

```python
from aiogram import Router, F
from aiogram.types import Message

router = Router()
bot = FunctionCallingBot(tools=tools)

@router.message(F.text)
async def handle_message(message: Message):
    response = bot.process(message.text)
    await message.answer(response)
```

## 🎓 Best Practices

1. **Clear Descriptions** - пишите чёткие описания функций для LLM
2. **Type Hints** - используйте type hints для параметров
3. **Error Handling** - обрабатывайте ошибки в функциях
4. **Rate Limiting** - ограничивайте частоту вызовов API
5. **Validation** - валидируйте параметры перед выполнением
6. **Logging** - логируйте все вызовы функций
7. **Security** - не давайте доступ к опасным функциям

## 🔒 Безопасность

```python
# Whitelist разрешённых функций
ALLOWED_FUNCTIONS = ["search_web", "get_weather", "calculate"]

# Проверка перед выполнением
def execute_function(name: str, params: dict):
    if name not in ALLOWED_FUNCTIONS:
        raise SecurityError(f"Function {name} not allowed")
    return functions[name](**params)
```

## 📚 Ресурсы

- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [LangChain Tools Documentation](https://python.langchain.com/docs/modules/agents/tools/)

# Библиотека рецептов

Настольное приложение для ведения личной коллекции кулинарных рецептов.
Требования: `docs/Requirements.pdf` (v4.0).

## Стек

- Python 3.12/3.13, PySide6 (Qt 6)
- SQLite (WAL) для данных, файловый каталог для фотографий
- Тесты: pytest, pytest-qt, hypothesis, freezegun
- uv для зависимостей, ruff + mypy для качества

## Разработка

```bash
uv sync                 # установить зависимости
uv run pytest           # прогнать тесты
uv run ruff check .     # линтер
uv run mypy             # проверка типов
```

## Структура

```
src/recipelib/
  domain/          # чистая бизнес-логика (без UI и БД)
  application/     # сценарии использования
  infrastructure/  # SQLite, файлы, миграции
  ui/              # PySide6
tests/
  unit/            # быстрые юнит-тесты бизнес-логики
  integration/     # SQLite, файловая система
  acceptance/      # приёмочные тесты по ТЗ
```

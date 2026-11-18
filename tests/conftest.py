"""Общие фикстуры для тестов."""

import os

# Тесты и CI работают без дисплея: Qt использует offscreen-платформу.
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

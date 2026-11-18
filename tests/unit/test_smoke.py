"""Проверка работоспособности тестового окружения."""

from PySide6.QtWidgets import QLabel


def test_pyside6_widget_can_be_created(qtbot) -> None:  # type: ignore[no-untyped-def]
    label = QLabel("привет")
    qtbot.addWidget(label)
    assert label.text() == "привет"

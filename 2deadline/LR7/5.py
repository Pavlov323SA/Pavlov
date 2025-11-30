def format_report(title: str, *points: str, **meta: str):
    print(f">>> {title.upper()} <<<")
    
    print("\nОсновные пункты:")
    for point in points:
        print(f"• {point}")
    
    print("\nДополнительно:")
    for key, val in meta.items():
        print(f"{key}: {val}")
    
    print(f"\nКонец отчета")

format_report(
    "Еженедельный обзор",
    "Завершён проект 'Альфа'",
    "Проведено 5 встреч",
    "Принято 3 новых сотрудника",
    руководитель="Иванова М.К.",
    период="23-29.10.2023",
    статус="утверждён"
)
import pandas as pd

# Словарь для описания типов данных
data_types = {
    "ID": int,
    "Age": int,
    "G": str,  # "M" или "F"
    "H": str,  # "normal", "menopause", "hypothyroidism", etc.
    "F": bool,
    "R": str,  # "White", "Black", "Asian", etc.
    "B": float,
    "C": str,  # "low", "normal", "high", etc. - или числовые значения, если возможно
    "V": str,  # "low", "normal", "high", etc. - или числовые значения
    "P": str,  # "low", "moderate", "high"
    # Добавьте другие переменные, если нужно
}

# Инициализация пустого DataFrame
df = pd.DataFrame(columns=data_types.keys())

# Функция для добавления пациента (можно упростить для разных типов данных)
def add_patient(patient_data):
    try:
        patient = {key: data_type(val) if data_type is not str else val for key, data_type, val in zip(data_types.keys(), data_types.values(), patient_data.values())}
        df = df.append(patient, ignore_index=True)

        # В случае ошибки, возможно, нужно вывести диагностическое сообщение
        print(f"Пациент успешно добавлен.")
    except ValueError as e:
        print(f"Ошибка при добавлении пациента: {e}")
        # Возможно, нужно обрабатывать ошибки более гибко,
        # например, возвращать False, если ввод некорректен


# Пример использования
patient_data = {
    "ID": 1,
    "Age": 60,
    "G": "F",
    "H": "normal",
    "F": True,
    "R": "White",
    "B": 70.5,
    "C": "low",
    "V": "low",
    "P": "low"
}
add_patient(patient_data)

# ... (Добавление других пациентов)

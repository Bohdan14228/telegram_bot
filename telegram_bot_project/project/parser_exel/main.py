import asyncio
from openpyxl import load_workbook


async def parse_excel(file_path, tt):
    # Открываем Excel-файл
    workbook = load_workbook(filename=file_path)

    # Выбираем активный лист
    sheet = workbook.active

    for index, row in enumerate(sheet.iter_rows(values_only=True)):
        if index != 0 and row[1].split()[0] == str(tt):
            text = f"Регіон: {row[0]}\n" \
                   f"ТТ: {row[1].split()[0]}\n" \
                   f"Адреса: {' '.join(row[1].split()[1:])}\n" \
                   f"ТМ: {row[2]}\n" \
                   f"Тел.: {row[3] if row[3] else ''}{', ' if row[3] and row[4] else ''}{row[4] if row[4] else ''}\n" \
                   f"Графік: {row[5]}"
            return text


async def main():
    file_path = 'contact.xlsx'
    tt = 3407
    data = await parse_excel(file_path, tt)
    print(data)


# Запускаем асинхронную функцию
asyncio.run(main())
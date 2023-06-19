# GoogleSheet

     ______   ______   ______   ______   __       ______   ______   __  __   ______   ______  ______  ______    
    /\  ___\ /\  __ \ /\  __ \ /\  ___\ /\ \     /\  ___\ /\  ___\ /\ \_\ \ /\  ___\ /\  ___\/\__  _\/\  ___\   
    \ \ \__ \\ \ \/\ \\ \ \/\ \\ \ \__ \\ \ \____\ \  __\ \ \___  \\ \  __ \\ \  __\ \ \  __\\/_/\ \/\ \___  \  
     \ \_____\\ \_____\\ \_____\\ \_____\\ \_____\\ \_____\\/\_____\\ \_\ \_\\ \_____\\ \_____\ \ \_\ \/\_____\ 
      \/_____/ \/_____/ \/_____/ \/_____/ \/_____/ \/_____/ \/_____/ \/_/\/_/ \/_____/ \/_____/  \/_/  \/_____/ 

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=30&pause=1000&color=F70000&center=true&vCenter=true&width=500&height=90&lines=GoogleSheets)](https://git.io/typing-svg)

<div>
<h1>Google Sheets Python API Usage</h1>
<p>Цей Python-скрипт демонструє базове використання Google Sheets API за допомогою бібліотеки gspread. 
Скрипт надає клас GoogleSheet для взаємодії з Google Sheets. 
Це включає вибір аркуша, читання та запис комірки, читання та запис діапазону комірок, додавання та видалення рядків, а також надання доступу до аркуша іншим користувачам.</p>

<h1>Встановлення</h1>
<p>Перед запуском скрипта переконайтеся, що ви встановили наступні залежності:</p>
    
    pip install -r requirements.txt

<h1>Налаштування Google Sheets API</h1>
<p>Вам потрібно налаштувати Google Sheets API, щоб отримати облікові дані для доступу до вашого електронного аркуша.</p>
<ul>
    <li>Перейдіть до Google API Console (https://console.developers.google.com/)</li>
    <li>Створіть новий проект.</li>
    <li>Увімкніть Google Sheets API для вашого проекту.</li>
    <li>Створіть облікові дані для API.</li>
    <li>Оберіть JSON як тип ключа і завантажте JSON файл.</li>
    <li>Перемістіть цей JSON файл до директорії вашого проекту.</li>
</ul>

<h1>Використання</h1>
<p>Створіть екземпляр класу GoogleSheet з вашим файлом облікових даних Google Sheets та ідентифікатором електронного аркуша.</p>
<p>Приклад:</p>

    google_sheet = GoogleSheet("your_credentials.json", "spreadsheet_id")

<p>Цей скрипт надає методи для виконання різних операцій з Google Sheet:</p>
<ul>
 <li>select_sheet(sheet_name): вибрати певний аркуш з електронної таблиці.</li>
 <li>share(email, perm_type, role): поділитися електронною таблицею з кимось.</li>
 <li>read_cell(cell): прочитати значення з певної комірки.</li>
 <li>write_cell(cell, value): записати значення в певну комірку.</li>
 <li>read_range(start_cell, end_cell): прочитати значення з діапазону комірок.</li>
 <li>write_range(start_cell, end_cell, values): записати значення в діапазон комірок.</li>
 <li>append_row(values): додати рядок до аркуша.</li>
 <li>delete_rows(start, end): видалити рядки з аркуша.</li>
 <li>find_telegram_channels(start_cell, end_cell): знайти всі посилання на канали Telegram в діапазоні комірок.</li>
</ul>

<p>Для запуску скрипта використовуйте наступну команду:</p>

    python your_script_name.py "Sheet1" "A1" "A10"

<p>У вищенаведеній команді "Sheet1" - це ім'я аркуша, "A1" - початкова комірка, а "A10" - кінцева комірка. 
Скрипт буде шукати посилання на канали Telegram у діапазоні від "A1" до "A10" на "Sheet1" 
і записувати знайдені посилання у файл "telegram_channels.txt".</p>

<h1>Журналювання</h1>
<p>Скрипт використовує бібліотеку logging для журналювання активності. 
Ви можете налаштувати рівень журналювання в скрипті, щоб керувати деталізацією журналів.</p>
</div>


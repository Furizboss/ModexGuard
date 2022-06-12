# 🛡️ ModerGuard

Дискорд бот для модерации серверов!
> Для работы программы требуеться Python 3, а также несклоько библиотек указаные в файле requirements.txt
# 📥 Установка
### Linux or Termux 
```sh
apt update && apt upgrade -y
apt install python
apt install git
git clone https://github.com/illia841/ModerGuard/
cd ModerGuard
pip install -r requirements.txt
```
### Windows
Установите релиз на странице проекта.

Также установите [Python(3)](https://www.python.org/downloads/), если он у вас не был установлен. 

После этого откройте командную строку из папки в которую вы скачали проект, и пропишите следующую команду:

```pip insall -r requirements.txt```

# ⚙️ Настройки
Настройки занимают всего пару минут!
Зайдите на [официальный портал разработчиков discord](https://discord.com/developers/applications), авторизуйтесь через свой дискорд аккаунт. Далее создайте новую программу (Aplication), а затем и бота. Скопируйте Application ID и Token во вкладке bot, затем вставьте в соответственные строки в файле config.py. Также в этом же файле вы можете установить префикс и имя бота!
# ⌨️ Использование 
### Linux or Termux 
Зайдите в папку в которую устанавливали проект, а далее введите команды ниже
```sh
cd ModerGuard
python3 bot.py
```

### Windows
В уже открытой командной строке пропишите следующую команду:
```sh
python bot.py
```

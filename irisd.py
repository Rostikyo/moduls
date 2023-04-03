# meta developer: @modwini
import json as JSON
import logging
from .. import loader, utils

logger = logging.getLogger(__name__)



def register(cb):
    cb(AutoIris())
@loader.tds
class AutoIris(loader.Module):
    """Автоматизация заражения Ирис"""
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "Id_chat",
                None,
                lambda: "chat_id",
                validator=loader.validators.Hidden(),
            ),
        )
    strings = {

        "name": "AutoIris",

        "not_reply": "<emoji document_id=5215273032553078755>❌</emoji> Нет реплая.",

        "not_args": "<emoji document_id=5215273032553078755>❌</emoji> Нет аргументов.",

        "nolink": "<emoji document_id=5197248832928227386>😢</emoji> Нет ссылки на жертву.",

        "hueta": "🤔 Что за хуета?",

        "r.save":
            "<emoji document_id=5212932275376759608>🦠</emoji> Жертва <b><code>{}</code></b> сохранена.\n"
            "<b>☣️ +{}{}</b> био-опыта.",
        "auto.save":
            "<emoji document_id=5212932275376759608>🦠</emoji> Жертва <b><code>{}</code></b> сохранена.\n"
            "<b>☣️ {}+{}</b> био-опыта.",
        "search":
            "<emoji document_id=5212932275376759608>✅</emoji> Жертва <code>{}</code> приносит:\n"
            "<b>☣️ +{} био-опыта.</b>\n"
            "📆 Дата: <i>{}</i>",

        "nf": "<emoji document_id=5215273032553078755>❎</emoji> Жертва не найдена.",

        "no_user": "<emoji document_id=5215273032553078755>❎</emoji> user {} don't exist.",

        "nous": "<emoji document_id=5215273032553078755>❎</emoji> Жертва или пользователь не существует.",

        "anf": "<emoji document_id=5215329773366025981>🤔</emoji> а кого искать?..",

        "aicmd":
            "<b>🥷🏻</b> <a href='tg://openmessage?user_id={}'>{}</a>\n"
            "<b>🆔:</b> <code>@{}</code>",
        "myid": "<b>My 🆔:</b> <code>@{}</code>",

        "guidedov":
            "<b>❔ Как использовать доверку:</b>\n"
            "\n<b>{0}</b>  <code>бей</code> | <code>кус</code>[ьайни] | <code>зарази</code>[тьть] "  # 🔽
            "| <code>еб</code>[ниажшь] | <code>уеб</code>[жиаошть] [1-10] (@id|@user|link)"
            "\n<b>{0}</b>  <code>цен</code>[ау] | <code>вч</code>[ек]  <i>(цена вакцины)</i>"
            "\n<b>{0}</b>  <code>вак</code>[цинау] | <code>леч</code>[ись] | <code>хи</code>[лльсяйинг] | <code>лек</code>[арство]"
            "\n<b>{0}</b>  <code>жертв</code>[ыау] | <code>еж</code>[ау]"
            "\n<b>{0}</b>  <code>бол</code>[езьни]"
            "\n<b>{0}</b>  <code>#лаб</code>[уа] | <code>%лаб</code>[уа] | <code>/лаб</code>[уа]"
            "\n<b>{0}</b>  <code>увед</code>[ыаомления]  <i>(+вирусы)</i>"
            "\n<b>{0}</b>  <code>-вирус</code>[ыа]\n\n"
            "〽️ <b>Апгрейд навыков:</b>\n"
            "<b>{0}  навык (0-5)</b> или\n<b>{0}  чек навык (0-5)</b>\n"
            "<i> Например: <b>{0} квалификация 4</b>\n"
            "(улучшает квалификацию учённых на 4 ур.)</i>\n\n"
            "〽️ <b>Доступные навыки:</b>\n"
            "🧪 Патоген (<b>пат</b> [огены])\n👨‍🔬 Квалификация (<b>квал</b> [ификацияула] | <b>разраб</b> [откау])\n"
            "🦠 Заразность (<b>зз</b> | <b>зараз</b> [аностьку])\n🛡 Иммунитет (<b>иммун</b> [итеткау])\n"
            "☠️ Летальность (<b>летал</b> [ьностькау])\n🕵️‍♂️ Безопасность (<b>сб</b> | <b>служб</b> [ау] | <b>безопасно</b> [сть])\n\n"
            "<b>🔎 Поиск жертв в зарлисте:</b>\n"
            "<b>{0}  з [ @id ]</b> или\n"
            "<b>{0}  з [ реплай ]</b>\n"
            "<i>см. <code>{1}config bio</code> для настройки.</i>",

        "dov":
            "<b>🌘 <code>{5}Дов сет</code> [ id|реплай ]</b> --- <b>Добавить/удалить саппорта.</b>\n"
            "<i>   ✨ Доверенные пользователи:</i>\n"
            "{0}\n\n"
            "<b>🌘 <code>{5}Дов ник</code> ник</b> --- <b>Установить ник</b>.\n <i>Например: <b><code>.Дов ник {3}</code></b></i>.\n"
            "<b>   🔰 Ваш ник: <code>{1}</code></b>\n\n"
            "<b>🌘 <code>{5}Дов пуск</code></b> --- <b>Запустить/Остановить</b>.\n"
            "<b>   {2}</b>\n"
            "<i><b>Доступ открыт к:</b></i>\n{4}",

        "zarlistHelp":
            "<b>Как пользоваться зарлистом:</b>\n\n"
            "<i>По умолчанию, все новые жертвы автоматически заносятся в зарлист,"
            " кроме, когда в сообщении ириса о заражении нету ссылки на жертву.</i>\n\n"
            "Шаблоны для добавления жертвы:\n"
            "{0}зар @id 1.1к\n"
            "жд @id 1.1к\n\n"
            "Чтобы найти жертву используй:\n"
            "{0}зар @id/реплай ф\n"
            "{1} з @id/реплай\n"
            "жл @id/реплай\n\n"
            "Также, инфу о бонусе с жертвы можно увидеть рядом с именем при использовании команды {0}б",

        "user_rm": "❎ Саппорт <b><code>{}</code></b> удалён.",

        "user_add": "<emoji document_id=5212932275376759608>✅</emoji> Саппорт <b><code>{}</code></b> добавлен!",

        "wrong_nick": "<b>📝 Введите ник.</b>",

        "nick_add": "🔰 Ник <b>{}</b> установлен!",

        "dov_start": "<b><emoji document_id=5212932275376759608>✅</emoji> Успешно запущено!</b>",

        "dov_stop": "<b>❎ Успешно остановлено.</b>",

        "dov.wrong_args":
            "<b><emoji document_id=5215273032553078755>❌</emoji> Неизвестный аргумент.</b>\n"
            "<i>📝 Введите <code>.дов</code> для просмотра команд.</i>",

        "wrong_id": "👀 Правильно 🆔 введи, дубина.",

        "ex": "❎ Исключение: <code>{}</code>",

        "wrong_ot-do": '<emoji document_id=5215273032553078755>❌</emoji> еблан, Используй <b>правильно</b> функцию "от-до".',

        "no_sargs": "<emoji document_id=5215273032553078755>❌</emoji> Не найдено совпадение в начале строк с аргументами.",

        "no_link": "<emoji document_id=5215273032553078755>❌</emoji> Ссылка не найдена.",

        "too_much_args": "<emoji document_id=5215273032553078755>❌</emoji> Кол-во аргументов <b>больше</b> одного, либо начинается <b>не</b> со знака <code>@</code>",

        "no_zar_reply": "<emoji document_id=5215273032553078755>❌</emoji> Нет реплая на сообщение ириса о заражении.",

        "empty_zar": "<emoji document_id=5215273032553078755>❌</emoji> Список заражений пуст.",

        "wrong_zar_reply": '<emoji document_id=5215273032553078755>❌</emoji> Реплай <b>не</b> на сообщение ириса о заражении "<b>...подверг заражению...</b>"',

        "wrong_cmd": "<emoji document_id=5215273032553078755>❌</emoji> Команда введена некорректно.",

        "empty_ex": "<emoji document_id=5215273032553078755>❌</emoji> Cписок исключений пуст.",

        "tids": "<b><emoji document_id=5212932275376759608>✅</emoji> Id'ы успешно извлечены.</b>",

        "tzar": "<emoji document_id=5212932275376759608>✅</emoji> Заражения завершены.",

        "clrex": "❎ Список исключений очищен.",

        "zar_rm": "❎ Жертва <b><code>{0}</code></b> {1}удалена.",

        "exadd": "✅ Пользователь <code>{}</code> в исключениях.",

        "exrm": "❎ Пользователь <code>{}</code> удален.",

        "clrzar": "✅ Зарлист <b>очищен</b>.",

        "guide":
            "<b>Помощь по модулю BioHelper:</b>\n\n"
            "<code>{0}biohelp дов</code> 👈 Помощь по доверке\n"
            "<code>{0}biohelp зарлист</code> 👈 Помощь по зарлисту"

    }

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def idcmd(self, message):
        """узнать айди чата"""
        chatt = str(message.chat_id)[1:]
        await message.reply(chatt)

    async def watche(self, message):
        """Интересно, почему он именно watche называется... 🤔"""
        gf = message.text
        id_chat = str(message.chat_id)[1:]
        if id_chat == self.config["Id_chat"]:
            if "🕵️‍♂️" in gf:
                exlist = self.db.get("NumMod", "exUsers")
                err = "1"
                json = JSON.loads(message.to_json())
                try:
                    for i in range(len(message.entities)):
                        try:
                            link = json["entities"][i]["url"]
                            if link.startswith('tg'):
                                users = '@' + link.split('=')[1]
                                if users in exlist:
                                    await message.reply(
                                        self.strings("ex").format(
                                            users
                                        )
                                    )
                                else:
                                    await message.reply(f'/заразить {users}')
                            elif link.startswith('https://t.me'):
                                a = '@' + str(link.split("/")[3])
                                if a in exlist:
                                    await message.reply(
                                        self.strings("ex").format(
                                            a
                                        )
                                    )
                                else:
                                    await message.reply(f'/заразить {a}')
                            else:
                                await message.reply(
                                    self.strings("hueta")
                                )
                        except Exception:
                            blayt = message.raw_text[
                                    json["entities"][i]["offset"]:json["entities"][i]["offset"] + json["entities"][i][
                                        "length"]]
                            if blayt in exlist:
                                await message.reply(
                                    self.strings("ex").format(
                                        blayt
                                    )
                                )
                            else:
                                await message.reply(f"/заразить {blayt}")
                        await asyncio.sleep(3.3)

                except TypeError:
                    err = "2"
                    await message.reply(
                        self.strings("hueta")
                    )
                if err != "2":
                    await message.delete()

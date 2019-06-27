class BotCommandsCommand:
    
    @property
    def message(self):
        return '——— Команды бота ———\n\n— Информационные команды:\n     1. `!commands` — выводит сообщение со списком команд бота и ссылку на соответствующий канал;\n     2.`!regulations` или `!rules` — выводит сообщение с частью правил сервера и ссылку на соответствующий канал;\n     3. `!roles` — выводит сообщение с частью ролей сервера и ссылку на соответствующий канал.\n\nПодробнее на канале `🤖-commands` (https://discord.gg/22vAjCh).'

    def sendResult(self):
        return self.message
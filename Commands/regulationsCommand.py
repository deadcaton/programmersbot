class RegulationsCommand:

    @property
    def message(self):
        return '——— Правила сервера ———\n\n— Запрещены:\n1. Оскорбления и унижения (везде):\n     1.1. Личности/лица, его чести, достоинства, окружения, интересов.\n2. Любое разжигание ненависти и схожих чувств;\n3. Мат/нецензурная брань в текстовых каналах/чатах в виде текстового сообщения.\n\nПодробнее на канале: `❗-regulations` (https://discord.gg/2HyYrpy).'

    def sendResult(self):
        return self.message
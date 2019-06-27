from CommandsF.botCommandsCommand import BotCommandsCommand
from CommandsF.regulationsCommand import RegulationsCommand
from CommandsF.rolesCommand import RolesCommand
from CommandsF.banCommand import BanCommand


botCommandsCommand = BotCommandsCommand()
regulationsCommand = RegulationsCommand()
rolesCommand = RolesCommand()
banCommand = BanCommand()


class Command:
    def __init__(self):
        self.commandsList = ['info', 'about', 'commands', 'rules', 'roles']

    def define(self, command):
        response = ''
        
        if command == '!commands':
            response = botCommandsCommand.sendResult()

        if command == '!rules' or command == '!regulations':
            response = regulationsCommand.sendResult()

        if command == '!roles':
            response = rolesCommand.sendResult()            

        if command.startswith('!ban'):
            print('')

        return response
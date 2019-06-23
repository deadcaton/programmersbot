from Commands.botCommandsCommand import BotCommandsCommand
from Commands.regulationsCommand import RegulationsCommand
from Commands.rolesCommand import RolesCommand
from Commands.banCommand import BanCommand


botCommandsCommand = BotCommandsCommand()
regulationsCommand = RegulationsCommand()
rolesCommand = RolesCommand()
banCommand = BanCommand()


class Router:
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
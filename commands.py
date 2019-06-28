from CommandsF.botCommandsCommand import BotCommandsCommand
from CommandsF.regulationsCommand import RegulationsCommand
from CommandsF.rolesCommand import RolesCommand
from CommandsF.banCommand import BanCommand


botCommandsCommand = BotCommandsCommand()
regulationsCommand = RegulationsCommand()
rolesCommand = RolesCommand()
banCommand = BanCommand()


class Commands:
    def __init__(self):
        self.commandsList = ['!info', '!about', '!commands', '!rules', '!roles']

    def define(self, userText):
        response = ''

        if userText == '!commands':
            response = botCommandsCommand.sendResult()
            return response
        
        if userText == '!rules':
            response = regulationsCommand.sendResult()
            return response
        
        if userText == '!roles':
            response = rolesCommand.sendResult()
            return response
        
        if userText.startswith('!ban'):
            print('')
            return response
                
        return response
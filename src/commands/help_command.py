import command_system


def help(request):
    ans = ""
    for command in command_system.command_list:
        ans += "{}\n".format(command.description)
    return ans


help_command = command_system.Command()

help_command.keys = [r'/start\s*', r'/help\s*']
help_command.description = '/help - print commands description'
help_command.process = help

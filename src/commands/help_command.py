import command_system


def help(request):
    ans = ""
    for command in command_system.command_list:
        ans += "{}: {}\n".format(command.keys[-1], command.description)
    return ans


help_command = command_system.Command()

help_command.keys = [r'/start\s*', r'/help\s*']
help_command.description = 'print help'
help_command.process = help

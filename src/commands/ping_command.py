import time
import command_system


def get_ping(request):
    return 'pong ({0} ms)'.format(int(1000 * (time.time() - request['message']['date'])))


ping_command = command_system.Command()

ping_command.keys = [r'/ping']
ping_command.description = '/ping - get ping'
ping_command.process = get_ping

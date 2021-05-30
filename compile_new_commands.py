new_commands = open('new_commands.txt', 'r', encoding='utf-8').read().split('\n')

for commands in new_commands:
    print('- command:')
    arg = commands.split('|')
    print('    input: ', arg[0])
    print('    entity: ', arg[1])
    print('    action: ', arg[2])

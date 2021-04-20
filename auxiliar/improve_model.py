

def write_nem_commands(text):
    inputs = open('inputs.txt', 'r', encoding='utf-8').read().split('\n')
    new_commands = open('new_commands.txt', 'r', encoding='utf-8').read().split('\n')

    if text not in inputs and text not in new_commands:
        fwrite = open('new_commands.txt', 'a', encoding='utf-8')

        fwrite.write(text + '\n')
        fwrite.close()
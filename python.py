from termcolor import colored

# Print the META-NET text in the center of the screen
meta_net_text = colored('META-NET', 'blue', attrs=['bold'])
print('\n'.join([' '*37]*10))
print(meta_net_text.center(80))
print('\n'.join([' '*37]*5))

# Set up method names with unique colors
methods = [
    colored('OVH', 'red', attrs=['bold']),
    colored('UDPPOWER', 'green', attrs=['bold']),
    colored('TCPBREAK', 'yellow', attrs=['bold']),
    colored('AZURE', 'cyan', attrs=['bold']),
    colored('AMAZONKILL', 'magenta', attrs=['bold']),
    colored('TS3REBOOT', 'red', attrs=['bold']),
    colored('UDP-ULTRA', 'green', attrs=['bold']),
    colored('OVH-GAME', 'yellow', attrs=['bold']),
    colored('OVH-DUMP', 'cyan', attrs=['bold']),
    colored('NULL-UDP', 'magenta', attrs=['bold'])
]

# Print method names in the center of the screen
for method in methods:
    print(method.center(80))
print('\n')

# Prompt user for input
host_ip = input('Enter the host IP: ')
host_port = input('Enter the host port: ')

# Print user input
print(f'Host IP: {host_ip}')
print(f'Host port: {host_port}')

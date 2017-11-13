class Website:
    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = queries


def read_website(string):
    string = string.split(' | ')
    try:
        queries = string[2].split(',')
        return Website(string[0], string[1], queries)
    except:
        return Website(string[0], string[1], '')

string = input()
while string != 'end':
    website = read_website(string)
    if len(website.queries) > 0:
        print('https://www.{}.{}/query?=[{}]'.format(website.host, website.domain, ']&['.join(website.queries)))
    else:
        print('https://www.{}.{}'.format(website.host, website.domain))
    string = input()

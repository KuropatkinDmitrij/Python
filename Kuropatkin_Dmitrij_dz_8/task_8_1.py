import re


def email_parse(email_address):
    func_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w*)', re.IGNORECASE)
    if not func_email.match(email_address):
        raise ValueError(f'wrong email: {email_address}')
    print(func_email.match(email_address).groupdict())


email_parse('dima@mail.ru')

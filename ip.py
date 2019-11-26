def ip_correct(ip):
    '''
    Проверяет IPv4 на корректность, аргумент должен быть строкой
    The address is checked for correctness, the argumet must be a string
    '''
    if len(ip.split('.')) == 4:
        return all([int(octet) in range(0,256) for octet in [octet.isdigit() for octet in ip.split('.')]]
    else:
        return False
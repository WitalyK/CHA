def ip_correct(ip):
    '''
    Проверяет IPv4 на корректность, аргумент должен быть строкой
    The address is checked for correctness, the argumet must be a string
    '''
    if len(ip.split('.')) == 4:
        return all([octet.isdigit() and (int(octet) in range(0, 256)) for octet in ip.split('.')])
    else:
        return False


#не запускать при импорте
if __name__ == "__main__":
    ip = input('Enter IP: ')
    if ip_correct(ip):
        print(ip)
    else:
        print('Error')
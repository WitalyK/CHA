ip = input('Input IP Address: ')
ip_correct = False
while not ip_correct:
    ipp = ip.split('.')
    if len(ipp) == 4:
        for i in ipp:
            ip_correct = True
            if not i.isdigit():
                ip_correct = False
                break
            elif not (0 <= int(i) <= 255):
                ip_correct = False
                break
    if ip_correct:
        ip1 = int(ip.split('.')[0])
        if 1 <= ip1 <= 223:
            print('unicast')
        elif 224 <= ip1 <= 239:
            print('multicast')
        elif ip == '255.255.255.255':
            print('local broadcast')
        elif ip == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
        continue
    print('Неправильный IP-адрес!')
    ip = input('Input IP Address: ')

#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    filename = sys.argv[1]

    try:
        with open(filename, 'r') as logfile:
            ip = []
            bytes = []
            status = []
            for line in logfile:
                split = line.split()
                ip.append(split[0])
                bytes.append(split[9])
                status.append(split[8])
    except OSError:
        print(filename, 'not existing')
        exit()
    except IndexError:
        print(filename, 'format not in CLF')
        exit()

    ip_list = []
    status_list = []

    ip_count = []
    status_count = []

    sort = int(
        input('Do you want to sort results by ip[1] or status[2]? [ANSWER]: '))
    if sort == 1:
        for match in (ip):
            if match not in ip_list:
                ip_list.append(match)
    if sort == 2:
        for match in (status):
            if match not in status_list:
                status_list.append(match)

    desired_output = int(input(
        'Choose Desired Output: [count] -o- [percentage] -o- [bytes]: '))
    if sort == 1:
        for match in ip_list:
            count = 0
            for ip_match in ip:
                if match == ip_match:
                    count += 1
                ip_count.append(count)

        if desired_output == 1:
            ip_count, ip_list = zip(
                *sorted(zip(ip_count, ip_list), reverse=True))
            for i in range(len(ip_list)):
                print('IP: ' + str(ip_list[i]) + ' count: ' + str(ip_count[i]))
        if desired_output == 2:
            ip_count, ip_list = zip(
                *sorted(zip(ip_count, ip_list), reverse=True))
            for i in range(len(ip_list)):
                print('IP: ' + str(ip_list[i]) + ' percentage: ' +
                      str(round(ip_count[i]/len(ip)*100, 2)) + '%')
        if desired_output == 3:
            cnt_bytes = []
            for v in range(len(ip_list)):
                tmp = 0
                for k in range(len(ip)):
                    if ip_list[v] == ip[k]:
                        if bytes[k] == '-':
                            bytes[k] = 0
                        tmp += int(bytes[k])
                    cnt_bytes.append(tmp)
                ip_list, cnt_bytes = zip(
                    *sorted(zip(cnt_bytes, ip_list), reverse=True))
                for line in range(len(ip_list)):
                    print('IP: ' + str(ip_list[line]) +
                          'bytes: ' + str(cnt_bytes[line]))
    
    if sort == 2:
        for match in status_list:
            count = 0
            for status_match in status:
                if match == status_match:
                    count += 1
                status_count.append(count)

        if desired_output == 1:
            status_count, status_list = zip(
                *sorted(zip(status_count, status_list), reverse=True))
            for i in range(len(status_list)):
                print('Status: ' + str(status_list[i]) + ' count: ' + str(status_count[i]))
        if desired_output == 2:
            status_count, status_list = zip(
                *sorted(zip(status_count, status_list), reverse=True))
            for i in range(len(status_list)):
                print('Status: ' + str(status_list[i]) + ' percentage: ' +
                      str(round(status_count[i]/len(status)*100, 2)) + '%')
        if desired_output == 3:
            cnt_bytes = []
            for v in range(len(status_list)):
                tmp = 0
                for k in range(len(status)):
                    if status_list[v] == status[k]:
                        if bytes[k] == '-':
                            bytes[k] = 0
                        tmp += int(bytes[k])
                    cnt_bytes.append(tmp)
                cnt_bytes, status_list = zip(
                    *sorted(zip(cnt_bytes, status_list), reverse=True))
                for line in range(len(status_list)):
                    print('Status: ' + str(status_list[line]) +
                          'bytes: ' + str(cnt_bytes[line]))

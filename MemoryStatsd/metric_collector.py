#!/usr/bin/python3

import os
import re
import socket

host = os.getenv('STATSD_HOST')
port = os.getenv('STATSD_PORT')


def get_pids():
    pids = []
    for i in os.listdir('/proc'):
        if i.isnumeric():
            pids.append(i)
    return pids


def get_process_name(pid):
    with open('/proc/{}/comm'.format(pid), 'r') as comm_file:
        process_name = comm_file.readline().strip('\n').split(' ')
    return process_name[0]


def get_memory_usage_in_bytes(pid):
    memory_usage = 0
    with open('/proc/{}/smaps'.format(pid), 'r') as smaps_file:
        smaps = smaps_file.readlines()
        for line in smaps:
            if 'Rss' in line:
                memory_usage += int(re.search(r'\d+', line).group(0))
    return memory_usage * 1024


def get_metrics():
    metrics = ''
    for i in get_pids():
        metric = "{}_{}_memory_usage:{}|{}\n".format(
            get_process_name(i), i, get_memory_usage_in_bytes(i), 'g')
        metrics += metric
    return metrics


def send_metrics(metrics, hostname, port):
    message = bytes(metrics, 'utf-8')
    statsd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    statsd.sendto(message, (host, int(port)))


# print(get_metrics())
send_metrics(get_metrics(), host, port)

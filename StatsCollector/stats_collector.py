#!/usr/local/bin/python3

import sys
import re

cgroup_prefix = sys.argv[1]
proc_path = sys.argv[2]
pid = sys.argv[3]


def save_state(cpu_total, cpu_process):
    print("{0} {1}".format(cpu_total, cpu_process), end='', file=sys.stderr)


def read_state():
    state = sys.stdin.read()
    return state


def get_cgroup_path(cgroup_type):
    with open('{}/{}/cgroup'.format(proc_path, pid), 'r') as cgroup_file:
        lines = cgroup_file.readlines()
        for line in lines:
            if cgroup_type in line:
                cgroup_suffix = re.search(r'\/.*', line).group(0)
                cgroup_path = "{}/{}{}".format(cgroup_prefix,
                                               cgroup_type, cgroup_suffix)
    return cgroup_path


def memory_limit_in_bytes(path):
    with open('{}/memory.limit_in_bytes'.format(path), 'r') as memory_limit_file:
        memory_limit = memory_limit_file.readline().strip('\n').split(' ')
    return int(memory_limit[0])


def cpu_limit(path):
    with open('{}/cpu.cfs_quota_us'.format(path), 'r') as cpu_quota_file:
        cpu_quota = int(cpu_quota_file.readline().strip('\n'))
    with open('{}/cpu.cfs_period_us'.format(path), 'r') as cpu_period_file:
        cpu_period = int(cpu_period_file.readline().strip('\n'))
    return cpu_quota / cpu_period


def get_cpu_core_count():
    with open('{}/cpuinfo'.format(proc_path), 'r') as cpuinfo_file:
        cpuinfo = cpuinfo_file.readlines()
        for line in cpuinfo:
            if 'cpu cores' in line:
                core_count = int(re.search(r'\d+', line).group(0))
    return core_count


def cpu_total():
    # total_cpu_usage1 = user + nice + system + idle;
    with open('{}/stat'.format(proc_path), 'r') as stat_file:
        stat = stat_file.readline().strip('\n').split(' ')
    return sum(map(int, stat[2:6]))


def cpu_process():
    # utime + stime
    with open('{}/{}/stat'.format(proc_path, pid), 'r') as pid_stat_file:
        pid_stat = pid_stat_file.readline().strip('\n').split(' ')
    return sum(map(int, pid_stat[13:15]))


def cpu_usage_in_percents(state):
    cpu_usage = 0
    total_after = cpu_total()
    process_after = cpu_process()
    save_state(total_after, process_after)
    if state:
        total_before = int(state[0])
        process_before = int(state[1])
        cpu_usage = 100 * get_cpu_core_count() * (process_after - process_before) / \
            (total_after - total_before) / cpu_limit(get_cgroup_path('cpu'))
    return cpu_usage


def memory_usage_in_bytes():
    memory_usage = 0
    with open('{}/{}/smaps'.format(proc_path, pid), 'r') as pid_smaps_file:
        smaps = pid_smaps_file.readlines()
        for line in smaps:
            if 'Pss' in line:
                memory_usage += int(re.search(r'\d+', line).group(0))
    return memory_usage * 1024


def memory_usage_in_percents(usage, limit):
    return usage / limit * 100


def output_metrics(cpu, memory):
    if cpu:
        print("cpu,pid={} value={}".format(pid, round(cpu)))
    print("memory,pid={} value={}".format(pid, round(memory)))


output_metrics(cpu_usage_in_percents(read_state()), memory_usage_in_percents(
    memory_usage_in_bytes(), memory_limit_in_bytes(get_cgroup_path('memory'))))

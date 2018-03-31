#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import psutil

##获取CPU信息
cpuCount = psutil.cpu_count() #CPU逻辑数量
print(cpuCount)

logicCpuCount = psutil.cpu_count(logical=False) #CPU物理核心
print(logicCpuCount)

##统计CPU的用户/系统/空闲时间
cpuTimes = psutil.cpu_times()
print(cpuTimes)

print('\n---------------华丽的分割线--------------\n')

##类似top命令的CPU使用率
for x in range(10):
    pass
    #print(psutil.cpu_percent(interval=1, percpu=True))

print('\n---------------华丽的分割线--------------\n')

##获取磁盘信息
diskInfo = psutil.disk_partitions() #磁盘分区信息
print(diskInfo)
diskUseInfo = psutil.disk_usage('/') #磁盘使用情况
print(diskUseInfo)
diskIOInfo = psutil.disk_io_counters() #磁盘IO
print(diskIOInfo)

print('\n---------------华丽的分割线--------------\n')

##获取网络信息
netInfo = psutil.net_io_counters() #获取网络读写字节/包的个数
print(netInfo)
netInterfaceInfo = psutil.net_if_addrs() #获取网络接口信息
print(netInterfaceInfo)
netInterfaceStats = psutil.net_if_stats() #获取网络接口状态
print(netInterfaceStats)
##会报错，psutil获取信息走系统接口，获取网络连接信息需要root权限，可以使用sudo运行
#netConnection = psutil.net_connections() #获取网络连接信息
#print(netConnection)

print('\n---------------华丽的分割线--------------\n')

##获取进程信息
pids = psutil.pids() #所有进程ID
print("所有进程ID：",pids)
p = psutil.Process(585) #获取指定进程ID=5008
print("进程名称：", p.name()) #进程名称
print("进程exe路径：", p.exe()) #进程exe路径
print("进程工作目录：", p.cwd()) #进程工作目录
print("进程启动的命令行：", p.cmdline()) #进程启动的命令行
print("父进程ID：", p.ppid) #父进程ID
print("父进程：", p.parent()) #父进程
print("子进程列表：", p.children) #子进程列表
print("进程状态：", p.status()) #进程状态
print("进程用户名：", p.username()) #进程用户名
print("进程创建时间：", p.create_time()) #进程创建时间
print("进程终端：", p.terminal()) #进程终端
print("进程使用的CPU时间：", p.cpu_times) #进程使用的CPU时间
print("进程使用的内存：", p.memory_info) #进程使用的内存
print("进程打开的文件：", p.open_files()) #进程打开的文件
print("进程相关网络连接：", p.connections()) #进程相关网络连接
print("进程的线程数量：", p.num_threads()) #进程的线程数量
#print("所有进程信息：",p.threads()) #所有线程信息
print("进程环境变量：", p.environ()) #进程环境变量
#print(p.terminate()) #结束进程
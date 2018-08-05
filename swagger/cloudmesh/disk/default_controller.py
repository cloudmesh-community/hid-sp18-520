import connexion
import six

from swagger_server.models.free import FREE  # noqa: E501
from swagger_server.models.total import TOTAL  # noqa: E501
from swagger_server.models.usage import USAGE  # noqa: E501
from swagger_server.models.used import USED  # noqa: E501
from swagger_server.models.mgmt_usage import MgmtUSAGE  # noqa: E501
from swagger_server.models.disk_io import DiskIO  # noqa: E501
from swagger_server import util
import os, platform, subprocess, re, psutil


def get_totdsk_name():
    st=os.statvfs('/')
    tot_info = str((st.f_blocks*st.f_frsize)/(1024*1024))+" MB"
    return (tot_info)

def get_usedsk_name():
    st=os.statvfs('/')
    use_info = str(((st.f_blocks-st.f_bfree)*st.f_frsize)/(1024*1024))+" MB"
    return (use_info)

def get_freedsk_name():
    st=os.statvfs('/')
    free_info = str((st.f_bavail*st.f_frsize)/(1024*1024))+" MB"
    return (free_info)

def get_diskusage_name():
    all_info = subprocess.check_output("df -h".split()).split("\n")
    return (all_info)

def get_diskmgmt_name():
        par_info = []
        disk_partitions = psutil.disk_partitions(all=False)
        for partition in disk_partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            device = {'device': partition.device,
                      'mountpoint': partition.mountpoint,
                      'fstype': partition.fstype,
                      'opts': partition.opts,
                      'percent': usage.percent
                      }
            par_info.append(device)
        return (par_info)

def get_diskio_counter():
    sdiskio = psutil.disk_io_counters()

    io_info = {
        'iostats': {
            'disks_read': sdiskio.read_bytes/(1024*1024),
            'disks_write': sdiskio.write_bytes/(1024*1024),
            'disks_read_count': sdiskio.read_count/(1024 * 1024),
            'disks_write_count': sdiskio.write_count/(1024 * 1024),
            'disks_read_time': sdiskio.read_time/1000,
            'disks_write_time': sdiskio.write_time/1000,
            'disks_busy_time': sdiskio.write_time/1000,
        }
    }
    return (io_info)

def dusage_get():  # noqa: E501
    """diskusage_get

    Returns disk space information of the hosting server # noqa: E501


    :rtype: USAGE
    """
    return USAGE(get_diskusage_name())


def free_dget():  # noqa: E501
    """free_disk_get

    Returns disk space information of the hosting server # noqa: E501


    :rtype: FREE
    """
    return FREE(get_freedsk_name())


def total_dget():  # noqa: E501
    """total_disk_get

    Returns disk space information of the hosting server # noqa: E501


    :rtype: TOTAL
    """
    return TOTAL(get_totdsk_name())


def used_dget():  # noqa: E501
    """used_disk_get

    Returns disk space information of the hosting server # noqa: E501


    :rtype: USED
    """
    return USED(get_usedsk_name())

def mgmtusage_get():  # noqa: E501
    """used_disk_get

    Returns disk space information of the hosting server # noqa: E501


    :rtype: MgmtUSAGE
    """
    return MgmtUSAGE(get_diskmgmt_name())

def diocounter_get():  # noqa: E501
    """used_disk_get

    Returns disk space information of the hosting server # noqa: E501


    :rtype: MgmtUSAGE
    """
    return DiskIO(get_diskio_counter())

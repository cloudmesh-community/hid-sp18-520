import connexion
import six

from swagger_server.models.free import FREE  # noqa: E501
from swagger_server.models.total import TOTAL  # noqa: E501
from swagger_server.models.usage import USAGE  # noqa: E501
from swagger_server.models.used import USED  # noqa: E501
from swagger_server import util
import os, platform, subprocess, re


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

def diskusage_get():  # noqa: E501
    """diskusage_get

    Returns disk space information of the hosting server # noqa: E501


    :rtype: USAGE
    """
    return USAGE(get_diskusage_name())#'do some magic!'


def free_disk_get():  # noqa: E501
    """free_disk_get

    Returns disk space information of the hosting server # noqa: E501


    :rtype: FREE
    """
    return FREE(get_freedsk_name())#'do some magic!'


def total_disk_get():  # noqa: E501
    """total_disk_get

    Returns disk space information of the hosting server # noqa: E501


    :rtype: TOTAL
    """
    return TOTAL(get_totdsk_name())#'do some magic!'


def used_disk_get():  # noqa: E501
    """used_disk_get

    Returns disk space information of the hosting server # noqa: E501


    :rtype: USED
    """
    return USED(get_usedsk_name())#'do some magic!'

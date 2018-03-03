import connexion
import six

from swagger_server.models.diskspace import DISKSPACE  # noqa: E501
from swagger_server import util

import os, platform, subprocess, re

def get_processor_name():
    all_info = subprocess.check_output("df -h".split()).split("\n")
    return (all_info)


def diskspace_get():  # noqa: E501
    """diskspace_get

    Returns disk space information of the hosting server # noqa: E501


    :rtype: DISKSPACE
    """
    return DISKSPACE(get_processor_name())

#'do some magic!'

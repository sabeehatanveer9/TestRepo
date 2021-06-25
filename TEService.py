#!/usr/bin/env python3
import json
import time
import netifaces
import netaddr
import socket
import os
import subprocess
import xmltodict
import sqlite3
from sqlite3 import Error
from urllib.request import urlopen
import requests
import sys
from getmac import get_mac_address
from datetime import datetime, timedelta
import TECommon
import urllib.request
import glob
import RPi.GPIO as GPIO

##########################################################################################
def clean_db_stats():
    try:
        TECommon.LogWrite("TEService-clean_db_stats:INFO:Start")
        ##################################################################################
        TECommon.DBExecuteOnlyQuery(TECommon.qryTEServiceCleanTBLogs)
        TECommon.DBExecuteOnlyQuery(TECommon.qryTEServiceCleanTBStats)
        ##################################################################################
        TECommon.LogWrite("TEService-clean_db_stats:INFO:End")
    except:
        TECommon.LogWrite("TEService-clean_db_stats:ERROR:" + TECommon.ErrorGet(sys))
##########################################################################################

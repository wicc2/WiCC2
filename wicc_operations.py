#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    WiCC (Wifi Cracking Camp)
    Second version of the original WiCC tool at https://github.com/pabloibiza/WiCC
    GUI tool for wireless pentesting on WEP and WPA/WPA2 networks.
    Project developed by Pablo Sanz Alguacil, Miguel Yanes Fernández.
"""


class Operation:
    """
    Enumeration class for the operations used in the notifys between View and Control
    """
    SELECT_INTERFACE = "Select interface"
    SELECT_NETWORK = "Select network"
    ATTACK_NETWORK = "Attack network"
    STOP_SCAN = "Stop scan"
    STOP_RUNNING = "Stop running"
    RANDOMIZE_MAC = "Randomize mac"
    CUSTOMIZE_MAC = "Customize mac"
    RESTORE_MAC = "Restore mac"
    SPOOF_MAC = "Spoof mac"
    SELECT_CUSTOM_WORDLIST = "Select custom wordlist"
    SCAN_OPTIONS = "Scan Options"
    CHECK_MAC = "Check mac"
    PATH_GENERATED_LISTS = "Path generated lists"
    GENERATE_LIST = "Generate list"
    SELECT_TEMPORARY_FILES_LOCATION = "Select temporary files location"
    START_SCAN_WPA = "Start scan wpa"
    SILENT_SCAN = "Silent Scan"
    OPEN_CRACKED = "open cracked"
    DOS_ATTACK = "start dos attack"
    DECRYPT_FILE = "decrypt file"


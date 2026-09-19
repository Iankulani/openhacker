#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   openHacker v1.0.0 - Requirements Checker                                   ║
║                                                                              ║
║   This script checks all dependencies and system tools required for          ║
║   openHacker to run at full capacity.                                        ║
║                                                                              ║
║   Author: Ian Carter Kulani, MSc                                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import sys
import os
import subprocess
import shutil
import platform
import importlib
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field

# =====================
# VERSION & METADATA
# =====================
VERSION = "1.0.0"
NAME = "openHacker Requirements Checker"
AUTHOR = "Ian Carter Kulani, MSc"

# =====================
# COLORS
# =====================
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'

# =====================
# DATA CLASSES
# =====================
@dataclass
class Dependency:
    name: str
    import_name: str
    pip_name: str
    required: bool = True
    category: str = "General"
    description: str = ""
    min_version: Optional[str] = None
    installed_version: Optional[str] = None
    status: str = "unknown"  # installed, missing, outdated, error

@dataclass
class SystemTool:
    name: str
    command: str
    required: bool = False
    category: str = "System"
    description: str = ""
    installed: bool = False
    version: Optional[str] = None
    path: Optional[str] = None

@dataclass
class CheckResult:
    dependencies: List[Dependency] = field(default_factory=list)
    tools: List[SystemTool] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

# =====================
# DEPENDENCY LIST
# =====================
def get_python_dependencies() -> List[Dependency]:
    """Define all Python dependencies for openHacker"""
    return [
        # Core Dependencies
        Dependency("requests", "requests", "requests", True, "Core", "HTTP library for Python", "2.31.0"),
        Dependency("urllib3", "urllib3", "urllib3", True, "Core", "HTTP client library", "2.0.0"),
        Dependency("certifi", "certifi", "certifi", True, "Core", "Python package for providing Mozilla's CA Bundle", "2023.7.22"),
        Dependency("charset-normalizer", "charset_normalizer", "charset-normalizer", True, "Core", "Universal charset detector", "3.3.0"),
        Dependency("idna", "idna", "idna", True, "Core", "Internationalized Domain Names in Applications", "3.4"),
        
        # System Information
        Dependency("psutil", "psutil", "psutil", True, "System", "Cross-platform system monitoring", "5.9.0"),
        
        # Terminal Colors
        Dependency("colorama", "colorama", "colorama", True, "Terminal", "Cross-platform colored terminal text", "0.4.6"),
        
        # Cryptography
        Dependency("cryptography", "cryptography", "cryptography", True, "Security", "Cryptographic recipes and primitives", "41.0.0"),
        Dependency("pycryptodome", "Crypto", "pycryptodome", False, "Security", "Cryptographic library for Python", "3.19.0"),
        
        # SSH
        Dependency("paramiko", "paramiko", "paramiko", True, "SSH", "SSH2 protocol library", "3.3.0"),
        Dependency("bcrypt", "bcrypt", "bcrypt", False, "SSH", "Modern password hashing", "4.1.0"),
        Dependency("pynacl", "nacl", "pynacl", False, "SSH", "Python binding to NaCl library", "1.5.0"),
        
        # Discord
        Dependency("discord.py", "discord", "discord.py", False, "Platform", "Discord API wrapper", "2.3.0"),
        
        # Telegram
        Dependency("telethon", "telethon", "telethon", False, "Platform", "Telegram client library", "1.34.0"),
        
        # Slack
        Dependency("slack-sdk", "slack_sdk", "slack-sdk", False, "Platform", "Slack SDK for Python", "3.23.0"),
        Dependency("slack-bolt", "slack_bolt", "slack-bolt", False, "Platform", "Slack Bolt framework", "1.18.0"),
        
        # Google Chat
        Dependency("google-auth", "google.auth", "google-auth", False, "Platform", "Google authentication library", "2.23.0"),
        Dependency("google-auth-oauthlib", "google_auth_oauthlib", "google-auth-oauthlib", False, "Platform", "Google OAuth library", "1.1.0"),
        Dependency("google-api-python-client", "googleapiclient", "google-api-python-client", False, "Platform", "Google API client", "2.100.0"),
        
        # Selenium (WhatsApp)
        Dependency("selenium", "selenium", "selenium", False, "Platform", "Browser automation", "4.15.0"),
        Dependency("webdriver-manager", "webdriver_manager", "webdriver-manager", False, "Platform", "WebDriver manager", "4.0.0"),
        
        # Web Framework
        Dependency("flask", "flask", "flask", True, "Web", "Web framework for Python", "3.0.0"),
        Dependency("flask-socketio", "flask_socketio", "flask-socketio", True, "Web", "Socket.IO integration for Flask", "5.3.0"),
        Dependency("flask-cors", "flask_cors", "flask-cors", True, "Web", "CORS support for Flask", "4.0.0"),
        Dependency("python-socketio", "socketio", "python-socketio", False, "Web", "Socket.IO server and client", "5.10.0"),
        Dependency("python-engineio", "engineio", "python-engineio", False, "Web", "Engine.IO server", "4.8.0"),
        Dependency("eventlet", "eventlet", "eventlet", False, "Web", "Concurrent networking library", "0.34.0"),
        Dependency("gunicorn", "gunicorn", "gunicorn", False, "Web", "WSGI HTTP Server", "21.2.0"),
        
        # Network & Packet Manipulation
        Dependency("scapy", "scapy", "scapy", True, "Network", "Packet manipulation library", "2.5.0"),
        
        # WHOIS
        Dependency("python-whois", "whois", "python-whois", False, "Network", "WHOIS lookup library", "0.8.0"),
        
        # QR Code
        Dependency("qrcode", "qrcode", "qrcode", False, "Utility", "QR code generator", "7.4.2"),
        Dependency("pillow", "PIL", "pillow", False, "Utility", "Python Imaging Library", "10.1.0"),
        
        # URL Shortening
        Dependency("pyshorteners", "pyshorteners", "pyshorteners", False, "Utility", "URL shortening library", "1.0.1"),
        
        # Data Visualization
        Dependency("matplotlib", "matplotlib", "matplotlib", False, "Graphics", "Plotting library", "3.8.0"),
        Dependency("seaborn", "seaborn", "seaborn", False, "Graphics", "Statistical data visualization", "0.13.0"),
        Dependency("numpy", "numpy", "numpy", False, "Graphics", "Numerical computing library", "1.26.0"),
        Dependency("pandas", "pandas", "pandas", False, "Graphics", "Data analysis library", "2.1.0"),
        
        # PDF Generation
        Dependency("reportlab", "reportlab", "reportlab", True, "Reporting", "PDF generation library", "4.0.0"),
        
        # Keylogger
        Dependency("pynput", "pynput", "pynput", True, "Keylogger", "Keyboard and mouse control", "1.7.6"),
        Dependency("pyautogui", "pyautogui", "pyautogui", False, "Keylogger", "GUI automation", "0.9.54"),
        Dependency("pyperclip", "pyperclip", "pyperclip", False, "Keylogger", "Clipboard access", "1.8.2"),
        Dependency("pygetwindow", "pygetwindow", "pygetwindow", False, "Keylogger", "Window management", "0.0.9"),
        
        # DNS
        Dependency("dnspython", "dns", "dnspython", True, "Network", "DNS toolkit for Python", "2.4.0"),
        
        # Web Scraping
        Dependency("beautifulsoup4", "bs4", "beautifulsoup4", False, "Scraping", "HTML/XML parser", "4.12.0"),
        Dependency("lxml", "lxml", "lxml", False, "Scraping", "XML/HTML processing", "4.9.0"),
        
        # Email
        Dependency("secure-smtplib", "smtplib", "secure-smtplib", False, "Email", "Secure SMTP library", "0.1.1"),
        
        # Data Processing
        Dependency("xmltodict", "xmltodict", "xmltodict", False, "Data", "XML to dict converter", "0.13.0"),
        Dependency("defusedxml", "defusedxml", "defusedxml", False, "Data", "XML bomb protection", "0.7.1"),
        
        # Progress Bars
        Dependency("tqdm", "tqdm", "tqdm", False, "Utility", "Progress bar library", "4.66.0"),
        
        # Date/Time
        Dependency("python-dateutil", "dateutil", "python-dateutil", False, "Utility", "Date utilities", "2.8.2"),
        Dependency("pytz", "pytz", "pytz", False, "Utility", "Timezone library", "2023.3"),
        
        # Environment
        Dependency("python-dotenv", "dotenv", "python-dotenv", False, "Utility", "Environment variable management", "1.0.0"),
        
        # Logging
        Dependency("loguru", "loguru", "loguru", False, "Utility", "Logging library", "0.7.0"),
        
        # HTTP/2
        Dependency("h2", "h2", "h2", False, "Network", "HTTP/2 protocol", "4.1.0"),
        Dependency("hpack", "hpack", "hpack", False, "Network", "HTTP/2 header encoding", "4.0.0"),
        Dependency("hyperframe", "hyperframe", "hyperframe", False, "Network", "HTTP/2 framing", "6.0.0"),
        
        # Async
        Dependency("aiohttp", "aiohttp", "aiohttp", False, "Network", "Async HTTP client/server", "3.9.0"),
        Dependency("aiofiles", "aiofiles", "aiofiles", False, "Utility", "Async file operations", "23.2.0"),
        
        # Validation
        Dependency("pydantic", "pydantic", "pydantic", False, "Utility", "Data validation", "2.5.0"),
        Dependency("email-validator", "email_validator", "email-validator", False, "Utility", "Email validation", "2.1.0"),
    ]

# =====================
# SYSTEM TOOLS LIST
# =====================
def get_system_tools() -> List[SystemTool]:
    """Define all system tools for openHacker"""
    return [
        # Network Tools
        SystemTool("ping", "ping", True, "Network", "Network connectivity test"),
        SystemTool("nmap", "nmap", True, "Network", "Network port scanner"),
        SystemTool("traceroute", "traceroute", True, "Network", "Network path tracing"),
        SystemTool("netcat", "nc", True, "Network", "Network Swiss army knife"),
        SystemTool("wget", "wget", True, "Network", "File downloader"),
        SystemTool("curl", "curl", True, "Network", "HTTP client"),
        SystemTool("dig", "dig", True, "Network", "DNS lookup utility"),
        SystemTool("whois", "whois", False, "Network", "Domain registration lookup"),
        SystemTool("fping", "fping", False, "Network", "Fast ping utility"),
        SystemTool("mtr", "mtr", False, "Network", "Network diagnostic tool"),
        SystemTool("tcpdump", "tcpdump", False, "Network", "Packet analyzer"),
        
        # Security Tools
        SystemTool("nikto", "nikto", False, "Security", "Web vulnerability scanner"),
        SystemTool("hashcat", "hashcat", False, "Security", "Password cracking tool"),
        SystemTool("john", "john", False, "Security", "John the Ripper password cracker"),
        SystemTool("hydra", "hydra", False, "Security", "Network login cracker"),
        SystemTool("sqlmap", "sqlmap", False, "Security", "SQL injection tool"),
        SystemTool("metasploit", "msfconsole", False, "Security", "Penetration testing framework"),
        SystemTool("aircrack-ng", "aircrack-ng", False, "Security", "WiFi security auditing"),
        SystemTool("ettercap", "ettercap", False, "Security", "Network sniffer"),
        
        # System Tools
        SystemTool("iptables", "iptables", False, "System", "Firewall management"),
        SystemTool("netstat", "netstat", False, "System", "Network statistics"),
        SystemTool("ss", "ss", False, "System", "Socket statistics"),
        SystemTool("arp", "arp", False, "System", "ARP table management"),
        SystemTool("ip", "ip", False, "System", "IP routing utilities"),
        SystemTool("ifconfig", "ifconfig", False, "System", "Network interface config"),
        SystemTool("route", "route", False, "System", "Routing table management"),
        
        # Container Tools
        SystemTool("docker", "docker", False, "Container", "Container platform"),
        SystemTool("docker-compose", "docker-compose", False, "Container", "Multi-container orchestration"),
        
        # Development Tools
        SystemTool("git", "git", False, "Development", "Version control"),
        SystemTool("python3", "python3", True, "Development", "Python interpreter"),
        SystemTool("pip3", "pip3", True, "Development", "Python package manager"),
        SystemTool("ssh", "ssh", False, "Development", "SSH client"),
        SystemTool("scp", "scp", False, "Development", "Secure copy"),
        SystemTool("ssh-keygen", "ssh-keygen", False, "Development", "SSH key generation"),
        
        # Communication
        SystemTool("signal-cli", "signal-cli", False, "Communication", "Signal messaging"),
        
        # Monitoring
        SystemTool("htop", "htop", False, "Monitoring", "Interactive process viewer"),
        SystemTool("iftop", "iftop", False, "Monitoring", "Network bandwidth monitor"),
        SystemTool("nethogs", "nethogs", False, "Monitoring", "Network usage monitor"),
        SystemTool("iotop", "iotop", False, "Monitoring", "Disk I/O monitor"),
    ]

# =====================
# CHECKER FUNCTIONS
# =====================
def print_header():
    """Print the header banner"""
    banner = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.CYAN}                                                                              {Colors.CYAN}║
║{Colors.WHITE}   🐙 openHacker v{VERSION} - Requirements Checker                               {Colors.WHITE}║
║{Colors.CYAN}                                                                              {Colors.CYAN}║
║{Colors.DIM}   Author: {AUTHOR}                                          {Colors.DIM}║
║{Colors.CYAN}                                                                              {Colors.CYAN}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

def print_section(title: str):
    """Print a section header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}  {title}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}\n")

def check_python_version() -> Tuple[bool, str]:
    """Check Python version"""
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    
    if version >= (3, 7):
        return True, version_str
    return False, version_str

def check_pip() -> Tuple[bool, str]:
    """Check if pip is available"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            version = result.stdout.strip().split()[1]
            return True, version
    except:
        pass
    return False, "not found"

def check_dependency(dep: Dependency) -> Dependency:
    """Check if a Python dependency is installed"""
    try:
        module = importlib.import_module(dep.import_name)
        
        # Try to get version
        if hasattr(module, '__version__'):
            dep.installed_version = module.__version__
        elif hasattr(module, 'VERSION'):
            dep.installed_version = module.VERSION
        elif hasattr(module, 'version'):
            dep.installed_version = module.version
        else:
            dep.installed_version = "unknown"
        
        dep.status = "installed"
        
        # Check version if specified
        if dep.min_version and dep.installed_version != "unknown":
            try:
                from packaging import version
                if version.parse(dep.installed_version) < version.parse(dep.min_version):
                    dep.status = "outdated"
            except:
                pass
        
    except ImportError:
        dep.status = "missing"
    except Exception as e:
        dep.status = "error"
        dep.installed_version = str(e)
    
    return dep

def check_system_tool(tool: SystemTool) -> SystemTool:
    """Check if a system tool is available"""
    path = shutil.which(tool.command)
    
    if path:
        tool.installed = True
        tool.path = path
        
        # Try to get version
        try:
            version_commands = [
                [tool.command, '--version'],
                [tool.command, '-V'],
                [tool.command, '-v'],
                [tool.command, 'version'],
            ]
            
            for cmd in version_commands:
                try:
                    result = subprocess.run(
                        cmd, capture_output=True, text=True, timeout=5
                    )
                    if result.returncode == 0 and result.stdout:
                        # Extract first line as version
                        version_line = result.stdout.strip().split('\n')[0]
                        tool.version = version_line[:50]
                        break
                except:
                    continue
        except:
            pass
    
    return tool

def get_install_command(dep: Dependency) -> str:
    """Get the pip install command for a dependency"""
    return f"pip install {dep.pip_name}"

def get_system_install_command(tool: SystemTool, os_type: str) -> str:
    """Get the system install command for a tool"""
    commands = {
        'linux': {
            'debian': f"sudo apt-get install -y {tool.name}",
            'ubuntu': f"sudo apt-get install -y {tool.name}",
            'fedora': f"sudo dnf install -y {tool.name}",
            'centos': f"sudo yum install -y {tool.name}",
            'arch': f"sudo pacman -S {tool.name}",
            'default': f"sudo apt-get install -y {tool.name}",
        },
        'darwin': {
            'default': f"brew install {tool.name}",
        },
        'windows': {
            'default': f"choco install {tool.name}",
        }
    }
    
    if os_type == 'linux':
        # Detect Linux distribution
        try:
            with open('/etc/os-release', 'r') as f:
                content = f.read().lower()
                if 'ubuntu' in content or 'debian' in content:
                    return commands['linux']['debian']
                elif 'fedora' in content:
                    return commands['linux']['fedora']
                elif 'centos' in content or 'rhel' in content:
                    return commands['linux']['centos']
                elif 'arch' in content:
                    return commands['linux']['arch']
        except:
            pass
        return commands['linux']['default']
    elif os_type == 'darwin':
        return commands['darwin']['default']
    elif os_type == 'windows':
        return commands['windows']['default']
    
    return f"Install {tool.name} manually"

def check_all_dependencies() -> CheckResult:
    """Check all dependencies"""
    result = CheckResult()
    dependencies = get_python_dependencies()
    
    print(f"{Colors.WHITE}Checking {len(dependencies)} Python dependencies...{Colors.RESET}\n")
    
    for dep in dependencies:
        dep = check_dependency(dep)
        result.dependencies.append(dep)
        
        if dep.status == "installed":
            status_icon = f"{Colors.GREEN}✅{Colors.RESET}"
            version_info = f" ({dep.installed_version})" if dep.installed_version != "unknown" else ""
        elif dep.status == "outdated":
            status_icon = f"{Colors.YELLOW}⚠️{Colors.RESET}"
            version_info = f" (installed: {dep.installed_version}, required: {dep.min_version})"
        elif dep.status == "missing":
            status_icon = f"{Colors.RED}❌{Colors.RESET}"
            version_info = ""
            if dep.required:
                result.errors.append(f"Missing required dependency: {dep.name}")
            else:
                result.warnings.append(f"Missing optional dependency: {dep.name}")
        else:
            status_icon = f"{Colors.RED}🔴{Colors.RESET}"
            version_info = f" ({dep.installed_version})"
            result.errors.append(f"Error checking {dep.name}: {dep.installed_version}")
        
        req_marker = f"{Colors.RED}[REQUIRED]{Colors.RESET}" if dep.required else f"{Colors.DIM}[optional]{Colors.RESET}"
        print(f"  {status_icon} {dep.name:<30} {req_marker}{version_info}")
    
    return result

def check_all_tools() -> CheckResult:
    """Check all system tools"""
    result = CheckResult()
    tools = get_system_tools()
    
    print(f"\n{Colors.WHITE}Checking {len(tools)} system tools...{Colors.RESET}\n")
    
    for tool in tools:
        tool = check_system_tool(tool)
        result.tools.append(tool)
        
        if tool.installed:
            status_icon = f"{Colors.GREEN}✅{Colors.RESET}"
            version_info = f" ({tool.version[:40]})" if tool.version else ""
        else:
            status_icon = f"{Colors.RED}❌{Colors.RESET}"
            version_info = ""
            if tool.required:
                result.errors.append(f"Missing required tool: {tool.name}")
            else:
                result.warnings.append(f"Missing optional tool: {tool.name}")
        
        req_marker = f"{Colors.RED}[REQUIRED]{Colors.RESET}" if tool.required else f"{Colors.DIM}[optional]{Colors.RESET}"
        print(f"  {status_icon} {tool.name:<25} {req_marker}{version_info}")
    
    return result

def print_summary(result: CheckResult):
    """Print a summary of the check results"""
    print_section("📊 SUMMARY")
    
    # Python dependencies summary
    installed_deps = sum(1 for d in result.dependencies if d.status == "installed")
    outdated_deps = sum(1 for d in result.dependencies if d.status == "outdated")
    missing_deps = sum(1 for d in result.dependencies if d.status == "missing")
    required_missing_deps = sum(1 for d in result.dependencies if d.status == "missing" and d.required)
    
    print(f"{Colors.BOLD}Python Dependencies:{Colors.RESET}")
    print(f"  {Colors.GREEN}✅ Installed:{Colors.RESET} {installed_deps}")
    print(f"  {Colors.YELLOW}⚠️ Outdated:{Colors.RESET}  {outdated_deps}")
    print(f"  {Colors.RED}❌ Missing:{Colors.RESET}   {missing_deps} ({required_missing_deps} required)")
    
    # System tools summary
    installed_tools = sum(1 for t in result.tools if t.installed)
    missing_tools = sum(1 for t in result.tools if not t.installed)
    required_missing_tools = sum(1 for t in result.tools if not t.installed and t.required)
    
    print(f"\n{Colors.BOLD}System Tools:{Colors.RESET}")
    print(f"  {Colors.GREEN}✅ Installed:{Colors.RESET} {installed_tools}")
    print(f"  {Colors.RED}❌ Missing:{Colors.RESET}   {missing_tools} ({required_missing_tools} required)")
    
    # Overall status
    print(f"\n{Colors.BOLD}Overall Status:{Colors.RESET}")
    if required_missing_deps == 0 and required_missing_tools == 0:
        print(f"  {Colors.GREEN}🎉 All required dependencies and tools are installed!{Colors.RESET}")
        print(f"  {Colors.GREEN}✅ openHacker is ready to run!{Colors.RESET}")
    else:
        print(f"  {Colors.RED}❌ {required_missing_deps} required Python dependencies missing{Colors.RESET}")
        print(f"  {Colors.RED}❌ {required_missing_tools} required system tools missing{Colors.RESET}")
        print(f"  {Colors.YELLOW}⚠️ Please install the missing requirements before running openHacker{Colors.RESET}")

def print_install_instructions(result: CheckResult):
    """Print installation instructions for missing dependencies"""
    os_type = platform.system().lower()
    
    # Missing Python dependencies
    missing_deps = [d for d in result.dependencies if d.status == "missing"]
    outdated_deps = [d for d in result.dependencies if d.status == "outdated"]
    
    if missing_deps or outdated_deps:
        print_section("📦 PYTHON DEPENDENCIES INSTALLATION")
        
        if missing_deps:
            print(f"{Colors.YELLOW}Missing Python packages:{Colors.RESET}")
            pip_names = [d.pip_name for d in missing_deps]
            print(f"\n  {Colors.CYAN}pip install {' '.join(pip_names)}{Colors.RESET}\n")
        
        if outdated_deps:
            print(f"{Colors.YELLOW}Outdated Python packages (upgrade recommended):{Colors.RESET}")
            pip_names = [d.pip_name for d in outdated_deps]
            print(f"\n  {Colors.CYAN}pip install --upgrade {' '.join(pip_names)}{Colors.RESET}\n")
        
        print(f"{Colors.DIM}Or install all requirements at once:{Colors.RESET}")
        print(f"  {Colors.CYAN}pip install -r requirements.txt{Colors.RESET}\n")
    
    # Missing system tools
    missing_tools = [t for t in result.tools if not t.installed and t.required]
    
    if missing_tools:
        print_section("🔧 SYSTEM TOOLS INSTALLATION")
        
        for tool in missing_tools:
            cmd = get_system_install_command(tool, os_type)
            print(f"  {Colors.YELLOW}{tool.name}{Colors.RESET}: {Colors.CYAN}{cmd}{Colors.RESET}")
        
        print()
    
    # Optional tools
    optional_missing = [t for t in result.tools if not t.installed and not t.required]
    if optional_missing:
        print_section("💡 OPTIONAL TOOLS (Recommended)")
        
        for tool in optional_missing[:10]:
            cmd = get_system_install_command(tool, os_type)
            print(f"  {Colors.DIM}{tool.name}{Colors.RESET}: {Colors.CYAN}{cmd}{Colors.RESET}")
        
        if len(optional_missing) > 10:
            print(f"  ... and {len(optional_missing) - 10} more")
        print()

def print_platform_info():
    """Print platform information"""
    print_section("💻 PLATFORM INFORMATION")
    
    print(f"  {Colors.BOLD}OS:{Colors.RESET} {platform.system()} {platform.release()}")
    print(f"  {Colors.BOLD}Architecture:{Colors.RESET} {platform.machine()}")
    print(f"  {Colors.BOLD}Processor:{Colors.RESET} {platform.processor()}")
    print(f"  {Colors.BOLD}Python:{Colors.RESET} {sys.version}")
    print(f"  {Colors.BOLD}Python Path:{Colors.RESET} {sys.executable}")
    print(f"  {Colors.BOLD}Working Directory:{Colors.RESET} {os.getcwd()}")
    
    # Check if running as admin/root
    is_admin = False
    if platform.system().lower() == 'linux':
        is_admin = os.geteuid() == 0
    elif platform.system().lower() == 'windows':
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            pass
    elif platform.system().lower() == 'darwin':
        is_admin = os.geteuid() == 0
    
    admin_status = f"{Colors.GREEN}Yes{Colors.RESET}" if is_admin else f"{Colors.YELLOW}No{Colors.RESET}"
    print(f"  {Colors.BOLD}Admin/Root:{Colors.RESET} {admin_status}")
    
    if not is_admin:
        print(f"\n  {Colors.YELLOW}⚠️ Some features (firewall, raw sockets) require admin/root privileges{Colors.RESET}")

def export_report(result: CheckResult, filename: str = "requirements_report.json"):
    """Export the check results to a JSON file"""
    import json
    
    report = {
        'timestamp': __import__('datetime').datetime.now().isoformat(),
        'version': VERSION,
        'platform': {
            'os': platform.system(),
            'release': platform.release(),
            'machine': platform.machine(),
            'python': sys.version,
        },
        'dependencies': [
            {
                'name': d.name,
                'pip_name': d.pip_name,
                'required': d.required,
                'category': d.category,
                'status': d.status,
                'installed_version': d.installed_version,
                'min_version': d.min_version,
            }
            for d in result.dependencies
        ],
        'tools': [
            {
                'name': t.name,
                'command': t.command,
                'required': t.required,
                'category': t.category,
                'installed': t.installed,
                'version': t.version,
                'path': t.path,
            }
            for t in result.tools
        ],
        'errors': result.errors,
        'warnings': result.warnings,
        'summary': {
            'dependencies_installed': sum(1 for d in result.dependencies if d.status == 'installed'),
            'dependencies_missing': sum(1 for d in result.dependencies if d.status == 'missing'),
            'dependencies_outdated': sum(1 for d in result.dependencies if d.status == 'outdated'),
            'tools_installed': sum(1 for t in result.tools if t.installed),
            'tools_missing': sum(1 for t in result.tools if not t.installed),
        }
    }
    
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n{Colors.SUCCESS}📄 Report exported to: {filename}{Colors.RESET}")

def generate_install_script(result: CheckResult, filename: str = "install_requirements.sh"):
    """Generate an installation script for missing requirements"""
    os_type = platform.system().lower()
    
    script_lines = [
        "#!/bin/bash",
        "# openHacker Requirements Installation Script",
        f"# Generated: {__import__('datetime').datetime.now().isoformat()}",
        "",
        "set -e",
        "",
        "echo '🐙 Installing openHacker requirements...'",
        "",
    ]
    
    # Python dependencies
    missing_deps = [d for d in result.dependencies if d.status == "missing"]
    if missing_deps:
        script_lines.append("# Install missing Python packages")
        pip_names = ' '.join([d.pip_name for d in missing_deps])
        script_lines.append(f"pip3 install {pip_names}")
        script_lines.append("")
    
    # System tools
    missing_tools = [t for t in result.tools if not t.installed and t.required]
    if missing_tools:
        script_lines.append("# Install missing system tools")
        for tool in missing_tools:
            cmd = get_system_install_command(tool, os_type)
            script_lines.append(cmd)
        script_lines.append("")
    
    script_lines.extend([
        "echo '✅ Installation complete!'",
        "echo '🐙 You can now run: python3 openhacker.py'",
    ])
    
    with open(filename, 'w') as f:
        f.write('\n'.join(script_lines))
    
    os.chmod(filename, 0o755)
    print(f"{Colors.SUCCESS}📜 Installation script generated: {filename}{Colors.RESET}")

def check_network_connectivity() -> bool:
    """Check network connectivity"""
    print_section("🌐 NETWORK CONNECTIVITY")
    
    import socket
    
    hosts = [
        ("8.8.8.8", 53, "Google DNS"),
        ("1.1.1.1", 53, "Cloudflare DNS"),
        ("github.com", 443, "GitHub"),
        ("pypi.org", 443, "PyPI"),
    ]
    
    all_ok = True
    for host, port, name in hosts:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((host, port))
            sock.close()
            
            if result == 0:
                print(f"  {Colors.GREEN}✅{Colors.RESET} {name} ({host}:{port})")
            else:
                print(f"  {Colors.RED}❌{Colors.RESET} {name} ({host}:{port})")
                all_ok = False
        except Exception as e:
            print(f"  {Colors.RED}❌{Colors.RESET} {name} ({host}:{port}) - {e}")
            all_ok = False
    
    return all_ok

def main():
    """Main entry point"""
    print_header()
    
    # Parse arguments
    import argparse
    parser = argparse.ArgumentParser(description='openHacker Requirements Checker')
    parser.add_argument('--json', '-j', action='store_true', help='Export report as JSON')
    parser.add_argument('--script', '-s', action='store_true', help='Generate install script')
    parser.add_argument('--quiet', '-q', action='store_true', help='Quiet mode')
    args = parser.parse_args()
    
    if not args.quiet:
        print_platform_info()
    
    # Check Python version
    print_section("🐍 PYTHON VERSION")
    py_ok, py_version = check_python_version()
    if py_ok:
        print(f"  {Colors.GREEN}✅ Python {py_version}{Colors.RESET}")
    else:
        print(f"  {Colors.RED}❌ Python {py_version} (3.7+ required){Colors.RESET}")
        sys.exit(1)
    
    # Check pip
    pip_ok, pip_version = check_pip()
    if pip_ok:
        print(f"  {Colors.GREEN}✅ pip {pip_version}{Colors.RESET}")
    else:
        print(f"  {Colors.RED}❌ pip not found{Colors.RESET}")
    
    # Check network connectivity
    if not args.quiet:
        check_network_connectivity()
    
    # Check Python dependencies
    print_section("📦 PYTHON DEPENDENCIES")
    dep_result = check_all_dependencies()
    
    # Check system tools
    print_section("🔧 SYSTEM TOOLS")
    tool_result = check_all_tools()
    
    # Combine results
    result = CheckResult(
        dependencies=dep_result.dependencies,
        tools=tool_result.tools,
        errors=dep_result.errors + tool_result.errors,
        warnings=dep_result.warnings + tool_result.warnings,
    )
    
    # Print summary
    print_summary(result)
    
    # Print install instructions
    print_install_instructions(result)
    
    # Export report if requested
    if args.json:
        export_report(result)
    
    # Generate install script if requested
    if args.script:
        generate_install_script(result)
    
    # Final status
    required_missing_deps = sum(1 for d in result.dependencies if d.status == "missing" and d.required)
    required_missing_tools = sum(1 for t in result.tools if not t.installed and t.required)
    
    if required_missing_deps == 0 and required_missing_tools == 0:
        print(f"\n{Colors.GREEN}{'='*60}{Colors.RESET}")
        print(f"{Colors.GREEN}  🎉 SUCCESS: All requirements met!{Colors.RESET}")
        print(f"{Colors.GREEN}  🐙 openHacker is ready to run!{Colors.RESET}")
        print(f"{Colors.GREEN}{'='*60}{Colors.RESET}\n")
        sys.exit(0)
    else:
        print(f"\n{Colors.RED}{'='*60}{Colors.RESET}")
        print(f"{Colors.RED}  ❌ FAILED: Missing required components{Colors.RESET}")
        print(f"{Colors.RED}  ⚠️ Please install missing requirements{Colors.RESET}")
        print(f"{Colors.RED}{'='*60}{Colors.RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()

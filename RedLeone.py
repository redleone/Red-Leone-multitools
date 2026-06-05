# ─────────────────────────────────────────────────────────────────
# REDLEONE MULTITOOL – INTERFACE ADAPTATIVE – NAV CENTRÉE
# ─────────────────────────────────────────────────────────────────
from Program.Config.Config import *
from Program.Config.Util import *

try:
    import webbrowser
    import re
    import pyzipper
    import shutil
except Exception as e:
    ErrorModule(e)

# ───── PALETTE ─────
C_RESET  = '\033[0m'
C_RED    = '\033[91m'
C_GREEN  = '\033[92m'
C_YELLOW = '\033[93m'
C_BLUE   = '\033[94m'
C_CYAN   = '\033[96m'
C_WHITE  = '\033[97m'
C_DIM    = '\033[2m'
C_BOLD   = '\033[1m'

# ───── STYLES ─────
BORDER = C_DIM + C_CYAN
TITLE  = C_BOLD + C_YELLOW
NUM    = C_BLUE
TXT    = C_WHITE
NAV    = C_YELLOW
PROMPT = C_GREEN

# ───── CARACTÈRES DE CADRE ─────
HL = '─' ; VL = '│' ; HB = '━'
TL = '┌' ; TR = '┐' ; BL = '└' ; BR = '┘'
DH = '┬' ; UH = '┴' ; LH = '├' ; RH = '┤' ; CH = '┼'

def get_term_width():
    return shutil.get_terminal_size().columns

def vis_len(s):
    return len(re.sub(r'\x1b\[[0-9;]*m', '', s))

def pad(s, width):
    need = width - vis_len(s)
    return s + ' ' * max(0, need)

def fmt_option(num, txt, col_w):
    raw = f"{NUM}[{num}]{C_RESET} {C_DIM}•{C_RESET} {TXT}{txt}"
    if vis_len(raw) <= col_w:
        return raw
    result = ''
    cur_len = 0
    i = 0
    while i < len(raw) and cur_len < col_w - 2:
        if raw[i] == '\033':
            j = raw.index('m', i)
            result += raw[i:j+1]
            i = j + 1
        else:
            result += raw[i]
            cur_len += 1
            i += 1
    return result + '…'

# ───── DÉFINITION DES OPTIONS ─────
OPT_NET = [
    ("01","Website Vulnerability Scanner"),
    ("02","Website Info Scanner"),
    ("03","Website Url Scanner"),
    ("04","Ip Scanner"),
    ("05","Ip Port Scanner"),
    ("06","Ip Pinger"),
]
OPT_OSINT = [
    ("07","D0x Create"),
    ("08","D0x Tracker"),
    ("09","Get Image Exif"),
    ("10","Google Dorking"),
    ("11","Username Tracker"),
    ("12","Email Tracker"),
    ("13","Email Lookup"),
    ("14","Phone Number Lookup"),
    ("15","Ip Lookup"),
    ("16","Instagram Account"),
]
OPT_UTILS = [
    ("17","Phishing Attack"),
    ("18","Password Zip Cracked Attack"),
    ("19","Password Hash Decrypted Attack"),
    ("20","Password Hash Encrypted"),
    ("21","Search In DataBase"),
    ("22","Dark Web Links"),
    ("23","Ip Generator"),
    ("24","DDoS Attack"),
    ("25","File Recovery"),
]
OPT_BUILD = [
    ("26","Virus Builder"),
    ("27","Keylogger"),
]
OPT_ROBLOX = [
    ("28","Roblox Cookie Login"),
    ("29","Roblox Cookie Info"),
    ("30","Roblox Id Info"),
    ("31","Roblox User Info"),
]
OPT_DISCORD = [
    ("32","Discord Token Nuker"),
    ("33","Discord Token Info"),
    ("34","Discord Token Joiner"),
    ("35","Discord Token Leaver"),
    ("36","Discord Token Login"),
    ("37","Discord Token To Id And Brute"),
    ("38","Discord Token Server Raid"),
    ("39","Discord Token Spammer"),
    ("40","Discord Token Delete Friends"),
    ("41","Discord Token Block Friends"),
    ("42","Discord Token Mass Dm"),
    ("43","Discord Token Delete Dm"),
    ("44","Discord Token Status Changer"),
    ("45","Discord Token Language Changer"),
    ("46","Discord Token House Changer"),
    ("47","Discord Token Theme Changer"),
    ("48","Discord Token Generator"),
    ("49","Discord Bot Server Nuker"),
    ("50","Discord Bot Invite To Id"),
    ("51","Discord Server Info"),
    ("52","Discord Nitro Generator"),
    ("53","Discord Webhook Info"),
    ("54","Discord Webhook Delete"),
    ("55","Discord Webhook Spammer"),
    ("56","Discord Webhook Generator"),
    ("57","Server Cloner"),
]

OPT_DISC_A = OPT_DISCORD[:12]   # 32-43
OPT_DISC_B = OPT_DISCORD[12:]   # 44-57

# ───── CONSTRUCTION DU MENU ─────
def build_menu(cols, titles, col_w):
    ncols = len(cols)
    max_rows = max(len(c) for c in cols)
    padded = [c + [("","")] * (max_rows - len(c)) for c in cols]

    def line(cells, l, m, r):
        parts = [pad(c, col_w) for c in cells]
        return f"{BORDER}{l}{C_RESET}" + f"{BORDER}{m}{C_RESET}".join(parts) + f"{BORDER}{r}{C_RESET}"

    top = BORDER + TL + HL*col_w
    for _ in range(1, ncols): top += DH + HL*col_w
    top += TR + C_RESET

    header = line([f"{TITLE}{t.center(col_w)}{C_RESET}" for t in titles], VL, VL, VL)
    sep = BORDER + LH + HB*col_w
    for _ in range(1, ncols): sep += CH + HB*col_w
    sep += RH + C_RESET

    rows = []
    for r in range(max_rows):
        cells = []
        for c in range(ncols):
            num, txt = padded[c][r]
            cells.append(fmt_option(num, txt, col_w) if num else '')
        rows.append(line(cells, VL, VL, VL))

    bottom = BORDER + BL + HL*col_w
    for _ in range(1, ncols): bottom += UH + HL*col_w
    bottom += BR + C_RESET

    return '\n'.join([top, header, sep] + rows + [bottom])

def center_block(text):
    """Centre un bloc de texte dans la largeur du terminal."""
    term_w = get_term_width()
    lines = text.split('\n')
    max_line = max(vis_len(line) for line in lines)
    if max_line >= term_w:
        return text
    padding = (term_w - max_line) // 2
    return '\n'.join(' ' * padding + line for line in lines)

COL_W_3 = 30
COL_W_2 = 48

menu1 = center_block(build_menu([OPT_NET, OPT_OSINT, OPT_UTILS],
                                [" Network Scanner ", " Osint ", " Utilities "],
                                COL_W_3))
menu2 = center_block(build_menu([OPT_BUILD, OPT_ROBLOX],
                                [" Virus Builder ", " Roblox "],
                                COL_W_2))
menu3 = center_block(build_menu([OPT_DISC_A, OPT_DISC_B],
                                [" Discord (1/2) ", " Discord (2/2) "],
                                COL_W_2))

# ───── BARRE DE NAVIGATION ─────
NAV_BACK  = f"{NAV}[B]{C_RESET} Back"
NAV_NEXT  = f"{NAV}[N]{C_RESET} Next"
NAV_INFO  = f"{NAV}[I]{C_RESET} Info"
NAV_SITE  = f"{NAV}[S]{C_RESET} Site"

def nav_bar(page):
    items = [NAV_INFO, NAV_SITE]
    if page in ("1","2"): items.append(NAV_NEXT)
    if page in ("2","3"): items.append(NAV_BACK)
    return "   ".join(items)

# ───── BANNIÈRE ASCII + LIEN CLIQUABLE ─────
BANNER = f"""
 
			██████╗ ███████╗██████╗     ██╗     ███████╗ ██████╗ ███╗   ██╗███████╗
			██╔══██╗██╔════╝██╔══██╗    ██║     ██╔════╝██╔═══██╗████╗  ██║██╔════╝
			██████╔╝█████╗  ██║  ██║    ██║     █████╗  ██║   ██║██╔██╗ ██║█████╗  
			██╔══██╗██╔══╝  ██║  ██║    ██║     ██╔══╝  ██║   ██║██║╚██╗██║██╔══╝  
			██║  ██║███████╗██████╔╝    ███████╗███████╗╚██████╔╝██║ ╚████║███████╗
			╚═╝  ╚═╝╚══════╝╚═════╝     ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                                       
                                                      https://{github_tool}                 
                                                                       
                                                                                                                                                                                                                   
                                                                                                                
                                                                                                                                            {white} 		 
"""

# ───── GESTION DES PAGES (sans popups) ─────
def Update():
    popup_version = ""
    try:
        new_version = re.search(r'version_tool\s*=\s*"([^"]+)"', requests.get(url_config).text).group(1)
        if new_version != version_tool:
            webbrowser.open(f"https://{github_tool}")
            colorama.init()
            input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Nouvelle version : {C_WHITE}{version_tool}{C_RED} -> {C_WHITE}{new_version}")
            popup_version = f"{C_RED}New Version: {C_WHITE}{version_tool}{C_RED} -> {C_WHITE}{new_version}"
            colorama.deinit()
            Clear()
    except: pass
    return popup_version

menu_path = os.path.join(tool_path, "Program", "Config", "Menu.txt")

def Menu():
    popup_version = Update()
    try:
        with open(menu_path, "r") as f:
            page = f.read().strip()
    except:
        page = "1"
    menus = {"1": menu1, "2": menu2, "3": menu3}
    current = menus.get(page, menu1)
    nav_raw = nav_bar(page)
    nav_centered = center_block(nav_raw)   # Décolle du bord
    full = f"{popup_version}\n{BANNER}\n{nav_centered}\n\n{current}\n"
    return full, page

# ───── BOUCLE PRINCIPALE ─────
while True:
    try:
        Clear()
        banner, page = Menu()
        Title(f"RedLeone - Page {page}")
        Slow(MainColor(banner))

        prompt = f" {BORDER}┌─[{C_WHITE}{username_pc}@{os_name}{BORDER}]─[{PROMPT}page-{page}{BORDER}]\n └─{C_WHITE}$ {C_RESET}"
        choice = input(MainColor(prompt)).strip()

        if choice.lower() in ('n','next'):
            nxt = {"1":"2","2":"3","3":"1"}.get(page,"1")
            with open(menu_path,"w") as f: f.write(nxt)
            continue
        elif choice.lower() in ('b','back'):
            bck = {"2":"1","3":"2"}.get(page,"1")
            with open(menu_path,"w") as f: f.write(bck)
            continue
        elif choice.lower() in ('i','info'):
            StartProgram("Info.py")
            continue
        elif choice.lower() in ('s','site'):
            StartProgram("Site.py")
            continue

        # Mapping global des scripts
        all_opts = {}
        for lst in [OPT_NET, OPT_OSINT, OPT_UTILS, OPT_BUILD, OPT_ROBLOX, OPT_DISCORD]:
            for num, name in lst:
                all_opts[num] = name
        if choice in all_opts:
            StartProgram(f"{all_opts[choice].replace(' ', '-')}.py")
        elif '0' + choice in all_opts:
            StartProgram(f"{all_opts['0' + choice].replace(' ', '-')}.py")
        else:
            ErrorChoiceStart()

    except Exception as e:
        Error(e)
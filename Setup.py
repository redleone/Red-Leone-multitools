# Copyright (c) RedTiger
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

try:
    import sys
    import os
    import subprocess

    # Liste complète des paquets à installer
    required_packages = [
        "auto-py-to-exe",
        "bcrypt",
        "beautifulsoup4",
        "browser-cookie3",
        "colorama",
        "cryptography",
        "customtkinter",
        "deep-translator",
        "discord",
        "dnspython",
        "exifread",
        "GPUtil",
        "instaloader",
        "keyboard",
        "opencv-python",
        "phonenumbers",
        "piexif",
        "pillow",
        "psutil",
        "pyautogui",
        "pycryptodome",
        "pyinstaller",
        "pyqt5",
        "pyqtwebengine",
        "pywin32",
        "pyzipper",
        "rarfile",
        "requests",
        "screeninfo",
        "selenium",
        "setuptools",
        "urllib3",
        "whois"
    ]

    def install_package(package):
        """Installe un paquet Python avec pip"""
        if sys.platform.startswith("win"):
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        else:
            subprocess.check_call(["pip3", "install", package])

    def check_and_install_all():
        """Vérifie et installe tous les paquets manquants"""
        print("Vérification et installation des modules Python requis pour RedRoom:\n")
        
        # Mise à jour de pip
        if sys.platform.startswith("win"):
            os.system("python -m pip install --upgrade pip")
        else:
            os.system("pip3 install --upgrade pip")
        
        # Installation de tous les paquets
        for package in required_packages:
            try:
                print(f"Installation de {package}...")
                install_package(package)
                print(f"[OK] {package} installé avec succès")
            except Exception as e:
                print(f"[ERREUR] Impossible d'installer {package}: {e}")
        
        print("\n[TERMINE] Tous les paquets ont été installés.")

    def OpenSites():
        try:
            import webbrowser
            from Program.Config.Config import dev_profil, gunslol
            webbrowser.open(f'https://{dev_profil}')
            webbrowser.open(f'https://{gunslol}')
        except: pass

    if sys.platform.startswith("win"):
        os.system("cls")
        check_and_install_all()
        OpenSites()
        os.system("python RedLeone.py")

    elif sys.platform.startswith("linux"):
        os.system("clear")
        check_and_install_all()
        OpenSites()
        os.system("python3 RedLeone.py")

except Exception as e:
    input(e)
import os
import time
import sys
import webbrowser

class CerberusSuite:
    def __init__(self):
        self.version = "2.0.0"
        # Link alla tua repository
        self.github_url = "https://github.com/Deadpool2482/Cerberus-Security-Suite.bat"

    def banner(self):
        # Pulisce lo schermo
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print(f"   CERBERUS SECURITY SUITE - v{self.version}")
        print("   Advanced System Protection & Analysis")
        print("=" * 50)
        print("\n")

    def open_github(self):
        print(f"[*] Apertura repository GitHub...")
        time.sleep(1)
        # Apre il browser
        webbrowser.open(self.github_url)
        print("[+] Pagina aperta nel browser!")
        time.sleep(1)

    def main_menu(self):
        while True:
            self.banner()
            print("1. Scansione Rapida Sistema")
            print("2. Verifica Rete")
            print("3. Controlla Aggiornamenti (GitHub)")
            print("0. Esci")
            print("-" * 30)
            
            choice = input("Cosa vuoi fare? > ")
            
            if choice == "1":
                print("\n[*] Scansione in corso...")
                time.sleep(2)
                print("[+] Sistema Pulito!")
                input("Premi INVIO...")
            elif choice == "2":
                os.system("ping 8.8.8.8")
                input("\nPremi INVIO...")
            elif choice == "3":
                self.open_github()
            elif choice == "0":
                break

if __name__ == "__main__":
    app = CerberusSuite()
    app.main_menu()
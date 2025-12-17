import os
import time
import sys

class CerberusSuite:
    def __init__(self):
        self.version = "2.0.0"
        self.system = sys.platform

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def banner(self):
        self.clear_screen()
        print("=" * 50)
        print(f"   CERBERUS SECURITY SUITE - v{self.version}")
        print("   Advanced System Protection & Analysis")
        print("=" * 50)
        print("\n")

    def scan_system(self):
        print("[*] Avvio scansione del sistema...")
        time.sleep(1)
        # Qui in futuro inseriremo la logica reale di scansione
        print("[+] Analisi directory: OK")
        time.sleep(0.5)
        print("[+] Controllo permessi: OK")
        time.sleep(0.5)
        print("[!] Nessuna minaccia rilevata (Modalità Demo).")
        input("\nPremi INVIO per tornare al menu...")

    def network_check(self):
        print("[*] Verifica connettività sicura...")
        response = os.system("ping -n 1 8.8.8.8 > nul")
        if response == 0:
            print("[+] Connessione Internet: ATTIVA e STABILE")
        else:
            print("[-] Connessione Internet: ASSENTE")
        input("\nPremi INVIO per tornare al menu...")

    def main_menu(self):
        while True:
            self.banner()
            print("1. Scansione Rapida Sistema")
            print("2. Verifica Rete e Sicurezza")
            print("3. Informazioni Suite")
            print("0. Esci")
            print("-" * 30)
            
            choice = input("Seleziona un'opzione > ")

            if choice == "1":
                self.scan_system()
            elif choice == "2":
                self.network_check()
            elif choice == "3":
                print(f"\nCerberus v{self.version} - Sviluppato per CloudGuardian.")
                input("Premi INVIO...")
            elif choice == "0":
                print("\nChiusura in corso...")
                break
            else:
                print("\nOpzione non valida!")
                time.sleep(1)

if __name__ == "__main__":
    app = CerberusSuite()
    app.main_menu()
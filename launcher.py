from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import os
import hashlib  # Libreria di sicurezza per la crittografia

Window.clearcolor = (0.05, 0.05, 0.07, 1)

# Questa è la frase segreta e sicura che conosci solo tu
FRASE_SEGRETA_MASTER = "LaMiaConsoleSuperSicura@2026!Blindata#SonyInvidia"

# Generiamo l'hash SHA-256 che la console si aspetta (inviolabile)
HASH_ATTESO = hashlib.sha256(FRASE_SEGRETA_MASTER.encode()).hexdigest()

PERCORSO_SD = "/storage/emulated/0/Download/MicroSD" 

class ConsoleLauncher(App):
    def build(self):
        self.layout_principale = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Titolo stile PS5
        self.titolo = Label(
            text="MY CONSOLE OS", font_size='32sp', bold=True, 
            color=(0, 0.6, 1, 1), size_hint_y=None, height=50
        )
        self.layout_principale.add_widget(self.titolo)
        
        # Avvia il controllo crittografico
        self.controlla_sicurezza_sd()
        
        return self.layout_principale

    def controlla_sicurezza_sd(self):
        file_chiave = os.path.join(PERCORSO_SD, "security.dat")
        
        if os.path.exists(file_chiave):
            with open(file_chiave, 'r') as file:
                codice_sd = file.read().strip()
            
            # La console confronta l'hash sul file con quello generato internamente
            if codice_sd == HASH_ATTESO:
                self.carica_home_giochi()
                return
                
        # Se il file manca o l'hash è sbagliato, scatta il blocco
        self.mostra_errore_sicurezza()

    def carica_home_giochi(self):
        scroll_giochi = ScrollView(size_hint=(1, 1), do_scroll_x=True, do_scroll_y=False)
        lista_orizzontale = BoxLayout(orientation='horizontal', spacing=20, size_hint_x=None)
        lista_orizzontale.bind(minimum_width=lista_orizzontale.setter('width'))
        
        giochi_rilevati = ["Gioco Sicuro 1", "Gioco Sicuro 2", "Retro Emulatore"]
        
        for gioco in giochi_rilevati:
            pulsante_gioco = Button(
                text=gioco, size_hint=(None, None), size=(250, 350),
                background_color=(0.1, 0.15, 0.25, 1), color=(1, 1, 1, 1), font_size='20sp'
            )
            lista_orizzontale.add_widget(pulsante_gioco)
            
        scroll_giochi.add_widget(lista_orizzontale)
        self.layout_principale.add_widget(scroll_giochi)

    def mostra_errore_sicurezza(self):
        errore_label = Label(
            text="ERRORE: Il gioco non è sicuro.\nMicroSD non autorizzata.", 
            font_size='24sp', color=(1, 0.2, 0.2, 1), bold=True, halign="center"
        )
        self.layout_principale.add_widget(errore_label)

if __name__ == '__main__':
    ConsoleLauncher().run()

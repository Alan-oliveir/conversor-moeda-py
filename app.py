
import customtkinter
from main import api_key, converter_moeda


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("460x420")
        self.title("Conversor de Moeda")

        title_font = customtkinter.CTkFont(family="Arial", size=34, weight='bold')

        # add widgets to app
        self.label_title = customtkinter.CTkLabel(self, text="Conversor de Moeda", fg_color="transparent", width=420,
                                                  height=50, font=title_font)
        self.label_title.grid(row=0, column=0, padx=20, pady=(10, 5))

        self.label_origem = customtkinter.CTkLabel(self, text="Moeda de Origem:", fg_color="transparent", width=420)
        self.label_origem.grid(row=1, column=0, padx=20, pady=0)

        self.entry_origem = customtkinter.CTkEntry(self, width=400, height=35)
        self.entry_origem.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.label_destino = customtkinter.CTkLabel(self, text="Moeda de Destino:", fg_color="transparent", width=420)
        self.label_destino.grid(row=3, column=0, padx=20, pady=0)

        self.entry_destino = customtkinter.CTkEntry(self, width=400, height=35)
        self.entry_destino.grid(row=4, column=0, padx=20, pady=(10, 10))

        self.label_valor = customtkinter.CTkLabel(self, text="Valor:", fg_color="transparent", width=420)
        self.label_valor.grid(row=5, column=0, padx=20, pady=0)

        self.entry_valor = customtkinter.CTkEntry(self, width=400, height=35)
        self.entry_valor.grid(row=6, column=0, padx=20, pady=(10, 5))

        self.button = customtkinter.CTkButton(self, command=self.on_button_click, text="Converter", fg_color='#4caf50',
                                              hover_color='#449e48', width=400, height=36)
        self.button.grid(row=7, column=0, padx=20, pady=10)

        self.textbox = customtkinter.CTkTextbox(self, width=400, fg_color="transparent")
        self.textbox.grid(row=8, column=0)

    def on_button_click(self):
        valor = float(self.entry_valor.get())
        moeda_origem = self.entry_origem.get()
        moeda_destino = self.entry_destino.get()
        resultado = converter_moeda(api_key, valor, moeda_origem, moeda_destino)
        if resultado:
            self.textbox.delete("1.0", customtkinter.END)
            self.textbox.insert("1.0", f"{valor} {moeda_origem} = {resultado} {moeda_destino}")
        else:
            self.textbox.delete("1.0", customtkinter.END)
            self.textbox.insert("1.0", "Erro ao obter a conversão.")


app = App()
app.mainloop()

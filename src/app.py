# pylint: disable
import json
import customtkinter as ctk
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from encryption_decryption import encrypt, format_as_poem
from encryption_decryption import decryption

class PoetryApp:
    def __init__(self):
        # Initialize main window
        self.root = ctk.CTk()
        self.root.title("نظام تشفير الشعر العربي")
        self.root.geometry("1024x720")

        # Configure Arabic font
        self.arabic_font = ("Tahoma", 14)

        # Create UI elements
        self.create_widgets()
    
        # Load verse database
        with open("database/verses_database.json", "r", encoding="utf-8") as f:
            self.db = json.load(f)

        # Run application
        self.root.mainloop()

    def create_widgets(self):
        # Configure grid
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkLabel(
            self.root,
            text=get_display(reshape("نظام تشفير الشعر العربي")),
            font=("Tahoma", 20, "bold")
        )
        header.grid(row=0, column=0, pady=20)

        # Main notebook (tabs)
        self.tabs = ctk.CTkTabview(self.root)
        self.tabs.grid(row=1, column=0, padx=20, pady=(0,20), sticky="nsew")

        # Create tabs
        self.tab_encrypt = self.tabs.add(get_display(reshape("تشفير")))
        self.tab_decrypt = self.tabs.add(get_display(reshape("فك التشفير")))

        # Build tab contents
        self.build_encrypt_tab()
        self.build_decrypt_tab()

        # Theme switcher
        self.theme_switch = ctk.CTkSwitch(
            self.root,
            text=get_display(reshape("الوضع النهاري")),
            command=self.toggle_theme
        )
        self.theme_switch.grid(row=2, column=0, pady=10)

    def copy_to_clipboard(self, text):
        self.root.clipboard_clear()
        text = get_display(reshape(text))
        self.root.clipboard_append(text)

    def paste_from_clipboard(self, target_widget):
        text = self.root.clipboard_get()
        processed_text = get_display(reshape(text))

        if isinstance(target_widget, ctk.CTkEntry):
            target_widget.delete(0, 'end')
            target_widget.insert(0, processed_text)
        elif isinstance(target_widget, ctk.CTkTextbox):
            target_widget.delete('1.0', 'end')
            target_widget.insert('1.0', processed_text)

    def build_encrypt_tab(self):
        # Input frame
        input_frame = ctk.CTkFrame(self.tab_encrypt)
        input_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(
            input_frame,
            text = get_display(reshape('لصق')),
            font = self.arabic_font,
            width = 80,
            command = lambda: self.paste_from_clipboard(self.message_entry)
        ).pack(side = 'right',padx= 10, pady = (0 ,88))
        # Message entry
        ctk.CTkLabel(
            input_frame,
            text=get_display(reshape("الرسالة")),
            font=self.arabic_font
        ).pack(anchor="n")


        self.message_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text=get_display(reshape("أدخل النص هنا...")),
            font=self.arabic_font,
            width=400
        )
        self.message_entry.pack(fill="x", pady=5)


        # Category dropdown
        ctk.CTkLabel(
            input_frame,
            text=get_display(reshape("التصنيف")),
            font=self.arabic_font
        ).pack(anchor="n")

        self.category_var = ctk.StringVar(value="general")
        self.category_menu = ctk.CTkOptionMenu(
            input_frame,
            values=["general", "حب","حكمة", "صداقة", "تفاؤل", "رومنسية", "دينية", "أخلاق"],
            variable=self.category_var,
            font=self.arabic_font
        )
        self.category_menu.pack(fill="x", pady=5)

        # Encrypt button
        encrypt_btn = ctk.CTkButton(
            input_frame,
            text=get_display(reshape("تشفير")),
            command=self.run_encryption,
            font=self.arabic_font
        )
        encrypt_btn.pack(pady=10)
        
        # Output frame
        output_frame = ctk.CTkFrame(self.tab_encrypt)
        output_frame.pack(fill="both", expand=True, padx=20, pady=(0,20))
        
        ctk.CTkLabel(
            output_frame, 
            text=get_display(reshape("القصيدة المشفرة")),
            font=self.arabic_font
        ).pack(anchor="n", pady=5, padx= (0, 100))
        
        self.poetry_output = ctk.CTkTextbox(
            output_frame,
            font=self.arabic_font,
            wrap="word",
            height=200,
        )
        self.poetry_output.pack(fill="both", expand=True, padx=10, pady=(0,10))

        copy_frame = ctk.CTkFrame(output_frame, fg_color="transparent")
        copy_frame.pack(fill = "x", padx = 10, pady=(0, 10))

        ctk.CTkButton(
            copy_frame,
            text=get_display(reshape("نسخ")),
            font=self.arabic_font,
            width=80,
            command=lambda: self.copy_to_clipboard(self.poetry_output.get('1.0', 'end'))
        ).pack(side ="right", padx = 5)
    
    def build_decrypt_tab(self):
        # Input frame
        input_frame = ctk.CTkFrame(self.tab_decrypt)
        input_frame.pack(fill="x", padx=20, pady=10)


        # Poem entry
        ctk.CTkLabel(
            input_frame,
            text=get_display(reshape("القصيدة")),
            font=self.arabic_font
        ).pack(anchor="n")

        self.poem_entry = ctk.CTkTextbox(
            input_frame,
            wrap="word",
            font=self.arabic_font,
            height=150
        )
        self.poem_entry.pack(fill="x", pady=5)
         #paste button
        ctk.CTkButton(
            input_frame,
            text=get_display(reshape('لصق')),
            font=self.arabic_font,
            width=80,
            command= lambda: self.paste_from_clipboard(self.poem_entry)
        ).pack(anchor = 'e', pady = 10)

        # Decrypt button
        decrypt_btn = ctk.CTkButton(
            input_frame,
            text=get_display(reshape("فك التشفير")),
            command=self.decrypt_poem,
            font=self.arabic_font
        )
        decrypt_btn.pack(pady = 10, anchor = 'n')

        # Output frame
        output_frame = ctk.CTkFrame(self.tab_decrypt)
        output_frame.pack(fill="both", expand=True, padx=20, pady=(0,20))

        ctk.CTkLabel(
            output_frame,
            text=get_display(reshape("الرسالة الأصلية")),
            font=self.arabic_font
        ).pack(anchor="n", padx=10, pady=5)

        self.decrypted_output = ctk.CTkEntry(
            output_frame,
            font=self.arabic_font,
            width=400,
            height=50,
        )
        self.decrypted_output.pack(fill="x", padx=10, pady=(0,10))

    def run_encryption(self):
        message = self.message_entry.get()
        category = self.category_var.get()

        encrypted_message = encrypt(message, category)
        self.formatted_poem = format_as_poem(encrypted_message)

        # Display with RTL support

        self.poetry_output.delete("1.0", "end")
        self.poetry_output.insert("1.0", get_display(reshape(self.formatted_poem)))

    def decrypt_poem(self):

        poem = self.formatted_poem

        decrypted = decryption(poem)

        self.decrypted_output.delete(0, "end")
        self.decrypted_output.insert(0, get_display(reshape(decrypted)))

    def toggle_theme(self):
        if self.theme_switch.get() == 0:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

# Run the application
if __name__ == "__main__":
    PoetryApp()
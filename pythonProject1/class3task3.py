import random
import string
import tkinter as tk


class SubstitutionCipherGUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Substitution Cipher')
        self.logged_in = False
        self.create_login_page()

    def create_login_page(self):
        self.username_label = tk.Label(self.master, text='Username:')
        self.username_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.username_entry = tk.Entry(self.master, width=40)
        self.username_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        self.password_label = tk.Label(self.master, text='Password:')
        self.password_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.password_entry = tk.Entry(self.master, show='*', width=40)
        self.password_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        self.login_button = tk.Button(self.master, text='Login', command=self.login)
        self.login_button.grid(row=2, column=1, padx=5, pady=5)
        self.quit_button = tk.Button(self.master, text='Quit', command=self.quit)
        self.quit_button.grid(row=2, column=2, padx=5, pady=5)

    def create_widgets(self):
        self.plaintext_label = tk.Label(self.master, text='Plaintext:')
        self.plaintext_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.plaintext_entry = tk.Entry(self.master, width=40)
        self.plaintext_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        self.key_label = tk.Label(self.master, text='Key:')
        self.key_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.key_entry = tk.Entry(self.master, width=40, state='disabled')
        self.key_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        self.generate_key_button = tk.Button(self.master, text='Generate Key', command=self.generate_key)
        self.generate_key_button.grid(row=2, column=0, padx=5, pady=5)
        self.encrypt_button = tk.Button(self.master, text='Encrypt', command=self.encrypt)
        self.encrypt_button.grid(row=2, column=1, padx=5, pady=5)
        self.decrypt_button = tk.Button(self.master, text='Decrypt', command=self.decrypt)
        self.decrypt_button.grid(row=2, column=2, padx=5, pady=5)
        self.ciphertext_label = tk.Label(self.master, text='Ciphertext:')
        self.ciphertext_label.grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.ciphertext_entry = tk.Entry(self.master, width=40, state='disabled')
        self.ciphertext_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == 'admin' and password == 'password':
            self.logged_in = True
            self.username_label.grid_forget()
            self.username_entry.grid_forget()
            self.password_label.grid_forget()
            self.password_entry.grid_forget()
            self.login_button.grid_forget()
            self.quit_button.grid_forget()
            self.create_widgets()
        else:
            self.error_label = tk.Label(self.master, text='Incorrect username or password')
            self.error_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
    def create_widgets(self):
        self.plaintext_label = tk.Label(self.master, text='Plaintext:')
        self.plaintext_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.plaintext_entry = tk.Entry(self.master, width=40)
        self.plaintext_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        self.key_label = tk.Label(self.master, text='Key:')
        self.key_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.key_entry = tk.Entry(self.master, width=40, state='disabled')
        self.key_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        self.generate_key_button = tk.Button(self.master, text='Generate Key', command=self.generate_key)
        self.generate_key_button.grid(row=2, column=0, padx=5, pady=5)
        self.encrypt_button = tk.Button(self.master, text='Encrypt', command=self.encrypt)
        self.encrypt_button.grid(row=2, column=1, padx=5, pady=5)
        self.decrypt_button = tk.Button(self.master, text='Decrypt', command=self.decrypt)
        self.decrypt_button.grid(row=2, column=2, padx=5, pady=5)
        self.ciphertext_label = tk.Label(self.master, text='Ciphertext:')
        self.ciphertext_label.grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.ciphertext_entry = tk.Entry(self.master, width=40, state='disabled')
        self.ciphertext_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
        if self.logged_in:
            self.key_entry.config(state='normal')
            self.ciphertext_entry.config(state='normal')


    def generate_key(self):
        alphabet = string.ascii_lowercase
        key = ''.join(random.sample(alphabet, len(alphabet)))
        self.key_entry.config(state='normal')
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, key)
        self.key_entry.config(state='normal')

    def encrypt(self):
        plaintext = self.plaintext_entry.get().lower()
        key = self.key_entry.get()
        encryption_dict = dict(zip(string.ascii_lowercase, key))
        ciphertext = ''.join(encryption_dict.get(letter, letter) for letter in plaintext)
        self.ciphertext_entry.config(state='normal')
        self.ciphertext_entry.delete(0, tk.END)
        self.ciphertext_entry.insert(0, ciphertext)
        self.ciphertext_entry.config(state='disabled')

    def decrypt(self):
        ciphertext = self.ciphertext_entry.get().lower()
        key = self.key_entry.get()
        decryption_dict = dict(zip(key, string.ascii_lowercase))
        plaintext = ''.join(decryption_dict.get(letter, letter) for letter in ciphertext)
        self.plaintext_entry.delete(0, tk.END)
        self.plaintext_entry.insert(0, plaintext)


if __name__ == '__main__':
    root = tk.Tk()
    app = SubstitutionCipherGUI(master=root)
    app.mainloop()

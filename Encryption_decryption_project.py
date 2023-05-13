import tkinter as tk

def encrypt():
    plaintext = entry1.get().lower()
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            num = ord(letter) - 97
            num = (num + 11) % 26
            ciphertext += str(num) + " "
        else:
            ciphertext += letter
            
    entry2.delete(0, tk.END)
    entry2.insert(0, ciphertext)

def decrypt():
    ciphertext = entry2.get()
    words = ciphertext.split(" ")
    plaintext = ""
    for word in words:
        if word.isdigit():
            num = int(word)
            num = (num - 11) % 26
            plaintext += chr(num + 97)
        else:
            plaintext += " "
            
    entry1.delete(0, tk.END)
    entry1.insert(0, plaintext)

root = tk.Tk()

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

label1 = tk.Label(root, text="Enter text to encrypt:")
label2 = tk.Label(root, text="Enter text to decrypt:")

button1 = tk.Button(root, text="Encrypt", command=encrypt)
button2 = tk.Button(root, text="Decrypt", command=decrypt)

label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
button1.grid(row=0, column=2)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
button2.grid(row=1, column=2)

root.mainloop()

import tkinter as tk
from tkinter import scrolledtext

# Basic phonetic mapping for English to Bangla
phonetic_map = {
    'a': 'া', 'aa': 'আ', 'i': 'ি', 'ii': 'ী', 'u': 'ু', 'uu': 'ূ', 'e': 'ে', 'oi': 'ৈ', 'o': 'ো', 'ou': 'ৌ',
    'k': 'ক', 'kh': 'খ', 'g': 'গ', 'gh': 'ঘ', 'ng': 'ঙ',
    'c': 'চ', 'ch': 'ছ', 'j': 'জ', 'jh': 'ঝ', 'ny': 'ঞ',
    't': 'ত', 'th': 'থ', 'd': 'দ', 'dh': 'ধ', 'n': 'ন',
    'p': 'প', 'ph': 'ফ', 'b': 'ব', 'bh': 'ভ', 'm': 'ম',
    'y': 'য', 'r': 'র', 'l': 'ল', 'sh': 'শ', 's': 'স', 'h': 'হ',
    'rri': 'ঋ', 'ngh': 'ঙ', 'tr': 'ত্র', 'gn': 'জ্ঞ', 'kkh': 'ক্ষ',
    'yya': 'য়', '': '্'
}

# Function to convert English to Bangla phonetically
def convert_to_bangla(text):
    result = ''
    i = 0
    while i < len(text):
        # Check for two-character combinations first (e.g., 'aa', 'ii', 'kh')
        if i + 1 < len(text) and text[i:i+2] in phonetic_map:
            result += phonetic_map[text[i:i+2]]
            i += 2
        else:  # Otherwise check single characters
            result += phonetic_map.get(text[i], text[i])
            i += 1  # Default to the same character if not in map
    return result

# Function to handle button click
def on_convert():
    english_text = input_box.get('1.0', tk.END).strip()
    bangla_text = convert_to_bangla(english_text)
    output_box.config(state=tk.NORMAL)
    output_box.delete('1.0', tk.END)
    output_box.insert(tk.END, bangla_text)
    output_box.config(state=tk.DISABLED)

# Tkinter GUI setup
root = tk.Tk()
root.title('Phonetic English to Bangla Converter')
root.geometry('500x400')

# Input Text Box
tk.Label(root, text='Enter English Text:', font=('Arial', 14)).pack(pady=5)
input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=('Arial', 12), height=5)
input_box.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Convert Button
convert_button = tk.Button(root, text='Convert to Bangla', font=('Arial', 14), command=on_convert)
convert_button.pack(pady=10)

# Output Text Box
tk.Label(root, text='Bangla Output:', font=('Arial', 14)).pack(pady=5)
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=('Arial', 12), height=5, state=tk.DISABLED)
output_box.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Credit Label
tk.Label(root, text='This software is made by Safwan Sabit', font=('Arial', 10), fg='gray').pack(pady=10)

root.mainloop()

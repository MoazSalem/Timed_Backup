import os
import shutil
import threading
import time
import tkinter as tk
from tkinter import filedialog

class BackupApplication:
    def __init__(self, master):
        self.master = master
        master.title("Timed Backup")
        
        # Initialize variables
        self.file_path = tk.StringVar()
        self.backup_dir = "./backups/"
        self.backup_interval = 120 # in seconds, 2 minutes
        self.backup_count = 0
        
        # Create widgets
        self.file_label = tk.Label(master, text="File path:")
        self.file_entry = tk.Entry(master, textvariable=self.file_path)
        self.file_button = tk.Button(master, text="Browse", command=self.select_file)
        self.start_button = tk.Button(master, text="Start", command=self.start_backup)
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_backup, state="disabled")
        self.count_label = tk.Label(master, text="Backups: 0")
        
        # Lay out widgets
        self.file_label.grid(row=0, column=0, sticky="w")
        self.file_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        self.file_button.grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.start_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.stop_button.grid(row=1, column=1, padx=5, pady=5, sticky="e")
        self.count_label.grid(row=1, column=2, padx=5, pady=5, sticky="e")
    
    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)
    
    def start_backup(self):
        self.backup_thread = threading.Thread(target=self.backup_loop)
        self.backup_thread.daemon = True
        self.backup_thread.start()
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
    
    def stop_backup(self):
        self.running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
    
    def backup_loop(self):
        self.running = True
        while self.running:
            current_time = time.localtime()
            backup_subdir = time.strftime("%H-%M", current_time)
            backup_path = os.path.join(self.backup_dir, backup_subdir)
            
            if not os.path.exists(backup_path):
                os.makedirs(backup_path)
            
            source_path = self.file_path.get()
            if os.path.exists(source_path):
                dest_path = os.path.join(backup_path, os.path.basename(source_path))
                shutil.copy(source_path, dest_path)
                self.backup_count += 1
                self.count_label.config(text=f"Backups: {self.backup_count}")
            
            time.sleep(self.backup_interval)

# Initialize GUI
root = tk.Tk()
app = BackupApplication(root)
root.mainloop()
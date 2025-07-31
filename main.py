#!/usr/bin/env python3
"""
Custom IDE - Main Application
A modern, feature-rich code editor with AI-powered error fixing
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import sys
from editor import CodeEditor
from runner import CodeRunner
from ai_fix import AIFixer
from file_manager import FileManager
from theme_manager import ThemeManager

class CustomIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 Custom IDE - Multi-Language Editor")
        self.root.geometry("1400x900")
        self.root.minsize(1000, 700)
        
        # Set window icon if available
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass
        
        # Initialize components
        self.theme_manager = ThemeManager()
        self.file_manager = FileManager()
        self.ai_fixer = AIFixer()
        
        # Current file info
        self.current_file = None
        self.current_language = None
        
        # Configure styles
        self.setup_styles()
        
        self.setup_ui()
        self.apply_theme()
        
    def setup_styles(self):
        """Setup modern ttk styles"""
        style = ttk.Style()
        
        # Configure modern button styles
        style.configure("Modern.TButton",
                       padding=(12, 8),
                       font=("Segoe UI", 9),
                       borderwidth=0,
                       focuscolor="none")
        
        style.configure("Accent.TButton",
                       padding=(12, 8),
                       font=("Segoe UI", 9, "bold"),
                       borderwidth=0,
                       focuscolor="none")
        
        style.configure("Toolbar.TButton",
                       padding=(8, 6),
                       font=("Segoe UI", 8),
                       borderwidth=0,
                       focuscolor="none")
        
        # Configure frame styles
        style.configure("Panel.TFrame",
                       borderwidth=0,
                       relief="flat")
        
        style.configure("Toolbar.TFrame",
                       borderwidth=0,
                       relief="flat")
        
        # Configure label styles
        style.configure("Title.TLabel",
                       font=("Segoe UI", 12, "bold"),
                       padding=(0, 5))
        
        style.configure("Status.TLabel",
                       font=("Segoe UI", 9),
                       padding=(10, 5))
        
    def setup_ui(self):
        """Setup the main user interface"""
        # Configure main window
        self.root.configure(bg="#1e1e1e")
        
        # Create main container
        main_container = ttk.Frame(self.root, style="Panel.TFrame")
        main_container.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Create toolbar
        self.create_toolbar(main_container)
        
        # Create main content area
        content_frame = ttk.Frame(main_container, style="Panel.TFrame")
        content_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 0))
        
        # Create editor and output panels
        self.create_editor_panel(content_frame)
        self.create_output_panel(content_frame)
        
        # Create status bar
        self.create_status_bar(main_container)
        
        # Bind keyboard shortcuts
        self.bind_shortcuts()
        
    def create_toolbar(self, parent):
        """Create the modern toolbar with file operations and theme toggle"""
        toolbar = ttk.Frame(parent, style="Toolbar.TFrame")
        toolbar.pack(fill=tk.X, pady=(0, 0))
        
        # File operations section
        file_frame = ttk.Frame(toolbar, style="Toolbar.TFrame")
        file_frame.pack(side=tk.LEFT, padx=(10, 0))
        
        ttk.Button(file_frame, text="📄 New", command=self.new_file, 
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(file_frame, text="📂 Open", command=self.open_file, 
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(file_frame, text="💾 Save", command=self.save_file, 
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(file_frame, text="💾 Save As", command=self.save_file_as, 
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=(0, 5))
        
        # Separator
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=15)
        
        # Run section
        run_frame = ttk.Frame(toolbar, style="Toolbar.TFrame")
        run_frame.pack(side=tk.LEFT, padx=(0, 0))
        
        ttk.Button(run_frame, text="▶️ Run", command=self.run_code, 
                  style="Accent.TButton").pack(side=tk.LEFT, padx=(0, 5))
        
        # Separator
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=15)
        
        # AI section
        ai_frame = ttk.Frame(toolbar, style="Toolbar.TFrame")
        ai_frame.pack(side=tk.LEFT, padx=(0, 0))
        
        ttk.Button(ai_frame, text="🤖 AI Fix", command=self.ask_ai_fix, 
                  style="Modern.TButton").pack(side=tk.LEFT, padx=(0, 5))
        
        # Separator
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=15)
        
        # Theme toggle
        self.theme_var = tk.StringVar(value="dark")
        ttk.Button(toolbar, text="🌙", command=self.toggle_theme, 
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=(0, 5))
        
        # File info label
        self.file_label = ttk.Label(toolbar, text="📝 No file open", style="Status.TLabel")
        self.file_label.pack(side=tk.RIGHT, padx=(0, 10))
        
    def create_editor_panel(self, parent):
        """Create the code editor panel"""
        editor_frame = ttk.Frame(parent, style="Panel.TFrame")
        editor_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        # Editor header
        editor_header = ttk.Frame(editor_frame, style="Panel.TFrame")
        editor_header.pack(fill=tk.X, padx=(10, 5), pady=(10, 5))
        
        ttk.Label(editor_header, text="📝 Code Editor", style="Title.TLabel").pack(side=tk.LEFT)
        
        # Language indicator
        self.language_label = ttk.Label(editor_header, text="", style="Status.TLabel")
        self.language_label.pack(side=tk.RIGHT)
        
        # Create code editor
        self.editor = CodeEditor(editor_frame, self.theme_manager)
        self.editor.pack(fill=tk.BOTH, expand=True, padx=(10, 5), pady=(0, 10))
        
    def create_output_panel(self, parent):
        """Create the output panel with terminal and AI fix button"""
        output_frame = ttk.Frame(parent, style="Panel.TFrame")
        output_frame.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT, padx=(5, 10))
        
        # Output header
        output_header = ttk.Frame(output_frame, style="Panel.TFrame")
        output_header.pack(fill=tk.X, padx=(5, 10), pady=(10, 5))
        
        ttk.Label(output_header, text="🖥️ Output & Terminal", style="Title.TLabel").pack(side=tk.LEFT)
        
        # Clear output button
        ttk.Button(output_header, text="🗑️ Clear", command=self.clear_output, 
                  style="Toolbar.TButton").pack(side=tk.RIGHT)
        
        # Output text area
        output_container = ttk.Frame(output_frame, style="Panel.TFrame")
        output_container.pack(fill=tk.BOTH, expand=True, padx=(5, 10), pady=(0, 10))
        
        # Create output text widget with modern styling
        self.output_text = tk.Text(
            output_container,
            wrap=tk.WORD,
            font=("Consolas", 10),
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="#ffffff",
            selectbackground="#264f78",
            selectforeground="#ffffff",
            relief="flat",
            borderwidth=0,
            padx=10,
            pady=10
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        # Scrollbar for output
        output_scrollbar = ttk.Scrollbar(output_container, orient=tk.VERTICAL, command=self.output_text.yview)
        output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.configure(yscrollcommand=output_scrollbar.set)
        
        # Create code runner
        self.runner = CodeRunner(self.output_text)
        
    def create_status_bar(self, parent):
        """Create a modern status bar"""
        status_bar = ttk.Frame(parent, style="Toolbar.TFrame")
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Status information
        self.status_label = ttk.Label(status_bar, text="Ready", style="Status.TLabel")
        self.status_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Line and column info
        self.position_label = ttk.Label(status_bar, text="Ln 1, Col 1", style="Status.TLabel")
        self.position_label.pack(side=tk.RIGHT, padx=(0, 10))
        
    def clear_output(self):
        """Clear the output panel"""
        self.output_text.delete(1.0, tk.END)
        self.update_status("Output cleared")
        
    def update_status(self, message):
        """Update status bar message"""
        self.status_label.config(text=message)
        
    def update_position(self, line, col):
        """Update position indicator"""
        self.position_label.config(text=f"Ln {line}, Col {col}")
        
    def bind_shortcuts(self):
        """Bind keyboard shortcuts"""
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-r>", lambda e: self.run_code())
        self.root.bind("<F5>", lambda e: self.run_code())
        self.root.bind("<Control-f>", lambda e: self.ask_ai_fix())
        self.root.bind("<Control-t>", lambda e: self.toggle_theme())
        
    def new_file(self):
        """Create a new file"""
        self.current_file = None
        self.current_language = None
        self.editor.clear()
        self.file_label.config(text="📝 New file")
        self.language_label.config(text="")
        self.output_text.delete(1.0, tk.END)
        self.update_status("New file created")
        
    def open_file(self):
        """Open an existing file"""
        file_path = filedialog.askopenfilename(
            title="Open File",
            filetypes=[
                ("All supported", "*.py *.js *.cs *.html *.css *.json *.txt"),
                ("Python", "*.py"),
                ("JavaScript", "*.js"),
                ("C#", "*.cs"),
                ("HTML", "*.html"),
                ("CSS", "*.css"),
                ("JSON", "*.json"),
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                content = self.file_manager.load_file(file_path)
                self.editor.set_content(content)
                self.current_file = file_path
                self.current_language = self.file_manager.get_language_from_extension(file_path)
                self.editor.set_language(self.current_language)
                self.file_label.config(text=f"📄 {os.path.basename(file_path)}")
                self.language_label.config(text=f"🔤 {self.current_language.upper()}")
                self.output_text.delete(1.0, tk.END)
                self.update_status(f"Opened {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {str(e)}")
                
    def save_file(self):
        """Save the current file"""
        if self.current_file:
            try:
                content = self.editor.get_content()
                self.file_manager.save_file(self.current_file, content)
                self.update_status(f"Saved {os.path.basename(self.current_file)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {str(e)}")
        else:
            self.save_file_as()
            
    def save_file_as(self):
        """Save file with a new name"""
        file_path = filedialog.asksaveasfilename(
            title="Save File As",
            defaultextension=".txt",
            filetypes=[
                ("Python", "*.py"),
                ("JavaScript", "*.js"),
                ("C#", "*.cs"),
                ("HTML", "*.html"),
                ("CSS", "*.css"),
                ("JSON", "*.json"),
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                content = self.editor.get_content()
                self.file_manager.save_file(file_path, content)
                self.current_file = file_path
                self.current_language = self.file_manager.get_language_from_extension(file_path)
                self.editor.set_language(self.current_language)
                self.file_label.config(text=f"📄 {os.path.basename(file_path)}")
                self.language_label.config(text=f"🔤 {self.current_language.upper()}")
                self.update_status(f"Saved as {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {str(e)}")
                
    def run_code(self):
        """Run the current code"""
        code = self.editor.get_content()
        if not code.strip():
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "No code to run.\n")
            return
            
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "🚀 Running code...\n\n")
        self.update_status("Running code...")
        self.root.update()
        
        try:
            result = self.runner.run_code(code, self.current_language)
            self.output_text.insert(tk.END, result)
            self.update_status("Code executed successfully")
        except Exception as e:
            self.output_text.insert(tk.END, f"❌ Error: {str(e)}\n")
            self.update_status("Code execution failed")
            
    def ask_ai_fix(self):
        """Ask AI to fix the current code"""
        code = self.editor.get_content()
        if not code.strip():
            messagebox.showwarning("Warning", "No code to fix.")
            return
            
        # Get current output/error
        current_output = self.output_text.get(1.0, tk.END).strip()
        
        try:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "🤖 Asking AI to fix your code...\n")
            self.update_status("AI is analyzing code...")
            self.root.update()
            
            fixed_code = self.ai_fixer.fix_code(code, self.current_language, current_output)
            
            if fixed_code:
                self.editor.set_content(fixed_code)
                self.output_text.insert(tk.END, "✅ Code has been fixed by AI!\n")
                self.output_text.insert(tk.END, "The corrected code has been loaded into the editor.\n")
                self.update_status("AI fix applied successfully")
            else:
                self.output_text.insert(tk.END, "❌ Could not get AI fix. Please check your API key.\n")
                self.update_status("AI fix failed")
                
        except Exception as e:
            self.output_text.insert(tk.END, f"❌ Error getting AI fix: {str(e)}\n")
            self.update_status("AI fix error")
            
    def toggle_theme(self):
        """Toggle between light and dark themes"""
        current_theme = self.theme_var.get()
        new_theme = "light" if current_theme == "dark" else "dark"
        self.theme_var.set(new_theme)
        self.theme_manager.set_theme(new_theme)
        self.apply_theme()
        self.update_status(f"Switched to {new_theme} theme")
        
    def apply_theme(self):
        """Apply the current theme to all components"""
        theme = self.theme_manager.get_current_theme()
        self.editor.apply_theme(theme)
        
        # Apply theme to output text
        self.output_text.configure(
            bg=theme["output_bg"],
            fg=theme["output_fg"],
            insertbackground=theme["output_fg"]
        )
        
        # Apply theme to main window
        self.root.configure(bg=theme["bg"])

def main():
    """Main entry point"""
    root = tk.Tk()
    app = CustomIDE(root)
    
    # Set window icon if available
    try:
        root.iconbitmap("icon.ico")
    except:
        pass
    
    root.mainloop()

if __name__ == "__main__":
    main() 
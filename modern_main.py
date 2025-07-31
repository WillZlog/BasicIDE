#!/usr/bin/env python3
"""
Modern Custom IDE - Premium Desktop Application
A beautiful, modern code editor that looks better than VS Code
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys
from modern_ui import ModernButton, ModernFrame, ModernText, ModernScrollbar, ModernLabel
from runner import CodeRunner
from ai_fix import AIFixer
from file_manager import FileManager
from theme_manager import ThemeManager

class ModernIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 Custom IDE - Premium Code Editor")
        self.root.geometry("1600x1000")
        self.root.minsize(1200, 800)
        
        # Configure main window with gradient background
        self.root.configure(bg="#0d1117")
        
        # Initialize components
        self.theme_manager = ThemeManager()
        self.file_manager = FileManager()
        self.ai_fixer = AIFixer()
        
        # Current file info
        self.current_file = None
        self.current_language = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the modern user interface"""
        # Create main container with gradient
        self.main_container = ModernFrame(self.root, bg="#0d1117")
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Create modern toolbar
        self.create_toolbar()
        
        # Create main content area
        self.create_content_area()
        
        # Create modern status bar
        self.create_status_bar()
        
        # Bind keyboard shortcuts
        self.bind_shortcuts()
        
    def create_toolbar(self):
        """Create the modern toolbar with gradient and shadows"""
        # Toolbar container
        self.toolbar = ModernFrame(self.main_container, bg="#161b22", height=60)
        self.toolbar.pack(fill=tk.X, padx=0, pady=0)
        
        # Logo and title
        title_label = ModernLabel(self.toolbar, text="🚀 Custom IDE", 
                                font=("Segoe UI", 16, "bold"), fg="#ffffff")
        title_label.pack(side=tk.LEFT, padx=(20, 0), pady=15)
        
        # File operations section
        file_frame = ModernFrame(self.toolbar, bg="#161b22")
        file_frame.pack(side=tk.LEFT, padx=(30, 0), pady=10)
        
        ModernButton(file_frame, text="📄 New", command=self.new_file, 
                    style="secondary", width=80, height=35).pack(side=tk.LEFT, padx=(0, 8))
        ModernButton(file_frame, text="📂 Open", command=self.open_file, 
                    style="secondary", width=80, height=35).pack(side=tk.LEFT, padx=(0, 8))
        ModernButton(file_frame, text="💾 Save", command=self.save_file, 
                    style="secondary", width=80, height=35).pack(side=tk.LEFT, padx=(0, 8))
        ModernButton(file_frame, text="💾 Save As", command=self.save_file_as, 
                    style="secondary", width=90, height=35).pack(side=tk.LEFT, padx=(0, 8))
        
        # Separator
        separator = ModernFrame(self.toolbar, bg="#30363d", width=2, height=40)
        separator.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Run section
        run_frame = ModernFrame(self.toolbar, bg="#161b22")
        run_frame.pack(side=tk.LEFT, padx=(0, 0), pady=10)
        
        ModernButton(run_frame, text="▶️ Run Code", command=self.run_code, 
                    style="success", width=100, height=35).pack(side=tk.LEFT, padx=(0, 8))
        
        # Separator
        separator2 = ModernFrame(self.toolbar, bg="#30363d", width=2, height=40)
        separator2.pack(side=tk.LEFT, padx=20, pady=10)
        
        # AI section
        ai_frame = ModernFrame(self.toolbar, bg="#161b22")
        ai_frame.pack(side=tk.LEFT, padx=(0, 0), pady=10)
        
        ModernButton(ai_frame, text="🤖 AI Fix", command=self.ask_ai_fix, 
                    style="primary", width=90, height=35).pack(side=tk.LEFT, padx=(0, 8))
        
        # Separator
        separator3 = ModernFrame(self.toolbar, bg="#30363d", width=2, height=40)
        separator3.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Theme toggle
        self.theme_var = tk.StringVar(value="dark")
        ModernButton(self.toolbar, text="🌙", command=self.toggle_theme, 
                    style="secondary", width=50, height=35).pack(side=tk.LEFT, padx=(0, 8))
        
        # File info label
        self.file_label = ModernLabel(self.toolbar, text="📝 No file open", 
                                    font=("Segoe UI", 10), fg="#8b949e")
        self.file_label.pack(side=tk.RIGHT, padx=(0, 20), pady=15)
        
    def create_content_area(self):
        """Create the main content area with editor and output"""
        # Content container
        content_frame = ModernFrame(self.main_container, bg="#0d1117")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Editor panel
        self.create_editor_panel(content_frame)
        
        # Output panel
        self.create_output_panel(content_frame)
        
    def create_editor_panel(self, parent):
        """Create the modern code editor panel"""
        # Editor container
        editor_container = ModernFrame(parent, bg="#0d1117")
        editor_container.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(20, 10), pady=20)
        
        # Editor header
        editor_header = ModernFrame(editor_container, bg="#161b22", height=50)
        editor_header.pack(fill=tk.X, pady=(0, 10))
        
        title_label = ModernLabel(editor_header, text="📝 Code Editor", 
                                font=("Segoe UI", 14, "bold"), fg="#ffffff")
        title_label.pack(side=tk.LEFT, padx=(20, 0), pady=15)
        
        # Language indicator
        self.language_label = ModernLabel(editor_header, text="", 
                                        font=("Segoe UI", 10), fg="#8b949e")
        self.language_label.pack(side=tk.RIGHT, padx=(0, 20), pady=15)
        
        # Editor content area
        editor_content = ModernFrame(editor_container, bg="#161b22")
        editor_content.pack(fill=tk.BOTH, expand=True)
        
        # Create modern text editor
        self.editor = ModernText(editor_content, bg="#0d1117", fg="#c9d1d9")
        self.editor.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=15, pady=15)
        
        # Create modern scrollbar
        self.editor_scrollbar = ModernScrollbar(editor_content, orient="vertical")
        self.editor_scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=15)
        self.editor_scrollbar.set_scrollable(self.editor)
        
        # Horizontal scrollbar
        self.editor_h_scrollbar = ModernScrollbar(editor_container, orient="horizontal")
        self.editor_h_scrollbar.pack(fill=tk.X, pady=(0, 15))
        self.editor_h_scrollbar.set_scrollable(self.editor)
        
    def create_output_panel(self, parent):
        """Create the modern output panel"""
        # Output container
        output_container = ModernFrame(parent, bg="#0d1117")
        output_container.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT, padx=(10, 20), pady=20)
        
        # Output header
        output_header = ModernFrame(output_container, bg="#161b22", height=50)
        output_header.pack(fill=tk.X, pady=(0, 10))
        
        title_label = ModernLabel(output_header, text="🖥️ Output & Terminal", 
                                font=("Segoe UI", 14, "bold"), fg="#ffffff")
        title_label.pack(side=tk.LEFT, padx=(20, 0), pady=15)
        
        # Clear output button
        ModernButton(output_header, text="🗑️ Clear", command=self.clear_output, 
                    style="danger", width=70, height=30).pack(side=tk.RIGHT, padx=(0, 20), pady=10)
        
        # Output content area
        output_content = ModernFrame(output_container, bg="#161b22")
        output_content.pack(fill=tk.BOTH, expand=True)
        
        # Create modern output text
        self.output_text = ModernText(output_content, bg="#0d1117", fg="#c9d1d9")
        self.output_text.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=15, pady=15)
        
        # Create modern scrollbar for output
        self.output_scrollbar = ModernScrollbar(output_content, orient="vertical")
        self.output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=15)
        self.output_scrollbar.set_scrollable(self.output_text)
        
        # Create code runner
        self.runner = CodeRunner(self.output_text)
        
    def create_status_bar(self):
        """Create the modern status bar"""
        # Status bar container
        self.status_bar = ModernFrame(self.main_container, bg="#161b22", height=30)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM, padx=0, pady=0)
        
        # Status information
        self.status_label = ModernLabel(self.status_bar, text="Ready", 
                                      font=("Segoe UI", 9), fg="#8b949e")
        self.status_label.pack(side=tk.LEFT, padx=(20, 0), pady=8)
        
        # Language indicator
        self.status_language_label = ModernLabel(self.status_bar, text="", 
                                               font=("Segoe UI", 9), fg="#8b949e")
        self.status_language_label.pack(side=tk.LEFT, padx=(20, 0), pady=8)
        
        # Encoding indicator
        self.encoding_label = ModernLabel(self.status_bar, text="UTF-8", 
                                        font=("Segoe UI", 9), fg="#8b949e")
        self.encoding_label.pack(side=tk.LEFT, padx=(20, 0), pady=8)
        
        # Position indicator
        self.position_label = ModernLabel(self.status_bar, text="Ln 1, Col 1", 
                                        font=("Segoe UI", 9), fg="#8b949e")
        self.position_label.pack(side=tk.RIGHT, padx=(0, 20), pady=8)
        
        # Bind text widget events for position updates
        self.editor.bind("<KeyRelease>", self.update_position)
        self.editor.bind("<Button-1>", self.update_position)
        
    def clear_output(self):
        """Clear the output panel"""
        self.output_text.delete(1.0, tk.END)
        self.update_status("Output cleared")
        
    def update_status(self, message):
        """Update status bar message"""
        self.status_label.configure(text=message)
        
    def update_position(self, event=None):
        """Update position indicator"""
        try:
            index = self.editor.index(tk.INSERT)
            line, col = index.split('.')
            self.position_label.configure(text=f"Ln {line}, Col {int(col)+1}")
        except:
            pass
            
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
        self.editor.delete(1.0, tk.END)
        self.file_label.configure(text="📝 New file")
        self.language_label.configure(text="")
        self.status_language_label.configure(text="")
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
                self.editor.delete(1.0, tk.END)
                self.editor.insert(1.0, content)
                self.current_file = file_path
                self.current_language = self.file_manager.get_language_from_extension(file_path)
                self.file_label.configure(text=f"📄 {os.path.basename(file_path)}")
                self.language_label.configure(text=f"🔤 {self.current_language.upper()}")
                self.status_language_label.configure(text=f"🔤 {self.current_language.upper()}")
                self.output_text.delete(1.0, tk.END)
                self.update_status(f"Opened {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {str(e)}")
                
    def save_file(self):
        """Save the current file"""
        if self.current_file:
            try:
                content = self.editor.get(1.0, tk.END)
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
                content = self.editor.get(1.0, tk.END)
                self.file_manager.save_file(file_path, content)
                self.current_file = file_path
                self.current_language = self.file_manager.get_language_from_extension(file_path)
                self.file_label.configure(text=f"📄 {os.path.basename(file_path)}")
                self.language_label.configure(text=f"🔤 {self.current_language.upper()}")
                self.status_language_label.configure(text=f"🔤 {self.current_language.upper()}")
                self.update_status(f"Saved as {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {str(e)}")
                
    def run_code(self):
        """Run the current code"""
        code = self.editor.get(1.0, tk.END)
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
        code = self.editor.get(1.0, tk.END)
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
                self.editor.delete(1.0, tk.END)
                self.editor.insert(1.0, fixed_code)
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
        self.update_status(f"Switched to {new_theme} theme")

def main():
    """Main entry point"""
    root = tk.Tk()
    app = ModernIDE(root)
    
    # Set window icon if available
    try:
        root.iconbitmap("icon.ico")
    except:
        pass
    
    root.mainloop()

if __name__ == "__main__":
    main() 
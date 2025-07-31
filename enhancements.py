#!/usr/bin/env python3
"""
Enhancements for Custom IDE
Additional VS Code-like features and improvements
"""

import tkinter as tk
from tkinter import ttk, messagebox
import re

class SearchPanel:
    """Search and replace functionality"""
    
    def __init__(self, parent, text_widget):
        self.parent = parent
        self.text_widget = text_widget
        self.search_frame = None
        self.search_var = tk.StringVar()
        self.replace_var = tk.StringVar()
        self.case_sensitive = tk.BooleanVar()
        self.whole_word = tk.BooleanVar()
        self.current_match = 0
        self.matches = []
        
    def show_search_panel(self):
        """Show the search panel"""
        if self.search_frame:
            self.search_frame.destroy()
            
        self.search_frame = ttk.Frame(self.parent, style="Panel.TFrame")
        self.search_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Search input
        search_label = ttk.Label(self.search_frame, text="🔍 Search:")
        search_label.pack(side=tk.LEFT, padx=(0, 5))
        
        search_entry = ttk.Entry(self.search_frame, textvariable=self.search_var, width=20)
        search_entry.pack(side=tk.LEFT, padx=(0, 5))
        search_entry.focus()
        
        # Replace input
        replace_label = ttk.Label(self.search_frame, text="🔄 Replace:")
        replace_label.pack(side=tk.LEFT, padx=(10, 5))
        
        replace_entry = ttk.Entry(self.search_frame, textvariable=self.replace_var, width=20)
        replace_entry.pack(side=tk.LEFT, padx=(0, 5))
        
        # Options
        case_check = ttk.Checkbutton(self.search_frame, text="Aa", variable=self.case_sensitive)
        case_check.pack(side=tk.LEFT, padx=(5, 0))
        
        word_check = ttk.Checkbutton(self.search_frame, text="Word", variable=self.whole_word)
        word_check.pack(side=tk.LEFT, padx=(5, 0))
        
        # Buttons
        ttk.Button(self.search_frame, text="⬆️", command=self.find_prev, 
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=(10, 2))
        ttk.Button(self.search_frame, text="⬇️", command=self.find_next, 
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=2)
        ttk.Button(self.search_frame, text="🔄 Replace", command=self.replace, 
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=(10, 2))
        ttk.Button(self.search_frame, text="🔄 Replace All", command=self.replace_all, 
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=2)
        ttk.Button(self.search_frame, text="❌", command=self.hide_search_panel, 
                  style="Toolbar.TButton").pack(side=tk.LEFT, padx=(10, 0))
        
        # Bind search on input change
        self.search_var.trace('w', self.on_search_change)
        
    def hide_search_panel(self):
        """Hide the search panel"""
        if self.search_frame:
            self.search_frame.destroy()
            self.search_frame = None
        self.clear_highlights()
        
    def on_search_change(self, *args):
        """Handle search input changes"""
        self.find_matches()
        
    def find_matches(self):
        """Find all matches in the text"""
        search_term = self.search_var.get()
        if not search_term:
            self.clear_highlights()
            return
            
        # Clear previous highlights
        self.clear_highlights()
        
        # Build regex pattern
        pattern = re.escape(search_term)
        if self.whole_word.get():
            pattern = r'\b' + pattern + r'\b'
        
        flags = 0 if self.case_sensitive.get() else re.IGNORECASE
        
        # Find all matches
        content = self.text_widget.get(1.0, tk.END)
        self.matches = list(re.finditer(pattern, content, flags))
        
        # Highlight matches
        for match in self.matches:
            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"
            self.text_widget.tag_add("search_highlight", start, end)
            
        # Configure highlight tag
        self.text_widget.tag_configure("search_highlight", 
                                     background="#ffff00", 
                                     foreground="#000000")
        
        # Update status
        if self.matches:
            self.current_match = 0
            self.highlight_current_match()
            
    def highlight_current_match(self):
        """Highlight the current match"""
        if not self.matches:
            return
            
        # Clear previous current match highlight
        self.text_widget.tag_remove("current_match", 1.0, tk.END)
        
        # Highlight current match
        match = self.matches[self.current_match]
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        self.text_widget.tag_add("current_match", start, end)
        
        # Configure current match tag
        self.text_widget.tag_configure("current_match", 
                                     background="#ff6b6b", 
                                     foreground="#ffffff")
        
        # Scroll to current match
        self.text_widget.see(start)
        
    def find_next(self):
        """Find next match"""
        if not self.matches:
            return
        self.current_match = (self.current_match + 1) % len(self.matches)
        self.highlight_current_match()
        
    def find_prev(self):
        """Find previous match"""
        if not self.matches:
            return
        self.current_match = (self.current_match - 1) % len(self.matches)
        self.highlight_current_match()
        
    def replace(self):
        """Replace current match"""
        if not self.matches:
            return
            
        match = self.matches[self.current_match]
        start = f"1.0+{match.start()}c"
        end = f"1.0+{match.end()}c"
        
        self.text_widget.delete(start, end)
        self.text_widget.insert(start, self.replace_var.get())
        
        # Refresh search
        self.find_matches()
        
    def replace_all(self):
        """Replace all matches"""
        if not self.matches:
            return
            
        # Confirm replacement
        result = messagebox.askyesno("Replace All", 
                                   f"Replace {len(self.matches)} occurrences?")
        if not result:
            return
            
        # Replace all matches (in reverse order to maintain positions)
        for match in reversed(self.matches):
            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"
            self.text_widget.delete(start, end)
            self.text_widget.insert(start, self.replace_var.get())
            
        # Clear search
        self.search_var.set("")
        self.clear_highlights()
        
    def clear_highlights(self):
        """Clear all search highlights"""
        self.text_widget.tag_remove("search_highlight", 1.0, tk.END)
        self.text_widget.tag_remove("current_match", 1.0, tk.END)
        self.matches = []

class Minimap:
    """Minimap for code overview"""
    
    def __init__(self, parent, text_widget):
        self.parent = parent
        self.text_widget = text_widget
        self.minimap_canvas = None
        self.scale_factor = 0.1
        
    def create_minimap(self):
        """Create the minimap"""
        if self.minimap_canvas:
            return
            
        # Create minimap frame
        minimap_frame = ttk.Frame(self.parent, style="Panel.TFrame")
        minimap_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(5, 0))
        
        # Create canvas
        self.minimap_canvas = tk.Canvas(minimap_frame, 
                                      width=100, 
                                      bg="#1e1e1e",
                                      highlightthickness=0)
        self.minimap_canvas.pack(fill=tk.Y, expand=True)
        
        # Bind events
        self.minimap_canvas.bind("<Button-1>", self.on_click)
        self.minimap_canvas.bind("<B1-Motion>", self.on_drag)
        
        # Update minimap
        self.update_minimap()
        
    def update_minimap(self):
        """Update the minimap display"""
        if not self.minimap_canvas:
            return
            
        self.minimap_canvas.delete("all")
        
        # Get text content
        content = self.text_widget.get(1.0, tk.END)
        lines = content.split('\n')
        
        # Calculate dimensions
        canvas_height = self.minimap_canvas.winfo_height()
        line_height = max(1, canvas_height // len(lines))
        
        # Draw lines
        for i, line in enumerate(lines):
            y = i * line_height
            if y >= canvas_height:
                break
                
            # Simple line representation
            if line.strip():
                # Non-empty line
                self.minimap_canvas.create_line(5, y, 95, y, 
                                              fill="#4ec9b0", 
                                              width=1)
            else:
                # Empty line
                self.minimap_canvas.create_line(5, y, 95, y, 
                                              fill="#3c3c3c", 
                                              width=1)
                
    def on_click(self, event):
        """Handle minimap click"""
        # Calculate line number
        canvas_height = self.minimap_canvas.winfo_height()
        content = self.text_widget.get(1.0, tk.END)
        lines = content.split('\n')
        line_height = max(1, canvas_height // len(lines))
        
        line_num = int(event.y // line_height) + 1
        line_num = min(line_num, len(lines))
        
        # Jump to line
        self.text_widget.see(f"{line_num}.0")
        
    def on_drag(self, event):
        """Handle minimap drag"""
        self.on_click(event)

class StatusBar:
    """Enhanced status bar with more information"""
    
    def __init__(self, parent, text_widget):
        self.parent = parent
        self.text_widget = text_widget
        self.status_frame = None
        self.status_label = None
        self.position_label = None
        self.encoding_label = None
        self.language_label = None
        
    def create_status_bar(self):
        """Create the enhanced status bar"""
        self.status_frame = ttk.Frame(self.parent, style="Toolbar.TFrame")
        self.status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Status information
        self.status_label = ttk.Label(self.status_frame, text="Ready", style="Status.TLabel")
        self.status_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # Language indicator
        self.language_label = ttk.Label(self.status_frame, text="", style="Status.TLabel")
        self.language_label.pack(side=tk.LEFT, padx=(20, 0))
        
        # Encoding indicator
        self.encoding_label = ttk.Label(self.status_frame, text="UTF-8", style="Status.TLabel")
        self.encoding_label.pack(side=tk.LEFT, padx=(20, 0))
        
        # Position indicator
        self.position_label = ttk.Label(self.status_frame, text="Ln 1, Col 1", style="Status.TLabel")
        self.position_label.pack(side=tk.RIGHT, padx=(0, 10))
        
        # Bind text widget events
        self.text_widget.bind("<KeyRelease>", self.update_position)
        self.text_widget.bind("<Button-1>", self.update_position)
        
    def update_position(self, event=None):
        """Update position indicator"""
        try:
            index = self.text_widget.index(tk.INSERT)
            line, col = index.split('.')
            self.position_label.config(text=f"Ln {line}, Col {int(col)+1}")
        except:
            pass
            
    def update_status(self, message):
        """Update status message"""
        if self.status_label:
            self.status_label.config(text=message)
            
    def update_language(self, language):
        """Update language indicator"""
        if self.language_label:
            self.language_label.config(text=f"🔤 {language.upper()}" if language else "")
            
    def update_encoding(self, encoding):
        """Update encoding indicator"""
        if self.encoding_label:
            self.encoding_label.config(text=encoding) 
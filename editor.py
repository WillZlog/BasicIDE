#!/usr/bin/env python3
"""
Code Editor Component
Provides syntax highlighting and code editing functionality with VS Code-like features
"""

import tkinter as tk
from tkinter import ttk
import re
import keyword

class CodeEditor(ttk.Frame):
    def __init__(self, parent, theme_manager):
        super().__init__(parent)
        self.theme_manager = theme_manager
        self.current_language = None
        self.line_numbers = True
        
        # Syntax highlighting patterns
        self.syntax_patterns = {
            'python': {
                'keywords': keyword.kwlist,
                'strings': r'"[^"]*"|\'[^\']*\'',
                'comments': r'#.*$',
                'numbers': r'\b\d+\.?\d*\b',
                'functions': r'\b\w+(?=\()',
                'classes': r'\bclass\s+(\w+)',
                'decorators': r'@\w+',
            },
            'javascript': {
                'keywords': ['function', 'var', 'let', 'const', 'if', 'else', 'for', 'while', 
                           'return', 'class', 'import', 'export', 'try', 'catch', 'finally',
                           'switch', 'case', 'default', 'break', 'continue', 'new', 'delete',
                           'typeof', 'instanceof', 'this', 'super', 'null', 'undefined', 'true', 'false',
                           'async', 'await', 'static', 'private', 'public', 'protected'],
                'strings': r'"[^"]*"|\'[^\']*\'|`[^`]*`',
                'comments': r'//.*$|/\*.*?\*/',
                'numbers': r'\b\d+\.?\d*\b',
                'functions': r'\b\w+(?=\()',
                'classes': r'\bclass\s+(\w+)',
                'template_literals': r'\$\{[^}]*\}',
            },
            'csharp': {
                'keywords': ['using', 'namespace', 'class', 'public', 'private', 'protected', 
                           'static', 'void', 'int', 'string', 'bool', 'double', 'float', 'char',
                           'if', 'else', 'for', 'while', 'foreach', 'switch', 'case', 'default',
                           'break', 'continue', 'return', 'new', 'try', 'catch', 'finally', 'throw',
                           'true', 'false', 'null', 'var', 'const', 'readonly', 'virtual', 'override',
                           'async', 'await', 'interface', 'enum', 'struct', 'delegate', 'event'],
                'strings': r'"[^"]*"|\'[^\']*\'',
                'comments': r'//.*$|/\*.*?\*/',
                'numbers': r'\b\d+\.?\d*\b',
                'functions': r'\b\w+(?=\()',
                'classes': r'\bclass\s+(\w+)',
                'interfaces': r'\binterface\s+(\w+)',
            },
            'html': {
                'tags': r'</?\w+[^>]*>',
                'attributes': r'\w+="[^"]*"',
                'comments': r'<!--.*?-->',
                'doctype': r'<!DOCTYPE[^>]*>',
                'entities': r'&[a-zA-Z]+;|&#\d+;',
            },
            'css': {
                'selectors': r'[.#]?\w+[^{]*{',
                'properties': r'\w+:\s*[^;]+;',
                'values': r':\s*[^;]+',
                'comments': r'/\*.*?\*/',
                'numbers': r'\b\d+\.?\d*\b',
                'units': r'\b(px|em|rem|%|vh|vw|deg|rad)\b',
                'colors': r'#[0-9a-fA-F]{3,6}|\b(rgb|rgba|hsl|hsla)\s*\(',
            },
            'json': {
                'keys': r'"[^"]*":',
                'strings': r'"[^"]*"',
                'numbers': r'\b\d+\.?\d*\b',
                'booleans': r'\b(true|false|null)\b',
            }
        }
        
        self.setup_editor()
        
    def setup_editor(self):
        """Setup the code editor with text widget and scrollbars"""
        # Create main editor frame
        editor_frame = ttk.Frame(self, style="Panel.TFrame")
        editor_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create line numbers widget
        self.line_numbers_widget = tk.Text(
            editor_frame,
            width=6,
            padx=8,
            pady=10,
            takefocus=0,
            border=0,
            font=("Consolas", 12),
            bg="#1e1e1e",
            fg="#858585",
            insertbackground="#858585",
            selectbackground="#264f78",
            selectforeground="#ffffff",
            relief="flat",
            state="disabled"
        )
        self.line_numbers_widget.pack(side=tk.LEFT, fill=tk.Y)
        
        # Create text widget
        self.text_widget = tk.Text(
            editor_frame,
            wrap=tk.NONE,
            font=("Consolas", 12),
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="#ffffff",
            selectbackground="#264f78",
            selectforeground="#ffffff",
            padx=10,
            pady=10,
            undo=True,
            relief="flat",
            borderwidth=0
        )
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create scrollbars
        self.v_scrollbar = ttk.Scrollbar(editor_frame, orient=tk.VERTICAL, command=self.yview)
        self.h_scrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.text_widget.xview)
        
        # Configure text widget scrolling
        self.text_widget.configure(
            yscrollcommand=self.yview,
            xscrollcommand=self.h_scrollbar.set
        )
        
        # Pack scrollbars
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Configure grid weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Bind events
        self.text_widget.bind("<KeyRelease>", self.on_text_change)
        self.text_widget.bind("<Tab>", self.handle_tab)
        self.text_widget.bind("<Shift-Tab>", self.handle_shift_tab)
        self.text_widget.bind("<Key>", self.on_key_press)
        self.text_widget.bind("<MouseWheel>", self.on_mousewheel)
        self.text_widget.bind("<Button-1>", self.on_click)
        
        # Apply initial theme
        self.apply_theme(self.theme_manager.get_current_theme())
        
    def yview(self, *args):
        """Synchronize scrolling between text widget and line numbers"""
        self.text_widget.yview(*args)
        self.line_numbers_widget.yview(*args)
        
    def on_key_press(self, event):
        """Handle key press events"""
        self.update_line_numbers()
        
    def on_click(self, event):
        """Handle click events"""
        self.update_line_numbers()
        
    def on_mousewheel(self, event):
        """Handle mouse wheel events"""
        self.update_line_numbers()
        
    def update_line_numbers(self):
        """Update line numbers display"""
        if not self.line_numbers:
            return
            
        try:
            # Get current content
            content = self.text_widget.get(1.0, tk.END)
            lines = content.split('\n')
            
            # Update line numbers widget
            self.line_numbers_widget.config(state="normal")
            self.line_numbers_widget.delete(1.0, tk.END)
            
            for i in range(1, len(lines) + 1):
                self.line_numbers_widget.insert(tk.END, f"{i}\n")
                
            self.line_numbers_widget.config(state="disabled")
            
            # Synchronize scroll position
            self.line_numbers_widget.yview_moveto(self.text_widget.yview()[0])
            
        except Exception as e:
            # Silently ignore errors
            pass
        
    def handle_tab(self, event):
        """Handle tab key for indentation"""
        self.text_widget.insert(tk.INSERT, "    ")
        return "break"
        
    def handle_shift_tab(self, event):
        """Handle shift+tab for unindentation"""
        try:
            current_line = self.text_widget.get("insert linestart", "insert")
            if current_line.startswith("    "):
                self.text_widget.delete("insert-4c", "insert")
        except:
            pass
        return "break"
        
    def on_text_change(self, event=None):
        """Handle text changes for syntax highlighting"""
        self.highlight_syntax()
        self.update_line_numbers()
        
    def set_language(self, language):
        """Set the programming language for syntax highlighting"""
        self.current_language = language
        self.highlight_syntax()
        
    def highlight_syntax(self):
        """Apply syntax highlighting based on current language"""
        if not self.current_language or self.current_language not in self.syntax_patterns:
            return
            
        # Get current content
        content = self.text_widget.get(1.0, tk.END)
        if not content.strip():
            return
            
        # Remove existing tags
        for tag in self.text_widget.tag_names():
            if tag != "sel":
                self.text_widget.tag_remove(tag, 1.0, tk.END)
                
        # Apply highlighting based on language
        patterns = self.syntax_patterns[self.current_language]
        theme = self.theme_manager.get_current_theme()
        
        if self.current_language == 'python':
            self._highlight_python(patterns, theme)
        elif self.current_language == 'javascript':
            self._highlight_javascript(patterns, theme)
        elif self.current_language == 'csharp':
            self._highlight_csharp(patterns, theme)
        elif self.current_language == 'html':
            self._highlight_html(patterns, theme)
        elif self.current_language == 'css':
            self._highlight_css(patterns, theme)
        elif self.current_language == 'json':
            self._highlight_json(patterns, theme)
            
    def _highlight_python(self, patterns, theme):
        """Highlight Python syntax"""
        # Keywords
        for keyword in patterns['keywords']:
            self._highlight_pattern(r'\b' + re.escape(keyword) + r'\b', 
                                  'keyword', theme['keyword_color'])
        
        # Strings
        self._highlight_pattern(patterns['strings'], 'string', theme['string_color'])
        
        # Comments
        self._highlight_pattern(patterns['comments'], 'comment', theme['comment_color'])
        
        # Numbers
        self._highlight_pattern(patterns['numbers'], 'number', theme['number_color'])
        
        # Functions
        self._highlight_pattern(patterns['functions'], 'function', theme['function_color'])
        
        # Classes
        self._highlight_pattern(patterns['classes'], 'class', theme['class_color'])
        
        # Decorators
        self._highlight_pattern(patterns['decorators'], 'decorator', theme['keyword_color'])
        
    def _highlight_javascript(self, patterns, theme):
        """Highlight JavaScript syntax"""
        # Keywords
        for keyword in patterns['keywords']:
            self._highlight_pattern(r'\b' + re.escape(keyword) + r'\b', 
                                  'keyword', theme['keyword_color'])
        
        # Strings
        self._highlight_pattern(patterns['strings'], 'string', theme['string_color'])
        
        # Comments
        self._highlight_pattern(patterns['comments'], 'comment', theme['comment_color'])
        
        # Numbers
        self._highlight_pattern(patterns['numbers'], 'number', theme['number_color'])
        
        # Functions
        self._highlight_pattern(patterns['functions'], 'function', theme['function_color'])
        
        # Classes
        self._highlight_pattern(patterns['classes'], 'class', theme['class_color'])
        
        # Template literals
        self._highlight_pattern(patterns['template_literals'], 'template', theme['string_color'])
        
    def _highlight_csharp(self, patterns, theme):
        """Highlight C# syntax"""
        # Keywords
        for keyword in patterns['keywords']:
            self._highlight_pattern(r'\b' + re.escape(keyword) + r'\b', 
                                  'keyword', theme['keyword_color'])
        
        # Strings
        self._highlight_pattern(patterns['strings'], 'string', theme['string_color'])
        
        # Comments
        self._highlight_pattern(patterns['comments'], 'comment', theme['comment_color'])
        
        # Numbers
        self._highlight_pattern(patterns['numbers'], 'number', theme['number_color'])
        
        # Functions
        self._highlight_pattern(patterns['functions'], 'function', theme['function_color'])
        
        # Classes
        self._highlight_pattern(patterns['classes'], 'class', theme['class_color'])
        
        # Interfaces
        self._highlight_pattern(patterns['interfaces'], 'interface', theme['class_color'])
        
    def _highlight_html(self, patterns, theme):
        """Highlight HTML syntax"""
        # Tags
        self._highlight_pattern(patterns['tags'], 'tag', theme['tag_color'])
        
        # Attributes
        self._highlight_pattern(patterns['attributes'], 'attribute', theme['attribute_color'])
        
        # Comments
        self._highlight_pattern(patterns['comments'], 'comment', theme['comment_color'])
        
        # DOCTYPE
        self._highlight_pattern(patterns['doctype'], 'doctype', theme['doctype_color'])
        
        # Entities
        self._highlight_pattern(patterns['entities'], 'entity', theme['string_color'])
        
    def _highlight_css(self, patterns, theme):
        """Highlight CSS syntax"""
        # Selectors
        self._highlight_pattern(patterns['selectors'], 'selector', theme['selector_color'])
        
        # Properties
        self._highlight_pattern(patterns['properties'], 'property', theme['property_color'])
        
        # Values
        self._highlight_pattern(patterns['values'], 'value', theme['value_color'])
        
        # Comments
        self._highlight_pattern(patterns['comments'], 'comment', theme['comment_color'])
        
        # Numbers
        self._highlight_pattern(patterns['numbers'], 'number', theme['number_color'])
        
        # Units
        self._highlight_pattern(patterns['units'], 'unit', theme['number_color'])
        
        # Colors
        self._highlight_pattern(patterns['colors'], 'color', theme['string_color'])
        
    def _highlight_json(self, patterns, theme):
        """Highlight JSON syntax"""
        # Keys
        self._highlight_pattern(patterns['keys'], 'key', theme['key_color'])
        
        # Strings
        self._highlight_pattern(patterns['strings'], 'string', theme['string_color'])
        
        # Numbers
        self._highlight_pattern(patterns['numbers'], 'number', theme['number_color'])
        
        # Booleans and null
        self._highlight_pattern(patterns['booleans'], 'boolean', theme['boolean_color'])
        
    def _highlight_pattern(self, pattern, tag_name, color):
        """Apply highlighting for a specific pattern"""
        try:
            # Create tag if it doesn't exist
            if tag_name not in self.text_widget.tag_names():
                self.text_widget.tag_configure(tag_name, foreground=color)
            
            # Find and tag all matches
            content = self.text_widget.get(1.0, tk.END)
            for match in re.finditer(pattern, content, re.MULTILINE):
                start = f"1.0+{match.start()}c"
                end = f"1.0+{match.end()}c"
                self.text_widget.tag_add(tag_name, start, end)
        except Exception as e:
            # Silently ignore highlighting errors
            pass
            
    def get_content(self):
        """Get the current content of the editor"""
        return self.text_widget.get(1.0, tk.END)
        
    def set_content(self, content):
        """Set the content of the editor"""
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(1.0, content)
        self.highlight_syntax()
        self.update_line_numbers()
        
    def clear(self):
        """Clear the editor content"""
        self.text_widget.delete(1.0, tk.END)
        self.update_line_numbers()
        
    def apply_theme(self, theme):
        """Apply theme colors to the editor"""
        # Apply to text widget
        self.text_widget.configure(
            bg=theme["editor_bg"],
            fg=theme["editor_fg"],
            insertbackground=theme["cursor_color"],
            selectbackground=theme["select_bg"],
            selectforeground=theme["select_fg"]
        )
        
        # Apply to line numbers widget
        self.line_numbers_widget.configure(
            bg=theme["editor_bg"],
            fg=theme.get("line_number_color", "#858585"),
            insertbackground=theme.get("line_number_color", "#858585"),
            selectbackground=theme["select_bg"],
            selectforeground=theme["select_fg"]
        )
        
        # Reconfigure existing tags with new colors
        for tag_name in self.text_widget.tag_names():
            if tag_name == "sel":
                continue
            if tag_name in theme:
                self.text_widget.tag_configure(tag_name, foreground=theme[tag_name])
                
    def toggle_line_numbers(self):
        """Toggle line numbers display"""
        self.line_numbers = not self.line_numbers
        if self.line_numbers:
            self.line_numbers_widget.pack(side=tk.LEFT, fill=tk.Y)
            self.update_line_numbers()
        else:
            self.line_numbers_widget.pack_forget() 
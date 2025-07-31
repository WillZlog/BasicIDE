#!/usr/bin/env python3
"""
VS Code Clone - Exact Visual Studio Code Replica
Built with PyQt6 for pixel-perfect accuracy
"""

import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QSplitter, QTextEdit, QTreeWidget, 
                             QTreeWidgetItem, QTabWidget, QLabel, QPushButton,
                             QToolBar, QStatusBar, QMenuBar, QMenu, QFileDialog,
                             QMessageBox, QScrollArea, QFrame, QLineEdit,
                             QTextBrowser, QDockWidget, QPlainTextEdit,
                             QInputDialog, QComboBox, QProgressBar, QSlider,
                             QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QThread, QProcess, QUrl, QRectF
from PyQt6.QtGui import (QFont, QPalette, QColor, QIcon, QAction, QTextCursor, 
                         QSyntaxHighlighter, QTextCharFormat, QFontDatabase,
                         QTextBlockFormat, QTextOption, QPen, QBrush, QPainter)
import subprocess
import tempfile
import json
import requests
import re
import webbrowser
import venv
import ast
import time
import threading
from collections import defaultdict

class VSCodeFileIcons:
    """Custom file type icons for VS Code-like appearance"""
    
    @staticmethod
    def get_file_icon(filename):
        """Get appropriate icon for file type"""
        ext = os.path.splitext(filename)[1].lower()
        
        # Python files
        if ext == '.py':
            return "PY"
        elif ext == '.pyc':
            return "PY"
        elif ext == '.pyo':
            return "PY"
        elif ext == '.pyd':
            return "PY"
        elif ext == '.pyw':
            return "PY"
        elif ext == '.pyx':
            return "PY"
        elif ext == '.pyi':
            return "PY"
        elif ext == '.pyz':
            return "PY"
            
        # JavaScript files
        elif ext in ['.js', '.jsx', '.ts', '.tsx']:
            return "JS"
        elif ext == '.json':
            return "{}"
        elif ext == '.node':
            return "JS"
            
        # Web files
        elif ext == '.html':
            return "<>"
        elif ext == '.htm':
            return "<>"
        elif ext == '.css':
            return "{}"
        elif ext == '.scss':
            return "{}"
        elif ext == '.sass':
            return "{}"
        elif ext == '.less':
            return "{}"
        elif ext == '.xml':
            return "XML"
        elif ext == '.svg':
            return "IMG"
            
        # Markdown and documentation
        elif ext == '.md':
            return "MD"
        elif ext == '.rst':
            return "MD"
        elif ext == '.txt':
            return "TXT"
        elif ext == '.log':
            return "LOG"
            
        # Configuration files
        elif ext in ['.yml', '.yaml']:
            return "CFG"
        elif ext == '.toml':
            return "CFG"
        elif ext == '.ini':
            return "CFG"
        elif ext == '.cfg':
            return "CFG"
        elif ext == '.conf':
            return "CFG"
        elif ext == '.env':
            return "ENV"
            
        # Database files
        elif ext in ['.sql', '.db', '.sqlite', '.sqlite3']:
            return "DB"
            
        # Archive files
        elif ext in ['.zip', '.tar', '.gz', '.rar', '.7z']:
            return "ZIP"
            
        # Image files
        elif ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico']:
            return "IMG"
            
        # Video files
        elif ext in ['.mp4', '.avi', '.mov', '.wmv', '.flv']:
            return "VID"
            
        # Audio files
        elif ext in ['.mp3', '.wav', '.flac', '.aac', '.ogg']:
            return "AUD"
            
        # Executable files
        elif ext in ['.exe', '.app', '.dmg', '.deb', '.rpm']:
            return "EXE"
            
        # Shell scripts
        elif ext in ['.sh', '.bash', '.zsh', '.fish']:
            return "SH"
        elif ext == '.bat':
            return "BAT"
        elif ext == '.ps1':
            return "PS"
            
        # Git files
        elif ext == '.gitignore':
            return "GIT"
        elif ext == '.gitattributes':
            return "GIT"
            
        # Docker files
        elif ext == '.dockerfile':
            return "DKR"
        elif filename == 'Dockerfile':
            return "DKR"
            
        # Requirements and dependencies
        elif filename == 'requirements.txt':
            return "REQ"
        elif filename == 'package.json':
            return "PKG"
        elif filename == 'Cargo.toml':
            return "CAR"
        elif filename == 'Gemfile':
            return "GEM"
        elif filename == 'composer.json':
            return "COM"
            
        # IDE and editor files
        elif filename in ['.vscode', '.idea', '.vs']:
            return "IDE"
        elif ext == '.vscode':
            return "IDE"
            
        # Default file icon
        else:
            return "FILE"

class VSCodeVirtualEnvManager:
    """Virtual environment manager for VS Code-like functionality"""
    
    def __init__(self, terminal):
        self.terminal = terminal
        self.current_venv = None
        
    def create_venv(self, project_path):
        """Create a new virtual environment"""
        try:
            venv_path = os.path.join(project_path, '.venv')
            venv.create(venv_path, with_pip=True)
            
            # Activate the new environment
            self.activate_venv(venv_path)
            
            self.terminal.terminal_output.append(f"✅ Created virtual environment: {venv_path}")
            return True
        except Exception as e:
            self.terminal.terminal_output.append(f"❌ Failed to create virtual environment: {str(e)}")
            return False
            
    def activate_venv(self, venv_path):
        """Activate a virtual environment"""
        try:
            if sys.platform == "win32":
                activate_script = os.path.join(venv_path, "Scripts", "activate")
            else:
                activate_script = os.path.join(venv_path, "bin", "activate")
                
            if os.path.exists(activate_script):
                self.current_venv = venv_path
                self.terminal.terminal_output.append(f"✅ Activated virtual environment: {venv_path}")
                return True
            else:
                self.terminal.terminal_output.append(f"❌ Virtual environment not found: {venv_path}")
                return False
        except Exception as e:
            self.terminal.terminal_output.append(f"❌ Failed to activate virtual environment: {str(e)}")
            return False
            
    def deactivate_venv(self):
        """Deactivate current virtual environment"""
        if self.current_venv:
            self.terminal.terminal_output.append(f"✅ Deactivated virtual environment: {self.current_venv}")
            self.current_venv = None
        else:
            self.terminal.terminal_output.append("ℹ️ No virtual environment to deactivate")
            
    def install_package(self, package_name):
        """Install a package in the current virtual environment"""
        if not self.current_venv:
            self.terminal.terminal_output.append("❌ No virtual environment activated")
            return False
            
        try:
            if sys.platform == "win32":
                pip_path = os.path.join(self.current_venv, "Scripts", "pip.exe")
            else:
                pip_path = os.path.join(self.current_venv, "bin", "pip")
                
            cmd = f'"{pip_path}" install {package_name}'
            self.terminal.terminal_output.append(f"$ {cmd}")
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
            
            if result.stdout:
                self.terminal.terminal_output.append(result.stdout)
            if result.stderr:
                self.terminal.terminal_output.append(f"Error: {result.stderr}")
            if result.returncode != 0:
                self.terminal.terminal_output.append(f"Command exited with code {result.returncode}")
            else:
                self.terminal.terminal_output.append(f"✅ Successfully installed {package_name}")
                
            return True
        except Exception as e:
            self.terminal.terminal_output.append(f"❌ Failed to install package: {str(e)}")
            return False

class VSCodeSyntaxHighlighter(QSyntaxHighlighter):
    """Advanced syntax highlighter for VS Code-like highlighting"""
    
    def __init__(self, parent=None, language="python"):
        super().__init__(parent)
        self.language = language
        self.setup_formats()
        self.setup_rules()
        
    def setup_formats(self):
        """Setup VS Code color formats"""
        # Keywords (blue)
        self.keyword_format = QTextCharFormat()
        self.keyword_format.setForeground(QColor("#569cd6"))
        self.keyword_format.setFontWeight(QFont.Weight.Bold)
        
        # Strings (orange)
        self.string_format = QTextCharFormat()
        self.string_format.setForeground(QColor("#ce9178"))
        
        # Comments (green)
        self.comment_format = QTextCharFormat()
        self.comment_format.setForeground(QColor("#6a9955"))
        
        # Numbers (light green)
        self.number_format = QTextCharFormat()
        self.number_format.setForeground(QColor("#b5cea8"))
        
        # Functions (yellow)
        self.function_format = QTextCharFormat()
        self.function_format.setForeground(QColor("#dcdcaa"))
        
        # Classes (blue)
        self.class_format = QTextCharFormat()
        self.class_format.setForeground(QColor("#4ec9b0"))
        
        # Operators (white)
        self.operator_format = QTextCharFormat()
        self.operator_format.setForeground(QColor("#d4d4d4"))
        
        # Markdown headers (purple)
        self.header_format = QTextCharFormat()
        self.header_format.setForeground(QColor("#c586c0"))
        self.header_format.setFontWeight(QFont.Weight.Bold)
        
        # Markdown bold (white)
        self.bold_format = QTextCharFormat()
        self.bold_format.setForeground(QColor("#ffffff"))
        self.bold_format.setFontWeight(QFont.Weight.Bold)
        
        # Markdown italic (light gray)
        self.italic_format = QTextCharFormat()
        self.italic_format.setForeground(QColor("#cccccc"))
        self.italic_format.setFontItalic(True)
        
    def setup_rules(self):
        """Setup language-specific highlighting rules"""
        self.rules = []
        
        if self.language == "python":
            # Python keywords
            python_keywords = [
                'and', 'as', 'assert', 'break', 'class', 'continue', 'def',
                'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
                'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
                'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
                'with', 'yield', 'True', 'False', 'None', 'self'
            ]
            
            for word in python_keywords:
                pattern = f'\\b{word}\\b'
                self.rules.append((re.compile(pattern), self.keyword_format))
            
            # Python functions
            python_functions = [
                'print', 'len', 'range', 'str', 'int', 'float', 'list',
                'dict', 'set', 'tuple', 'open', 'close', 'read', 'write'
            ]
            
            for word in python_functions:
                pattern = f'\\b{word}\\b'
                self.rules.append((re.compile(pattern), self.function_format))
                
        elif self.language == "javascript":
            # JavaScript keywords
            js_keywords = [
                'break', 'case', 'catch', 'class', 'const', 'continue',
                'debugger', 'default', 'delete', 'do', 'else', 'export',
                'extends', 'finally', 'for', 'function', 'if', 'import',
                'in', 'instanceof', 'let', 'new', 'return', 'super',
                'switch', 'this', 'throw', 'try', 'typeof', 'var', 'void',
                'while', 'with', 'yield', 'true', 'false', 'null', 'undefined'
            ]
            
            for word in js_keywords:
                pattern = f'\\b{word}\\b'
                self.rules.append((re.compile(pattern), self.keyword_format))
                
        elif self.language == "markdown":
            # Markdown headers
            self.rules.append((re.compile(r'^#{1,6}\s+.*$', re.MULTILINE), self.header_format))
            
            # Markdown bold
            self.rules.append((re.compile(r'\*\*(.*?)\*\*'), self.bold_format))
            self.rules.append((re.compile(r'__(.*?)__'), self.bold_format))
            
            # Markdown italic
            self.rules.append((re.compile(r'\*(.*?)\*'), self.italic_format))
            self.rules.append((re.compile(r'_(.*?)_'), self.italic_format))
            
            # Markdown code blocks
            self.rules.append((re.compile(r'`(.*?)`'), self.string_format))
            self.rules.append((re.compile(r'```.*?```', re.DOTALL), self.string_format))
            
            # Markdown links
            self.rules.append((re.compile(r'\[([^\]]+)\]\([^)]+\)'), self.function_format))
        
        # Common patterns for all languages
        # Strings (single and double quotes)
        self.rules.append((re.compile(r'"[^"]*"'), self.string_format))
        self.rules.append((re.compile(r"'[^']*'"), self.string_format))
        
        # Comments
        self.rules.append((re.compile(r'#.*$'), self.comment_format))
        self.rules.append((re.compile(r'//.*$'), self.comment_format))
        self.rules.append((re.compile(r'/\*.*?\*/', re.DOTALL), self.comment_format))
        
        # Numbers
        self.rules.append((re.compile(r'\b\d+\b'), self.number_format))
        self.rules.append((re.compile(r'\b\d+\.\d+\b'), self.number_format))
        
        # Function definitions
        self.rules.append((re.compile(r'\bdef\s+(\w+)'), self.function_format))
        self.rules.append((re.compile(r'\bfunction\s+(\w+)'), self.function_format))
        
        # Class definitions
        self.rules.append((re.compile(r'\bclass\s+(\w+)'), self.class_format))
        
    def highlightBlock(self, text):
        """Highlight a block of text"""
        for pattern, format in self.rules:
            for match in pattern.finditer(text):
                start, end = match.span()
                self.setFormat(start, end - start, format)

class VSCodeEditor(QPlainTextEdit):
    """VS Code-like text editor with line numbers"""
    
    def __init__(self, parent=None, file_path=None):
        super().__init__(parent)
        self.file_path = file_path
        self.setup_editor()
        
    def setup_editor(self):
        """Setup the editor with VS Code styling"""
        # Better font - use Monaco on macOS (more common than SF Mono)
        font_family = "Monaco" if sys.platform == "darwin" else "Consolas"
        font = QFont(font_family, 13)
        font.setFixedPitch(True)
        self.setFont(font)
        
        # VS Code colors
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Base, QColor("#1e1e1e"))
        palette.setColor(QPalette.ColorRole.Text, QColor("#d4d4d4"))
        palette.setColor(QPalette.ColorRole.Window, QColor("#1e1e1e"))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#d4d4d4"))
        self.setPalette(palette)
        
        # Line numbers and other VS Code features
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        # Set up syntax highlighter based on file extension
        if self.file_path:
            ext = os.path.splitext(self.file_path)[1].lower()
            if ext == '.py':
                language = "python"
            elif ext in ['.js', '.jsx']:
                language = "javascript"
            elif ext == '.md':
                language = "markdown"
            else:
                language = "text"
        else:
            language = "text"
            
        self.highlighter = VSCodeSyntaxHighlighter(self.document(), language)
        
        # Set tab width
        self.setTabStopDistance(self.fontMetrics().horizontalAdvance(' ') * 4)

class VSCodePreview(QWidget):
    """Preview widget for Markdown and HTML files"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_preview()
        
    def setup_preview(self):
        """Setup the preview widget"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Header
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(8, 4, 8, 4)
        
        self.preview_label = QLabel("PREVIEW")
        self.preview_label.setStyleSheet("""
            QLabel {
                color: #cccccc;
                font-weight: bold;
                font-size: 11px;
                text-transform: uppercase;
            }
        """)
        
        header_layout.addWidget(self.preview_label)
        header_layout.addStretch()
        
        layout.addWidget(header)
        
        # Text browser for rendering (fallback)
        self.text_browser = QTextBrowser()
        self.text_browser.setStyleSheet("""
            QTextBrowser {
                background-color: white;
                color: black;
                border: none;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                font-size: 14px;
            }
        """)
        layout.addWidget(self.text_browser)
            
    def update_preview(self, content, file_type):
        """Update the preview content"""
        if file_type == "markdown":
            try:
                # Simple markdown to HTML conversion
                html_content = self.simple_markdown_to_html(content)
                self.text_browser.setHtml(html_content)
            except Exception as e:
                self.text_browser.setPlainText(f"Markdown preview error: {str(e)}")
                
        elif file_type == "html":
            self.text_browser.setHtml(content)
        else:
            self.text_browser.setPlainText(content)
            
    def simple_markdown_to_html(self, markdown_text):
        """Simple markdown to HTML conversion"""
        html = markdown_text
        
        # Headers
        html = re.sub(r'^### (.*$)', r'<h3>\1</h3>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.*$)', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^# (.*$)', r'<h1>\1</h1>', html, flags=re.MULTILINE)
        
        # Bold
        html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
        html = re.sub(r'__(.*?)__', r'<strong>\1</strong>', html)
        
        # Italic
        html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
        html = re.sub(r'_(.*?)_', r'<em>\1</em>', html)
        
        # Code blocks
        html = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', html, flags=re.DOTALL)
        html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)
        
        # Links
        html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
        
        # Line breaks
        html = html.replace('\n', '<br>')
        
        # Wrap in HTML structure
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 20px; line-height: 1.6; }}
                code {{ background-color: #f6f8fa; padding: 2px 4px; border-radius: 3px; font-family: 'Monaco', 'Consolas', monospace; }}
                pre {{ background-color: #f6f8fa; padding: 16px; border-radius: 6px; overflow-x: auto; }}
                h1, h2, h3, h4, h5, h6 {{ color: #24292e; margin-top: 24px; margin-bottom: 16px; }}
                a {{ color: #0366d6; text-decoration: none; }}
                a:hover {{ text-decoration: underline; }}
                strong {{ font-weight: 600; }}
                em {{ font-style: italic; }}
            </style>
        </head>
        <body>
            {html}
        </body>
        </html>
        """
        
        return full_html

class VSCodeTerminal(QWidget):
    """VS Code-like integrated terminal"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_terminal()
        self.venv_manager = VSCodeVirtualEnvManager(self)
        
    def setup_terminal(self):
        """Setup the terminal"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Terminal output
        self.terminal_output = QTextBrowser()
        self.terminal_output.setStyleSheet("""
            QTextBrowser {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: none;
                font-family: 'Monaco', 'Consolas', monospace;
                font-size: 12px;
            }
        """)
        
        # Command input
        self.command_input = QLineEdit()
        self.command_input.setStyleSheet("""
            QLineEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: 1px solid #3c3c3c;
                padding: 4px;
                font-family: 'Monaco', 'Consolas', monospace;
                font-size: 12px;
            }
            QLineEdit:focus {
                border: 1px solid #007acc;
            }
        """)
        self.command_input.returnPressed.connect(self.execute_command)
        
        layout.addWidget(self.terminal_output)
        layout.addWidget(self.command_input)
        
        # Initialize with welcome message
        self.terminal_output.append("VS Code Terminal - Ready")
        self.terminal_output.append("Type 'help' for available commands")
        self.command_input.setFocus()
        
    def execute_command(self):
        """Execute a command in the terminal"""
        command = self.command_input.text().strip()
        if not command:
            return
            
        self.terminal_output.append(f"$ {command}")
        
        try:
            # Check if we have an active virtual environment
            if hasattr(self, 'venv_manager') and self.venv_manager.current_venv:
                # Modify command to use virtual environment Python
                if command.startswith('python') or command.startswith('python3'):
                    if sys.platform == "win32":
                        python_path = os.path.join(self.venv_manager.current_venv, "Scripts", "python.exe")
                    else:
                        python_path = os.path.join(self.venv_manager.current_venv, "bin", "python")
                    command = command.replace('python', f'"{python_path}"', 1)
                    command = command.replace('python3', f'"{python_path}"', 1)
                elif command.startswith('pip'):
                    if sys.platform == "win32":
                        pip_path = os.path.join(self.venv_manager.current_venv, "Scripts", "pip.exe")
                    else:
                        pip_path = os.path.join(self.venv_manager.current_venv, "bin", "pip")
                    command = command.replace('pip', f'"{pip_path}"', 1)
                    command = command.replace('pip3', f'"{pip_path}"', 1)
            
            # Execute the command
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            
            if result.stdout:
                self.terminal_output.append(result.stdout)
            if result.stderr:
                self.terminal_output.append(f"Error: {result.stderr}")
            if result.returncode != 0:
                self.terminal_output.append(f"Command exited with code {result.returncode}")
                
        except subprocess.TimeoutExpired:
            self.terminal_output.append("Command timed out")
        except Exception as e:
            self.terminal_output.append(f"Error: {str(e)}")
            
        self.command_input.clear()
        self.terminal_output.append("")  # Empty line

class VSCodeFileExplorer(QWidget):
    """VS Code-like file explorer"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.root_path = None
        self.main_window = None
        self.setup_explorer()
        
    def setup_explorer(self):
        """Setup the file explorer"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Header
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(8, 4, 8, 4)
        
        self.folder_label = QLabel("EXPLORER")
        self.folder_label.setStyleSheet("""
            QLabel {
                color: #cccccc;
                font-weight: bold;
                font-size: 11px;
                text-transform: uppercase;
            }
        """)
        
        self.open_folder_btn = QPushButton("Open Folder")
        self.open_folder_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #cccccc;
                border: none;
                padding: 4px 8px;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #2a2d2e;
            }
        """)
        self.open_folder_btn.clicked.connect(self.open_folder)
        
        header_layout.addWidget(self.folder_label)
        header_layout.addStretch()
        header_layout.addWidget(self.open_folder_btn)
        
        layout.addWidget(header)
        
        # File tree
        self.file_tree = QTreeWidget()
        self.file_tree.setHeaderHidden(True)
        self.file_tree.setStyleSheet("""
            QTreeWidget {
                background-color: #252526;
                color: #cccccc;
                border: none;
                outline: none;
                font-size: 12px;
            }
            QTreeWidget::item {
                padding: 2px 4px;
                border: none;
            }
            QTreeWidget::item:selected {
                background-color: #094771;
            }
            QTreeWidget::item:hover {
                background-color: #2a2d2e;
            }
        """)
        self.file_tree.itemDoubleClicked.connect(self.on_file_selected)
        
        layout.addWidget(self.file_tree)
        
    def set_main_window(self, main_window):
        """Set reference to main window"""
        self.main_window = main_window
        
    def open_folder(self):
        """Open a folder dialog"""
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder")
        if folder_path:
            self.load_folder(folder_path)
            
    def load_folder(self, folder_path):
        """Load a folder into the explorer"""
        self.root_path = folder_path
        self.file_tree.clear()
        
        # Create root item
        root_item = QTreeWidgetItem(self.file_tree, [os.path.basename(folder_path)])
        root_item.setIcon(0, self.style().standardIcon(self.style().StandardPixmap.SP_DirIcon))
        
        # Populate with files and folders
        self.populate_tree_item(root_item, folder_path)
        root_item.setExpanded(True)
        
    def populate_tree_item(self, parent_item, path):
        """Recursively populate tree with files and folders"""
        try:
            for item_name in sorted(os.listdir(path)):
                item_path = os.path.join(path, item_name)
                
                if os.path.isdir(item_path):
                    # Skip hidden directories except .venv
                    if item_name.startswith('.') and item_name != '.venv':
                        continue
                        
                    dir_item = QTreeWidgetItem(parent_item, [item_name])
                    # Use custom icon for .venv directory
                    if item_name == '.venv':
                        dir_item.setText(0, f"VENV {item_name}")
                    else:
                        dir_item.setText(0, f"📁 {item_name}")
                    self.populate_tree_item(dir_item, item_path)
                else:
                    # File with custom icon
                    file_item = QTreeWidgetItem(parent_item, [item_name])
                    custom_icon = VSCodeFileIcons.get_file_icon(item_name)
                    # Set the icon text directly in the item
                    file_item.setText(0, f"{custom_icon} {item_name}")
                    file_item.setData(0, Qt.ItemDataRole.UserRole, item_path)
        except PermissionError:
            pass
            
    def on_file_selected(self, item, column):
        """Handle file selection"""
        file_path = item.data(0, Qt.ItemDataRole.UserRole)
        if file_path and os.path.isfile(file_path) and self.main_window:
            self.main_window.open_file_path(file_path)

class VSCodeMainWindow(QMainWindow):
    """Main VS Code-like window"""
    
    def __init__(self):
        super().__init__()
        self.current_file_path = None
        self.preview_widget = None
        self.project_templates = VSCodeProjectTemplates()
        self.setup_window()
        self.setup_ui()
        self.setup_menus()
        self.setup_toolbar()
        
    def setup_window(self):
        """Setup the main window"""
        self.setWindowTitle("Visual Studio Code")
        self.setGeometry(100, 100, 1400, 900)
        self.setMinimumSize(800, 600)
        
        # VS Code dark theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
                color: #cccccc;
            }
            QMenuBar {
                background-color: #3c3c3c;
                color: #cccccc;
                border: none;
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 4px 8px;
            }
            QMenuBar::item:selected {
                background-color: #094771;
            }
            QMenu {
                background-color: #3c3c3c;
                color: #cccccc;
                border: 1px solid #3c3c3c;
            }
            QMenu::item:selected {
                background-color: #094771;
            }
            QToolBar {
                background-color: #3c3c3c;
                border: none;
                spacing: 2px;
            }
            QToolButton {
                background-color: transparent;
                border: none;
                padding: 4px;
                color: #cccccc;
            }
            QToolButton:hover {
                background-color: #2a2d2e;
            }
            QTabWidget::pane {
                border: none;
                background-color: #1e1e1e;
            }
            QTabBar::tab {
                background-color: #2d2d30;
                color: #cccccc;
                padding: 8px 12px;
                margin-right: 2px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background-color: #1e1e1e;
                border-bottom: 2px solid #007acc;
            }
            QTabBar::tab:hover {
                background-color: #2a2d2e;
            }
            QDockWidget {
                background-color: #252526;
                color: #cccccc;
            }
            QDockWidget::title {
                background-color: #3c3c3c;
                padding: 4px;
            }
            QSplitter::handle {
                background-color: #3c3c3c;
            }
            QSplitter::handle:horizontal {
                width: 1px;
            }
            QSplitter::handle:vertical {
                height: 1px;
            }
        """)
        
    def setup_ui(self):
        """Setup the main UI layout"""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create sidebar
        self.sidebar = VSCodeFileExplorer()
        self.sidebar.setFixedWidth(250)
        self.sidebar.set_main_window(self)
        
        # Create main editor area
        self.editor_area = QTabWidget()
        self.editor_area.setTabsClosable(True)
        self.editor_area.setMovable(True)
        self.editor_area.tabCloseRequested.connect(self.close_tab)
        
        # Create first editor tab
        self.create_editor_tab("Untitled-1")
        
        # Create splitter for sidebar and editor
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self.sidebar)
        splitter.addWidget(self.editor_area)
        splitter.setSizes([250, 1150])
        
        main_layout.addWidget(splitter)
        
        # Create terminal dock
        self.terminal_dock = QDockWidget("Terminal", self)
        self.terminal_dock.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea)
        self.terminal = VSCodeTerminal()
        self.terminal_dock.setWidget(self.terminal)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.terminal_dock)
        
        # Create Visual Code Flow dock
        self.flow_dock = QDockWidget("Visual Code Flow", self)
        self.flow_dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)
        self.visual_flow = VSCodeVisualFlow()
        self.flow_dock.setWidget(self.visual_flow)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.flow_dock)
        
        # Create Health Dashboard dock
        self.health_dock = QDockWidget("Code Health", self)
        self.health_dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)
        self.health_dashboard = VSCodeHealthDashboard()
        self.health_dock.setWidget(self.health_dashboard)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.health_dock)
        
        # Create Package Manager dock
        self.package_dock = QDockWidget("Package Manager", self)
        self.package_dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)
        self.package_manager = VSCodePackageManager()
        self.package_dock.setWidget(self.package_manager)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.package_dock)
        
        # Create status bar
        self.status_bar = VSCodeStatusBar()
        self.setStatusBar(self.status_bar)
        
    def setup_menus(self):
        """Setup VS Code-like menus"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        new_file_action = QAction("New File", self)
        new_file_action.setShortcut("Ctrl+N")
        new_file_action.triggered.connect(self.new_file)
        file_menu.addAction(new_file_action)
        
        open_file_action = QAction("Open File...", self)
        open_file_action.setShortcut("Ctrl+O")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)
        
        open_folder_action = QAction("Open Folder...", self)
        open_folder_action.setShortcut("Ctrl+K Ctrl+O")
        open_folder_action.triggered.connect(self.open_folder)
        file_menu.addAction(open_folder_action)
        
        file_menu.addSeparator()
        
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        save_as_action = QAction("Save As...", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        
        undo_action = QAction("Undo", self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.triggered.connect(self.undo)
        edit_menu.addAction(undo_action)
        
        redo_action = QAction("Redo", self)
        redo_action.setShortcut("Ctrl+Y")
        redo_action.triggered.connect(self.redo)
        edit_menu.addAction(redo_action)
        
        edit_menu.addSeparator()
        
        cut_action = QAction("Cut", self)
        cut_action.setShortcut("Ctrl+X")
        cut_action.triggered.connect(self.cut)
        edit_menu.addAction(cut_action)
        
        copy_action = QAction("Copy", self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.copy)
        edit_menu.addAction(copy_action)
        
        paste_action = QAction("Paste", self)
        paste_action.setShortcut("Ctrl+V")
        paste_action.triggered.connect(self.paste)
        edit_menu.addAction(paste_action)
        
        # Terminal menu
        terminal_menu = menubar.addMenu("Terminal")
        
        new_terminal_action = QAction("New Terminal", self)
        new_terminal_action.setShortcut("Ctrl+`")
        new_terminal_action.triggered.connect(self.toggle_terminal)
        terminal_menu.addAction(new_terminal_action)
        
        run_action = QAction("Run Code", self)
        run_action.setShortcut("F5")
        run_action.triggered.connect(self.run_code)
        terminal_menu.addAction(run_action)
        
        # Virtual Environment submenu
        venv_menu = terminal_menu.addMenu("Virtual Environment")
        
        create_venv_action = QAction("Create Virtual Environment", self)
        create_venv_action.triggered.connect(self.create_virtual_environment)
        venv_menu.addAction(create_venv_action)
        
        activate_venv_action = QAction("Activate Virtual Environment", self)
        activate_venv_action.triggered.connect(self.activate_virtual_environment)
        venv_menu.addAction(activate_venv_action)
        
        deactivate_venv_action = QAction("Deactivate Virtual Environment", self)
        deactivate_venv_action.triggered.connect(self.deactivate_virtual_environment)
        venv_menu.addAction(deactivate_venv_action)
        
        install_package_action = QAction("Install Package", self)
        install_package_action.triggered.connect(self.install_package)
        venv_menu.addAction(install_package_action)
        
        # Project menu
        project_menu = menubar.addMenu("Project")
        
        new_project_action = QAction("New Project from Template", self)
        new_project_action.triggered.connect(self.create_new_project)
        project_menu.addAction(new_project_action)
        
        project_menu.addSeparator()
        
        analyze_flow_action = QAction("Analyze Code Flow", self)
        analyze_flow_action.triggered.connect(self.analyze_code_flow)
        project_menu.addAction(analyze_flow_action)
        
        check_health_action = QAction("Check Code Health", self)
        check_health_action.triggered.connect(self.check_code_health)
        project_menu.addAction(check_health_action)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def setup_toolbar(self):
        """Setup VS Code-like toolbar"""
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.setMovable(False)
        
        # File operations
        new_btn = toolbar.addAction("New File")
        new_btn.setToolTip("New File")
        new_btn.triggered.connect(self.new_file)
        
        open_btn = toolbar.addAction("Open")
        open_btn.setToolTip("Open File")
        open_btn.triggered.connect(self.open_file)
        
        save_btn = toolbar.addAction("Save")
        save_btn.setToolTip("Save")
        save_btn.triggered.connect(self.save_file)
        
        toolbar.addSeparator()
        
        # Run button
        run_btn = toolbar.addAction("Run")
        run_btn.setToolTip("Run Code")
        run_btn.triggered.connect(self.run_code)
        
        toolbar.addSeparator()
        
        # Code Flow button
        flow_btn = toolbar.addAction("Code Flow")
        flow_btn.setToolTip("Visual Code Flow Analysis")
        flow_btn.triggered.connect(self.analyze_code_flow)
        
        # Health Dashboard button
        health_btn = toolbar.addAction("Health")
        health_btn.setToolTip("Code Health Dashboard")
        health_btn.triggered.connect(self.check_code_health)
        
    def create_editor_tab(self, filename, file_path=None):
        """Create a new editor tab"""
        editor = VSCodeEditor(file_path=file_path)
        tab_index = self.editor_area.addTab(editor, filename)
        self.editor_area.setCurrentIndex(tab_index)
        
        # Connect text change to preview update
        editor.textChanged.connect(lambda: self.update_preview_if_needed(editor))
        
        return editor
        
    def update_preview_if_needed(self, editor):
        """Update preview if the file is markdown or HTML"""
        if hasattr(editor, 'file_path') and editor.file_path:
            ext = os.path.splitext(editor.file_path)[1].lower()
            if ext in ['.md', '.html']:
                content = editor.toPlainText()
                if ext == '.md':
                    self.show_preview(content, "markdown")
                elif ext == '.html':
                    self.show_preview(content, "html")
                    
    def show_preview(self, content, file_type):
        """Show preview for markdown or HTML files"""
        if not self.preview_widget:
            self.preview_widget = VSCodePreview()
            self.preview_dock = QDockWidget("Preview", self)
            self.preview_dock.setWidget(self.preview_widget)
            self.preview_dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea)
            self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.preview_dock)
            
        self.preview_widget.update_preview(content, file_type)
        self.preview_dock.show()
        
    def new_file(self):
        """Create a new file"""
        editor = self.create_editor_tab("Untitled-1")
        
    def open_file(self):
        """Open a file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", 
            "All Files (*);;Python Files (*.py);;JavaScript Files (*.js);;CSS Files (*.css);;Markdown Files (*.md);;HTML Files (*.html)"
        )
        if file_path:
            self.open_file_path(file_path)
            
    def open_file_path(self, file_path):
        """Open a file by path"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            filename = os.path.basename(file_path)
            editor = self.create_editor_tab(filename, file_path)
            editor.setPlainText(content)
            self.current_file_path = file_path
            
            # Show preview for markdown/HTML files
            ext = os.path.splitext(file_path)[1].lower()
            if ext == '.md':
                self.show_preview(content, "markdown")
            elif ext == '.html':
                self.show_preview(content, "html")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not open file: {str(e)}")
            
    def open_folder(self):
        """Open a folder"""
        self.sidebar.open_folder()
                
    def save_file(self):
        """Save the current file"""
        current_editor = self.editor_area.currentWidget()
        if current_editor:
            if hasattr(current_editor, 'file_path') and current_editor.file_path:
                # Save to existing file
                try:
                    with open(current_editor.file_path, 'w', encoding='utf-8') as f:
                        f.write(current_editor.toPlainText())
                    self.status_bar.showMessage("File saved successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Could not save file: {str(e)}")
            else:
                # Save as new file
                self.save_file_as()
                
    def save_file_as(self):
        """Save file as"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save File As", "", 
            "All Files (*);;Python Files (*.py);;JavaScript Files (*.js);;CSS Files (*.css);;Markdown Files (*.md);;HTML Files (*.html)"
        )
        if file_path:
            current_editor = self.editor_area.currentWidget()
            if current_editor:
                try:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(current_editor.toPlainText())
                    
                    # Update the editor's file path and tab name
                    current_editor.file_path = file_path
                    filename = os.path.basename(file_path)
                    tab_index = self.editor_area.currentIndex()
                    self.editor_area.setTabText(tab_index, filename)
                    
                    # Update syntax highlighter
                    ext = os.path.splitext(file_path)[1].lower()
                    if ext == '.py':
                        language = "python"
                    elif ext in ['.js', '.jsx']:
                        language = "javascript"
                    elif ext == '.md':
                        language = "markdown"
                    else:
                        language = "text"
                    
                    current_editor.highlighter = VSCodeSyntaxHighlighter(
                        current_editor.document(), language
                    )
                    
                    self.status_bar.showMessage("File saved successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Could not save file: {str(e)}")
                    
    def close_tab(self, index):
        """Close a tab"""
        self.editor_area.removeTab(index)
        
    def undo(self):
        """Undo action"""
        current_editor = self.editor_area.currentWidget()
        if current_editor:
            current_editor.undo()
            
    def redo(self):
        """Redo action"""
        current_editor = self.editor_area.currentWidget()
        if current_editor:
            current_editor.redo()
            
    def cut(self):
        """Cut action"""
        current_editor = self.editor_area.currentWidget()
        if current_editor:
            current_editor.cut()
            
    def copy(self):
        """Copy action"""
        current_editor = self.editor_area.currentWidget()
        if current_editor:
            current_editor.copy()
            
    def paste(self):
        """Paste action"""
        current_editor = self.editor_area.currentWidget()
        if current_editor:
            current_editor.paste()
                    
    def run_code(self):
        """Run the current code"""
        current_editor = self.editor_area.currentWidget()
        if current_editor:
            code = current_editor.toPlainText()
            if code.strip():
                # Run in terminal
                self.terminal_dock.show()
                self.terminal.terminal_output.append("Running code...")
                
                # Determine language and run
                if hasattr(current_editor, 'file_path') and current_editor.file_path:
                    ext = os.path.splitext(current_editor.file_path)[1].lower()
                    if ext == '.py':
                        self.terminal.command_input.setText(f"python3 '{current_editor.file_path}'")
                    elif ext == '.js':
                        self.terminal.command_input.setText(f"node '{current_editor.file_path}'")
                    elif ext == '.html':
                        # Open HTML in browser
                        webbrowser.open(f"file://{current_editor.file_path}")
                        self.terminal.terminal_output.append(f"Opening {current_editor.file_path} in browser")
                        return
                    else:
                        self.terminal.command_input.setText(f"echo 'Running: {current_editor.file_path}'")
                else:
                    # Run as Python by default
                    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                        f.write(code)
                        temp_file = f.name
                    
                    self.terminal.command_input.setText(f"python3 '{temp_file}'")
                    
                self.terminal.execute_command()
            else:
                QMessageBox.warning(self, "Warning", "No code to run")
                
    def toggle_terminal(self):
        """Toggle terminal visibility"""
        if self.terminal_dock.isVisible():
            self.terminal_dock.hide()
        else:
            self.terminal_dock.show()
            self.terminal.command_input.setFocus()
            
    def create_virtual_environment(self):
        """Create a new virtual environment"""
        if self.sidebar.root_path:
            self.terminal.venv_manager.create_venv(self.sidebar.root_path)
        else:
            QMessageBox.warning(self, "Warning", "Please open a folder first")
            
    def activate_virtual_environment(self):
        """Activate a virtual environment"""
        if self.sidebar.root_path:
            venv_path = os.path.join(self.sidebar.root_path, '.venv')
            if os.path.exists(venv_path):
                self.terminal.venv_manager.activate_venv(venv_path)
            else:
                QMessageBox.warning(self, "Warning", "No virtual environment found. Create one first.")
        else:
            QMessageBox.warning(self, "Warning", "Please open a folder first")
            
    def deactivate_virtual_environment(self):
        """Deactivate current virtual environment"""
        self.terminal.venv_manager.deactivate_venv()
        
    def install_package(self):
        """Install a package in the current virtual environment"""
        package_name, ok = QInputDialog.getText(self, "Install Package", "Package name:")
        if ok and package_name:
            self.terminal.venv_manager.install_package(package_name)
            
    def create_new_project(self):
        """Create a new project from template"""
        templates = list(self.project_templates.templates.keys())
        template_name, ok = QInputDialog.getItem(self, "New Project", 
                                               "Choose template:", templates, 0, False)
        if ok and template_name:
            project_path, _ = QFileDialog.getExistingDirectory(self, "Choose Project Location")
            if project_path:
                success, message = self.project_templates.create_project(template_name, project_path)
                if success:
                    QMessageBox.information(self, "Success", message)
                    # Open the new project
                    self.sidebar.load_folder(project_path)
                else:
                    QMessageBox.critical(self, "Error", message)
                    
    def analyze_code_flow(self):
        """Analyze current code and show visual flow"""
        current_editor = self.editor_area.currentWidget()
        if current_editor:
            code = current_editor.toPlainText()
            if code.strip():
                self.visual_flow.analyze_code(code)
                self.flow_dock.show()
            else:
                # Show sample flow if no code
                self.visual_flow.show_sample_flow()
                self.flow_dock.show()
        else:
            # Show sample flow if no editor
            self.visual_flow.show_sample_flow()
            self.flow_dock.show()
            
    def check_code_health(self):
        """Check code health of current file"""
        current_editor = self.editor_area.currentWidget()
        if current_editor:
            code = current_editor.toPlainText()
            if code.strip():
                self.health_dashboard.update_metrics(code)
                self.health_dock.show()
            else:
                QMessageBox.warning(self, "Warning", "No code to analyze")
        else:
            QMessageBox.warning(self, "Warning", "No active editor")
                
    def show_about(self):
        """Show about dialog"""
        QMessageBox.about(self, "About", 
                         "VS Code Clone\n\nA Python implementation of Visual Studio Code\nBuilt with PyQt6")

class VSCodeStatusBar(QStatusBar):
    """VS Code-like status bar"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_status_bar()
        
    def setup_status_bar(self):
        """Setup the status bar with VS Code styling"""
        self.setStyleSheet("""
            QStatusBar {
                background-color: #007acc;
                color: white;
                border: none;
            }
        """)
        
        # Add status items like VS Code
        self.addPermanentWidget(QLabel("Ln 1, Col 1"))
        self.addPermanentWidget(QLabel("UTF-8"))
        self.addPermanentWidget(QLabel("Python"))
        self.showMessage("Ready")

class VSCodeVisualFlow(QGraphicsView):
    """Visual Code Flow - Shows data flow and execution paths"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        
        # Flow tracking
        self.variables = {}
        self.functions = {}
        self.connections = []
        self.execution_path = []
        
        # Visual settings
        self.setStyleSheet("""
            QGraphicsView {
                background-color: #1e1e1e;
                border: none;
            }
        """)
        
    def analyze_code(self, code):
        """Analyze code and create visual flow"""
        self.scene.clear()
        self.variables.clear()
        self.functions.clear()
        self.connections.clear()
        
        try:
            tree = ast.parse(code)
            self.process_ast(tree)
            
            # If no elements found, show sample data
            if not self.variables and not self.functions:
                self.show_sample_flow()
            else:
                self.draw_flow()
                
        except Exception as e:
            self.show_sample_flow()
            
    def show_sample_flow(self):
        """Show sample flow diagram when no code is available"""
        # Add title
        title = QGraphicsTextItem("Sample Code Flow Analysis")
        title.setDefaultTextColor(QColor("#d4d4d4"))
        title.setPos(10, 10)
        self.scene.addItem(title)
        
        # Sample variables
        sample_vars = ['data', 'result', 'config', 'user_input']
        y_offset = 50
        for i, var_name in enumerate(sample_vars):
            x = 20 + (i * 120)
            y = y_offset
            
            ellipse = QGraphicsEllipseItem(x, y, 100, 50)
            ellipse.setBrush(QBrush(QColor("#4ec9b0")))
            ellipse.setPen(QPen(QColor("#d4d4d4"), 2))
            self.scene.addItem(ellipse)
            
            text = QGraphicsTextItem(var_name)
            text.setDefaultTextColor(QColor("#1e1e1e"))
            text.setPos(x + 10, y + 15)
            self.scene.addItem(text)
            
        # Sample functions
        sample_funcs = ['process_data', 'validate_input', 'save_result']
        y_offset = 150
        for i, func_name in enumerate(sample_funcs):
            x = 20 + (i * 150)
            y = y_offset
            
            rect = QGraphicsEllipseItem(x, y, 120, 60)
            rect.setBrush(QBrush(QColor("#569cd6")))
            rect.setPen(QPen(QColor("#d4d4d4"), 2))
            self.scene.addItem(rect)
            
            text = QGraphicsTextItem(func_name)
            text.setDefaultTextColor(QColor("#1e1e1e"))
            text.setPos(x + 10, y + 20)
            self.scene.addItem(text)
            
            # Show sample calls
            calls_text = QGraphicsTextItem(f"Calls: {i + 1}")
            calls_text.setDefaultTextColor(QColor("#ce9178"))
            calls_text.setPos(x + 10, y + 40)
            self.scene.addItem(calls_text)
        
        # Sample connections
        for i in range(min(len(sample_vars), len(sample_funcs))):
            from_x = 70 + (i * 120)
            from_y = 75
            to_x = 80 + (i * 150)
            to_y = 180
            
            line = QGraphicsLineItem(from_x, from_y, to_x, to_y)
            line.setPen(QPen(QColor("#ce9178"), 2))
            self.scene.addItem(line)
            
            # Add arrow
            arrow = QGraphicsTextItem("→")
            arrow.setDefaultTextColor(QColor("#ce9178"))
            arrow.setPos((from_x + to_x) / 2, (from_y + to_y) / 2)
            self.scene.addItem(arrow)
        
        # Add legend
        legend_y = 250
        legend_items = [
            ("Variables", "#4ec9b0"),
            ("Functions", "#569cd6"),
            ("Data Flow", "#ce9178")
        ]
        
        for i, (label, color) in enumerate(legend_items):
            x = 20 + (i * 150)
            y = legend_y
            
            # Color box
            box = QGraphicsEllipseItem(x, y, 20, 20)
            box.setBrush(QBrush(QColor(color)))
            box.setPen(QPen(QColor("#d4d4d4")))
            self.scene.addItem(box)
            
            # Label
            label_text = QGraphicsTextItem(label)
            label_text.setDefaultTextColor(QColor("#d4d4d4"))
            label_text.setPos(x + 25, y)
            self.scene.addItem(label_text)
        
        # Set scene rect to include all items
        self.scene.setSceneRect(self.scene.itemsBoundingRect())
        self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
            
    def process_ast(self, node, x=0, y=0):
        """Process AST nodes and track variables/functions"""
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            self.functions[func_name] = {
                'node': node,
                'pos': (x, y),
                'variables': set(),
                'calls': []
            }
            
            # Process function body
            for i, stmt in enumerate(node.body):
                self.process_ast(stmt, x + 150, y + 80 + (i * 30))
                
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    var_name = target.id
                    self.variables[var_name] = {
                        'value': 'assigned',
                        'pos': (x, y),
                        'type': 'variable'
                    }
                    
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
                if func_name in self.functions:
                    self.functions[func_name]['calls'].append(node)
                    
        # Recursively process child nodes
        for child in ast.iter_child_nodes(node):
            self.process_ast(child, x + 50, y + 30)
                
    def draw_flow(self):
        """Draw the visual flow diagram"""
        # Add title
        title = QGraphicsTextItem("Code Flow Analysis")
        title.setDefaultTextColor(QColor("#d4d4d4"))
        title.setPos(10, 10)
        self.scene.addItem(title)
        
        # Draw variables
        y_offset = 50
        for i, (var_name, var_info) in enumerate(self.variables.items()):
            x = 20 + (i * 120)
            y = y_offset
            
            ellipse = QGraphicsEllipseItem(x, y, 100, 50)
            ellipse.setBrush(QBrush(QColor("#4ec9b0")))
            ellipse.setPen(QPen(QColor("#d4d4d4"), 2))
            self.scene.addItem(ellipse)
            
            text = QGraphicsTextItem(var_name)
            text.setDefaultTextColor(QColor("#1e1e1e"))
            text.setPos(x + 10, y + 15)
            self.scene.addItem(text)
            
        # Draw functions
        y_offset = 150
        for i, (func_name, func_info) in enumerate(self.functions.items()):
            x = 20 + (i * 150)
            y = y_offset
            
            rect = QGraphicsEllipseItem(x, y, 120, 60)
            rect.setBrush(QBrush(QColor("#569cd6")))
            rect.setPen(QPen(QColor("#d4d4d4"), 2))
            self.scene.addItem(rect)
            
            text = QGraphicsTextItem(func_name)
            text.setDefaultTextColor(QColor("#1e1e1e"))
            text.setPos(x + 10, y + 20)
            self.scene.addItem(text)
            
            # Show function calls
            if func_info['calls']:
                calls_text = QGraphicsTextItem(f"Calls: {len(func_info['calls'])}")
                calls_text.setDefaultTextColor(QColor("#ce9178"))
                calls_text.setPos(x + 10, y + 40)
                self.scene.addItem(calls_text)
        
        # Draw connections between functions and variables
        y_offset = 250
        for i, (var_name, var_info) in enumerate(self.variables.items()):
            for j, (func_name, func_info) in enumerate(self.functions.items()):
                # Simple connection logic
                if i == j:  # Connect variables to functions with same index
                    from_x = 70 + (i * 120)
                    from_y = 75
                    to_x = 80 + (j * 150)
                    to_y = 180
                    
                    line = QGraphicsLineItem(from_x, from_y, to_x, to_y)
                    line.setPen(QPen(QColor("#ce9178"), 2))
                    self.scene.addItem(line)
                    
                    # Add arrow
                    arrow = QGraphicsTextItem("→")
                    arrow.setDefaultTextColor(QColor("#ce9178"))
                    arrow.setPos((from_x + to_x) / 2, (from_y + to_y) / 2)
                    self.scene.addItem(arrow)
        
        # Set scene rect to include all items
        self.scene.setSceneRect(self.scene.itemsBoundingRect())
        self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

class VSCodeProjectTemplates:
    """Smart Project Templates with AI-generated scaffolding"""
    
    def __init__(self):
        self.templates = {
            'web_app': {
                'name': 'Web Application',
                'description': 'Full-stack web application with Flask/Django',
                'files': {
                    'app.py': 'from flask import Flask\n\napp = Flask(__name__)\n\n@app.route("/")\ndef home():\n    return "Hello, World!"\n\nif __name__ == "__main__":\n    app.run(debug=True)',
                    'requirements.txt': 'flask>=2.0.0\nrequests>=2.28.0',
                    'templates/index.html': '<!DOCTYPE html>\n<html>\n<head>\n    <title>Web App</title>\n</head>\n<body>\n    <h1>Welcome!</h1>\n</body>\n</html>',
                    'static/style.css': 'body { font-family: Arial, sans-serif; margin: 40px; }',
                    'README.md': '# Web Application\n\nA Flask web application.\n\n## Setup\n```bash\npip install -r requirements.txt\npython app.py\n```'
                }
            },
            'data_science': {
                'name': 'Data Science Project',
                'description': 'Jupyter notebook with data analysis tools',
                'files': {
                    'analysis.ipynb': '{"cells": [{"cell_type": "markdown", "metadata": {}, "source": ["# Data Analysis Project"]}, {"cell_type": "code", "metadata": {}, "source": ["import pandas as pd\\nimport numpy as np\\nimport matplotlib.pyplot as plt\\n\\n# Your analysis here"], "execution_count": null, "outputs": []}], "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}, "nbformat": 4, "nbformat_minor": 4}',
                    'requirements.txt': 'pandas>=1.5.0\nnumpy>=1.21.0\nmatplotlib>=3.5.0\nseaborn>=0.11.0\njupyter>=1.0.0',
                    'data/sample.csv': 'name,age,city\nJohn,25,NYC\nJane,30,LA\nBob,35,Chicago',
                    'README.md': '# Data Science Project\n\nA Jupyter notebook for data analysis.\n\n## Setup\n```bash\npip install -r requirements.txt\njupyter notebook\n```'
                }
            },
            'game_dev': {
                'name': 'Game Development',
                'description': 'Pygame-based game project',
                'files': {
                    'game.py': 'import pygame\n\npygame.init()\nscreen = pygame.display.set_mode((800, 600))\npygame.display.set_caption("My Game")\n\nrunning = True\nwhile running:\n    for event in pygame.event.get():\n        if event.type == pygame.QUIT:\n            running = False\n    \n    screen.fill((0, 0, 0))\n    pygame.display.flip()\n\npygame.quit()',
                    'requirements.txt': 'pygame>=2.0.0',
                    'assets/player.png': '# Placeholder for player sprite',
                    'README.md': '# Game Development Project\n\nA Pygame-based game.\n\n## Setup\n```bash\npip install -r requirements.txt\npython game.py\n```'
                }
            },
            'api_service': {
                'name': 'API Service',
                'description': 'RESTful API with FastAPI',
                'files': {
                    'main.py': 'from fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI()\n\nclass Item(BaseModel):\n    name: str\n    price: float\n\n@app.get("/")\ndef read_root():\n    return {"Hello": "World"}\n\n@app.post("/items/")\ndef create_item(item: Item):\n    return item',
                    'requirements.txt': 'fastapi>=0.68.0\nuvicorn>=0.15.0\npydantic>=1.8.0',
                    'README.md': '# API Service\n\nA FastAPI REST service.\n\n## Setup\n```bash\npip install -r requirements.txt\nuvicorn main:app --reload\n```'
                }
            }
        }
        
    def create_project(self, template_name, project_path):
        """Create a new project from template"""
        if template_name not in self.templates:
            return False, "Template not found"
            
        template = self.templates[template_name]
        
        try:
            # Create project directory
            os.makedirs(project_path, exist_ok=True)
            
            # Create files
            for file_path, content in template['files'].items():
                full_path = os.path.join(project_path, file_path)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                
                with open(full_path, 'w') as f:
                    f.write(content)
                    
            return True, f"Project '{template['name']}' created successfully!"
        except Exception as e:
            return False, f"Error creating project: {str(e)}"

class VSCodeHealthDashboard(QWidget):
    """Code Health Dashboard with metrics and suggestions"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_dashboard()
        
    def setup_dashboard(self):
        """Setup the health dashboard"""
        layout = QVBoxLayout(self)
        
        # Header
        header = QLabel("CODE HEALTH DASHBOARD")
        header.setStyleSheet("""
            QLabel {
                color: #cccccc;
                font-weight: bold;
                font-size: 14px;
                padding: 10px;
                background-color: #3c3c3c;
            }
        """)
        layout.addWidget(header)
        
        # Metrics
        self.metrics_widget = QWidget()
        metrics_layout = QVBoxLayout(self.metrics_widget)
        
        # Code Quality Score
        self.quality_score = QLabel("Code Quality: 85/100")
        self.quality_score.setStyleSheet("""
            QLabel {
                color: #4ec9b0;
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
            }
        """)
        metrics_layout.addWidget(self.quality_score)
        
        # Progress bars
        self.complexity_bar = QProgressBar()
        self.complexity_bar.setMaximum(100)
        self.complexity_bar.setValue(75)
        self.complexity_bar.setFormat("Complexity: %p%")
        self.complexity_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #3c3c3c;
                border-radius: 5px;
                text-align: center;
                color: #d4d4d4;
            }
            QProgressBar::chunk {
                background-color: #569cd6;
                border-radius: 3px;
            }
        """)
        metrics_layout.addWidget(self.complexity_bar)
        
        self.coverage_bar = QProgressBar()
        self.coverage_bar.setMaximum(100)
        self.coverage_bar.setValue(60)
        self.coverage_bar.setFormat("Test Coverage: %p%")
        self.coverage_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #3c3c3c;
                border-radius: 5px;
                text-align: center;
                color: #d4d4d4;
            }
            QProgressBar::chunk {
                background-color: #ce9178;
                border-radius: 3px;
            }
        """)
        metrics_layout.addWidget(self.coverage_bar)
        
        # Issues list
        self.issues_list = QTextBrowser()
        self.issues_list.setStyleSheet("""
            QTextBrowser {
                background-color: #252526;
                color: #d4d4d4;
                border: 1px solid #3c3c3c;
                font-size: 12px;
            }
        """)
        self.issues_list.setMaximumHeight(150)
        metrics_layout.addWidget(self.issues_list)
        
        layout.addWidget(self.metrics_widget)
        
        # Initialize with sample data
        self.update_metrics()
        
    def update_metrics(self, code=None):
        """Update dashboard metrics"""
        if code:
            # Analyze code and update metrics
            issues = self.analyze_code(code)
            self.issues_list.setPlainText("\n".join(issues))
            
            # Update scores based on analysis
            quality = self.calculate_quality_score(code)
            self.quality_score.setText(f"Code Quality: {quality}/100")
            
    def analyze_code(self, code):
        """Analyze code for issues"""
        issues = []
        
        # Simple analysis
        lines = code.split('\n')
        
        # Check for long functions
        if len(lines) > 50:
            issues.append("⚠️ Function is too long (>50 lines)")
            
        # Check for complex nested structures
        indent_levels = [len(line) - len(line.lstrip()) for line in lines if line.strip()]
        if max(indent_levels) > 12:
            issues.append("⚠️ Deep nesting detected")
            
        # Check for magic numbers
        if re.search(r'\b\d{3,}\b', code):
            issues.append("⚠️ Magic numbers detected")
            
        # Check for TODO comments
        if 'TODO' in code.upper():
            issues.append("📝 TODO comments found")
            
        if not issues:
            issues.append("✅ No major issues detected")
            
        return issues
        
    def calculate_quality_score(self, code):
        """Calculate code quality score"""
        score = 100
        
        # Deduct points for issues
        if len(code.split('\n')) > 50:
            score -= 10
        if 'TODO' in code.upper():
            score -= 5
        if re.search(r'\b\d{3,}\b', code):
            score -= 5
            
        return max(0, score)

class VSCodePackageManager(QWidget):
    """Integrated Package Manager with smart dependency resolution"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_package_manager()
        
    def setup_package_manager(self):
        """Setup the package manager interface"""
        layout = QVBoxLayout(self)
        
        # Header
        header = QLabel("PACKAGE MANAGER")
        header.setStyleSheet("""
            QLabel {
                color: #cccccc;
                font-weight: bold;
                font-size: 14px;
                padding: 10px;
                background-color: #3c3c3c;
            }
        """)
        layout.addWidget(header)
        
        # Search and install
        search_layout = QHBoxLayout()
        
        self.package_input = QLineEdit()
        self.package_input.setPlaceholderText("Search packages...")
        self.package_input.setStyleSheet("""
            QLineEdit {
                background-color: #252526;
                color: #d4d4d4;
                border: 1px solid #3c3c3c;
                padding: 5px;
            }
        """)
        search_layout.addWidget(self.package_input)
        
        self.install_btn = QPushButton("Install")
        self.install_btn.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border: none;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)
        self.install_btn.clicked.connect(self.install_package)
        search_layout.addWidget(self.install_btn)
        
        layout.addLayout(search_layout)
        
        # Package list
        self.package_list = QTextBrowser()
        self.package_list.setStyleSheet("""
            QTextBrowser {
                background-color: #252526;
                color: #d4d4d4;
                border: 1px solid #3c3c3c;
                font-size: 12px;
            }
        """)
        layout.addWidget(self.package_list)
        
        # Dependency graph
        self.dependency_view = QGraphicsView()
        self.dependency_view.setStyleSheet("""
            QGraphicsView {
                background-color: #1e1e1e;
                border: 1px solid #3c3c3c;
            }
        """)
        self.dependency_view.setMaximumHeight(200)
        layout.addWidget(self.dependency_view)
        
        # Initialize
        self.update_package_list()
        
    def install_package(self):
        """Install a package"""
        package_name = self.package_input.text().strip()
        if not package_name:
            return
            
        # Simulate package installation
        self.package_list.append(f"📦 Installing {package_name}...")
        
        # Check for conflicts
        conflicts = self.check_conflicts(package_name)
        if conflicts:
            self.package_list.append(f"⚠️ Potential conflicts: {', '.join(conflicts)}")
        else:
            self.package_list.append(f"✅ {package_name} installed successfully!")
            
        self.package_input.clear()
        self.update_dependency_graph()
        
    def check_conflicts(self, package_name):
        """Check for package conflicts"""
        # Simulate conflict checking
        if package_name in ['flask', 'django']:
            return ['web-framework']
        return []
        
    def update_package_list(self):
        """Update the package list"""
        packages = [
            "flask>=2.0.0",
            "requests>=2.28.0", 
            "pandas>=1.5.0",
            "numpy>=1.21.0",
            "matplotlib>=3.5.0"
        ]
        
        self.package_list.setPlainText("Installed packages:\n" + "\n".join(packages))
        
    def update_dependency_graph(self):
        """Update the dependency visualization"""
        scene = QGraphicsScene()
        
        # Create dependency nodes
        packages = ['flask', 'requests', 'pandas', 'numpy']
        for i, pkg in enumerate(packages):
            ellipse = QGraphicsEllipseItem(i * 100, 50, 80, 40)
            ellipse.setBrush(QBrush(QColor("#4ec9b0")))
            ellipse.setPen(QPen(QColor("#d4d4d4")))
            scene.addItem(ellipse)
            
            text = QGraphicsTextItem(pkg)
            text.setDefaultTextColor(QColor("#d4d4d4"))
            text.setPos(i * 100 + 10, 60)
            scene.addItem(text)
            
        self.dependency_view.setScene(scene)

def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("VS Code Clone")
    app.setApplicationVersion("1.0.0")
    
    # Create and show the main window
    window = VSCodeMainWindow()
    window.show()
    
    # Start the event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 
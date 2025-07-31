#!/usr/bin/env python3
"""
Configuration file for Custom IDE
Customize settings here
"""

# IDE Settings
IDE_TITLE = "Custom IDE - Multi-Language Editor"
IDE_VERSION = "1.0.0"
DEFAULT_WINDOW_SIZE = "1200x800"
MIN_WINDOW_SIZE = "800x600"

# Editor Settings
DEFAULT_FONT = ("Consolas", 12)
EDITOR_PADDING = 10
TAB_SIZE = 4  # Number of spaces for tab indentation

# Theme Settings
DEFAULT_THEME = "dark"  # "dark" or "light"

# Code Execution Settings
EXECUTION_TIMEOUT = 30  # seconds
MAX_OUTPUT_LENGTH = 10000  # characters

# AI Settings
OPENAI_MODEL = "gpt-4o"
AI_MAX_TOKENS = 2000
AI_TEMPERATURE = 0.1

# File Settings
SUPPORTED_EXTENSIONS = {
    '.py': 'python',
    '.js': 'javascript',
    '.cs': 'csharp',
    '.html': 'html',
    '.htm': 'html',
    '.css': 'css',
    '.json': 'json',
    '.txt': 'text'
}

# Syntax Highlighting Settings
HIGHLIGHT_UPDATE_DELAY = 100  # milliseconds

# UI Settings
TOOLBAR_HEIGHT = 40
OUTPUT_PANEL_WIDTH_RATIO = 0.4  # 40% of window width

# Keyboard Shortcuts
SHORTCUTS = {
    'new_file': '<Control-n>',
    'open_file': '<Control-o>',
    'save_file': '<Control-s>',
    'run_code': '<Control-r>',
    'run_code_alt': '<F5>',
    'toggle_theme': '<Control-t>',
    'ai_fix': '<Control-f>'
}

# Error Messages
ERROR_MESSAGES = {
    'no_api_key': 'OpenAI API key not found. Set OPENAI_API_KEY environment variable.',
    'api_error': 'Error connecting to OpenAI API. Check your internet connection and API key.',
    'file_not_found': 'File not found or cannot be accessed.',
    'permission_denied': 'Permission denied. Check file permissions.',
    'runtime_not_found': 'Required runtime not found. Install the necessary language runtime.',
    'execution_timeout': 'Code execution timed out. Check for infinite loops.',
    'invalid_syntax': 'Invalid syntax detected in the code.'
}

# Success Messages
SUCCESS_MESSAGES = {
    'file_saved': 'File saved successfully.',
    'file_loaded': 'File loaded successfully.',
    'code_executed': 'Code executed successfully.',
    'ai_fix_applied': 'AI fix applied successfully.',
    'theme_changed': 'Theme changed successfully.'
} 
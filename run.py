#!/usr/bin/env python3
"""
BasicIDE Launcher
A simple launcher script for the BasicIDE Python IDE.
"""

import sys
import os

def main():
    """Launch BasicIDE"""
    try:
        # Import and run the main IDE
        from vscode_clone import main
        main()
    except ImportError as e:
        print(f"Error: Could not import required modules. {e}")
        print("Please install dependencies with: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Error launching BasicIDE: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Startup script for Custom IDE
Handles setup and launches the main application
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check if required dependencies are installed"""
    print("Checking dependencies...")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    
    # Check for requests
    try:
        import requests
        print("✅ requests library found")
    except ImportError:
        print("❌ requests library not found. Installing...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
            print("✅ requests library installed")
        except subprocess.CalledProcessError:
            print("❌ Failed to install requests library")
            return False
    
    return True

def check_optional_runtimes():
    """Check for optional language runtimes"""
    print("\nChecking optional language runtimes...")
    
    # Check Node.js
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Node.js {result.stdout.strip()}")
        else:
            print("⚠️  Node.js not found (JavaScript execution will not work)")
    except FileNotFoundError:
        print("⚠️  Node.js not found (JavaScript execution will not work)")
    
    # Check .NET
    try:
        result = subprocess.run(['dotnet', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ .NET {result.stdout.strip()}")
        else:
            print("⚠️  .NET not found (C# execution will not work)")
    except FileNotFoundError:
        print("⚠️  .NET not found (C# execution will not work)")

def check_openai_api():
    """Check OpenAI API key"""
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        print("✅ OpenAI API key found")
        print(f"OpenAI API key: {api_key}")
        return True
    else:
        print("⚠️  OpenAI API key not found (AI features will not work)")
        print("   Set OPENAI_API_KEY environment variable to enable AI features")
        return False

def main():
    """Main startup function"""
    print("🚀 Custom IDE - Multi-Language Code Editor")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Setup failed. Please install missing dependencies.")
        return
    
    # Check optional runtimes
    check_optional_runtimes()
    
    # Check OpenAI API
    check_openai_api()
    
    print("\n🎯 Starting Custom IDE...")
    print("=" * 50)
    
    try:
        # Import and run the main application
        from main import main as run_ide
        run_ide()
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all files are in the same directory")
    except Exception as e:
        print(f"❌ Error starting IDE: {e}")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Simple test to verify BasicIDE can be imported and basic functionality works.
This is used by the CI/CD pipeline to ensure the IDE is functional.
"""

import sys
import os

def test_import():
    """Test that the IDE module can be imported"""
    try:
        import ide
        print("✅ IDE module imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import IDE module: {e}")
        return False

def test_main_function():
    """Test that the main function exists"""
    try:
        import ide
        if hasattr(ide, 'main'):
            print("✅ Main function found")
            return True
        else:
            print("❌ Main function not found")
            return False
    except Exception as e:
        print(f"❌ Error checking main function: {e}")
        return False

def test_requirements():
    """Test that required dependencies are available"""
    required_modules = ['PyQt6', 'requests']
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module} imported successfully")
        except ImportError:
            print(f"❌ {module} not available")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"❌ Missing required modules: {missing_modules}")
        return False
    else:
        print("✅ All required modules available")
        return True

def main():
    """Run all tests"""
    print("🧪 Running BasicIDE tests...")
    
    tests = [
        test_import,
        test_main_function,
        test_requirements
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 
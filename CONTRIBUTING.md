# 🤝 Contributing to BasicIDE

Thank you for your interest in contributing to BasicIDE! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to your fork**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

## 📋 Development Setup

### Prerequisites
- Python 3.8 or higher
- PyQt6
- Git

### Local Development
```bash
# Clone your fork
git clone https://github.com/WillZLog/BasicIDE.git
cd BasicIDE

# Install dependencies
pip install -r requirements.txt

# Run the IDE
python3 ide.py
```

## 🎯 Areas for Contribution

### 🐛 Bug Fixes
- **UI Issues**: Interface problems, layout bugs
- **Functionality**: Broken features, unexpected behavior
- **Performance**: Slow operations, memory leaks
- **Compatibility**: Cross-platform issues

### ✨ New Features
- **Language Support**: Additional programming languages
- **AI Enhancements**: Improved code analysis and suggestions
- **Visual Tools**: Enhanced code flow and health dashboard
- **Productivity**: Code snippets, templates, shortcuts

### 📚 Documentation
- **README Updates**: Improved installation and usage guides
- **Code Comments**: Better inline documentation
- **API Documentation**: Function and class documentation
- **Tutorials**: Step-by-step guides for features

### 🧪 Testing
- **Unit Tests**: Test individual functions and classes
- **Integration Tests**: Test feature interactions
- **UI Tests**: Test user interface functionality
- **Performance Tests**: Benchmark critical operations

## 📝 Code Style Guidelines

### Python Code
- **PEP 8**: Follow Python style guide
- **Type Hints**: Use type annotations for function parameters and return values
- **Docstrings**: Document all public functions and classes
- **Line Length**: Maximum 88 characters (Black formatter)

### Example
```python
from typing import Optional, List, Dict

def process_code(code: str, language: str) -> Dict[str, any]:
    """
    Process code and return analysis results.
    
    Args:
        code: The source code to analyze
        language: Programming language identifier
        
    Returns:
        Dictionary containing analysis results
        
    Raises:
        ValueError: If code is empty or language is unsupported
    """
    if not code.strip():
        raise ValueError("Code cannot be empty")
    
    # Process the code...
    return {"status": "success", "results": []}
```

### PyQt6 Code
- **Signal/Slot**: Use proper signal-slot connections
- **Widget Naming**: Use descriptive widget names
- **Layout Management**: Use appropriate layout managers
- **Error Handling**: Handle Qt-specific exceptions

## 🧪 Testing Guidelines

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-qt

# Run all tests
pytest

# Run specific test file
pytest tests/test_editor.py

# Run with coverage
pytest --cov=.
```

### Writing Tests
```python
import pytest
from PyQt6.QtWidgets import QApplication
from ide import VSCodeEditor

class TestEditor:
    @pytest.fixture
    def app(self):
        """Create QApplication instance for testing."""
        return QApplication([])
    
    @pytest.fixture
    def editor(self, app):
        """Create editor instance for testing."""
        return VSCodeEditor()
    
    def test_editor_creation(self, editor):
        """Test that editor is created successfully."""
        assert editor is not None
        assert editor.toPlainText() == ""
    
    def test_syntax_highlighting(self, editor):
        """Test syntax highlighting functionality."""
        code = "def hello(): return 'world'"
        editor.setPlainText(code)
        # Add assertions for syntax highlighting
```

## 📋 Pull Request Guidelines

### Before Submitting
1. **Test your changes** thoroughly
2. **Update documentation** if needed
3. **Add tests** for new features
4. **Check code style** with linters
5. **Ensure compatibility** across platforms

### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] Cross-platform testing

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

## 🐛 Bug Reports

### Bug Report Template
```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., macOS 12.0]
- Python: [e.g., 3.9.7]
- PyQt6: [e.g., 6.2.0]
- BasicIDE Version: [e.g., 1.2.0]

## Additional Information
Screenshots, error messages, etc.
```

## 💡 Feature Requests

### Feature Request Template
```markdown
## Feature Description
Clear description of the requested feature

## Use Case
Why this feature would be useful

## Proposed Implementation
How you think it should work

## Alternatives Considered
Other approaches you've considered

## Additional Information
Mockups, examples, etc.
```

## 🏷️ Issue Labels

We use the following labels to categorize issues:

- **bug**: Something isn't working
- **enhancement**: New feature or request
- **documentation**: Improvements to documentation
- **good first issue**: Good for newcomers
- **help wanted**: Extra attention is needed
- **question**: Further information is requested
- **wontfix**: This will not be worked on

## 📞 Getting Help

### Communication Channels
- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Pull Requests**: For code contributions

### Before Asking for Help
1. **Check existing issues** for similar problems
2. **Read the documentation** thoroughly
3. **Try to reproduce** the issue in a minimal example
4. **Provide detailed information** about your environment

## 🎉 Recognition

Contributors will be recognized in:
- **README.md**: List of contributors
- **Release notes**: Credit for significant contributions
- **GitHub contributors page**: Automatic recognition

## 📄 License

By contributing to BasicIDE, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to BasicIDE! 🚀**

Your contributions help make BasicIDE better for everyone in the Python development community. 
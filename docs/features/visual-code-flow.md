# Visual Code Flow

## Overview

The Visual Code Flow feature provides real-time code structure visualization using Abstract Syntax Tree (AST) analysis. It creates interactive diagrams showing the relationships between functions, variables, and data flow in your Python code.

## Features

### 🕸️ AST-Based Analysis
- **Real-time parsing**: Analyzes code as you type
- **Structure mapping**: Identifies functions, classes, and variables
- **Relationship tracking**: Maps function calls and data dependencies

### 🎨 Interactive Visualization
- **Color-coded elements**: 
  - 🟢 Variables (teal circles)
  - 🔵 Functions (blue rectangles)
  - 🟠 Data flow (orange arrows)
- **Dynamic positioning**: Elements arranged based on code structure
- **Click interactions**: Explore relationships between components

### 📊 Sample Mode
When no code is available or analysis fails, the system displays:
- **Sample variables**: `data`, `result`, `config`, `user_input`
- **Sample functions**: `process_data`, `validate_input`, `save_result`
- **Example connections**: Demonstrates data flow patterns
- **Legend**: Explains color coding and symbols

## Usage

### Accessing Visual Code Flow

#### Method 1: Toolbar Button
1. Click the **"Code Flow"** button in the toolbar
2. The visual diagram appears in the right panel

#### Method 2: Menu
1. Go to **Project** → **Analyze Code Flow**
2. The diagram opens automatically

#### Method 3: Keyboard Shortcut
- **Ctrl+Shift+F** (configurable)

### Analyzing Your Code

1. **Open a Python file** with functions and variables
2. **Click "Code Flow"** to analyze
3. **Explore the diagram**:
   - Hover over elements for details
   - Click to focus on specific components
   - Follow arrows to understand data flow

### Example Code for Testing

```python
def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    result = a + b
    return result

def process_data(data_list):
    """Process a list of data items."""
    processed_items = []
    for item in data_list:
        processed = item * 2
        processed_items.append(processed)
    return processed_items

def main():
    """Main function to demonstrate code flow."""
    numbers = [1, 2, 3, 4, 5]
    total = calculate_sum(10, 20)
    results = process_data(numbers)
    print(f"Total: {total}, Results: {results}")

if __name__ == "__main__":
    main()
```

## Technical Details

### AST Processing

The system uses Python's `ast` module to:

1. **Parse code** into an Abstract Syntax Tree
2. **Extract elements**:
   - Function definitions (`ast.FunctionDef`)
   - Variable assignments (`ast.Assign`)
   - Function calls (`ast.Call`)
   - Class definitions (`ast.ClassDef`)

3. **Track relationships**:
   - Function-to-function calls
   - Variable-to-function usage
   - Data flow patterns

### Visualization Engine

Built with PyQt6's `QGraphicsView` and `QGraphicsScene`:

- **Scalable graphics**: Zoom in/out for detailed view
- **Interactive elements**: Clickable components
- **Real-time updates**: Reflects code changes immediately
- **Cross-platform**: Works on Windows, macOS, and Linux

### Performance Considerations

- **Efficient parsing**: Only re-analyzes when code changes
- **Memory management**: Clears previous diagrams before redrawing
- **Large file handling**: Optimized for files up to 10,000 lines
- **Background processing**: Analysis doesn't block the UI

## Customization

### Colors and Styling

You can customize the visual appearance by modifying:

```python
# Variable colors
VARIABLE_COLOR = "#4ec9b0"  # Teal
FUNCTION_COLOR = "#569cd6"  # Blue
FLOW_COLOR = "#ce9178"      # Orange

# Element sizes
VARIABLE_SIZE = (100, 50)
FUNCTION_SIZE = (120, 60)
```

### Layout Algorithms

The system supports different layout algorithms:

1. **Grid Layout**: Elements arranged in a grid pattern
2. **Hierarchical Layout**: Tree-like structure for nested functions
3. **Force-directed Layout**: Physics-based positioning (experimental)

## Troubleshooting

### Common Issues

#### Empty Diagram
- **Cause**: No valid Python code or syntax errors
- **Solution**: Check for syntax errors or add sample code

#### Missing Elements
- **Cause**: AST parsing limitations
- **Solution**: Ensure code follows standard Python syntax

#### Performance Issues
- **Cause**: Very large files or complex code
- **Solution**: Consider splitting large files into modules

### Error Messages

- **"Analysis error"**: Check Python syntax
- **"No elements found"**: Add functions or variables to your code
- **"Memory error"**: Close other applications or restart the IDE

## Future Enhancements

### Planned Features

- **Multi-language support**: Extend to JavaScript, C#, and other languages
- **Advanced filtering**: Show/hide specific element types
- **Export capabilities**: Save diagrams as PNG, SVG, or PDF
- **Collaborative features**: Share diagrams with team members
- **Integration**: Connect with version control systems

### API Integration

The Visual Code Flow system is designed to be extensible:

```python
class CustomFlowAnalyzer:
    def analyze_code(self, code: str) -> Dict:
        """Custom analysis implementation."""
        pass
    
    def create_visualization(self, analysis: Dict) -> QGraphicsScene:
        """Custom visualization implementation."""
        pass
```

## Contributing

To contribute to the Visual Code Flow feature:

1. **Fork the repository**
2. **Create a feature branch**
3. **Implement your changes**
4. **Add tests** for new functionality
5. **Submit a pull request**

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.

---

**Visual Code Flow** transforms how you understand and explore your code structure, making complex relationships visible and interactive. 
#!/usr/bin/env python3
"""
Code Runner Component
Executes code in different programming languages and handles errors
"""

import subprocess
import tempfile
import os
import sys
import json
import webbrowser
from io import StringIO
import traceback

class CodeRunner:
    def __init__(self, output_widget):
        self.output_widget = output_widget
        
    def run_code(self, code, language):
        """Run code in the specified language"""
        if not code.strip():
            return "No code to run.\n"
            
        if not language:
            return "Please save the file with a proper extension to run it.\n"
            
        try:
            if language == 'python':
                return self._run_python(code)
            elif language == 'javascript':
                return self._run_javascript(code)
            elif language == 'csharp':
                return self._run_csharp(code)
            elif language == 'html':
                return self._run_html(code)
            elif language == 'css':
                return self._run_css(code)
            elif language == 'json':
                return self._run_json(code)
            else:
                return f"Language '{language}' is not supported for execution.\n"
        except Exception as e:
            return f"Error running code: {str(e)}\n{traceback.format_exc()}\n"
            
    def _run_python(self, code):
        """Run Python code"""
        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                temp_file = f.name
                
            # Capture stdout and stderr
            result = subprocess.run(
                [sys.executable, temp_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Clean up
            os.unlink(temp_file)
            
            output = ""
            if result.stdout:
                output += f"Output:\n{result.stdout}\n"
            if result.stderr:
                output += f"Errors:\n{result.stderr}\n"
            if result.returncode != 0:
                output += f"Program exited with code {result.returncode}\n"
                
            return output if output else "Code executed successfully (no output)\n"
            
        except subprocess.TimeoutExpired:
            return "Code execution timed out (30 seconds)\n"
        except Exception as e:
            return f"Error executing Python code: {str(e)}\n"
            
    def _run_javascript(self, code):
        """Run JavaScript code using Node.js"""
        try:
            # Check if Node.js is available
            node_check = subprocess.run(['node', '--version'], capture_output=True, text=True)
            if node_check.returncode != 0:
                return "Node.js is not installed. Please install Node.js to run JavaScript code.\n"
                
            # Create a temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
                f.write(code)
                temp_file = f.name
                
            # Run with Node.js
            result = subprocess.run(
                ['node', temp_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Clean up
            os.unlink(temp_file)
            
            output = ""
            if result.stdout:
                output += f"Output:\n{result.stdout}\n"
            if result.stderr:
                output += f"Errors:\n{result.stderr}\n"
            if result.returncode != 0:
                output += f"Program exited with code {result.returncode}\n"
                
            return output if output else "Code executed successfully (no output)\n"
            
        except subprocess.TimeoutExpired:
            return "Code execution timed out (30 seconds)\n"
        except Exception as e:
            return f"Error executing JavaScript code: {str(e)}\n"
            
    def _run_csharp(self, code):
        """Run C# code using .NET"""
        try:
            # Check if .NET is available
            dotnet_check = subprocess.run(['dotnet', '--version'], capture_output=True, text=True)
            if dotnet_check.returncode != 0:
                return ".NET is not installed. Please install .NET to run C# code.\n"
                
            # Create a temporary directory for the project
            with tempfile.TemporaryDirectory() as temp_dir:
                # Create a simple console project
                project_file = os.path.join(temp_dir, "Program.csproj")
                with open(project_file, 'w') as f:
                    f.write("""<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>
</Project>""")
                
                # Create the main program file
                program_file = os.path.join(temp_dir, "Program.cs")
                with open(program_file, 'w') as f:
                    f.write(code)
                    
                # Build and run
                build_result = subprocess.run(
                    ['dotnet', 'build'],
                    cwd=temp_dir,
                    capture_output=True,
                    text=True
                )
                
                if build_result.returncode != 0:
                    return f"Build errors:\n{build_result.stderr}\n"
                    
                # Run the program
                run_result = subprocess.run(
                    ['dotnet', 'run'],
                    cwd=temp_dir,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                output = ""
                if run_result.stdout:
                    output += f"Output:\n{run_result.stdout}\n"
                if run_result.stderr:
                    output += f"Errors:\n{run_result.stderr}\n"
                if run_result.returncode != 0:
                    output += f"Program exited with code {run_result.returncode}\n"
                    
                return output if output else "Code executed successfully (no output)\n"
                
        except subprocess.TimeoutExpired:
            return "Code execution timed out (30 seconds)\n"
        except Exception as e:
            return f"Error executing C# code: {str(e)}\n"
            
    def _run_html(self, code):
        """Display HTML code in a web browser"""
        try:
            # Create a temporary HTML file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
                f.write(code)
                temp_file = f.name
                
            # Get the absolute path
            abs_path = os.path.abspath(temp_file)
            file_url = f"file://{abs_path}"
            
            # Open in default browser
            webbrowser.open(file_url)
            
            return f"HTML file opened in browser: {file_url}\n"
            
        except Exception as e:
            return f"Error displaying HTML: {str(e)}\n"
            
    def _run_css(self, code):
        """Create a simple HTML file to display CSS"""
        try:
            # Create a simple HTML template with the CSS
            html_template = f"""<!DOCTYPE html>
<html>
<head>
    <title>CSS Preview</title>
    <style>
{code}
    </style>
</head>
<body>
    <h1>CSS Preview</h1>
    <p>This is a paragraph to test your CSS styles.</p>
    <div class="test-div">This is a test div element.</div>
    <button class="test-button">Test Button</button>
</body>
</html>"""
            
            # Create a temporary HTML file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
                f.write(html_template)
                temp_file = f.name
                
            # Get the absolute path
            abs_path = os.path.abspath(temp_file)
            file_url = f"file://{abs_path}"
            
            # Open in default browser
            webbrowser.open(file_url)
            
            return f"CSS preview opened in browser: {file_url}\n"
            
        except Exception as e:
            return f"Error displaying CSS: {str(e)}\n"
            
    def _run_json(self, code):
        """Validate and format JSON code"""
        try:
            # Parse JSON to validate it
            parsed_json = json.loads(code)
            
            # Format it nicely
            formatted_json = json.dumps(parsed_json, indent=2)
            
            return f"Valid JSON! Formatted output:\n\n{formatted_json}\n"
            
        except json.JSONDecodeError as e:
            return f"Invalid JSON: {str(e)}\n"
        except Exception as e:
            return f"Error processing JSON: {str(e)}\n" 
#!/usr/bin/env python3
"""
File Manager Component
Handles file operations and language detection based on file extensions
"""

import os
import json

class FileManager:
    def __init__(self):
        # Language mapping based on file extensions
        self.language_extensions = {
            '.py': 'python',
            '.js': 'javascript',
            '.cs': 'csharp',
            '.html': 'html',
            '.htm': 'html',
            '.css': 'css',
            '.json': 'json',
            '.txt': 'text'
        }
        
    def load_file(self, file_path: str) -> str:
        """
        Load content from a file
        
        Args:
            file_path: Path to the file to load
            
        Returns:
            File content as string
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            # Try with different encoding if UTF-8 fails
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    return f.read()
            except Exception as e:
                raise Exception(f"Could not read file with any encoding: {str(e)}")
        except Exception as e:
            raise Exception(f"Error reading file: {str(e)}")
            
    def save_file(self, file_path: str, content: str) -> None:
        """
        Save content to a file
        
        Args:
            file_path: Path where to save the file
            content: Content to save
        """
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            raise Exception(f"Error saving file: {str(e)}")
            
    def get_language_from_extension(self, file_path: str) -> str:
        """
        Determine programming language from file extension
        
        Args:
            file_path: Path to the file
            
        Returns:
            Language identifier or 'text' if unknown
        """
        _, ext = os.path.splitext(file_path.lower())
        return self.language_extensions.get(ext, 'text')
        
    def get_language_from_content(self, content: str) -> str:
        """
        Try to determine language from file content (heuristic approach)
        
        Args:
            content: File content
            
        Returns:
            Language identifier or 'text' if unknown
        """
        content_lower = content.lower().strip()
        
        # Check for shebang
        if content_lower.startswith('#!'):
            if 'python' in content_lower:
                return 'python'
            elif 'node' in content_lower or 'javascript' in content_lower:
                return 'javascript'
                
        # Check for HTML
        if content_lower.startswith('<!doctype') or content_lower.startswith('<html'):
            return 'html'
            
        # Check for JSON
        if content_lower.startswith('{') or content_lower.startswith('['):
            try:
                json.loads(content)
                return 'json'
            except:
                pass
                
        # Check for CSS
        if any(selector in content_lower for selector in ['{', ':', ';']) and \
           any(property in content_lower for property in ['color', 'background', 'margin', 'padding']):
            return 'css'
            
        # Check for Python
        if any(keyword in content_lower for keyword in ['def ', 'import ', 'from ', 'class ', 'if __name__']):
            return 'python'
            
        # Check for JavaScript
        if any(keyword in content_lower for keyword in ['function ', 'var ', 'let ', 'const ', 'console.log']):
            return 'javascript'
            
        # Check for C#
        if any(keyword in content_lower for keyword in ['using ', 'namespace ', 'class ', 'public ', 'private ']):
            return 'csharp'
            
        return 'text'
        
    def is_binary_file(self, file_path: str) -> bool:
        """
        Check if a file is binary
        
        Args:
            file_path: Path to the file
            
        Returns:
            True if binary, False otherwise
        """
        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(1024)
                return b'\x00' in chunk
        except:
            return False
            
    def get_file_info(self, file_path: str) -> dict:
        """
        Get information about a file
        
        Args:
            file_path: Path to the file
            
        Returns:
            Dictionary with file information
        """
        try:
            stat = os.stat(file_path)
            _, ext = os.path.splitext(file_path)
            
            return {
                'name': os.path.basename(file_path),
                'path': file_path,
                'size': stat.st_size,
                'modified': stat.st_mtime,
                'extension': ext,
                'language': self.get_language_from_extension(file_path),
                'is_binary': self.is_binary_file(file_path)
            }
        except Exception as e:
            raise Exception(f"Error getting file info: {str(e)}")
            
    def create_backup(self, file_path: str) -> str:
        """
        Create a backup of a file
        
        Args:
            file_path: Path to the file to backup
            
        Returns:
            Path to the backup file
        """
        try:
            backup_path = f"{file_path}.backup"
            content = self.load_file(file_path)
            self.save_file(backup_path, content)
            return backup_path
        except Exception as e:
            raise Exception(f"Error creating backup: {str(e)}")
            
    def restore_backup(self, file_path: str) -> None:
        """
        Restore a file from its backup
        
        Args:
            file_path: Path to the file to restore
        """
        try:
            backup_path = f"{file_path}.backup"
            if os.path.exists(backup_path):
                content = self.load_file(backup_path)
                self.save_file(file_path, content)
            else:
                raise Exception("Backup file not found")
        except Exception as e:
            raise Exception(f"Error restoring backup: {str(e)}") 
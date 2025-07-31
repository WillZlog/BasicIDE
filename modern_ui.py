#!/usr/bin/env python3
"""
Modern UI Framework for Custom IDE
Creates a beautiful, modern desktop application with custom styling
"""

import tkinter as tk
from tkinter import ttk
import math

class ModernButton(tk.Canvas):
    """Modern button with gradients and hover effects"""
    
    def __init__(self, parent, text="", command=None, style="primary", width=120, height=32, **kwargs):
        super().__init__(parent, width=width, height=height, 
                        bg=parent.cget('bg'), highlightthickness=0, **kwargs)
        
        self.text = text
        self.command = command
        self.style = style
        self.width = width
        self.height = height
        self.hovered = False
        self.pressed = False
        
        # Color schemes
        self.colors = {
            "primary": {
                "bg": "#007acc",
                "hover": "#005a9e",
                "pressed": "#004578",
                "text": "#ffffff"
            },
            "secondary": {
                "bg": "#3c3c3c",
                "hover": "#4c4c4c",
                "pressed": "#2a2d2e",
                "text": "#d4d4d4"
            },
            "success": {
                "bg": "#4ec9b0",
                "hover": "#3db8a0",
                "pressed": "#2ca790",
                "text": "#ffffff"
            },
            "danger": {
                "bg": "#f44747",
                "hover": "#e51400",
                "pressed": "#d10000",
                "text": "#ffffff"
            }
        }
        
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)
        
        self.draw()
        
    def draw(self):
        """Draw the button"""
        self.delete("all")
        
        colors = self.colors[self.style]
        
        # Determine current color
        if self.pressed:
            bg_color = colors["pressed"]
        elif self.hovered:
            bg_color = colors["hover"]
        else:
            bg_color = colors["bg"]
        
        # Create gradient effect
        for i in range(self.height):
            # Calculate gradient intensity
            intensity = 1.0 - (i / self.height) * 0.2
            r, g, b = self.hex_to_rgb(bg_color)
            r = int(r * intensity)
            g = int(g * intensity)
            b = int(b * intensity)
            color = f"#{r:02x}{g:02x}{b:02x}"
            
            self.create_line(0, i, self.width, i, fill=color, width=1)
        
        # Add highlight at top
        highlight_color = self.lighten_color(bg_color, 0.3)
        self.create_line(0, 0, self.width, 0, fill=highlight_color, width=2)
        
        # Add text
        self.create_text(self.width//2, self.height//2, 
                        text=self.text, fill=colors["text"],
                        font=("Segoe UI", 9, "bold"))
        
    def hex_to_rgb(self, hex_color):
        """Convert hex color to RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def lighten_color(self, hex_color, factor):
        """Lighten a hex color by a factor"""
        r, g, b = self.hex_to_rgb(hex_color)
        r = min(255, int(r + (255 - r) * factor))
        g = min(255, int(g + (255 - g) * factor))
        b = min(255, int(b + (255 - b) * factor))
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def on_enter(self, event):
        """Handle mouse enter"""
        self.hovered = True
        self.draw()
        
    def on_leave(self, event):
        """Handle mouse leave"""
        self.hovered = False
        self.pressed = False
        self.draw()
        
    def on_press(self, event):
        """Handle mouse press"""
        self.pressed = True
        self.draw()
        
    def on_release(self, event):
        """Handle mouse release"""
        self.pressed = False
        self.draw()
        if self.command:
            self.command()

class ModernFrame(tk.Canvas):
    """Modern frame with gradient background and rounded corners"""
    
    def __init__(self, parent, bg="#1e1e1e", corner_radius=8, **kwargs):
        super().__init__(parent, bg=parent.cget('bg'), highlightthickness=0, **kwargs)
        
        self.bg = bg
        self.corner_radius = corner_radius
        self.bind("<Configure>", self.draw)
        
    def draw(self, event=None):
        """Draw the frame with gradient and rounded corners"""
        self.delete("all")
        
        width = self.winfo_width()
        height = self.winfo_height()
        
        if width <= 1 or height <= 1:
            return
        
        # Create gradient background
        for y in range(height):
            intensity = 0.95 + (y / height) * 0.05
            r, g, b = self.hex_to_rgb(self.bg)
            r = int(r * intensity)
            g = int(g * intensity)
            b = int(b * intensity)
            color = f"#{r:02x}{g:02x}{b:02x}"
            
            self.create_line(0, y, width, y, fill=color, width=1)
        
        # Add subtle border
        border_color = self.lighten_color(self.bg, 0.1)
        self.create_rectangle(0, 0, width-1, height-1, 
                            outline=border_color, width=1)
    
    def hex_to_rgb(self, hex_color):
        """Convert hex color to RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def lighten_color(self, hex_color, factor):
        """Lighten a hex color by a factor"""
        r, g, b = self.hex_to_rgb(hex_color)
        r = min(255, int(r + (255 - r) * factor))
        g = min(255, int(g + (255 - g) * factor))
        b = min(255, int(b + (255 - b) * factor))
        return f"#{r:02x}{g:02x}{b:02x}"

class ModernText(tk.Text):
    """Modern text widget with custom styling"""
    
    def __init__(self, parent, **kwargs):
        # Set default modern styling
        defaults = {
            'bg': '#1e1e1e',
            'fg': '#d4d4d4',
            'insertbackground': '#ffffff',
            'selectbackground': '#264f78',
            'selectforeground': '#ffffff',
            'font': ('Consolas', 12),
            'relief': 'flat',
            'borderwidth': 0,
            'padx': 15,
            'pady': 15,
            'wrap': 'none'
        }
        
        # Update with any provided kwargs
        defaults.update(kwargs)
        
        super().__init__(parent, **defaults)
        
        # Configure tags for modern appearance
        self.tag_configure("line_highlight", background="#2a2d2e")
        self.tag_configure("current_line", background="#2a2d2e")
        
        # Bind events for line highlighting
        self.bind("<KeyRelease>", self.highlight_current_line)
        self.bind("<Button-1>", self.highlight_current_line)
        
    def highlight_current_line(self, event=None):
        """Highlight the current line"""
        # Remove previous highlighting
        self.tag_remove("current_line", "1.0", "end")
        
        # Get current line
        current_line = self.index("insert").split('.')[0]
        line_start = f"{current_line}.0"
        line_end = f"{int(current_line) + 1}.0"
        
        # Highlight current line
        self.tag_add("current_line", line_start, line_end)

class ModernScrollbar(tk.Canvas):
    """Modern scrollbar with custom styling"""
    
    def __init__(self, parent, orient="vertical", **kwargs):
        super().__init__(parent, width=12, bg=parent.cget('bg'), 
                        highlightthickness=0, **kwargs)
        
        self.orient = orient
        self.scrollable = None
        self.scrollbar_bg = "#3c3c3c"
        self.scrollbar_fg = "#6a6a6a"
        self.scrollbar_hover = "#4c4c4c"
        self.hovered = False
        
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
        self.bind("<B1-Motion>", self.on_drag)
        
    def set_scrollable(self, scrollable):
        """Set the scrollable widget"""
        self.scrollable = scrollable
        if self.orient == "vertical":
            scrollable.configure(yscrollcommand=self.set)
        else:
            scrollable.configure(xscrollcommand=self.set)
            
    def set(self, first, last):
        """Set scrollbar position"""
        self.delete("all")
        
        if float(first) == 0.0 and float(last) == 1.0:
            return
            
        # Calculate thumb position and size
        if self.orient == "vertical":
            height = self.winfo_height()
            thumb_height = max(20, int(height * (float(last) - float(first))))
            thumb_y = int(height * float(first))
            
            # Draw track
            self.create_rectangle(2, 0, 10, height, 
                                fill=self.scrollbar_bg, outline="")
            
            # Draw thumb
            thumb_color = self.scrollbar_hover if self.hovered else self.scrollbar_fg
            self.create_rectangle(2, thumb_y, 10, thumb_y + thumb_height,
                                fill=thumb_color, outline="")
        else:
            width = self.winfo_width()
            thumb_width = max(20, int(width * (float(last) - float(first))))
            thumb_x = int(width * float(first))
            
            # Draw track
            self.create_rectangle(0, 2, width, 10,
                                fill=self.scrollbar_bg, outline="")
            
            # Draw thumb
            thumb_color = self.scrollbar_hover if self.hovered else self.scrollbar_fg
            self.create_rectangle(thumb_x, 2, thumb_x + thumb_width, 10,
                                fill=thumb_color, outline="")
    
    def on_enter(self, event):
        """Handle mouse enter"""
        self.hovered = True
        if self.scrollable:
            self.set(*self.scrollable.yview() if self.orient == "vertical" else self.scrollable.xview())
    
    def on_leave(self, event):
        """Handle mouse leave"""
        self.hovered = False
        if self.scrollable:
            self.set(*self.scrollable.yview() if self.orient == "vertical" else self.scrollable.xview())
    
    def on_click(self, event):
        """Handle click"""
        if not self.scrollable:
            return
            
        if self.orient == "vertical":
            height = self.winfo_height()
            y = event.y / height
            self.scrollable.yview_moveto(y)
        else:
            width = self.winfo_width()
            x = event.x / width
            self.scrollable.xview_moveto(x)
    
    def on_drag(self, event):
        """Handle drag"""
        self.on_click(event)

class ModernLabel(tk.Canvas):
    """Modern label with custom styling"""
    
    def __init__(self, parent, text="", font=("Segoe UI", 9), 
                 fg="#d4d4d4", bg=None, **kwargs):
        
        if bg is None:
            bg = parent.cget('bg')
            
        super().__init__(parent, bg=bg, highlightthickness=0, **kwargs)
        
        self.text = text
        self.font = font
        self.fg = fg
        self.bg = bg
        
        self.bind("<Configure>", self.draw)
        
    def draw(self, event=None):
        """Draw the label"""
        self.delete("all")
        
        width = self.winfo_width()
        height = self.winfo_height()
        
        if width <= 1 or height <= 1:
            return
        
        # Create text
        self.create_text(width//2, height//2, 
                        text=self.text, fill=self.fg,
                        font=self.font, anchor="center")
    
    def configure(self, **kwargs):
        """Configure the label"""
        if 'text' in kwargs:
            self.text = kwargs['text']
        if 'font' in kwargs:
            self.font = kwargs['font']
        if 'fg' in kwargs:
            self.fg = kwargs['fg']
        if 'bg' in kwargs:
            self.bg = kwargs['bg']
            
        self.draw() 
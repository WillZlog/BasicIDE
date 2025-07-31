#!/usr/bin/env python3
"""
Theme Manager Component
Handles light and dark themes with modern VS Code-like color schemes
"""

class ThemeManager:
    def __init__(self):
        self.current_theme = "dark"
        
        # Define modern VS Code-like themes
        self.themes = {
            "dark": {
                # Main UI colors (VS Code Dark+)
                "bg": "#1e1e1e",
                "fg": "#d4d4d4",
                "accent": "#007acc",
                "accent_hover": "#005a9e",
                "accent_light": "#4fc1ff",
                
                # Editor colors
                "editor_bg": "#1e1e1e",
                "editor_fg": "#d4d4d4",
                "select_bg": "#264f78",
                "select_fg": "#ffffff",
                "cursor_color": "#ffffff",
                "line_highlight": "#2a2d2e",
                
                # Output panel colors
                "output_bg": "#1e1e1e",
                "output_fg": "#d4d4d4",
                
                # Syntax highlighting colors (VS Code Dark+)
                "keyword_color": "#569cd6",
                "string_color": "#ce9178",
                "comment_color": "#6a9955",
                "number_color": "#b5cea8",
                "function_color": "#dcdcaa",
                "class_color": "#4ec9b0",
                "variable_color": "#9cdcfe",
                "constant_color": "#4fc1ff",
                "operator_color": "#d4d4d4",
                "type_color": "#4ec9b0",
                
                # HTML/CSS specific
                "tag_color": "#569cd6",
                "attribute_color": "#9cdcfe",
                "doctype_color": "#569cd6",
                "selector_color": "#d7ba7d",
                "property_color": "#9cdcfe",
                "value_color": "#ce9178",
                
                # JSON specific
                "key_color": "#9cdcfe",
                "boolean_color": "#569cd6",
                "null_color": "#569cd6",
                
                # Button colors
                "button_bg": "#3c3c3c",
                "button_fg": "#d4d4d4",
                "button_hover_bg": "#4c4c4c",
                "button_pressed_bg": "#2a2d2e",
                
                # Frame colors
                "frame_bg": "#2d2d30",
                "frame_fg": "#d4d4d4",
                "panel_bg": "#1e1e1e",
                "toolbar_bg": "#2d2d30",
                
                # Separator colors
                "separator_color": "#3c3c3c",
                "border_color": "#3c3c3c",
                
                # Status bar colors
                "status_bg": "#007acc",
                "status_fg": "#ffffff",
                "status_info_bg": "#2d2d30",
                "status_info_fg": "#d4d4d4",
                
                # Scrollbar colors
                "scrollbar_bg": "#3c3c3c",
                "scrollbar_fg": "#6a6a6a",
                "scrollbar_hover": "#4c4c4c",
                
                # Error/Success colors
                "error_color": "#f44747",
                "warning_color": "#ffcc02",
                "success_color": "#4ec9b0",
                "info_color": "#4fc1ff",
            },
            
            "light": {
                # Main UI colors (VS Code Light+)
                "bg": "#ffffff",
                "fg": "#1e1e1e",
                "accent": "#0078d4",
                "accent_hover": "#106ebe",
                "accent_light": "#4fc1ff",
                
                # Editor colors
                "editor_bg": "#ffffff",
                "editor_fg": "#1e1e1e",
                "select_bg": "#add6ff",
                "select_fg": "#000000",
                "cursor_color": "#000000",
                "line_highlight": "#f0f0f0",
                
                # Output panel colors
                "output_bg": "#f3f3f3",
                "output_fg": "#1e1e1e",
                
                # Syntax highlighting colors (VS Code Light+)
                "keyword_color": "#0000ff",
                "string_color": "#a31515",
                "comment_color": "#008000",
                "number_color": "#098658",
                "function_color": "#795e26",
                "class_color": "#267f99",
                "variable_color": "#001080",
                "constant_color": "#0000ff",
                "operator_color": "#1e1e1e",
                "type_color": "#267f99",
                
                # HTML/CSS specific
                "tag_color": "#0000ff",
                "attribute_color": "#001080",
                "doctype_color": "#0000ff",
                "selector_color": "#d73a49",
                "property_color": "#001080",
                "value_color": "#a31515",
                
                # JSON specific
                "key_color": "#001080",
                "boolean_color": "#0000ff",
                "null_color": "#0000ff",
                
                # Button colors
                "button_bg": "#f3f3f3",
                "button_fg": "#1e1e1e",
                "button_hover_bg": "#e3e3e3",
                "button_pressed_bg": "#d4d4d4",
                
                # Frame colors
                "frame_bg": "#f3f3f3",
                "frame_fg": "#1e1e1e",
                "panel_bg": "#ffffff",
                "toolbar_bg": "#f3f3f3",
                
                # Separator colors
                "separator_color": "#d4d4d4",
                "border_color": "#d4d4d4",
                
                # Status bar colors
                "status_bg": "#0078d4",
                "status_fg": "#ffffff",
                "status_info_bg": "#f3f3f3",
                "status_info_fg": "#1e1e1e",
                
                # Scrollbar colors
                "scrollbar_bg": "#f3f3f3",
                "scrollbar_fg": "#c1c1c1",
                "scrollbar_hover": "#d4d4d4",
                
                # Error/Success colors
                "error_color": "#e51400",
                "warning_color": "#ffcc02",
                "success_color": "#107c10",
                "info_color": "#0078d4",
            }
        }
        
    def set_theme(self, theme_name: str):
        """Set the current theme"""
        if theme_name in self.themes:
            self.current_theme = theme_name
        else:
            raise ValueError(f"Unknown theme: {theme_name}")
            
    def get_current_theme(self) -> dict:
        """Get the current theme colors"""
        return self.themes[self.current_theme]
        
    def get_theme_names(self) -> list:
        """Get list of available theme names"""
        return list(self.themes.keys())
        
    def get_color(self, color_name: str) -> str:
        """Get a specific color from the current theme"""
        theme = self.get_current_theme()
        return theme.get(color_name, "#000000")
        
    def toggle_theme(self) -> str:
        """Toggle between light and dark themes"""
        new_theme = "light" if self.current_theme == "dark" else "dark"
        self.set_theme(new_theme)
        return new_theme
        
    def apply_theme_to_widget(self, widget, theme_name: str = None):
        """Apply theme colors to a tkinter widget"""
        if theme_name is None:
            theme_name = self.current_theme
            
        theme = self.themes[theme_name]
        
        try:
            # Apply common widget colors
            if hasattr(widget, 'configure'):
                widget.configure(
                    background=theme.get("bg", "#ffffff"),
                    foreground=theme.get("fg", "#000000")
                )
        except:
            pass
            
    def get_style_config(self, theme_name: str = None) -> dict:
        """Get ttk style configuration for the theme"""
        if theme_name is None:
            theme_name = self.current_theme
            
        theme = self.themes[theme_name]
        
        return {
            "TFrame": {
                "configure": {
                    "background": theme["frame_bg"]
                }
            },
            "Panel.TFrame": {
                "configure": {
                    "background": theme["panel_bg"],
                    "borderwidth": 0,
                    "relief": "flat"
                }
            },
            "Toolbar.TFrame": {
                "configure": {
                    "background": theme["toolbar_bg"],
                    "borderwidth": 0,
                    "relief": "flat"
                }
            },
            "TLabel": {
                "configure": {
                    "background": theme["frame_bg"],
                    "foreground": theme["frame_fg"]
                }
            },
            "Title.TLabel": {
                "configure": {
                    "background": theme["panel_bg"],
                    "foreground": theme["frame_fg"],
                    "font": ("Segoe UI", 12, "bold"),
                    "padding": (0, 5)
                }
            },
            "Status.TLabel": {
                "configure": {
                    "background": theme["toolbar_bg"],
                    "foreground": theme["frame_fg"],
                    "font": ("Segoe UI", 9),
                    "padding": (10, 5)
                }
            },
            "TButton": {
                "configure": {
                    "background": theme["button_bg"],
                    "foreground": theme["button_fg"],
                    "borderwidth": 0,
                    "focuscolor": "none",
                    "font": ("Segoe UI", 9)
                },
                "map": {
                    "background": [
                        ("active", theme["button_hover_bg"]),
                        ("pressed", theme["button_pressed_bg"])
                    ]
                }
            },
            "Modern.TButton": {
                "configure": {
                    "background": theme["button_bg"],
                    "foreground": theme["button_fg"],
                    "borderwidth": 0,
                    "focuscolor": "none",
                    "font": ("Segoe UI", 9),
                    "padding": (12, 8)
                },
                "map": {
                    "background": [
                        ("active", theme["button_hover_bg"]),
                        ("pressed", theme["button_pressed_bg"])
                    ]
                }
            },
            "Accent.TButton": {
                "configure": {
                    "background": theme["accent"],
                    "foreground": "#ffffff",
                    "borderwidth": 0,
                    "focuscolor": "none",
                    "font": ("Segoe UI", 9, "bold"),
                    "padding": (12, 8)
                },
                "map": {
                    "background": [
                        ("active", theme["accent_hover"]),
                        ("pressed", theme["accent_hover"])
                    ]
                }
            },
            "Toolbar.TButton": {
                "configure": {
                    "background": theme["toolbar_bg"],
                    "foreground": theme["frame_fg"],
                    "borderwidth": 0,
                    "focuscolor": "none",
                    "font": ("Segoe UI", 8),
                    "padding": (8, 6)
                },
                "map": {
                    "background": [
                        ("active", theme["button_hover_bg"]),
                        ("pressed", theme["button_pressed_bg"])
                    ]
                }
            },
            "TSeparator": {
                "configure": {
                    "background": theme["separator_color"]
                }
            },
            "TScrollbar": {
                "configure": {
                    "background": theme["scrollbar_bg"],
                    "troughcolor": theme["scrollbar_bg"],
                    "borderwidth": 0,
                    "relief": "flat"
                },
                "map": {
                    "background": [
                        ("active", theme["scrollbar_hover"])
                    ]
                }
            }
        } 
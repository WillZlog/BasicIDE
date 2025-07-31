#!/usr/bin/env python3
"""
Icon Generator for Custom IDE
Creates a simple icon for the application
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    """Create a simple icon for the IDE"""
    # Create a 256x256 image with a dark background
    size = 256
    img = Image.new('RGBA', (size, size), (30, 30, 30, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw a modern code editor icon
    # Background rectangle
    draw.rectangle([20, 20, size-20, size-20], fill=(0, 122, 204, 255), outline=(255, 255, 255, 255), width=3)
    
    # Code lines
    line_color = (255, 255, 255, 255)
    line_width = 3
    
    # Line 1
    draw.rectangle([40, 60, 120, 60+line_width], fill=line_color)
    
    # Line 2
    draw.rectangle([40, 80, 180, 80+line_width], fill=line_color)
    
    # Line 3
    draw.rectangle([40, 100, 140, 100+line_width], fill=line_color)
    
    # Line 4
    draw.rectangle([40, 120, 160, 120+line_width], fill=line_color)
    
    # Line 5
    draw.rectangle([40, 140, 200, 140+line_width], fill=line_color)
    
    # Cursor
    draw.rectangle([40, 160, 40+line_width, 180], fill=(255, 255, 0, 255))
    
    # Save as ICO
    img.save('icon.ico', format='ICO', sizes=[(256, 256)])
    
    # Also save as PNG for reference
    img.save('icon.png', format='PNG')
    
    print("✅ Icon created successfully!")
    print("   - icon.ico (for Windows)")
    print("   - icon.png (for reference)")

if __name__ == "__main__":
    try:
        create_icon()
    except ImportError:
        print("❌ PIL/Pillow not installed. Install with: pip install Pillow")
    except Exception as e:
        print(f"❌ Error creating icon: {e}") 
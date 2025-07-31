#!/usr/bin/env python3
"""
Example Python file to test the Custom IDE
This file demonstrates various Python features and syntax highlighting
"""

import math
import random
from typing import List, Dict

class Calculator:
    """A simple calculator class to demonstrate OOP"""
    
    def __init__(self):
        self.history: List[float] = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers"""
        result = a + b
        self.history.append(result)
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers"""
        result = a * b
        self.history.append(result)
        return result
    
    def get_history(self) -> List[float]:
        """Get calculation history"""
        return self.history.copy()

def fibonacci(n: int) -> List[int]:
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence

def main():
    """Main function to demonstrate the IDE features"""
    print("Welcome to Custom IDE!")
    print("=" * 30)
    
    # Test calculator
    calc = Calculator()
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"4 * 7 = {calc.multiply(4, 7)}")
    print(f"History: {calc.get_history()}")
    
    # Test Fibonacci
    fib_sequence = fibonacci(10)
    print(f"First 10 Fibonacci numbers: {fib_sequence}")
    
    # Test some math operations
    numbers = [random.randint(1, 100) for _ in range(5)]
    print(f"Random numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
    print(f"Square root of 16: {math.sqrt(16)}")
    
    # Test string operations
    message = "Hello, Custom IDE!"
    print(f"Original: {message}")
    print(f"Uppercase: {message.upper()}")
    print(f"Lowercase: {message.lower()}")
    print(f"Length: {len(message)}")
    
    # Test list comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares of 1-5: {squares}")
    
    # Test dictionary
    person = {
        "name": "Developer",
        "age": 25,
        "skills": ["Python", "JavaScript", "C#"]
    }
    print(f"Person: {person}")
    
    print("\nIDE Features Tested:")
    print("- Syntax highlighting")
    print("- Code execution")
    print("- Error handling")
    print("- File management")
    print("- AI error fixing (if API key is set)")

if __name__ == "__main__":
    main() 
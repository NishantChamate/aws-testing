import logging
from logger import setup_logger

logger = setup_logger()

def add(a, b):
    logger.info(f"Addition started: {a} + {b}")
    return a + b

def subtract(a, b):
    logger.info(f"Subtraction started: {a} - {b}")
    return a - b

def multiply(a, b):
    logger.info(f"Multiplication started: {a} * {b}")
    return a * b

def divide(a, b):
    if b == 0:
        logger.error("Division by zero attempted")
        return "Error: Cannot divide by zero"
    logger.info(f"Division started: {a} / {b}")
    return a / b

if __name__ == "__main__":
    print(add(10, 5))
    print(subtract(20, 5))
    print(multiply(3, 4))
    print(divide(8, 2))

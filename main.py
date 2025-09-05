"""
Main Driver Program
Integrates all contributed mathematical utility functions into a cohesive application.

This file serves as the main entry point and demonstrates how all the contributed
functions work together. The Admin/Integrator will update this file as new
functions are added by contributors.

@author: Admin (Repository Owner)
"""

import argparse
import sys
from math_utils import basic_calculator, fibonacci_sequence
# Import other functions as they are added by contributors


def demo_functions():
    """
    Demonstrate all contributed functions.
    
    This function will be updated as new functions are added by team members.
    It showcases the integration of all mathematical utilities in a meaningful way.
    """
    print("=" * 60)
    print("COLLABORATIVE MATH UTILITIES - DEMONSTRATION")
    print("=" * 60)
    
    # Demonstrate basic calculator
    print("\n1. Basic Calculator Demo:")
    print("-" * 30)
    try:
        print(f"Addition: 5 + 3 = {basic_calculator('add', 5, 3)}")
        print(f"Subtraction: 10 - 4 = {basic_calculator('subtract', 10, 4)}")
        print(f"Multiplication: 6 * 7 = {basic_calculator('multiply', 6, 7)}")
        print(f"Division: 15 / 3 = {basic_calculator('divide', 15, 3)}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Demonstrate Fibonacci sequence
    print("\n2. Fibonacci Sequence Demo:")
    print("-" * 30)
    try:
        fib_sequence = fibonacci_sequence(10)
        print(f"First 10 Fibonacci numbers: {fib_sequence}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    
    # TODO: Add demonstrations for other functions as they are contributed
    # print("\n3. Matrix Operations Demo:")
    # print("-" * 30)
    # matrix_a = [[1, 2], [3, 4]]
    # matrix_b = [[2, 0], [1, 3]]
    # result = matrix_multiply(matrix_a, matrix_b)
    # print(f"Matrix multiplication result: {result}")
    
    # print("\n4. Statistical Analysis Demo:")
    # print("-" * 30)
    # data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # stats = statistical_analysis(data)
    # print(f"Statistical analysis: {stats}")
    
    # print("\n5. Prime Numbers Demo:")
    # print("-" * 30)
    # primes = prime_number_generator(20)
    # print(f"Prime numbers up to 20: {primes}")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)


def main():
    """
    Main driver function with multiple interface options.
    """
    parser = argparse.ArgumentParser(
        description='Math Utilities - Collaborative Project',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Run demonstration
  python main.py --analysis         # Run code analysis
        """
    )
    
    parser.add_argument('--analysis', action='store_true',
                       help='Run code analysis')
    parser.add_argument('--demo', action='store_true', default=True,
                       help='Run function demonstration (default)')
    
    args = parser.parse_args()
    
    if args.analysis:
        try:
            import subprocess
            import sys
            result = subprocess.run([sys.executable, 'code_analysis.py'], 
                                  capture_output=False, text=True)
            if result.returncode != 0:
                print("Code analysis completed with warnings or errors.")
        except Exception as e:
            print(f"Error running analysis: {e}")
            print("Make sure radon, flake8, and bandit are installed.")
            sys.exit(1)
    else:
        # Default: run demonstration
        demo_functions()


if __name__ == "__main__":
    main()

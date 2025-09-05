"""
Code Analysis Tool for Math Utilities
Analyzes code complexity, maintainability, and quality metrics.

@author: Admin (Repository Owner)
"""

import os
import sys
import subprocess
import json
from typing import Dict, List, Any
import argparse


class CodeAnalyzer:
    """Code analysis tool using radon and other quality tools."""
    
    def __init__(self, project_root: str = "."):
        self.project_root = project_root
        self.results = {}
    
    def run_radon_analysis(self) -> Dict[str, Any]:
        """Run radon analysis for complexity and maintainability."""
        print("Running radon analysis...")
        
        try:
            # Cyclomatic complexity
            cc_result = subprocess.run(
                ['radon', 'cc', 'math_utils.py', '-a', '--json'],
                capture_output=True, text=True, cwd=self.project_root
            )
            cc_data = json.loads(cc_result.stdout) if cc_result.stdout else []
            
            # Maintainability index
            mi_result = subprocess.run(
                ['radon', 'mi', 'math_utils.py', '-a', '--json'],
                capture_output=True, text=True, cwd=self.project_root
            )
            mi_data = json.loads(mi_result.stdout) if mi_result.stdout else []
            
            # Raw metrics
            raw_result = subprocess.run(
                ['radon', 'raw', 'math_utils.py', '-a', '--json'],
                capture_output=True, text=True, cwd=self.project_root
            )
            raw_data = json.loads(raw_result.stdout) if raw_result.stdout else []
            
            return {
                'cyclomatic_complexity': cc_data,
                'maintainability_index': mi_data,
                'raw_metrics': raw_data
            }
            
        except Exception as e:
            print(f"Error running radon analysis: {e}")
            return {}
    
    def run_flake8_analysis(self) -> Dict[str, Any]:
        """Run flake8 linting analysis."""
        print("Running flake8 analysis...")
        
        try:
            result = subprocess.run(
                ['flake8', 'math_utils.py', '--format=json'],
                capture_output=True, text=True, cwd=self.project_root
            )
            
            if result.stdout:
                return json.loads(result.stdout)
            else:
                return []
                
        except Exception as e:
            print(f"Error running flake8 analysis: {e}")
            return []
    
    def run_bandit_analysis(self) -> Dict[str, Any]:
        """Run bandit security analysis."""
        print("Running bandit security analysis...")
        
        try:
            result = subprocess.run(
                ['bandit', '-r', '.', '-f', 'json'],
                capture_output=True, text=True, cwd=self.project_root
            )
            
            if result.stdout:
                return json.loads(result.stdout)
            else:
                return {}
                
        except Exception as e:
            print(f"Error running bandit analysis: {e}")
            return {}
    
    def run_pytest_coverage(self) -> Dict[str, Any]:
        """Run pytest with coverage analysis."""
        print("Running pytest coverage analysis...")
        
        try:
            result = subprocess.run(
                ['pytest', 'tests/', '--cov=math_utils', '--cov-report=json'],
                capture_output=True, text=True, cwd=self.project_root
            )
            
            # Try to read coverage.json if it exists
            coverage_file = os.path.join(self.project_root, 'coverage.json')
            if os.path.exists(coverage_file):
                with open(coverage_file, 'r') as f:
                    return json.load(f)
            else:
                return {}
                
        except Exception as e:
            print(f"Error running pytest coverage: {e}")
            return {}
    
    def analyze_function_complexity(self, cc_data: List[Dict]) -> Dict[str, Any]:
        """Analyze function complexity and provide recommendations."""
        analysis = {
            'total_functions': len(cc_data),
            'complexity_distribution': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0},
            'high_complexity_functions': [],
            'recommendations': []
        }
        
        for func in cc_data:
            complexity = func.get('complexity', 0)
            grade = func.get('rank', 'F')
            analysis['complexity_distribution'][grade] += 1
            
            if complexity > 10:  # High complexity threshold
                analysis['high_complexity_functions'].append({
                    'name': func.get('name', 'unknown'),
                    'complexity': complexity,
                    'grade': grade,
                    'line': func.get('lineno', 0)
                })
        
        # Generate recommendations
        if analysis['high_complexity_functions']:
            analysis['recommendations'].append(
                "Consider refactoring high complexity functions for better maintainability"
            )
        
        if analysis['complexity_distribution']['F'] > 0:
            analysis['recommendations'].append(
                "Some functions have very high complexity (grade F) - immediate refactoring needed"
            )
        
        return analysis
    
    def analyze_maintainability(self, mi_data: List[Dict]) -> Dict[str, Any]:
        """Analyze maintainability index and provide recommendations."""
        analysis = {
            'average_mi': 0,
            'maintainability_distribution': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0},
            'low_maintainability_functions': [],
            'recommendations': []
        }
        
        if not mi_data:
            return analysis
        
        total_mi = 0
        for func in mi_data:
            mi = func.get('mi', 0)
            grade = func.get('rank', 'F')
            total_mi += mi
            analysis['maintainability_distribution'][grade] += 1
            
            if mi < 20:  # Low maintainability threshold
                analysis['low_maintainability_functions'].append({
                    'name': func.get('name', 'unknown'),
                    'mi': mi,
                    'grade': grade,
                    'line': func.get('lineno', 0)
                })
        
        analysis['average_mi'] = total_mi / len(mi_data) if mi_data else 0
        
        # Generate recommendations
        if analysis['average_mi'] < 30:
            analysis['recommendations'].append(
                "Overall maintainability is low - consider improving code structure and documentation"
            )
        
        if analysis['low_maintainability_functions']:
            analysis['recommendations'].append(
                "Some functions have low maintainability - focus on improving these first"
            )
        
        return analysis
    
    def generate_report(self, output_format: str = 'text') -> str:
        """Generate comprehensive code analysis report."""
        print("Generating comprehensive code analysis report...")
        
        # Run all analyses
        radon_results = self.run_radon_analysis()
        flake8_results = self.run_flake8_analysis()
        bandit_results = self.run_bandit_analysis()
        coverage_results = self.run_pytest_coverage()
        
        # Analyze results
        cc_analysis = self.analyze_function_complexity(radon_results.get('cyclomatic_complexity', []))
        mi_analysis = self.analyze_maintainability(radon_results.get('maintainability_index', []))
        
        # Generate report
        if output_format == 'json':
            return self.generate_json_report(radon_results, flake8_results, bandit_results, 
                                           coverage_results, cc_analysis, mi_analysis)
        else:
            return self.generate_text_report(radon_results, flake8_results, bandit_results, 
                                           coverage_results, cc_analysis, mi_analysis)
    
    def generate_text_report(self, radon_results, flake8_results, bandit_results, 
                           coverage_results, cc_analysis, mi_analysis) -> str:
        """Generate text format report."""
        report = []
        report.append("=" * 80)
        report.append("MATH UTILITIES - CODE ANALYSIS REPORT")
        report.append("=" * 80)
        report.append("")
        
        # Cyclomatic Complexity
        report.append("CYCLOMATIC COMPLEXITY ANALYSIS")
        report.append("-" * 40)
        report.append(f"Total Functions: {cc_analysis['total_functions']}")
        report.append(f"Complexity Distribution: {cc_analysis['complexity_distribution']}")
        
        if cc_analysis['high_complexity_functions']:
            report.append("\nHigh Complexity Functions:")
            for func in cc_analysis['high_complexity_functions']:
                report.append(f"  • {func['name']} (Line {func['line']}): {func['complexity']} ({func['grade']})")
        
        if cc_analysis['recommendations']:
            report.append("\nRecommendations:")
            for rec in cc_analysis['recommendations']:
                report.append(f"  • {rec}")
        
        # Maintainability Index
        report.append("\n\nMAINTAINABILITY INDEX ANALYSIS")
        report.append("-" * 40)
        report.append(f"Average MI: {mi_analysis['average_mi']:.2f}")
        report.append(f"Distribution: {mi_analysis['maintainability_distribution']}")
        
        if mi_analysis['low_maintainability_functions']:
            report.append("\nLow Maintainability Functions:")
            for func in mi_analysis['low_maintainability_functions']:
                report.append(f"  • {func['name']} (Line {func['line']}): {func['mi']:.2f} ({func['grade']})")
        
        if mi_analysis['recommendations']:
            report.append("\nRecommendations:")
            for rec in mi_analysis['recommendations']:
                report.append(f"  • {rec}")
        
        # Flake8 Results
        report.append("\n\nCODE STYLE ANALYSIS (FLAKE8)")
        report.append("-" * 40)
        if flake8_results:
            report.append(f"Total Issues: {len(flake8_results)}")
            for issue in flake8_results[:10]:  # Show first 10 issues
                report.append(f"  • Line {issue['line_number']}: {issue['text']}")
            if len(flake8_results) > 10:
                report.append(f"  ... and {len(flake8_results) - 10} more issues")
        else:
            report.append("No style issues found!")
        
        # Security Analysis
        report.append("\n\nSECURITY ANALYSIS (BANDIT)")
        report.append("-" * 40)
        if bandit_results and 'results' in bandit_results:
            issues = bandit_results['results']
            report.append(f"Security Issues: {len(issues)}")
            for issue in issues[:5]:  # Show first 5 issues
                report.append(f"  • {issue['test_name']}: {issue['issue_text']}")
            if len(issues) > 5:
                report.append(f"  ... and {len(issues) - 5} more issues")
        else:
            report.append("No security issues found!")
        
        # Coverage Analysis
        report.append("\n\nTEST COVERAGE ANALYSIS")
        report.append("-" * 40)
        if coverage_results and 'totals' in coverage_results:
            totals = coverage_results['totals']
            report.append(f"Coverage: {totals.get('percent_covered', 0):.1f}%")
            report.append(f"Lines Covered: {totals.get('covered_lines', 0)}")
            report.append(f"Total Lines: {totals.get('num_statements', 0)}")
        else:
            report.append("Coverage data not available")
        
        report.append("\n" + "=" * 80)
        report.append("END OF REPORT")
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def generate_json_report(self, radon_results, flake8_results, bandit_results, 
                           coverage_results, cc_analysis, mi_analysis) -> str:
        """Generate JSON format report."""
        report = {
            'timestamp': __import__('datetime').datetime.now().isoformat(),
            'cyclomatic_complexity': cc_analysis,
            'maintainability_index': mi_analysis,
            'code_style': {
                'total_issues': len(flake8_results),
                'issues': flake8_results
            },
            'security': bandit_results,
            'coverage': coverage_results.get('totals', {}) if coverage_results else {},
            'raw_radon_data': radon_results
        }
        
        return json.dumps(report, indent=2)


def main():
    """Main function for code analysis."""
    parser = argparse.ArgumentParser(description='Code Analysis Tool for Math Utilities')
    parser.add_argument('--format', '-f', choices=['text', 'json'], default='text',
                       help='Output format (default: text)')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    parser.add_argument('--project-root', '-p', default='.',
                       help='Project root directory (default: current directory)')
    
    args = parser.parse_args()
    
    analyzer = CodeAnalyzer(args.project_root)
    report = analyzer.generate_report(args.format)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report saved to {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()

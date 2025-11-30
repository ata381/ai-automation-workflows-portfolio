#!/usr/bin/env python3
"""
AI Automation Workflows Demo Runner
===================================

This script lets you easily try both of our AI automation workflows.
No technical knowledge required - just run this script and follow the prompts!

Perfect for non-technical clients who want to see AI automation in action.
"""

import os
import sys
import subprocess

def clear_screen():
    """Clear the terminal screen for better readability"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print a nice header for our demo"""
    print("=" * 60)
    print("🤖 AI AUTOMATION WORKFLOWS PORTFOLIO - LIVE DEMO")
    print("=" * 60)
    print()
    print("Welcome! This demo shows how AI can transform your business emails.")
    print("We'll run two powerful AI tools that work completely offline.")
    print()

def run_email_summary():
    """Run the email summary workflow"""
    print("📧 FIRST: EMAIL SUMMARY ASSISTANT")
    print("-" * 40)
    print("This AI tool reads customer emails and gives you:")
    print("• A quick summary of what they want")
    print("• How urgent their request is")
    print("• Exactly what action to take")
    print()
    print("Example: Turns a 300-word rambling email into 3 clear action items!")
    print()

    # Run the workflow
    try:
        result = subprocess.run([
            sys.executable,
            "single-workflow-email-summary/email_summary_workflow.py"
        ], capture_output=True, text=True, input="Y\n")

        print("AI OUTPUT:")
        print("-" * 20)
        # Extract just the output part (skip the input prompt)
        output_lines = result.stdout.strip().split('\n')
        # Find where the actual output starts
        for i, line in enumerate(output_lines):
            if "Summary:" in line:
                print('\n'.join(output_lines[i:]))
                break

    except Exception as e:
        print(f"Oops! Something went wrong: {e}")

    print()
    input("Press Enter to continue to the next demo...")

def run_inbox_helper():
    """Run the inbox helper workflow"""
    clear_screen()
    print("📨 SECOND: SMART INBOX HELPER")
    print("-" * 40)
    print("This comprehensive AI system processes customer emails in 3 steps:")
    print("1. Summarizes the email and detects customer mood")
    print("2. Extracts key information (name, email, order number, etc.)")
    print("3. Drafts a professional reply with the right tone")
    print()
    print("Perfect for businesses handling dozens of customer emails daily!")
    print()

    # Run the workflow
    try:
        result = subprocess.run([
            sys.executable,
            "multi-workflow-inbox-helper/inbox_helper_workflow.py"
        ], capture_output=True, text=True)

        print("AI OUTPUT:")
        print("-" * 20)
        print(result.stdout.strip())

    except Exception as e:
        print(f"Oops! Something went wrong: {e}")

    print()

def show_summary():
    """Show a summary of what they just saw"""
    print("🎉 DEMO COMPLETE!")
    print("-" * 40)
    print()
    print("What you just experienced:")
    print("✅ AI that summarizes emails instantly")
    print("✅ Smart urgency detection")
    print("✅ Automatic information extraction")
    print("✅ Professional reply drafting")
    print("✅ All working offline with no API keys needed!")
    print()
    print("Business Impact:")
    print("• Save hours of manual email processing")
    print("• Handle 3x more customers")
    print("• Reduce response time dramatically")
    print("• Maintain professional, personalized service")
    print()
    print("Ready to bring this AI power to your business?")
    print("Contact us to discuss a custom solution for your specific needs!")
    print()
    print("=" * 60)

def main():
    """Main demo runner"""
    clear_screen()
    print_header()

    print("Let's get started! We'll run two AI workflows:")
    print("1. Email Summary Assistant (for quick email processing)")
    print("2. Smart Inbox Helper (comprehensive customer service automation)")
    print()
    input("Press Enter to begin the first demo...")

    run_email_summary()
    run_inbox_helper()
    show_summary()

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
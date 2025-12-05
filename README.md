# final_project
using gradio to show how binary search does

# Binary search
I chose Gradio for this project because the interface created with this language is cleaner and simpler. I initially considered using Pygame, but setting up the desktop environment with Pygame was more cumbersome than with Gradio, so I abandoned that approach and chose Gradio instead.

<img width="1714" height="769" alt="image" src="https://github.com/user-attachments/assets/20eb87c6-bbed-47af-839d-bc992a4742f4" />

# Operating steps：
1. Copy the code from APP.py.
2. Install the requirement in the terminal. Copy the entire thing from 'requirement.txt'.
3. Run this code.
4. Click the link that is in the terminal, and it will jump to a website.

## Demonstration Instructions:
1. The left input box allows you to enter a sorted array (e.g., 1, 3, 5, 7, 9, 11).

2. The right input box allows you to enter the target value (e.g., 7).

3. Clicking "Generate Random Array" will generate a randomly sorted array.

4. Clicking "Start Search" will begin the search and display detailed steps.

# Instructions for Use
1. Enter a sorted array of integers (comma-separated) in the "Sorted array" input box.
2. Enter the integer value you want to find in the "Target value" input box.
3. Optional: Click "Generate Random Array" to generate a random test array.
4. Click "Start Search" to begin the binary search.
5. View the step-by-step search process displayed in the "Search steps" area.

## Problem Breakdown & Computational Thinking
This project provides a visual demonstration of the binary search algorithm. First, I divided this complex problem into six sub-tasks: input validation, array sorting check, pointer initialization, loop comparison, result recording, and user interface interaction. In the 'pattern recognition' stage, I identified the core patterns of the algorithm—the regularity of the search range halving after each comparison, and the deterministic behavior of the pointer moving left or right based on the comparison result. Next, I performed 'abstraction,' selecting to show users key information (such as changes in the search range, comparisons of intermediate values, and pointer movement direction) to focus the learning on the algorithm's logic rather than implementation details. Finally, by constructing a complete workflow—for example, the user provides input through a graphical interface, the program validates and processes it, and then presents the search process step-by-step, forming a clear teaching loop. This structured thinking process not only ensures the correctness of the code but also makes the final application educational, effectively helping users understand the working principle of binary search.

## AI Declainer: 
I also relied on AI to help me complete this project. Since Gradio was a language I was new to, there were many libraries I didn't know. However, the binary search code was entirely handwritten by me.

## Author Information:

Name: Zitian_Wang

Student ID: 20404102

Course: CISC-121-002

Queen's University

# Acknowledgment:
Instructor：
Thanks to Mr. Ruslan, the instructor of CISC-121, and the teaching assistants for providing detailed project guidelines and grading criteria.

Resource：
Thanks to the official Grado documentation and the technical resources for the Hugging Face Spaces user guide. And thanks to the developers of all the open-source tools and libraries.

# Project characteristics：
1. Clear step-by-step demonstration
2. The random data generation function facilitates testing.
3. Detailed annotations

# Last updated: December 2025

# License: This project is for CISC-121 coursework submissions only.

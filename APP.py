import gradio as gr
import random

def binary_search_visualization(arr_text, target):
    try:
        arr = [int(x.strip()) for x in arr_text.split(",") if x.strip() != ""]
        target = int(target)
    except Exception:
        return "Please provide a valid comma-separated list of integers and an integer target."
    
    if len(arr) == 0:
        return "The array is empty. Provide at least one integer."

    is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    if not is_sorted:
        return "The array must be sorted in non-decreasing order."

    left = 0
    right = len(arr) - 1
    step_count = 0
    steps = []

    while left <= right:
        step_count += 1
        mid = (left + right) // 2
        mid_val = arr[mid]

        steps.append(f"Step {step_count}: search range [{left}, {right}], mid = {mid}, mid_value = {mid_val}")

        if mid_val == target:
            steps.append(f"<!!!!>Found target {target} at index {mid}.")
            break
        elif mid_val < target:
            left = mid + 1
            steps.append(f"Mid moves to right:{mid_val} < {target}, searching right half.")
        else:
            right = mid - 1
            steps.append(f"Mid moves to left:{mid_val} > {target}, searching left half.")
    else:
        steps.append(f"Target {target} not found in the array.")

    return "\n".join(steps)

def generate_random_array(size, min_val, max_val):
    try:
        size = int(size)
        min_v = int(min_val)
        max_v = int(max_val)
    except Exception:
        size = max(1, int(size) if str(size).isdigit() else 8)
        min_v = int(min_val) if str(min_val).lstrip("-").isdigit() else -10
        max_v = int(max_val) if str(max_val).lstrip("-").isdigit() else 10

    if min_v > max_v:
        min_v, max_v = max_v, min_v

    size = max(1, min(1000, size))
    arr = sorted([random.randint(min_v, max_v) for _ in range(size)])
    return ",".join(str(x) for x in arr)

def generate_random_array_simple():
    return generate_random_array(8, -10, 10)

with gr.Blocks(title="Binary Search Visualization") as window:
    gr.Markdown("# 🔍 Binary Search Visualization")
    gr.Markdown("Enter a sorted list of integers and a target value to see each step of binary search.")

    with gr.Row():
        arr_input = gr.Textbox(label="Sorted array (comma separated)", placeholder="e.g.: 1,3,5,7,9,11")
        target_input = gr.Textbox(label="Target value", placeholder="e.g.: 7")

    gen_btn = gr.Button("Generate Random Array")

    btn = gr.Button("Start Search")
    output = gr.Textbox(label="Search steps", lines=12)

    gen_btn.click(
        fn=generate_random_array_simple,
        inputs=[],
        outputs=arr_input
    )

    btn.click(
        fn=binary_search_visualization,
        inputs=[arr_input, target_input],
        outputs=output
    )

    gr.Markdown("### Notes")
    gr.Markdown("- The array should be integers in order.")
    gr.Markdown("- Each step shows the current search range, midpoint and comparison result.")

if __name__ == "__main__":
    window.launch()
import gradio as gr
import random
from typing import List, Tuple

def generate_sorted_list(n:int, low:int=0, high:int=99)->List[int]:
    if n<=0:
        return []
    values=list(range(low, high + 1))
    random.shuffle(values)
    array=sorted(values[:n])
    return array

def binary_search(arr:List[int], target:int)->Tuple[bool,List[str]]:
    steps=[]
    left,right=0,len(arr)-1
    steps.append(f"Initial array: {arr}")
    steps.append(f"Target: {target}")
    step=1
    while left<=right:
        mid=(left + right)//2
        steps.append(f"Step {step}: left={left}, right={right}, mid={mid}, value={arr[mid]}")
        if arr[mid]==target:
            steps.append(f"FOUND {target} at index {mid}")
            return True, steps
        if arr[mid]<target:
            steps.append(f"{arr[mid]} < {target} => Searching RIGHT half of list")
            left=mid+1
        else:
            steps.append(f"{arr[mid]} > {target}=> Searching LEFT half of list")
            right=mid-1
        step+=1
    steps.append(f"Target {target} NOT FOUND")
    return False, steps

def run_search(size, target, seed):
    try:
        n=int(size)
        if n<1:
            return "The length of your List should be aleast 1", ""
    except:
        return "Pls input a integer.", ""
    if seed is not None:
        try:
            random.seed(int(seed))
        except:
            pass
    arr=generate_sorted_list(n)
    try:
        t=int(target)
    except:
        return "Target must be an integer.", f"Array: {arr}"
    found,steps=binary_search(arr, t)
    return "\n".join(steps), ("FOUND !" if found else "NOT FOUND X") + f" — Array: {arr}"

# ----------------- UI Layout -----------------

with gr.Blocks(title="Binary Search Simulator") as demo:
    gr.Markdown("# Binary Search Simulator")
    gr.Markdown("Enter a list size and target number. A sorted list will be generated step-by-step.")
    with gr.Row():
        size=gr.Number(label="List Size", value=10, precision=0)
        seed=gr.Number(label="Seed (optional)", value=0, precision=0)
        target=gr.Textbox(label="Target Number", placeholder="number you looking for, e.g. 13")
    run_btn=gr.Button("Run Binary Search")
    steps_output=gr.Textbox(label="Steps", lines=12)
    result_output = gr.Textbox(label="Result", lines=2)
    run_btn.click(run_search, inputs=[size, target, seed], outputs=[steps_output, result_output])

if __name__ == "__main__":
    demo.launch()

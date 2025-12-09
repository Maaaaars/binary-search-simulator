
---
title: Binary Search Simulator
emoji: 🔍
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "4.44.0"
app_file: app.py
pinned: false
---



Tianyi Li
CISC-121 Project

---
-Hugging Face Space
https://huggingface.co/spaces/DeadlyPants76/binary-search-simulator

-Github
https://github.com/Maaaaars/binary-search-simulator
---

-Overview
This project plays Binary Search with an interactive UI built using Gradio.  
The app generates a sorted list of integers and shows how each step of the binary search process.

---

Computational Thinking

-Decomposition
- Generate a sorted list that find a target number  
- Then perform binary search with it and record each comparison  
- At last display steps + result  

-Pattern Recognition
Binary search involve
- Finding the middle value and compares it against the target then halves the search list  

-Abstraction
it will be a simple app with ui, box to input array size and target num on top and then the
result comes on the big box below it.
- it needs a random list generation(need to prove array or array length)
- out put will be the steps

-Algorithm Design
Input:list size, target, and a seed(optional, just to randomize the list)
Process:generate list => run binary search => collect steps  
Output:the step logs and final result message

---

How to Run
1.paste this link in browser https://huggingface.co/spaces/DeadlyPants76/binary-search-simulator
2.It will lead you to the app on huggingface.co, then input List Size and Target Number on the input box on top.
3.click "Run Binary Search", the process and result will show on the box below.

---

-Testing 
-Target found
![Target found](screenshots/Found.png)
-Target not dound

![Not found](screenshots/NotFound.png)
-list size = 0

![Wrong value](screenshots/wrongInput.png)


























-egg:（Just to complain a bit, it freaking took me an hour to found out that I just different requirements in the requirement file and fix the runtime error, and it took me another to find out I need a Hugging Face Spaces configuration block on the top of the readme, I mean, what the xxxx?）










ps -- Fxxx python
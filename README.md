# sealing-visual-inspection-webui
Master Thesis project for inspecting sealing products using different deep learning models

# webui architecture 
In my webui for automated defect visual inspection, I want to achieve several things:

- I want to create multiple screens for different purposes
    - Main/Home Screen
    - Training Screen
    - Detection Screen
- In the training screen
    - The user to be able to choose different models for training
    - The user should be able to customize parameters such as epoch, batch size, an so on
    - The user should be able to see the training progress (the cmd line output)
    - The user should be able to stop the training progress
    - The user should be able to save the training results (weights and configuration) to the database so that the user can later access in the detection screen
- In the detection screen
    - The user should be able to choose different models for detecting
    - The user should be able to choose the training results that was done in the training screen
    - The user should be able to see the display of live camera
    - The user should be able to start detecting with the desired model and weights
    - The user should be able to see live detection
    - The user should be able to adjust parameters like different confidence level, and so on
    - The user should be able to also detect not live but videos.
    - After detection of a video the user will be prompted to choose if the user wants to see a report of the detection
    - After a period of live detection, the user can click on a button to stop live detection, and then be prompted to choose if the user wants to see a report of the live detection just now

# Webui-Database-Functions Flowchart
![System design](https://github.com/GunBay1008/sealing-visual-inspection-webui/assets/100042054/16d0af04-9c7f-4278-b199-365957d2443d)

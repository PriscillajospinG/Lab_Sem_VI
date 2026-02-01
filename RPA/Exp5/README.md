# Experiment 5: Typing the Data in Notepad Using RPA

## Aim
To automate notepad application using UiPath.

## Description
This experiment demonstrates automating the Notepad application using UiPath Studio. The workflow opens Notepad, types the text "RPA LAB," performs file menu operations, saves the file with a specified name, and closes the application automatically. This experiment highlights how UiPath can be used to automate basic desktop application tasks efficiently.

## Procedure

### Step 1: Start New Project
- Open UiPath Studio
- Click **Process** to start a new project

### Step 2: Create Blank Process
- Create a new blank process by giving a name
- Click **Create**

### Step 3: Open Main Workflow
- Click **Open Main Workflow**

### Step 4: Add Open Application Activity
- From **Activities**, choose **Open Application**
- Drag and drop it into the workflow
- Open Notepad application on your computer (don't minimize it)
- In the **Open Application** activity, click **Indicate window on screen**
- Select the Notepad window
- Close Notepad and run to verify if Notepad opens correctly

### Step 5: Add Type Into Activity
- From **Activities**, choose **Type Into**
- Drag and drop it inside the Open Application scope
- In the text field, type:
  ```
  "RPA LAB"
  ```
  (Include the double quotes)

### Step 6: Click on File Menu
- From **Activities**, choose **Click**
- Drag and drop it after Type Into
- Click **Indicate element inside window**
- Select the **File** menu in Notepad

### Step 7: Click on Save As
- From **Activities**, choose **Click**
- Drag and drop it
- Click **Indicate on screen**
- Press **F2** to add a delay (gives you time to navigate)
- Click on **Save As** option in the File menu
- Close Notepad and run to verify

### Step 8: Type File Name
- From **Activities**, choose **Type Into**
- Drag and drop it
- In the text field, type the filename you want to save:
  ```
  "RPA_Lab_File"
  ```
- Click **Indicate element inside window**
- Select the filename text box (where it shows `*.txt`)
- Close Notepad and run to verify

### Step 9: Click Save Button
- From **Activities**, choose **Click**
- Drag and drop it
- Click **Indicate element inside window**
- Select the **Save** button
- Close Notepad and run to verify

### Step 10: Click Close Button
- From **Activities**, choose **Click**
- Drag and drop it
- Click **Indicate element inside window**
- Select the **Close (X)** button of Notepad
- Before running the program, delete any previously saved file from desktop
- Close Notepad and run the complete workflow

## Workflow Structure
```
Main.xaml
├── Open Application (Notepad)
│   ├── Type Into ("RPA LAB")
│   ├── Click (File menu)
│   ├── Click (Save As)
│   ├── Type Into (filename)
│   ├── Click (Save button)
│   └── Click (Close button)
```

## Output
- Notepad opens automatically
- "RPA LAB" is typed in the Notepad
- File menu is clicked
- Save As dialog appears
- File is saved with the specified name
- Notepad closes automatically

## Result
Thus, typing the data in notepad using RPA is completed successfully.

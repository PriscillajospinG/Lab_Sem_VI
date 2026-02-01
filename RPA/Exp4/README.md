# Experiment 4: Copying of Data from Browser to Notepad

## Aim
To automate notepad application and copying data from browser to notepad using UiPath.

## Description
This experiment demonstrates automating the Notepad application using UiPath by copying text from a browser. UiPath Studio is used to open a browser, extract selected text from a web page, and store it in a variable. The extracted text is then typed into the Notepad application automatically. This shows how UiPath can integrate multiple applications to automate data transfer efficiently.

## Procedure

### Step 1: Start New Project
- Open UiPath Studio
- Click **Process** to start a new project

### Step 2: Create Blank Process
- Create a new blank process by giving a name
- Click **Create**

### Step 3: Open Main Workflow
- Click **Open Main Workflow**

### Step 4: Open Website in Browser
- Open any website in the browser (e.g., a webpage with text you want to copy)

### Step 5: Add Use Browser/Application Activity
- From **Activities**, choose **Use Browser/Application**
- Drop it into the workflow
- Click **Indicate window on screen** and select the browser window

### Step 6: Create Browser Variable
- Create a variable for the browser
- For Variable Type, search and select **UiPath.Core.Browser**

### Step 7: Add Get Text Activity
- From **Activities**, choose **Get Text**
- Drop it inside the Use Browser/Application scope
- Create a variable:
  - Variable Name: `Textout`
  - Scope: **Sequence**
- In the Properties panel (right corner):
  - Set **Output Text** to: `Textout`
- Click **Indicate element inside browser**
- Select the text element you want to copy from the webpage

### Step 8: Open Notepad Application
- Open Notepad application on your computer
- From **Activities**, choose **Use Browser/Application**
- Drop it after the browser scope
- Click **Indicate element inside browser** and select the Notepad window

### Step 9: Add Type Into Activity
- From **Activities**, choose **Type Into**
- Drop it inside the Notepad scope
- Click **Indicate element inside browser** and click on the Notepad text area where you want the text to appear
- In the text field, type:
  ```
  Textout
  ```

### Step 10: Save and Run
- Save the file
- Close Notepad
- Click **Run** or press **F5** to execute

## Workflow Structure
```
Main.xaml
├── Use Browser/Application (Browser)
│   └── Get Text → Textout
├── Use Browser/Application (Notepad)
│   └── Type Into (Textout)
```

## Output
- The bot opens the browser and extracts the selected text
- The bot opens Notepad and types the extracted text automatically
- The text from the browser appears in Notepad

## Result
Thus, the copying of data from browser to notepad is completed successfully.

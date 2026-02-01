# Experiment 3: Identifying Odd or Even Number in UiPath

## Aim
To check whether the given number is odd or even.

## Description
This experiment is designed to identify whether a given number is Odd or Even using UiPath Studio. In this workflow, a number is taken as input (from the user or assigned to a variable) and checked using the modulus operator (`Number Mod 2`). If the remainder is 0, the number is Even; otherwise, it is Odd. The result is displayed using a Message Box or Write Line, helping to understand the use of If conditions, variables, and decision-making logic in UiPath automation.

## Procedure

### Step 1: Start New Project
- Open UiPath Studio
- Click **Process** to start a new project

### Step 2: Create Blank Process
- Create a new blank process by giving a name
- Click **Create**

### Step 3: Open Main Workflow
- Click **Open Main Workflow**

### Step 4: Add Input Dialog
- From **Activities**, select **Input Dialog** and drop it into the workflow
- Configure:
  - **Dialog Title**: `"Enter a Number"`
  - **Input Label**: `"Number:"`
  - **Value Entered**: Store in variable

### Step 5: Create Variable
- For the value entered, create a variable:
  - Variable Name: `num1`
  - Variable Type: **Int32**
  - Scope: **Sequence**

### Step 6: Add If-Else Condition
- From **Activities**, select **If** activity and drop it in the main workflow
- In the **Condition** field, type:
  ```
  num1 Mod 2 = 0
  ```

### Step 7: Configure "Then" Block (Even)
- In the **Then** section:
  - From **Activities**, select **Message Box** and drop it
  - In the text field, type:
    ```
    "The number " + num1.ToString + " is EVEN"
    ```

### Step 8: Configure "Else" Block (Odd)
- In the **Else** section:
  - From **Activities**, select **Message Box** and drop it
  - In the text field, type:
    ```
    "The number " + num1.ToString + " is ODD"
    ```

### Step 9: Save and Run
- Save the project
- Click **Run** or press **F5** to execute the sequence

## Workflow Structure
```
Main.xaml
├── Input Dialog (Get number from user) → num1
└── If (num1 Mod 2 = 0)
    ├── Then: Message Box ("Even")
    └── Else: Message Box ("Odd")
```

## Output
- An input dialog appears asking for a number
- Based on the input:
  - If the number is divisible by 2: Displays **"The number X is EVEN"**
  - If the number is not divisible by 2: Displays **"The number X is ODD"**

### Example:
- Input: `10` → Output: "The number 10 is EVEN"
- Input: `7` → Output: "The number 7 is ODD"

## Result
Thus, whether the given number is odd or even is checked successfully.

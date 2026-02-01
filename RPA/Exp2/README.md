# Experiment 2: Arithmetic Operations Using UiPath

## Aim
To perform arithmetic operations on two numbers using UiPath.

## Description
This experiment is used to automate basic arithmetic operations on two input numbers using UiPath Studio. In this workflow, two numbers are taken as input (from the user or assigned in variables) and operations such as Addition, Subtraction, Multiplication, and Division are performed using UiPath activities and expressions. The calculated results are then displayed using a Message Box or Output panel, helping to understand the use of variables, data types, and calculations in UiPath automation.

## Procedure

### Step 1: Start New Project
- Open UiPath Studio
- Click **Process** to start a new project

### Step 2: Create Blank Process
- Create a new blank process by giving a name
- Click **Create**

### Step 3: Open Main Workflow
- Click **Open Main Workflow**

### Step 4: Add Input Dialog Boxes
- From **Activities**, select **Input Dialog** and drop it into the workflow
- Configure the first Input Dialog:
  - **Dialog Title**: `"Enter First Number"`
  - **Input Label**: `"Number 1:"`
  - **Value Entered**: Store in variable
- Add a second **Input Dialog** for the second number:
  - **Dialog Title**: `"Enter Second Number"`
  - **Input Label**: `"Number 2:"`
  - **Value Entered**: Store in variable

### Step 5: Create Variables
- For the values entered, create variables:
  - Variable Name: `num1`
  - Variable Type: **Int32**
- Create another variable:
  - Variable Name: `num2`
  - Variable Type: **Int32**

### Step 6: Perform Addition
- From **Activities**, select **Message Box** and drop it in the main workflow
- In the text field, type:
  ```
  "Sum: " + (num1 + num2).ToString
  ```

### Step 7: Perform Other Operations
Similarly, add Message Box activities for:

**Subtraction:**
```
"Difference: " + (num1 - num2).ToString
```

**Multiplication:**
```
"Product: " + (num1 * num2).ToString
```

**Division:**
```
"Quotient: " + (num1 / num2).ToString
```

### Step 8: Save and Run
- Save the project
- Click **Run** or press **F5** to execute the sequence

## Output
- Input dialogs appear to get two numbers from the user
- Message boxes display the results of:
  - Addition
  - Subtraction
  - Multiplication
  - Division

## Result
Thus, the arithmetic operations are performed successfully.

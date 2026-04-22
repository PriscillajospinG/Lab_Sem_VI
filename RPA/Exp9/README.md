# Experiment 9: PDF Automation in UiPath

## Aim
To automate reading and extracting text from a PDF file using UiPath Studio.

## Objective
This experiment shows how UiPath can read text from a PDF, display it, and save it into a text file.

## Prerequisites
- UiPath Studio installed
- PDF Activities package installed
- A sample PDF file
- Text editor or Notepad for viewing output

## Workflow Overview
The bot:
1. Installs the PDF package.
2. Creates a flowchart and sequence.
3. Uses **Read PDF Text** to extract the content.
4. Shows the result using a **Message Box**.
5. Saves the output using **Write Text File**.

## Procedure
### 1. Create a New Project
- Open UiPath Studio.
- Click **Process**.
- Create a new blank process.

### 2. Open the Main Workflow
- Click **Open Main Workflow**.

### 3. Install PDF Package
- Open **Manage Packages**.
- Search for the UiPath PDF package.
- Install it and save.

### 4. Create the Workflow
- Create a new **Flowchart** and name it `pdf read text`.
- Add a **Sequence** inside the flowchart.

### 5. Read the PDF
- Add **Read PDF Text**.
- Upload the PDF file.
- Set the range to `All`.
- Store the output in a variable such as `output`.

### 6. Display the Text
- Add **Message Box**.
- Type the output variable inside it.

### 7. Save the Text
- Add **Write Text File**.
- Provide the output variable.
- Save the text file.

### 8. Run the Workflow
- Save the project.
- Run the automation.

## Output
- Text is extracted from the PDF.
- The content is displayed in a message box.
- The same content is stored in a text file.

## Result
Thus, the process of reading PDF text using UiPath Studio is completed successfully.

## Viva Points
- Why do we install the PDF package?
- What is the use of `Read PDF Text`?
- Why do we save extracted text to a file?
- What is the purpose of a flowchart in UiPath?

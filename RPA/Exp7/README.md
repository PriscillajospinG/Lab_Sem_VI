# Experiment 7: Data Exporting from Excel to Webpage

## Aim
To automate exporting data from an Excel file to a webpage using UiPath Studio.

## Objective
This experiment shows how UiPath can read rows from an Excel sheet and fill a web form automatically using a loop.

## Prerequisites
- UiPath Studio installed
- Excel installed
- Browser access
- Basic knowledge of DataTable and loop activities

## Workflow Overview
The bot:
1. Downloads the RPA Challenge Excel file.
2. Reads the sheet into a DataTable.
3. Opens the RPA Challenge webpage.
4. Clicks the start button.
5. Uses a `For Each Row` loop to enter each record into the web form.
6. Submits all rows one by one.

## Procedure
### 1. Create a New Project
- Open UiPath Studio.
- Click **Process**.
- Create a new blank process.

### 2. Open the Main Workflow
- Click **Open Main Workflow**.

### 3. Download the Excel File
- Open the browser.
- Go to [rpachallenge.com](https://rpachallenge.com).
- Download the Excel file from the webpage.

### 4. Read the Excel Data
- Use **Use Browser/Application** to indicate the browser.
- Add **Read Range Workbook**.
- Select the Excel file and sheet name.
- Store the output in a `DataTable` variable, for example `contactdetails`.

### 5. Start the Web Challenge
- Open the RPA Challenge webpage.
- Click the **Start** button.

### 6. Loop Through the Rows
- Add **For Each Row in Data Table**.
- Use the DataTable variable in the loop.
- Inside the loop, use **Type Into** and **Click** activities.
- Use **Anchor Base** if needed to locate fields accurately.

### 7. Enter Data and Submit
- Enter each field value using `row(columnName).ToString`.
- Click **Submit** for each row.

## Output
- The Excel data is read successfully.
- The webpage is filled automatically.
- All records are submitted with minimal manual effort.

## Result
Thus, exporting of data from Excel to webpage using UiPath is completed successfully.

## Viva Points
- What is a DataTable in UiPath?
- Why do we use `For Each Row`?
- What is the purpose of `Read Range Workbook`?
- Why is `Anchor Base` useful in web automation?

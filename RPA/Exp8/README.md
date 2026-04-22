# Experiment 8: Data Scraping in UiPath Studio

## Aim
To perform data scraping from a website using UiPath Studio.

## Objective
This experiment demonstrates how to extract structured information from a webpage and save it into an Excel file.

## Prerequisites
- UiPath Studio installed
- Browser access
- Excel installed
- Basic understanding of scraping and Excel activities

## Workflow Overview
The bot:
1. Opens Amazon in a browser.
2. Searches for "Automation books".
3. Uses **Extract Table Data** to collect book names and prices.
4. Stores the extracted data in a table format.
5. Writes the data into an Excel file using **Write Range Workbook**.

## Procedure
### 1. Create a New Project
- Open UiPath Studio.
- Click **Process**.
- Create a new blank process.

### 2. Open the Main Workflow
- Click **Open Main Workflow**.

### 3. Open the Website
- Open a browser and go to [amazon.in](https://www.amazon.in).
- Use **Use Browser/Application** and indicate the browser.

### 4. Search for Books
- Add **Type Into**.
- Indicate the search bar.
- Type `Automation books`.
- Add **Click** and choose the **Go** button.

### 5. Extract Table Data
- Select **Extract Table Data** from activities.
- Click **Add column** and select the first book name.
- Add another column for the price.
- Rename columns if needed.
- Save the extraction.

### 6. Write Data to Excel
- Use **Write Range Workbook**.
- Create a blank Excel file.
- Indicate the first cell in the sheet.
- Enable **Add Headers** in the properties.

### 7. Set the Number of Items
- In the properties of **Extract Table Data**, specify the number of records required.

## Output
- Book details and prices are scraped from the webpage.
- The data is saved into an Excel sheet.

## Result
Thus, we successfully completed the data scraping using UiPath Studio.

## Viva Points
- What is data scraping?
- Why do we use `Extract Table Data`?
- What is the use of `Write Range Workbook`?
- Why are headers important in Excel output?

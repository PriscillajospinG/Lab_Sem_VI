# Experiment 10: Email Automation in UiPath

## Aim
To automate sending emails using UiPath Studio.

## Objective
This experiment demonstrates how UiPath can connect to a Gmail account and send an email automatically.

## Prerequisites
- UiPath Studio installed
- A Gmail account
- Internet connection
- Permission to use the account in UiPath

## Workflow Overview
The bot:
1. Opens a new UiPath process.
2. Connects to a Gmail account using **Use Gmail**.
3. Uses **Send Email** to compose and send the message.
4. Fills receiver email, subject, and body.
5. Sends the email directly without saving it as a draft.

## Procedure
### 1. Create a New Project
- Open UiPath Studio.
- Click **Process**.
- Create a new blank process.

### 2. Open the Main Workflow
- Click **Open Main Workflow**.

### 3. Connect Gmail Account
- Add **Use Gmail** activity.
- Click **Please select an account**.
- Add or choose a Google account.
- Confirm the account.

### 4. Send the Email
- Add the **Send Email** activity.
- Enter the receiver email address in double quotes.
- Enter the subject.
- Enter the body message.

### 5. Adjust Properties
- Go to properties.
- Deselect **Save as Draft** so the email is sent directly.

### 6. Run the Workflow
- Save the project.
- Run the automation.

## Output
- UiPath connects to the Gmail account.
- The email is sent successfully to the receiver.

## Result
Thus, the email automation is done using UiPath Studio.

## Viva Points
- What is the use of `Use Gmail` activity?
- Why do we disable `Save as Draft`?
- What fields are required in an email automation workflow?
- How does UiPath improve email processing?

# CLI APP
## Team Project - G7

> This command line interface (CLI) application allows you to easily manage your contacts, birthdays and notes. Follow the instructions below to interact with the app.

# How to use app?

## Step 1. Installation
1. Clone the repository:
```shell
git clone https://github.com/vorobeiDev/project-g7-contact-book-cli
```
2. Open project folder:
```
cd project_folder_name
```
3. [Download](https://www.python.org/downloads/) and install Python 3.10+.

4. Create a virtual environment for Python:
```shell
python -m venv /path/to/new/virtual/environment
```

5. Activate the virtual environment:
   - In cmd.exe, run:
    ```shell
    venv\Scripts\activate.bat
    ```
   - In PowerShell, run:
   ```shell
   venv\Scripts\Activate.ps1
   ```
6. Install required packages:
```shell
pip install -r requirements.txt
```

## Step 2. Run the program or create .exe file:

### Run python script:
   ```shell
   python app.py
   ```

### Crate build and run .exe file:
1. Run command:
```shell
python setup.py build
```
2. Open folder /app.
3. Run file g7cli.exe:
```shell
app/g7cli.exe
```

## Commands
1. Adding a new contact
   1. **Command:** `add`
   2. **Example:** `add`
2. Adding a phone to existing contact
   1. **Command:** `add-phone <name>`
   2. **Example:** `add-phone JohnDoe`
3. Adding an email to existing contact
   1. **Command:** `add-email <name>`
   2. **Example:** `add-emai John Doe`
4. Adding an address to existing contact
   1. **Command:** `add-address <name>`
   2. **Example:** `add-address John Doe`
5. Adding a birthday to existing contact
   1. **Command:** `add-birthday <name>`
   2. **Example:** `add-birthday John Doe`
6. Changing a contact's phone number
   1. **Command:** `change <name>`
   2. **Example:** `change John Doe`
7. Getting all phone numbers for a contact
   1. **Command**: `phone <name>`
   2. **Example:** `phone JohnDoe`
8. List all contacts
   1. **Command:** `all`
9. Displaying a contact's birthday
   1. **Command:** `birthday <name>`
   2. **Example:** `birthday John Doe`
10. Displaying birthdays for in the next days in advance
    1. **Command:** `birthdays <days_in_advance>`
11. Searching for contacts
    1. **Command:** `search <search_query>`
    2. **Example:** `search John` `search 09`
12. Deleting a contact
    1. **Command:** `delete <name>`
    2. **Example:** `delete UserName`
13. Adding a note
    1. **Command:** `add-note <title>`
    2. **Example:** `add-note reminding`
14. Editing a note
    1. **Command:** `change-note <id>`
    2. **Example:** `change-note 1`
15. Deleting a note
    1. **Command**: `delete-note <id>`
    2. **Example**: `delete-note 1`
16. Displaying all notes
    1. **Command**: `list-notes`
17. Adding a new tag to a note
    1. **Command**: `add-tag <id> <title>`
    2. **Example**: `add-tag 1 dog`
18. Deleting a tag from a note
    1. **Command**: `delete-tag <id> <title>`
    2. **Example**: `delete-tag 1 dog`
19. Exiting the program
20. Use any of the following **commands:** `exit, close`

## Additional Information
The program automatically saves your contacts in book.pkl and notes in notebook.pkl for future use.

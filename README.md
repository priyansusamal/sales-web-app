Sales Web App (Flask)

Project Overview

This project is a full stack web application built using Flask, SQLite, and HTML. It allows users to view, add, and delete sales data through a web interface.

---

Features

*  View sales data in a table
*  Add new records from the browser
*  Delete records
*  Real-time updates
*  Data stored in SQLite database

---

Technologies Used

* Python
* Flask
* SQLite
* HTML
* CSS

---

Project Structure

```
sales-web-app/
│
├── database/
│   └── sales.db
│
├── templates/
│   └── index.html
│
├── app.py
├── create_db.py
└── README.md
```

---

How to Run

1. Install dependencies:

```bash
pip install flask pandas
```

2. Create the database:

```bash
python create_db.py
```

3. Run the application:

```bash
python app.py
```

4. Open in browser:
```

---

Functionality

* Users can input product, region, category, and sales
* Data is stored in the database instantly
* Records are displayed dynamically
* Records can be deleted from the UI

---

Learning Outcomes

* Building web apps using Flask
* Connecting frontend with backend
* Handling forms and user input
* Performing CRUD operations in a web environment
* Working with databases in web applications

---

Future Improvements

* Add update/edit functionality
* Improve UI with advanced CSS or frameworks
* Add authentication (login system)
* Deploy the app online

---
Author

[Priyansu Samal]

---

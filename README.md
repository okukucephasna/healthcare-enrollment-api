
# Health Information System — Full Stack Application

This project is a simple but functional health information system designed to manage clients, health programs, and client enrollments. The system is built using **Flask** for the backend and **React** for the frontend.

The goal of this project is to demonstrate how a full-stack application can be structured with clean code, proper separation of concerns, and a simple API-first approach.

---

## 💡 Project Overview

The system allows a user (e.g., a doctor or administrator) to:

* **Register new clients** and view all registered clients.
* **Create and list health programs** (e.g., Malaria, HIV).
* **Enroll clients into one or more programs**.
* **View enrolled clients and their associated programs**.

The API is built with Flask using raw SQL queries via **PyMySQL**, and the frontend is a basic **React** app consuming this API using **Axios**. The React app is built and served through Flask, allowing both backend and frontend to be hosted together.

---

## 🎨 Current Features

* ✅ **Client Management** — Add new clients and view all registered clients.
* ✅ **Program Management** — Add new health programs and list existing ones.
* ✅ **Enrollments** — Enroll clients into selected programs and view enrollment lists.
* ✅ **REST API** — Cleanly structured API routes with proper validations.
* ✅ **React Frontend** — Simple interface with Axios fetching and posting data to the Flask backend.
* ✅ **Full Integration** — The React frontend is compiled and served through Flask after building.
* ✅ **Ready for expansion** — Future updates will include styling, authentication, and more features.

---

## 📸 Sample Screenshots

I’ll include sample screenshots here after running the application:

| Clients Page           | Programs Page           | Enrollments Page           |
| ---------------------- | ----------------------- | -------------------------- |
| Clients page
<img width="572" height="333" alt="image" src="https://github.com/user-attachments/assets/4bea390c-8927-466a-a779-0e3696a4ad63" /> | Enrollment page
<img width="453" height="334" alt="image" src="https://github.com/user-attachments/assets/a8ddff86-720c-4aa1-bae2-bbcd209380ca" />| *\[Enrollment Screenshot]* |

---

## 🛠️ Technologies Used

| Backend              | Frontend            | Database            |
| -------------------- | ------------------- | ------------------- |
| Flask (Python)       | React (JavaScript)  | MySQL (via PyMySQL) |
| Flask Blueprints     | Axios for API calls | Raw SQL Queries     |
| RESTful Architecture | React Router        |                     |

---

## 🚀 How to Run This Project

### 1. Clone the Repository

```bash
git clone <repository-link>
```

---

### 2. Backend Setup (Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

This will start the Flask API and also serve the frontend after building it.

---

### 3. Frontend Setup (React)

```bash
cd frontend
npm install
npm run build
```

This builds the React frontend. Flask will automatically serve the `build/` folder from the backend.

---

## 📂 Project Structure Overview

```
project-root/
├── backend/
│   ├── app.py               # Main Flask app
│   ├── db.py                # Database connection (PyMySQL)
│   ├── client_routes.py     # Client API routes
│   ├── program_routes.py    # Program API routes
│   └── enrollment_routes.py # Enrollment API routes
└── frontend/
    ├── src/components/      # React components
    └── build/               # React build folder served by Flask
```

---

API Overview

| Method | Endpoint       | Purpose                         |
| ------ | -------------- | ------------------------------- |
| GET    | `/clients`     | Retrieve all registered clients |
| POST   | `/clients`     | Register a new client           |
| GET    | `/programs`    | List all health programs        |
| POST   | `/programs`    | Add a new health program        |
| GET    | `/enrollments` | List all client enrollments     |
| POST   | `/enrollments` | Enroll a client in a program    |

---
Postman Screenshot of runnning the API, and get clients data from the mysql db
<img width="635" height="386" alt="image" src="https://github.com/user-attachments/assets/87786dec-e788-4122-8527-639505ef86b0" />

Postman Screenshot of runnning the API, and get eenrollments data from the mysql db
<img width="633" height="379" alt="image" src="https://github.com/user-attachments/assets/dc8e9230-d261-4d6c-8aff-2271693143dd" />

Postman Screenshot of runnning the API, and get program data from the mysql db
<img width="641" height="375" alt="image" src="https://github.com/user-attachments/assets/afb163bc-d0e2-4b42-9e2c-65ad0341e7a7" />

Future Plans

This version is a minimal functional setup focusing on API structure and React integration. Planned improvements include:

* ✅ Adding **Bootstrap** or **Material UI** for styling.
* ✅ Creating a **dashboard interface**.
* ✅ Implementing **user authentication** (login and protected routes).
* ✅ Dockerizing for easy deployment.
* ✅ Adding **unit tests** on both backend and frontend.
* ✅ Improving error handling and notifications on the frontend.

---

About the Author
Built and maintained by Cephas Okuku as part of a software engineering practical demonstration.


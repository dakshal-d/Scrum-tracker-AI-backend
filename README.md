# MemoryChronicles

<p>A MERN Stack project for storing day-to-day adventures of your life.</p>

![Screenshot 2023-08-22 124220](https://github.com/dakshal-d/MemoryChronicles/assets/103371054/5da3c417-0cd9-4077-b3e5-abf5a357cb5f)

![Screenshot 2023-08-22 124145](https://github.com/dakshal-d/MemoryChronicles/assets/103371054/f7ffabe1-9ce6-442e-9a38-4f37d0a1915c)

# Features

<ul>
    <li>User Registration and Authentication</li>
    <li>Login and Signup functionality</li>
    <li>Create, Read, Update, and Delete notes</li>
    <li>Secure access to account after login</li>
</ul>

# Python Backend

This backend has been migrated from Express/Node.js to Python Flask while keeping the same API routes and response shapes.

```shell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Required environment variables:

```env
PORT=4000
MONGO_CONNECTION_URL=your-mongodb-connection-string
MONGO_DB_NAME=test
JWT_SECRET=dakshal
```

API routes:

- `GET /`
- `GET /user`
- `POST /user/register`
- `POST /user/login`
- `GET /note`
- `POST /note/create`
- `PATCH /note`
- `DELETE /note`

For note routes, pass the login token in the `Authorization` header, matching the previous Node.js backend behavior.

# Installation

Clone the repository:

```shell
git clone https://github.com/dakshal-d/MemoryChronicles.git
```

Clone the backend repository:

```shell
git clone https://github.com/dakshal-d/MemoryChronicles-backend.git
```

Install backend dependencies and start the server:

```shell
pip install -r requirements.txt
python app.py
```

Open your browser and navigate to <a href="http://localhost:4000">http://localhost:4000</a> to use the API.

<h2 id="usage">Usage</h2>
<ol>
    <li>Register or log in to your account.</li>
    <li>Create, view, edit, and delete your adventure notes.</li>
    <li>Access your account securely after login.</li>
</ol>

# Technologies Used
<ul>
    <li>MongoDB</li>
    <li>Flask</li>
    <li>React</li>
    <li>Python</li>
    <li>Tailwind CSS</li>
</ul>




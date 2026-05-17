# FROM node:18
# WORKDIR /app
# COPY package*.json ./
# RUN npm install  # Install bcrypt here in Linux
# COPY . .
# RUN npm install -g nodemon
# EXPOSE 4000
# CMD ["nodemon", "app.js"]

FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4000
CMD ["python", "app.py"]

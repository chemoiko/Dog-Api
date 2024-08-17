# 🐶 Dog and Breed API

This project provides a simple Django REST API for managing dogs and their breeds. The API allows users to create, retrieve, update, and delete records for dogs and breeds. Each dog record is associated with a breed, and each breed has specific characteristics like size, friendliness, and trainability.

## 📋 Table of Contents
- [✨ Features](#-features)
- [🐕 Models](#-models)
- [📡 API Endpoints](#-api-endpoints)
- [🧪 Testing](#-testing)


## ✨ Features
- Create, retrieve, update, and delete dog records.
- Create, retrieve, update, and delete breed records.
- Easily extendable and customizable.
- Follows RESTful best practices.

## 🐕 Models

### Dog Model
**Fields:**
- **name**: Character string, name of the dog.
- **age**: Integer, age of the dog.
- **breed**: Foreign key to the Breed model.
- **gender**: Character string, gender of the dog.
- **color**: Character string, color of the dog.
- **favoritefood**: Character string, dog's favorite food.
- **favoritetoy**: Character string, dog's favorite toy.

### Breed Model
**Fields:**
- **name**: Character string, name of the breed.
- **size**: Character string, size of the breed (Tiny, Small, Medium, Large).
- **friendliness**: Integer, friendliness level (1-5).
- **trainability**: Integer, trainability level (1-5).
- **sheddingamount**: Integer, shedding amount (1-5).
- **exerciseneeds**: Integer, exercise needs (1-5).

## 📡 API Endpoints

### Dogs
- **GET** `/api/dogs/`: Retrieve the list of all dogs.
- **POST** `/api/dogs/`: Create a new dog.
- **GET** `/api/dogs/{id}/`: Retrieve a specific dog by ID.
- **PUT** `/api/dogs/{id}/`: Update a specific dog by ID.
- **DELETE** `/api/dogs/{id}/`: Delete a specific dog by ID.

### Breeds
- **GET** `/api/breeds/`: Retrieve the list of all breeds.
- **POST** `/api/breeds/`: Create a new breed.
- **GET** `/api/breeds/{id}/`: Retrieve a specific breed by ID.
- **PUT** `/api/breeds/{id}/`: Update a specific breed by ID.
- **DELETE** `/api/breeds/{id}/`: Delete a specific breed by ID.

## 🧪 Testing

You can test the API endpoints using tools like Postman or `curl`.

### Example Requests

#### Create a new Dog:

```json
POST /api/dogs/
{
  "name": "Rex",
  "age": 3,
  "breed": 1,
  "gender": "Male",
  "color": "Brown",
  "favoritefood": "Bones",
  "favoritetoy": "Ball"
}

PUT /api/dogs/1/
{
  "name": "Rex",
  "age": 4,
  "breed": 1,
  "gender": "Male",
  "color": "Brown",
  "favoritefood": "Meat",
  "favoritetoy": "Frisbee"
}


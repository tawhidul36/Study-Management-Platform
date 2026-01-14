# Study Management Platform API

A Django REST Framework backend for managing student study materials with JWT authentication.

## Setup Instructions

1. Clone repository  
   `git clone https://github.com/tawhidul36/Study-Management-Platform.git`

2. Create virtual environment  
   `python -m venv myenv`

3. Activate virtual environment  
   Linux / Mac: `source venv/bin/activate`  
   Windows: `venv\Scripts\activate`

4. Install dependencies  
   `pip install -r requirements.txt`

5. Run migrations  
   `python manage.py makemigrations`  
   `python manage.py migrate`

6. Create superuser  
   `python manage.py createsuperuser`

7. Start server  
   `python manage.py runserver`



## API Endpoints

### Authentication
- POST `/api/auth/register`
- POST `/api/auth/login`
- POST `/api/auth/forgot-password`
- POST `/api/auth/verify-otp`
- POST `/api/auth/reset-password`


<!-- Flashcard Endpoints

POST {{base_url}}/api/flashcards/
GET {{base_url}}/api/flashcards/
GET {{base_url}}/api/flashcards/{id}/
PUT {{base_url}}/api/flashcards/{id}/
PATCH {{base_url}}/api/flashcards/{id}/
DELETE {{base_url}}/api/flashcards/{id}/

Quiz Endpoints

POST {{base_url}}/api/quizzes/
GET {{base_url}}/api/quizzes/
GET {{base_url}}/api/quizzes/{id}/
PUT {{base_url}}/api/quizzes/{id}/
PATCH {{base_url}}/api/quizzes/{id}/
DELETE {{base_url}}/api/quizzes/{id}/

Matching Items Endpoints

POST {{base_url}}/api/matching-items/
GET {{base_url}}/api/matching-items/
GET {{base_url}}/api/matching-items/{id}/
PUT {{base_url}}/api/matching-items/{id}/
PATCH {{base_url}}/api/matching-items/{id}/
DELETE {{base_url}}/api/matching-items/{id}/

Notes Endpoints

POST {{base_url}}/api/notes/
GET {{base_url}}/api/notes/
GET {{base_url}}/api/notes/{id}/
PUT {{base_url}}/api/notes/{id}/
PATCH {{base_url}}/api/notes/{id}/
DELETE {{base_url}}/api/notes/{id}/ -->
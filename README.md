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



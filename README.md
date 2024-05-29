# Housify

Housify is a web application designed to make the process of finding and listing accommodations convenient and secure. The platform allows customers to search for available houses, apartments, and rooms, while vendors (property owners and agents) can list their properties for rent or sale.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
- [Challenges](#challenges)
- [Progress](#progress)
- [Contributing](#contributing)
- [License](#license)

## Features
- User Authentication: Secure login and registration for customers and vendors.
- Vendor Verification: Ensuring trust and safety through a verification process for vendors.
- Property Listings: Vendors can list properties with detailed descriptions and images.
- Search and Filter: Customers can search for properties based on various criteria.
- Messaging: Communication between customers and vendors through the platform.
- Reviews and Ratings: Customers can leave reviews and ratings for properties and vendors.

## Technologies
- **Backend:** Python, Django
- **Database:** Default Django database (SQLite) with optional MySQL migration
- **Frontend:** HTML, CSS, JavaScript
- **Other Libraries:** Django Rest Framework (DRF) for API endpoints, Bootstrap for UI components

## Installation

### Prerequisites
- Python 3.8+
- Git

### Steps
1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/housify.git
    cd housify
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```bash
    python manage.py runserver
    ```

### Optional: Migrate to MySQL
1. **Install MySQL server** and create a database for the project.
2. **Install MySQL client for Python**
    ```bash
    pip install mysqlclient
    ```
3. **Update the database settings in `housify/settings.py`**
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```
4. **Run migrations again**
    ```bash
    python manage.py migrate
    ```

## Usage
- **Access the application:** Open your browser and go to `http://localhost:8000`.
- **Admin panel:** Access the Django admin panel at `http://localhost:8000/admin`.

## Database Schema
![Database Schema](database_schema.png)

### Models
#### Vendor
- `name`: CharField
- `email`: EmailField
- `phone`: CharField
- `address`: CharField
- `verified`: BooleanField

#### Customer
- `name`: CharField
- `email`: EmailField
- `phone`: CharField
- `address`: CharField

#### Property
- `title`: CharField
- `description`: TextField
- `price`: DecimalField
- `location`: CharField
- `vendor`: ForeignKey to Vendor
- `availability_status`: BooleanField

## API Endpoints
### Authentication
- `POST /api/auth/register/`: Register a new user
- `POST /api/auth/login/`: Login a user
- `POST /api/auth/logout/`: Logout a user

### Properties
- `GET /api/properties/`: List all properties
- `GET /api/properties/{id}/`: Retrieve a specific property
- `POST /api/properties/`: Create a new property (Vendor only)
- `PUT /api/properties/{id}/`: Update a property (Vendor only)
- `DELETE /api/properties/{id}/`: Delete a property (Vendor only)

## Challenges
1. **Complexity of Backend Development:**
   - Initially underestimated, significant backend work required.
   - Solutions: Allocated more time for backend tasks, used Django's robust features.

2. **Security Concerns:**
   - Implemented security measures for user data protection.
   - Solutions: Used Django’s security features and ensured data encryption.

3. **Vendor Verification:**
   - Added a verification process to prevent scams.
   - Solutions: Integrated vendor verification through documentation and third-party services.

4. **Scalability and Performance:**
   - Needed to ensure smooth performance with multiple users.
   - Solutions: Database indexing, query optimization, and caching.

## Progress
- **Rating:** 6.5/10
- **Completed:** Backend development, database integration, vendor and customer models, basic security features.
- **Pending:** Frontend development, JavaScript integration, final testing.
- **Assessment:** On track but dependent on overcoming local constraints (e.g., power outages).

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.
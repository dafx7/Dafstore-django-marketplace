# Marketplace Website - Read Me

Welcome to DAFSTORE!


## Introduction
This project started as a tutorial from [FreeCodeCamp](https://www.youtube.com/watch?v=ZxMB6Njs3ck) but I have made significant modifications and added exciting features like authentication, communication between users, a dashboard for item management, form handling with customizations, and a carousel feature for multiple images per item. 


## Features

- **Authentication**: Users can sign up, log in, and manage their accounts securely. Only authenticated users can create listings, manage their items, and communicate with other users.

- **Communication Between Users**: Buyers and sellers can communicate with each other through a messaging system within the website, making it easier to ask questions or negotiate deals.

- **Dashboard for Your Items**: Sellers have access to a dashboard where they can view, edit, and delete their listings. This centralized control makes it convenient for sellers to manage their products.

- **Form Handling and Customizations**: The forms for creating and editing listings have been customized to provide a smooth user experience. Appropriate validations and error handling have been implemented to ensure data integrity.

- **Responsive Design with Tailwind CSS**: The website's front-end has been made responsive using Tailwind CSS, ensuring optimal user experience on various devices, including desktops, tablets, and smartphones.

- **Carousel Feature**: Each item can have multiple images, and you have implemented a carousel using the relational database to showcase these images, allowing users to view different angles of the product.

## Installation

To set up the Real Estate Listings Web Application locally:

1. Clone the repository:
```
git clone https://github.com/dafx7/Dafstore-django-marketplace.git
```
2. Navigate to the project directory:
```
cd dafstore
```
3. Create and activate a virtual environment (optional):
```
python3 -m venv venv
source venv/bin/activate
```
4. Install the required dependencies:
```
pip install requirements.txt
```
5. Set up the database:
```
python manage.py migrate
```
6. Start the development server:
```
python manage.py runserver
```
7. Access the web app at `http://localhost:8000` in your browser.

## Usage

- Use the sign-up and log-in features to access the full functionality of the marketplace.

- Buyers can view available listings and contact sellers through the messaging system.

- Sellers can manage their listings, including multiple images, through the dashboard.

- Customize and handle forms for creating and editing listings seamlessly.

## Technologies Used

- Django
- Python
- HTML
- CSS
- SQLite (Relational Database)
- Tailwind (Front-end Framework)


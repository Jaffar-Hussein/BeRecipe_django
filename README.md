## BeRecipe Backend

The BeRecipe Backend is a Django-based backend for the BeRecipe project, a recipe recommendation application. It serves as the server-side component that handles data storage, retrieval, and processing for the BeRecipe application.

### Features

- User Management: Allows users to register, login, and manage their profiles.
- Recipe Management: Provides functionality for creating, updating, and retrieving recipes.
- Ingredient Management: Handles the storage and retrieval of ingredients and their properties.
- Alternative Recipe Generation: Implements an algorithm to generate alternative recipes based on user preferences and ingredient substitutions.
- User Rating and Feedback System: Enables users to rate recipes and their alternative variations, providing valuable feedback for the recommendation algorithm.
- Admin Portal: Includes a dashboard admin portal for managing recipes, ingredients, and user ratings.
- API Endpoints: Offers a set of APIs for communication with the frontend and other components of the BeRecipe application.

### Technologies Used

- Django: A powerful Python web framework for building robust and scalable applications.
- Django REST Framework: A toolkit for building RESTful APIs in Django.
- PostgreSQL: A reliable and efficient open-source relational database.
- Docker: Provides containerization for easy deployment and scalability.
- AWS S3: Used for storing and serving recipe images.

### Getting Started

To get started with the BeRecipe Backend, follow these steps:

1. Clone the repository: 

 ```git clone https://github.com/Jaffar-Hussein/BeRecipe_django.git```
 
3. Install the required dependencies:

`pip install -r requirements.txt`

3. Set up the PostgreSQL database and configure the database settings.

5. Run database migrations:

```python manage.py migrate```

6. Create a superuser for accessing the admin portal:

```python manage.py createsuperuser```

7. Start the development server:

```python manage.py runserver```



### Contributing

We welcome contributions to the BeRecipe Backend! If you'd like to contribute, please follow the guidelines outlined in the [CONTRIBUTING.md](https://github.com/Jaffar-Hussein/BeRecipe_django/blob/master/CONTRIBUTING.md) file.

### License

This project is licensed under the [MIT License](https://github.com/Jaffar-Hussein/BeRecipe_django/blob/master/LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

### Contact

For any questions or inquiries regarding the BeRecipe Backend, please contact the project maintainer: [Jaffar Hussein](mailto:jaffar.hussein@universite-paris-saclay.fr).

We hope you find the BeRecipe Backend useful and enjoy using the BeRecipe application!

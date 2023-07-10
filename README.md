# African Recipes API

The African Recipes API is a service that retrieves and manages African recipes based on dietary restrictions, nutrient ranges, and calorie counts. The API aims to promote healthier habits and share traditional African cuisine with the world.

## Endpoints

The following endpoints are currently available:

- **`POST /recipes`**: Creates a new recipe with the given parameters.
- **`GET /recipes`**: Retrieves a list of all recipes in the database.
- **`GET /recipes/{recipe_id}`**: Retrieves a specific recipe by its ID.
- **`DELETE /recipes/{recipe_id}`**: Deletes a specific recipe by its ID.

## Technologies Used

The African Recipes API is built using the following technologies:

- **FastAPI**: a modern web framework for building APIs with Python.
- **Docker**: a platform for building, shipping, and running applications in containers.
- **PostgreSQL**: a powerful, open-source relational database management system.
- **Redis**: an in-memory data structure store used as a cache for the API.
- **Alembic**: a lightweight database migration tool for SQLAlchemy.
- **SQLAlchemy**: a Python SQL toolkit and ORM.

## Installation

To install and run the African Recipes API on your local machine, follow these steps:

1. Clone the repository: `git clone https://github.com/MoigeMatino/recipes-api.git`.
2. Install Docker and Docker Compose if you haven't already.
3. From the project root directory, run: `docker-compose up`.
4. The API will be available at `http://0.0.0.0:4002/docs`.
5. Don't forget to migrate tables by running `alembic upgrade head
   ` at the root of the directory

## Access
To access the api online [visit this link](http://54.209.15.213/docs)

## Performance Considerations

To ensure optimal performance of the African Recipes API, we:

- Use Redis caching to improve response times for frequently accessed data.

## Contributing

We welcome contributions to the African Recipes API! To get started, fork the repository and submit a pull request with your changes.

## Future Plans

In the future, we plan to:

- Complete the recipe model with more parameters for filtering.
- Optimize database queries and indexes to reduce query times.
- Use load testing tools to identify and fix performance bottlenecks.
- Consider using Firebase for the database to improve scalability and reliability.
- Consider using Kubernetes for container orchestration and management.

These improvements will make the African Recipes API more robust and scalable, allowing it to handle increased traffic and provide better reliability for users.

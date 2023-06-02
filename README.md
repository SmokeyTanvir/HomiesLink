# HomiesLink

HomiesLink is a web application built with Django that allows users to connect and interact with each other. Users can create profiles, share posts, like and comment on posts, and more.

## Features

- User registration and authentication
- User profiles with profile pictures
- Create, edit, and delete posts
- Like posts
- News feed to view posts from users

## Installation

1. Clone the repository:
```git clone https://github.com/SmokeyTanvir/HomiesLink.git```

2. Change into the project directory:
```cd social-media-app```

3. Create a virtual environment:
```python -m venv venv```

4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the project dependencies:
```pip install -r requirements.txt```

6. Configure the environment variables:
- Modify the `.env` file in the project root directory and set the required environment variables for configuration. You can refer to the provided `.env.example` file for the required variables.
- Update the `.env` file with your own values for each variable.
> Note: Make sure to keep the `.env` file secure and do not commit it to version control.

7. Run the application:
- On Windows:
  ```
  run.bat
  ```

- On macOS and Linux:
  ```
  ./run.sh
  ```

8. Open your browser and visit `http://localhost:8000` to access the application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


# SkyAI MVP- Agricultural Insurance

SkyAI is a web-based application designed to provide AI-driven crop valuation and personalized policy advice for the agricultural business. 
This project uses image processing techniques to analyze satellite images of farmland and generate detailed reports on crop health, land area and value.

## Features

- **Home Page**: Introduction to SkyAI and navigation to other features.
- **Valuation Reports**: AI-driven crop valuation reports, including crop type, health status, planting dates, and value per square meter.
- **Risk Assessments**: Placeholder for risk assessment feature.
- **Claims**: Placeholder for claims management feature.

## Technology Stack

- **Flask**: A lightweight WSGI web application framework.
- **OpenCV**: A library for computer vision and image processing.
- **Bootstrap**: A front-end framework for responsive web design.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/SkyAI.git
    cd SkyAI
    ```

2. **Set up a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```sh
    python run.py
    ```

5. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:5000/`.

## Project Structure

- **run.py**: The entry point of the application.
- **app/**: The main application package.
  - **__init__.py**: Application factory function.
  - **routes.py**: Route definitions and image processing logic.
  - **templates/**: HTML templates for rendering views.
  - **static/**: Static files (e.g., images, CSS).
- **config.py**: Configuration settings.

## Usage

- **Home Page**: Provides an overview of the application and navigation links.
- **Valuation Reports**: 
  - Select a policy holder and land to view the valuation report.
  - The report includes processed aerial images and a table of large crops with details on crop type, planting date, days till harvest, crop health, and value.

## Future Improvements

- **Risk Assessments**: Implement risk assessment algorithms.
- **Claims Management**: Develop a system for handling insurance claims.
- **User Authentication**: Add user login and authentication features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project uses the Flask framework and OpenCV library.
- Bootstrap framework for responsive design.



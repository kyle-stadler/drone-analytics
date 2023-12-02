# Flight Analytics Dashboard Readme

This readme gives an overview of the Flight Analytics Dashboard application developed for Parawave as part of the Software Engineering Capstone. The application is designed to display fire data, analyze drone flight data from a CSV file, and display relevant information along with a flight path on a map.

## Contents

1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Usage](#usage)
6. [File Structure](#file-structure)

## Getting Started

### Prerequisites

Make sure you have the following:

- Python
- Flask
- pandas
- Google Maps API Key

### Installation

1. Clone the repository to your local machine.

2. Install the required Python packages.

### Running the Application

1. Set up your Maps API Key

   - Create a project on the Google Cloud Console
   - Enable the "Maps JavaScript API" for your project
   - Create an API Keys

2. Create a config.py file in the same directory as app.py and add your API Key.

3. Run the application

   ```
   Python app.py
   ```

4. Open a web browser and navigate to the localhost the app is running on (should show in console)

### Usage

1. The home page (index.html) provides a Fire Analytics Dashboard along with a link to the Flight Analytics section.

2. In the Flight Analytics section, you can upload a CSV file containing flight log data using the file upload form.

3. The application processes the uploaded file, extracts relevant flight information, and displays it on the map.

### File Structure

    app.py: The main Flask application file.
    config.py: Configuration file for storing sensitive information, such as the Google Maps API Key.
    templates/
        index.html: Home page template.
        map.html: Flight Analytics page template.
    static/
        css/
            style.css: Stylesheet for HTML templates.
    uploads/: Directory where uploaded CSV files are stored temporarily.

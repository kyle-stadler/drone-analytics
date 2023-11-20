from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    api_key = app.config['API_KEY']
    uploaded_file = request.files['file']
    try:
        df = pd.read_csv(uploaded_file)
        # Get the flight info
        flight_duration = df['flightTime'].iloc[-1]
        flight_distance = df['flightDistance'].iloc[-1]
        flight_takeoff_lat = df['gps.lat'].iloc[1]
        flight_takeoff_lon = df['gps.lon'].iloc[1]

        # Rewriting coordinates into the proper format that MapsAPI will accept for drawing flight path
        coordinates = []
        for index, row in df.iloc[1:].iterrows():
            coordinates.append({'lat': row['gps.lat'], 'lng': row['gps.lon']})
        return render_template('map.html', api_key=api_key, flight_duration=flight_duration, flight_distance=flight_distance, coordinates=coordinates, flight_takeoff_lat=flight_takeoff_lat, flight_takeoff_lon=flight_takeoff_lon)
    except Exception as e:
        return f"An error occurred, make sure the uploaded file is a .csv flight log file with expected columns: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)

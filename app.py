# Import necessary libraries
import streamlit as st
import requests
import pandas as pd
import joblib

# Define a function to fetch weather data from OpenWeather API
def fetch_weather_data(api_key, city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# Define a function to preprocess weather data
def preprocess_weather_data(data):
    # Extract relevant features
    # You can extract more features as per your requirements
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    wind_gust = data['wind']['gust']
    clouds = data['clouds']['all']

    input_data = pd.DataFrame({
    'MinimumTemperature': [temp_min],
    'MaximumTemperature': [temp_max],
    'WindGustSpeed':wind_gust,
    'WindSpeed3pm': [wind_speed],
    'Humidity3pm': [humidity],
    'Pressure3pm': [pressure],
    'Cloud3pm': [clouds]
    })
    return input_data

# Main function to run the Streamlit app
def main():
    # Streamlit UI
    st.title('BBB App')

    # Get user input for city name
    city_name = st.text_input('Enter City Name')

    # Check if user input is not empty
    if city_name:
        # Fetch weather data
        weather_data = fetch_weather_data('5e5d431b17906d316dc226222b1047aa', city_name)
        
        # Preprocess weather data
        processed_data = preprocess_weather_data(weather_data)

        # Show the fetched data
        st.write('**Fetched Weather Data:**')
        st.write(processed_data)

        # Load ML model
        # Assuming you have a trained model saved
        # Initialize your model
        # Load your trained model using joblib or pickle
        model = joblib.load('model_bbb.joblib')

        # Make predictions
        prediction = model.predict(processed_data)  # Pass processed data to the model

        # Display prediction
        st.write('**Prediction:**')
        st.write(prediction)

        if(prediction):
            st.write('**VERY HIGH CHANCES OF CLOUDBURST !!!**')
            st.markdown("![Alt Text](https://media.giphy.com/media/3orieZMmRdBlKk5nY4/giphy.gif)")

        else:
            st.write('**No cloudburst ! FALSE ALARM !**')
            st.markdown("![Alt Text](https://media.giphy.com/media/xT5LMGBztUr4SRI25i/giphy.gif)")
        

# Run the main function
if __name__ == '__main__':
    main()


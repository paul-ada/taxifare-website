import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown(
    '''
    Fill these parameters to get your prediction:
    ''')

pickup_date = st.date_input('Pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('Pickup datetime', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_datetime = f'{pickup_date} {pickup_time}'
pickup_longitude = st.number_input('Pickup longitude', value=40.7614327)
pickup_latitude = st.number_input('Pickup latitude', value=-73.9798156)
dropoff_longitude = st.number_input('Dropoff longitude', value=40.6413111)
dropoff_latitude = st.number_input('Dropoff latitude', value=-73.7803331)
passenger_count = st.number_input('Passenger_count', min_value=1, max_value=8, step=1, value=1)

url = 'https://taxifare-api-h5aeb7v3mq-ew.a.run.app/predict'


# 2. Let's build a dictionary containing the parameters for our API...

X_pred = dict(
            key=pickup_datetime,
            pickup_datetime=pickup_datetime,
            pickup_longitude=pickup_longitude,
            pickup_latitude=pickup_latitude,
            dropoff_longitude=dropoff_longitude,
            dropoff_latitude=dropoff_latitude,
            passenger_count=passenger_count)

# 3. Let's call our API using the `requests` package...

response = requests.get(url, params=X_pred)

#4. Let's retrieve the prediction from the **JSON** returned by the API...

prediction = response.json()

## Finally, we can display the prediction to the user

to_display = round(prediction['fare_amount'], 2)

st.markdown(f"""
    # Your fare amount should be ${to_display}
""")

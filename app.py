import streamlit as st
import pandas as pd
import numpy as np
import pickle as pk

model = pk.load(open('car_dheko_RFmodel.pkl', 'rb'))
brand_encoder = pk.load(open('Car_brand.pkl', 'rb')) # one_hot encoding
yr_ord_encoder = pk.load(open('Year_of_manufacture1.pkl', 'rb')) 
ord_encoder = pk.load(open('engine.pkl', 'rb')) # ordinal encoding

st.set_page_config(page_title= "CarDheko Price Prediction", layout= "wide")
st.header('Used Car Price Prediction - Machine learning Model')

cars_data = pd.read_csv('car_dheko.csv')

st.sidebar.image("car_dhekoimage.jpeg", use_column_width= True, caption= "Used CAR Price Prediction")
st.sidebar.header("Please Filter Car Details")
with st.sidebar:
    
    car_brand = st.selectbox("Select Car Brand", cars_data["Car_brand"].unique())
    year = st.slider("Car Manufactured Year", 1995, 2023)
    kilometers_driven = st.slider("Kms Driven", 0, 100000)

    sorted_owners = sorted(cars_data["Number_of_previous_owners"].unique())
    Number_of_previous_owners = st.selectbox("Select no. of Previous Owner", sorted_owners)

    Transmission_type = st.selectbox("Transmission_type", cars_data["Transmission_type"].unique())
    Fuel_type = st.selectbox("Fuel_type", cars_data["Fuel_type"].unique())
    Body_type = st.selectbox("Body_type", cars_data["Body_type"].unique())
    engine_cc = st.slider("Engine CC", 0, 5000)
    df = pd.DataFrame({'Engine_CC': [engine_cc]})
    engine_category = pd.cut(df['Engine_CC'],
                        bins=[0, 500, 900, 1100, 1200, 1300, 1400, 1500, 1600, 2000, 3000, 4000, 5001],
                        labels=['0-500','501-900','901-1100', '1101-1200', '1201-1300', '1301-1400', 
                                '1401-1500', '1501-1600','1601-2000', '2001-3000', '3001-4000', '4001-5001'], right = False)
    engine_category = engine_category.iloc[0]
    Mileage = st.slider("Car Mileage", 7,40)
    Wheel_Base = st.slider("Wheel Base", 1800,3200)
    sorted_seats = sorted(cars_data["Seats"].unique())
    Seats = st.selectbox("No. of Seats", sorted_seats)
    sorted_Cylinder = sorted(cars_data["No of Cylinder"].unique())
    No_of_Cylinder = st.selectbox("No of Cylinder", sorted_Cylinder)
    City = st.selectbox("City", cars_data["City"].unique())

st.image("CarDekho-Feature.jpg")

if st.button("Predict"):
    
    car_brand = np.array([car_brand]).reshape(-1, 1)
    encoded_brand_input = brand_encoder.transform(car_brand).ravel()
    encoded_yr_input = yr_ord_encoder.transform([[year]]).ravel()
    encoded_yr_input = int(encoded_yr_input[0])
    engine_category= np.array([engine_category]).reshape(-1, 1)
    encoded_engine_input = ord_encoder.transform(engine_category).ravel()
    encoded_engine_input = int(encoded_engine_input[0])

    user_df = pd.DataFrame([[
        kilometers_driven, Number_of_previous_owners,Transmission_type,
        Fuel_type,Body_type,Mileage,Wheel_Base,Seats,No_of_Cylinder,City, 
        encoded_yr_input, encoded_engine_input, *encoded_brand_input]],
                           columns = ['Kilometers_driven','Number_of_previous_owners','Transmission_type',
                                      'Fuel_type','Body_type','Mileage','Wheel Base','Seats','No of Cylinder','City','year_encoded','Engine_encoded',
                                      'Car_brand_Audi', 'Car_brand_BMW', 'Car_brand_Chevrolet',
                                      'Car_brand_Citroen', 'Car_brand_Datsun', 'Car_brand_Fiat',
                                      'Car_brand_Ford', 'Car_brand_Hindustan Motors', 'Car_brand_Honda',
                                      'Car_brand_Hyundai', 'Car_brand_Isuzu', 'Car_brand_Jaguar',
                                      'Car_brand_Jeep', 'Car_brand_Kia', 'Car_brand_Land Rover',
                                      'Car_brand_Lexus', 'Car_brand_MG', 'Car_brand_Mahindra',
                                      'Car_brand_Mahindra Renault', 'Car_brand_Mahindra Ssangyong',
                                      'Car_brand_Maruti', 'Car_brand_Mercedes-Benz', 'Car_brand_Mini',
                                      'Car_brand_Mitsubishi', 'Car_brand_Nissan', 'Car_brand_Opel',
                                      'Car_brand_Porsche', 'Car_brand_Renault', 'Car_brand_Skoda',
                                      'Car_brand_Tata', 'Car_brand_Toyota', 'Car_brand_Volkswagen',
                                      'Car_brand_Volvo'])

    user_df['Transmission_type'].replace(['Manual', 'Automatic'], [1,2], inplace = True)
    user_df['Fuel_type'].replace(['Petrol', 'Diesel', 'Lpg', 'Cng', 'Electric'], [1,2,3,4,5], inplace = True)
    user_df['Body_type'].replace(['Hatchback', 'Minivans', 'Wagon', 'Pickup Trucks', 'Sedan', 'SUV', 'MUV', 'Hybrids', 
                                'Convertibles', 'Coupe'], [1,2,3,4,5,6,7,8,9,10], inplace = True)
    user_df['City'].replace(['Bangalore', 'Delhi', 'Chennai', 'Hyderabad', 'Kolkata', 'Jaipur'], [1,2,3,4,5,6], inplace = True)

    #st.write(user_df)
    car_price = round(model.predict(user_df)[0])
    st.markdown('Estimated CAR Price is Rs '+ str(car_price) + ' lakhs')
    
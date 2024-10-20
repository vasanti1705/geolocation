# Geolocation Flask App

## Overview

This project is a simple web application built with Flask that allows users to retrieve geolocation information based on an IP address. Utilizing the [IP Geolocation API](https://ipgeolocation.io/), users can input an IP address to get details about its location.

## Features

- Fetch geolocation data for a provided IP address.
- Automatically retrieves the geolocation of the server's IP if none is provided.
- User-friendly interface for easy IP input and results display.
- Error handling for invalid IP addresses.

### Prerequisites

- Python 3.x
- Flask
- Requests
- An API key from [IP Geolocation API](https://ipgeolocation.io/)

### Installation

1. *Clone the repository:*
```
   git clone https://github.com/vasanti1705/geolocation.git
   cd geolocation-flask-app
```   

2. *Set up your environment variables:*

   Creating a .env file in the root directory and adding the API key:

```   
   API_KEY=api_key_here
```

3. *Install dependencies:*
```
   pip install -r requirements.txt
```

### Usage

1. *Run the application:*
```
   python app.py
```  

   The application will be available at http://localhost:5000.
   
3. *Access the application:*
   - At the home page, information of users IP will be displayed.
     
   - Click on `search another IP` button to giving an IP address as input to fetch geolocation data.
   ![Input Page](https://github.com/user-attachments/assets/151a5696-2a9a-4620-9f8e-b1f6dd544e1a)
   
   - If the IP Address does not exist, the following error page is displayed.
   ![Error Page](https://github.com/user-attachments/assets/895d71b2-5ffc-4b67-9604-0d25d5f1a3b4)
   
   - Otherwise the Geolocation information of the IP given as input will be displayed.
     
   ![IP Information Page](https://github.com/user-attachments/assets/e90e09e8-1211-4451-915a-4b8eca879a1d)
   


### Using Docker

To run the application using Docker, following these steps:

1. *Build the Docker image:*
```
   docker build -t geolocation .
```   

2. *Run the Docker container:*
```
   docker run -p 5000:5000 --env-file .env geolocation
```
OR use 
```
   docker run -p 5000:5000 --env API_KEY=<api_key> geolocation
```

*Link to Docker image:*

```  docker pull vasanti1705/geolocation:latest ```
   

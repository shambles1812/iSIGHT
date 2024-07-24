
# iSIGHT - iAcademy Bulletin Board

## Created By:
- ESTEBAN, FRANCIS L.
- FABILA, KYLE L.
- VILLAFUERTE, CHRISTIAN JOSEPH N.
- VILLANUEVA, JOAQUIN R.

## Purpose
iSIGHT is a bulletin board system for iAcademy that provides daily updates about classes, office availability, and current weather conditions in Makati, Philippines. This application includes an admin interface for updating the bulletin board and a public interface for viewing the updates.

## Usable Links
- **Bulletin Board**: `/bulletin-board`
- **Admin Login**: `/login`
- **Generate Passcodes**: `/generate_passcode`

## Setup Instructions

### Prerequisites
- Python 3.x
- Node.js
- MongoDB

### Step-by-Step Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/iSIGHT.git
   cd iSIGHT
   ```

2. **Create and Activate Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Python Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB**
   Ensure MongoDB is running on your local machine. By default, the app connects to `mongodb://localhost:27017/school_updates`.

5. **Set Up Weather API**
   Sign up at [WeatherAPI](https://www.weatherapi.com/) and get your API key. Replace `your_weatherapi_key` in `app.py` with your actual API key.

6. **Run the Flask Application**
   ```sh
   python app.py
   ```

7. **Access the Application**
   Open your web browser and navigate to:
   - **Bulletin Board**: `http://127.0.0.1:5000/bulletin-board`
   - **Admin Login**: `http://127.0.0.1:5000/login`
   - **Generate Passcodes**: `http://127.0.0.1:5000/generate_passcode`

## Features

### Public Interface
- **Bulletin Board**: Displays daily updates about classes, office availability, and current weather conditions in Makati, Philippines.

### Admin Interface
- **Login**: Access the admin interface using a passcode.
- **Update Bulletin Board**: Update information about classes and office availability for the current day.
- **Manage Passcodes**: Generate and delete passcodes for admin access.

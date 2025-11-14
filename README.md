# 🌦 Weather Dashboard (CLI)

A clean, modular command-line weather application that fetches real-time weather data using the OpenWeatherMap API.  
API key is securely loaded from a `.env` file.

---

## 📂 Project Files
- **weather_dashboard.py** — Main script.
- **.env** — Contains your API key (`YOUR_API_KEY=XXXX`).

---

## 🚀 Features
- Reads API key securely from `.env` from the same folder as the weather_dashboard.py file exist.
- Fetches real-time weather details:
  - Temperature  
  - Feels-like temperature  
  - Humidity  
  - Wind speed  
  - Weather condition  
- Accepts **"city, country code" Format** for accurate weather lookup.
- Clean CLI formatting.
- Robust error handling for:
  - Invalid city input  
  - Network failures  
  - Missing API key  

---

## 🌍 Entering City With Country Code

The program requires entering the **city name followed by its country code**, separated by a comma.  
This ensures precise weather retrieval.

**Examples:**
```
Hyderabad, IN
London, UK
New York, US
Delhi, IN
```

---

## 🛠 Requirements
- Python 3.7+
- Dependencies:
  ```
  pip install python-dotenv requests
  ```

---

## ▶️ How to Run

1. Create a `.env` file in the same directory:

   ```
   YOUR_API_KEY=your_openweathermap_key_here
   ```
  Get API key from https://openweathermap.org/api

2. Clone the repository  
   ```bash
   git clone https://github.com/Balla-Hemanth-Srinivas/Weather-Dashboard.git
   ```

2. Navigate to the project folder with file **weather_dashboard.py**

2. Run the script:

   ```powershell
   python weather_dashboard.py
   ```

3. Enter a city with its country code when prompted.

---

## 📝 Example Session

```
Weather Dashboard App
----------------------
Enter city name followed by comma and country code.
Eg: Hyderabad,IN : Hyderabad,IN

=== Weather Dashboard ===
City         : Hyderabad
Temperature  : 27°C
Feels Like   : 28°C
Humidity     : 70%
Wind Speed   : 2.4 m/s
Condition    : Clear Sky
==========================
```

---

## ➕ Future Enhancements
- 5‑day and 7‑day forecasts  
- Temperature trend graphs  
- Recently searched city history  
- Tkinter GUI interface  

---

## 📄 License
This project is completely free to use, modify, and extend.

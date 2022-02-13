# Weather App in Python | Tkinter – GUI

![GUI Based Weather App In Python](https://www.askpython.com/wp-content/uploads/2022/01/GUI-based-Weather-App-in-Python-1024x512.png.webp)

## Code for Weather App in Python – GUI

Without further ado, let’s get right into the code setup for creating our GUI weather app in Python

### 1. Install and Import Tkinter

We begin with installing the required libraries using the [pip package manager](https://www.askpython.com/python-modules/python-pip). Enter the below commands in your command line or terminal to install the modules

We need to install:

- [Request](https://www.askpython.com/python-modules/requests-in-python): to fetch data from API
- [Tkinter](https://www.askpython.com/python-modules/tkinter/tkinter-font-class): to make our Weather app GUI (Graphical User Interface) based.
- [DateTime](https://www.askpython.com/python-modules/python-datetime-module): to change the time from API to a different format

```python
pip install tkinter 
pip install datetime
pip install requests
pip install json
```

After installing the required libraries from the terminal, we now move to our Python file to code. We start with importing the libraries as:

```
from` `tkinter ``import` `*``import` `requests``import` `json``from` `datetime ``import` `datetime
```

### 2. Initialize the Tkinter Window

As a next step, we initialize our GUI window using the Tkinter module.

```
#Initialize Window` `root ``=``Tk()``root.geometry(``"400x400"``) ``#size of the window by default``root.resizable(``0``,``0``) ``#to make the window size fixed``#title of our window``root.title(``"Weather App - AskPython.com"``)
```

### 3. OpenWeatherMap API

In our code, we will be using Open Weather API (free tier) to get the current weather information which is accurate and latest.

- To do so, go to [OpenWeatherMap](https://openweathermap.org/) website and **create** an account.
- After creating your account, go to profile and then “**My API keys**“.
- This will open a webpage for your API **Key**, as shown below, copy it for later use in code in the next step.

![Open Weather Api](https://www.askpython.com/wp-content/uploads/2022/01/open-weather-api-1024x261.png.webp)Open Weather Map API

### 4. Weather Function

Here, comes the part where we add functionality to our code. This part is the most crucial in getting correct weather information, as this involves fetching data from the API and displaying it in an accurate format.

We code the most important function of this code, which is for displaying weather, we do so as in the code:

```
city_value ``=` `StringVar()` `def` `showWeather():` `#Enter you api key, copies from the OpenWeatherMap dashboard``  ``api_key ``=` `"eda2b2s6d#sd65f4de7c4b8"` `#sample API` `  ``# Get city name from user from the input field (later in the code)``  ``city_name``=``city_value.get()` `  ``# API url``  ``weather_url ``=` `'http://api.openweathermap.org/data/2.5/weather?q='` `+` `city_name ``+` `'&appid='``+``api_key` `  ``# Get the response from fetched url``  ``response ``=` `requests.get(weather_url)` `  ``# changing response from json to python readable ``  ``weather_info ``=` `response.json()` `  ``tfield.delete(``"1.0"``, ``"end"``)  ``#to clear the text field for every new output` `#as per API documentation, if the cod is 200, it means that weather data was successfully fetched` `  ``if` `weather_info[``'cod'``] ``=``=` `200``:``    ``kelvin ``=` `273` `# value of kelvin` `#-----------Storing the fetched values of weather of a city` `    ``temp ``=` `int``(weather_info[``'main'``][``'temp'``] ``-` `kelvin)                   ``#converting default kelvin value to Celcius``    ``feels_like_temp ``=` `int``(weather_info[``'main'``][``'feels_like'``] ``-` `kelvin)``    ``pressure ``=` `weather_info[``'main'``][``'pressure'``]``    ``humidity ``=` `weather_info[``'main'``][``'humidity'``]``    ``wind_speed ``=` `weather_info[``'wind'``][``'speed'``] ``*` `3.6``    ``sunrise ``=` `weather_info[``'sys'``][``'sunrise'``]``    ``sunset ``=` `weather_info[``'sys'``][``'sunset'``]``    ``timezone ``=` `weather_info[``'timezone'``]``    ``cloudy ``=` `weather_info[``'clouds'``][``'all'``]``    ``description ``=` `weather_info[``'weather'``][``0``][``'description'``]` `    ``sunrise_time ``=` `time_format_for_location(sunrise ``+` `timezone)``    ``sunset_time ``=` `time_format_for_location(sunset ``+` `timezone)` `#assigning Values to our weather varaible, to display as output``    ` `    ``weather ``=` `f``"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"``  ``else``:``    ``weather ``=` `f``"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"`  `  ``tfield.insert(INSERT, weather)  ``#to insert or send value in our Text Field to display output
```

As a final step to adding functionality, we add a function to change the time format, this function checks for the local time as compared to the UTC(**Universal Time Coordinated**) in which the API gives the output to the time format as per our location. Ex. UTC to IST.

```
def` `time_format_for_location(utc_with_tz):``  ``local_time ``=` `datetime.utcfromtimestamp(utc_with_tz)``  ``return` `local_time.time()
```

### 5. Coding the GUI (frontend elements)

We now start to code the elements as per the GUI, for heading, text, labels, buttons, etc.

To start with, we code the **text field** for the **City Name** we want the weather for, along with the label to indicate so:

- We use the **[Label](https://www.askpython.com/python-modules/tkinter/tkinter-frame-and-label)** method to generate a label of text to indicate the purpose of the input field for city name.
- **[Entry](https://www.askpython.com/python-modules/tkinter/tkinter-entry-widget)** method is used to make an entry field for input of city name, to check its weather.
- The textvaraible widget is used to store the inputted value, in the variable named: city_value
- Other than these widgets we have also applied some styling to our code, by font size, color, etc.

```
city_head``=` `Label(root, text ``=` `'Enter City Name'``, font ``=` `'Arial 12 bold'``).pack(pady``=``10``) ``#to generate label heading` `inp_city ``=` `Entry(root, textvariable ``=` `city_value, width ``=` `24``, font``=``'Arial 14 bold'``).pack() ``#entry field
```

We code a **Check Weather Button**, on which we click to check the weather of the user inputted city:

- We give our button some styling, along with the name – ‘Check Weather’. We use the ‘**command**‘ widget, which shows what function (here, **showWeather** function) would run on the click (key press) of the button, as coded in the previous step.

```
Button(root, command ``=` `showWeather, text ``=` `"Check Weather"``, font``=``"Arial 10"``, bg``=``'lightblue'``, fg``=``'black'``, activebackground``=``"teal"``, padx``=``5``, pady``=``5` `).pack(pady``=` `20``)
```

After adding this, we add the output elements in our code. The elements on which our Weather information would be displayed.

- Yet again, we add a label to title our result in the following text box
- To display the output we use a **text field**, which gets its value, every time the “Check Weather” button is pressed. This envokes the function to check weather info fetched from the API after processing, [output from the showWeather function]

```
weather_now ``=` `Label(root, text ``=` `"The Weather is: "``, font ``=` `'arial 12 bold'``).pack(pady``=``10``)` `tfield ``=` `Text(root, width``=``46``, height``=``10``)``tfield.pack()
```

On execution of our code, the Tkinter displays this as output:

![Weather App Frontend In Python](https://www.askpython.com/wp-content/uploads/2022/01/Weather-app-frontend-in-python.png.webp)

Weather App Frontend In Python

## Final Code for GUI Weather App in Python

```
from` `tkinter ``import` `*``import` `requests``import` `json``from` `datetime ``import` `datetime` `#Initialize Window` `root ``=``Tk()``root.geometry(``"400x400"``) ``#size of the window by default``root.resizable(``0``,``0``) ``#to make the window size fixed``#title of our window``root.title(``"Weather App - AskPython.com"``)` `# ----------------------Functions to fetch and display weather info``city_value ``=` `StringVar()` `def` `time_format_for_location(utc_with_tz):``  ``local_time ``=` `datetime.utcfromtimestamp(utc_with_tz)``  ``return` `local_time.time()` `city_value ``=` `StringVar()` `def` `showWeather():``  ``#Enter you api key, copies from the OpenWeatherMap dashboard``  ``api_key ``=` `"eda2b2s6d#sd65f4de7c4b8"` `#sample API` `  ``# Get city name from user from the input field (later in the code)``  ``city_name``=``city_value.get()` `  ``# API url``  ``weather_url ``=` `'http://api.openweathermap.org/data/2.5/weather?q='` `+` `city_name ``+` `'&appid='``+``api_key` `  ``# Get the response from fetched url``  ``response ``=` `requests.get(weather_url)` `  ``# changing response from json to python readable ``  ``weather_info ``=` `response.json()` `  ``tfield.delete(``"1.0"``, ``"end"``)  ``#to clear the text field for every new output` `#as per API documentation, if the cod is 200, it means that weather data was successfully fetched` `  ``if` `weather_info[``'cod'``] ``=``=` `200``:``    ``kelvin ``=` `273` `# value of kelvin` `#-----------Storing the fetched values of weather of a city` `    ``temp ``=` `int``(weather_info[``'main'``][``'temp'``] ``-` `kelvin)                   ``#converting default kelvin value to Celcius``    ``feels_like_temp ``=` `int``(weather_info[``'main'``][``'feels_like'``] ``-` `kelvin)``    ``pressure ``=` `weather_info[``'main'``][``'pressure'``]``    ``humidity ``=` `weather_info[``'main'``][``'humidity'``]``    ``wind_speed ``=` `weather_info[``'wind'``][``'speed'``] ``*` `3.6``    ``sunrise ``=` `weather_info[``'sys'``][``'sunrise'``]``    ``sunset ``=` `weather_info[``'sys'``][``'sunset'``]``    ``timezone ``=` `weather_info[``'timezone'``]``    ``cloudy ``=` `weather_info[``'clouds'``][``'all'``]``    ``description ``=` `weather_info[``'weather'``][``0``][``'description'``]` `    ``sunrise_time ``=` `time_format_for_location(sunrise ``+` `timezone)``    ``sunset_time ``=` `time_format_for_location(sunset ``+` `timezone)` `#assigning Values to our weather varaible, to display as output``    ` `    ``weather ``=` `f``"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"``  ``else``:``    ``weather ``=` `f``"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"`  `  ``tfield.insert(INSERT, weather)  ``#to insert or send value in our Text Field to display output`  `#------------------------------Frontend part of code - Interface` `city_head``=` `Label(root, text ``=` `'Enter City Name'``, font ``=` `'Arial 12 bold'``).pack(pady``=``10``) ``#to generate label heading` `inp_city ``=` `Entry(root, textvariable ``=` `city_value, width ``=` `24``, font``=``'Arial 14 bold'``).pack()` `Button(root, command ``=` `showWeather, text ``=` `"Check Weather"``, font``=``"Arial 10"``, bg``=``'lightblue'``, fg``=``'black'``, activebackground``=``"teal"``, padx``=``5``, pady``=``5` `).pack(pady``=` `20``)` `#to show output` `weather_now ``=` `Label(root, text ``=` `"The Weather is:"``, font ``=` `'arial 12 bold'``).pack(pady``=``10``)` `tfield ``=` `Text(root, width``=``46``, height``=``10``)``tfield.pack()` `root.mainloop()
```


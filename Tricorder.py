from sense_hat import SenseHat, ACTION_PRESSED
from signal import pause

# Set up SenseHat
sense = SenseHat()
sense.clear()

# Inertial Measurements
def orientation(event):
    
    if event.action == ACTION_PRESSED:
        orientation = sense.get_orientation()
        pitch = orientation["pitch"]
        roll = orientation["roll"]
        yaw = orientation["yaw"]
        
        pitch = round(pitch,1)
        roll = round(roll,1)
        yaw = round(yaw,1)
        
        message = "Pitch {0}, Roll {1}, Yaw {2}".format(pitch, roll, yaw)
 #       print(message)
   # sense.show_message(message)
    


# Temp Measurement
def temperature():
    temp = sense.get_temperature()
    temp = round(temp,1)
    
    message = "Temperature: %s degrees Celsius" % temp
#   sense.show_message(message)
    print(message)
    
# Humidity
def humidity():
    humidity = sense.get_humidity()
    humidity = round(humidity,1)
  
    message = "Humidity: %s percent" % humidity
#    print(message)
#    sense.show_message("Humidity: %s percent" % humidity)
    
# Pressure
def pressure():
    
    pressure = sense.get_pressure()
    pressure = round(pressure,1)
    message = "Pressure: %s millibars" % pressure
#    print(message)
#    sense.show_message("Pressure: %s millibars" % pressure)
    
# Compass
def compass():
    for i in range(0,10):
        north = sense.get_compass()
    north = round(north,1)
    
    message = "North: %s degrees " % north
#    print(message)
#    sense.show_message("North: % degrees" % north)
    
# Set up Callbacks
sense.stick.direction_up = orientation
sense.stick.direction_right = temperature
sense.stick.direction_down = compass
sense.stick.direction_left = humidity
sense.stick.direction_middle = pressure

# Wait for input
pause()
#while True:
#    pass

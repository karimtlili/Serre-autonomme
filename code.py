import time
import board
import adafruit_bh1750
import adafruit_character_lcd.character_lcd as characterlcd
import adafruit_dht

i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)



import RPi.GPIO as GPIO
red_pin = 18
GPIO.setup(26,GPIO.OUT)
GPIO.setup(red_pin, GPIO.OUT)

def pump_on():#arrosage
    while True:
        GPIO.output(26,True)

def pump_off():
    while True:
        GPIO.output(26,False)


def rgb_on():#controler la luminosité

  GPIO.output(red_pin, False)         
    while True:
        
          GPIO.output(red_pin, True)

def lcd(x1,x2):#affichage des parametres

    lcd_columns = 16
    lcd_rows = 2
    lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,lcd_d7, lcd_columns, lcd_rows)
    lcd.clear()
    lcd_line_1="la temperature est "+str(x1)+" l'humidite "+str(x2)
    sleep(2)   
    time.sleep(2.0) 


dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False) #configuration du dht
while True:
    if (sensor.lux<500):
        rgb_on()

    time.sleep(1)
    try:
        
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        lcd(temperature_c,humidity)

    if (humidity<200):
        pump_on() 
    else:
        pump_off()       
 
   

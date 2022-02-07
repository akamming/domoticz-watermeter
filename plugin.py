# Basic Python Plugin Example
#
# Author: akamming / martin-g-it
#
"""
<plugin key="WMPS" name="WaterMeter NPN plugin" author="akamming / martin-g-it" version="1.0.2" wikilink="https://www.domoticz.com/wiki/Plugins" externallink="https://www.google.com/">
    <description>
        <h2>Watermeter</h2><br/>
        Plugin version of the Watermeter python script using a NPN sensor<br/>
        <h3>Features</h3>
        <ul style="list-style-type:square">
            <li>Exports the pin (not necessary to do before starting domoticz)</li>
            <li>Is  run from within domoticz (no need for making sure a seperate python scripts keeps up and running on your pi)</li>
            <li>Creates the watermeterdevice (no need for giving special http commands to create the needed device) </li>
            <li>Allow for overriding the meter reading manually (change the meterstand.txt to the meterstand you need) </li>
        </ul>
        <h3>Devices</h3>
        <ul style="list-style-type:square">
            <li>WaterMeter - Counts the liters of water running through your watermeter</li>
        </ul>
        <h3>Configuration</h3>
        Configure correctly. The plugin works using the default settings, but your system might need different settings...
        <ul style="list-style-type:square">
            <li>GPIO Pin Number - The GPIO Pin (BCM!) to which your NPN sensor is connected. To avoid conflicts, make sure the GPIO pin is not managed/configured somewhere else on your system to prevent confllicts. You can still use the normal GPIO drivers in domoticz for other pins as long as you don't configure the same pins.</li>
            <li>Resistor Type - Configure the correct type of resistor. If the NPN is soldered to the GPIO without any physical resistors in a scheme, you definitely should configure a resistor here. </li>
            <li>Interrupt and Check mode:</li>
            <li>-Interrupt: Configure if you want the meter to be triggered if the pin goes from 1 to 0 (falling), from 0 to -1 (rising) or on both changes (both). Normally it should be either falling or rising, but not both (both will get you double readings).</li>
            <li>-Last value check: Configure the false-positive check where the last value (on/off) is checked vs. the new value. Recommended when false-positives occur (ie. Domoticz meter value is higher than actual meter) is.</li>
            <li>-Consistency check: Configure the false-positive check where consistency of the On/Off value is checked 300ms after the interrupt. Recommended when false-positives occur (ie. Domoticz meter value is higher than actual meter). </li>
            <li>Debounce Time - Configure the cooldown time after the interrupt to prevent interrupt flooding. A high number is recommended, but it should be less then the time it takes to have 1 liter going throught your watermeter, to prevent lost measurements.</li> 
            <li>Meter Reading File - The path of the file where you want the actual meter reading to be stored. If you do not specifiy a path, the homefolder of this plugin will be used</li>
            <li>Increment - The amount your domoticz counter must be incremented when a pulse of the watermeter is detected. In NL this is normally 1 liter. In belgium apparently this is 2 ticks per liter (value should then be 0.5).</li>

            <br/>
            Last but not least: A normal (Dutch) watermeter measures 1 liter every pulse on the GPIO pin. The meter in domoticz is of the type M3. So in order to have this meter to show the correct amount, you have to change the RFX Meter/Counter Setup in domoticz. If this is not set correctly: <br />
            - Go to domoticz web interface<br/>
            - Click on Setup<br/>
            - Click on Settings<br/>
            - Click on Meters/Counters<br/>
            - Set the value of the water divider to 1000  (1 M3 = 1000 L ;-))<br/>
            - Click on Apply Settings  <br/><br/>
        </ul>
    </description>
    <params>
         <param field="Mode1" label="GPIO Pin Number" width="150px">
         <options>
            <option label="GPIO2" value="2" />
            <option label="GPIO3" value="3"/>
            <option label="GPIO4" value="4"/>
            <option label="GPIO5" value="5"/>
            <option label="GPIO6" value="6"/>
            <option label="GPIO7" value="7"/>
            <option label="GPIO8" value="8"/>
            <option label="GPIO9" value="9"/>
            <option label="GPIO12" value="12"/>
            <option label="GPIO13" value="13"/>
            <option label="GPIO14" value="14"/>
            <option label="GPIO15" value="15"/>
            <option label="GPIO16" value="16"/>
            <option label="GPIO17" value="17"/>
            <option label="GPIO18" value="18"/>
            <option label="GPIO19" value="19"/>
            <option label="GPIO20" value="20"/>
            <option label="GPIO21" value="21" default="true"/>
            <option label="GPIO22" value="22"/>
            <option label="GPIO23" value="23"/>
            <option label="GPIO24" value="24"/>
            <option label="GPIO25" value="25"/>
            <option label="GPIO26" value="26"/>
         </options>
         </param> 
         <param field="Mode2" label="Resistor Type" width="150px">
         <options>
            <option label="PullUp" value="PU" default="true"/>
            <option label="PullDown" value="PD"/>
            <option label="None" value="None"/>
         </options>
         </param> 
         <param field="Mode3" label="Interrupt and check mode" width="150px" required="true">
         <options>
            <option label="Falling / No checks" value="Falling" default="true"/>
            <option label="Falling / Last value check" value="FallingLast"/>
            <option label="Falling / Consistency check" value="FallingConsistency"/>
            <option label="Falling / Last value check / Consistency check" value="FallingLastConsistency"/>
            <option label="Rising  / No checks" value="Rising" default="true"/>
            <option label="Rising  / Last value check" value="RisingLast"/>
            <option label="Rising  / Consistency check" value="RisingConsistency"/>
            <option label="Rising  / Last value check / Consistency check" value="RisingLastConsistency"/>
            <option label="Both    / No checks" value="Both"/>	
            <option label="Both    / Last value check" value="BothLast"/>	
            <option label="Both    / Consistency check" value="BothConsistency"/>
            <option label="Both    / Last value check / Consistency check" value="BothLastConsistency"/>	
         </options>
         </param>
         <param field="Mode4" label="Debounce time (ms)" width="150px" required="true">
         <options>
            <option label="0" value="0" />
            <option label="50" value="50" />
            <option label="100" value="100" />
            <option label="150" value="150" />
            <option label="200" value="200" />
            <option label="250" value="250" />
            <option label="300" value="300" />
            <option label="350" value="350" default="true"/>
            <option label="400" value="400" />
            <option label="450" value="450" />
            <option label="500" value="500" />
			<option label="750" value="500" />
            <option label="1000" value="1000" />
			<option label="1250" value="1250" />
            <option label="1500" value="1500" />
			<option label="1750" value="1750" />
            <option label="2000" value="2000" />
         </options>
         </param>
         <param field="Mode5" label="Meter Reading File" width="150px" required="true" default="meterstand_water.txt" />
         <param field="Mode6" label="Increment" width="70px" default="1"/> 
     </params>
</plugin>
"""
import Domoticz
import RPi.GPIO as GPIO
import os
import time

#setup global vars
#global debug
#global fakereading

fakereading=False        # for testing purposes. Will generate a "tick" every 10 seconds

#Check if we have to go in debug mode
debug=False #True/False             # set to true to enable debug logging
#if os.path.exists(str(Parameters["HomeFolder"])+"DEBUG"): 

last_value        = 0
interrupt         = GPIO.BOTH
check_last_value  = False
check_consistency = False

last_watermeter_value = 0

class BasePlugin:

    enabled = False
    def __init__(self):
        return

    def onStart(self):
        global debug
        global fakereading
        global last_value
        global interrupt
        global gpio_pin
        global check_last_value
        global check_consistency

        Domoticz.Log("Watermeter plugin started...")

        #Check if we have to switch on debug mode
        if os.path.exists(str(Parameters["HomeFolder"])+"DEBUG"): 
            debug=True
            Domoticz.Log("File "+str(Parameters["HomeFolder"])+"DEBUG"+" exists, switching on Debug mode")
        else:
            debug=False #True/False

        #Check if we have to switch on pulse for testin purposes
        if os.path.exists(str(Parameters["HomeFolder"])+"TESTPULSE"): 
            fakereading=True
            Domoticz.Log("Plugin is in testing mode, generates a tick every 10 seconds by itself!!, delete file "+str(Parameters["HomeFolder"])+"TESTPULSE to switch off")
        else:
            fakereading=False


        Debug("OnStart called")
		
        if debug==True:
            Debug("In Debug mode: Dumping config to log...") 
            DumpConfigToLog()

        #get pin config from settings
        gpio_pin=int(Parameters["Mode1"])

        Debug("Pin "+str(gpio_pin)+" was configured")
        if Parameters["Mode2"]=="PU":
            Debug("Pull up resistor configured")
            resistor=GPIO.PUD_UP
        elif Parameters["Mode2"]=="PD":
            Debug("Pull Down resistor configured")
            resistor=GPIO.PUD_DOWN
        else:
            Debug("No resistor configured")

        # By default false positive checks are switched OFF
        check_last_value = False
        check_consistency = False

        # Get Interrupt and check mode config
        if Parameters["Mode3"]=="Falling" or Parameters["Mode3"]=="FallingLast" or Parameters["Mode3"]=="FallingConsistency" or Parameters["Mode3"]=="FallingLastConsistency":
            interrupt=GPIO.FALLING
            Debug("Falling interrupt detected")
            if Parameters["Mode3"]=="FallingLast":
                check_last_value = True
            elif Parameters["Mode3"]=="FallingConsistency":
                check_consistency = True
            elif Parameters["Mode3"]=="FallingLastConsistency":
                check_last_value = True 
                check_consistency = True
        elif Parameters["Mode3"]=="Rising" or Parameters["Mode3"]=="RisingLast" or Parameters["Mode3"]=="RisingConsistency" or Parameters["Mode3"]=="RisingLastConsistency":
            interrupt=GPIO.RISING
            Debug("Rising Interrupt detected")
            if Parameters["Mode3"]=="RisingLast":
                check_last_value = True
            elif Parameters["Mode3"]=="RisingConsistency":
                check_consistency = True
            elif Parameters["Mode3"]=="RisingLastConsistency":
                check_last_value = True
                check_consistency = True
        elif Parameters["Mode3"]=="Both" or Parameters["Mode3"]=="BothLast" or Parameters["Mode3"]=="BothConsistency" or Parameters["Mode3"]=="BothLastConsistency":
            interrupt=GPIO.BOTH
            Debug("Both interrupt detected")
            if Parameters["Mode3"]=="BothLast":
                check_last_value = True
            elif Parameters["Mode3"]=="BothConsistency":
                check_consistency = True
            elif Parameters["Mode3"]=="BothLastConsistency":
                check_last_value = True
                check_consistency = True

        Debug("Interrupt Type = "+str(interrupt))
        Debug("Consistency check = "+str(check_consistency))
        Debug("Last value check = "+str(check_last_value))

        bouncetime=int(Parameters["Mode4"])
        Debug("Bouncetime = "+str(bouncetime))

        fn=Parameters["Mode5"]
        increment=float(Parameters["Mode6"])
        Debug("Filename "+fn+" detected")
        Debug("increment "+str(increment)+" detected")


        # Setting up GPIO
        Debug("Setting up GPIO")
        GPIO.setmode(GPIO.BCM)
        if Parameters["Mode2"]=="PU" or Parameters["Mode2"]=="PD" :
            Debug("Adding resistortype"+str(Parameters["Mode2"]))
            GPIO.setup(gpio_pin, GPIO.IN, pull_up_down = resistor)
        else:
            GPIO.setup(gpio_pin, GPIO.IN)

        # Store initial value
        last_value=GPIO.input(gpio_pin)

        GPIO.add_event_detect(gpio_pin, GPIO.BOTH, callback = Interrupt, bouncetime = bouncetime)

        #Create device if needed
        if (len(Devices) == 0):
            Debug("Creating watermeter device")
            Domoticz.Device(Name="Water Usage", Unit=1, Type=113, Subtype=0, Switchtype=2).Create()

        #Get current counter
        counter=GetMeterFile()
        InitialReading=0
        if counter==-1:
            Debug("No meter file, creating one with value  ("+str(InitialReading)+")")
            counter=InitialReading
            WriteMeterFile(counter)

        # Update Sensor with counter
        Devices[1].Update(nValue=int(counter), sValue=str(counter))


    def onStop(self):
        Debug("onStop called: Cleaning up GPIO")
        GPIO.cleanup()

    def onConnect(self, Connection, Status, Description):
        Debug("onConnect called")

    def onMessage(self, Connection, Data):
        Debug("onMessage called")

    def onCommand(self, Unit, Command, Level, Hue):
        Debug("onCommand called for Unit " + str(Unit) + ": Parameter '" + str(Command) + "', Level: " + str(Level))

    def onNotification(self, Name, Subject, Text, Status, Priority, Sound, ImageFile):
        Debug("Notification: " + Name + "," + Subject + "," + Text + "," + Status + "," + str(Priority) + "," + Sound + "," + ImageFile)

    def onDisconnect(self, Connection):
        Debug("onDisconnect called")

    def onHeartbeat(self):
        global last_watermeter_value
        Debug("onHeartbeat called")
        if fakereading==True:
            Debug("FakeReading==True: Generating testpulse, not generated by watermeter itself!")
            Interrupt(1) #For testing purposes

        #Logging (Wordaround: domotic 2022.1 cause error in findmodule if log function is called during interrupt, so log in heartbeat if value has changed)
        counter=GetMeterFile()
        if last_watermeter_value!=counter:
            Domoticz.Log("RFXMeter/RFXMeter counter ("+Devices[1].Name+") - "+str(counter/1000)+" M3") 
            last_watermeter_value=counter


global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onConnect(Connection, Status, Description):
    global _plugin
    _plugin.onConnect(Connection, Status, Description)

def onMessage(Connection, Data):
    global _plugin
    _plugin.onMessage(Connection, Data)

def onCommand(Unit, Command, Level, Hue):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Hue)

def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    global _plugin
    _plugin.onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile)

def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

    # Generic helper functions
def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Log( "'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Log("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Log("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Log("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Log("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Log("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Log("Device LastLevel: " + str(Devices[x].LastLevel))
    return

def GetMeterFile():
    fn=Parameters["Mode5"] # Get filename
    Debug("GetMeterFile() called")
    if os.path.exists(fn):
        f = open(fn, "r+")
        line = f.readline()
        a,b,c = line.split()
        Counter = float(c)
        Debug("Meter file exists, current counter is "+str(Counter))
        return Counter
    else:
        Debug("No Meter File found")
        return -1

def WriteMeterFile(counter):
    fn=Parameters["Mode5"] # get Filename
    Debug("WriteMeterFile("+str(counter)+") called")
    f = open( fn, 'w')
    f.write( 'meterstand = ' + repr(counter))
    f.close()

def Interrupt(channel):

    global interrupt
    global gpio_pin
    global check_last_value
    global check_consistency
    global last_value

    Debug("Start processing...")
    Debug("Last value GPIO.input("+str(gpio_pin)+") = "+str(last_value))
    
    # Get current (new) GPIO value
    new_value = GPIO.input(gpio_pin)
    Debug("Detected value GPIO.input("+str(gpio_pin)+") = "+str(new_value))

    if (fakereading):
        if (check_consistency or check_last_value):
                Debug("Testpulse = true, ignoring additional checks")
    else:
        # Consistency check logic
        if check_consistency:
            # Sleep for 300 ms to check pin state for false positives and compare with previous known value
            time.sleep(0.3)
            Debug("And awake..")
                    
            # Get current (newest) GPIO value
            newest_value = GPIO.input(gpio_pin)
            Debug("Newest value GPIO.input("+str(gpio_pin)+") = "+str(newest_value))

            # Compare new value with newest (deviation within 300ms seems like a power fluctuation)
            if new_value != newest_value:
                Debug("Interrupt detected, but not consistent; last '"+str(last_value)+"' -> new '"+str(new_value)+"' -> newest '"+str(newest_value)+"'; false positive -> exit")
                return

        # Last value check logic    
        if check_last_value:
            # Compare newest value with last known value (before trigger)
            if new_value == last_value:
                Debug("Interrupt detected, but same value; last '"+str(last_value)+"' -> new '"+str(new_value)+"; false positive -> exit")
                return

            # We detect both falling and rising (otherwise we cannot detect false positives in both ways); but setting for Interrupt mode should be adhered to
        if (new_value == 1 and interrupt == GPIO.FALLING) or (new_value == 0 and interrupt == GPIO.RISING):
            Debug("Interrupt detected, but wrong type; last '"+str(last_value)+"' -> new '"+str(new_value)+"'; update 'last_value' with 'new_value' -> exit")
            last_value = new_value
            return

        Debug("Interrupt detected, checks (if applicable) are OK;")
        Debug("Last '"+str(last_value)+"' -> new '"+str(new_value)+"; change 'last_value' into new value")

        # Store current value as 'last_value' and continue 
        last_value = new_value
        Debug("Checks passed, continue increasing the counter..")
   
    Debug("Processing Meter Pulse (1 liter water)")

    counter=GetMeterFile()
    if counter==-1:
        # counter=int(Parameters["Mode6"]) # Get initial value from settings
        counter=0 # Configured above in the script
        Debug("No meter file, creating a new one")
    else:
        increment=float(Parameters["Mode6"])
        counter+=increment 
        Debug("incremented counter to "+str(counter))

    WriteMeterFile(counter)

    #Create device if it is no longer there 
    if (len(Devices) == 0): 
        Debug("Watermeter device gone...Creating watermeter device")
        Domoticz.Device(Name="Water Usage", Unit=1, Type=113, Subtype=0, Switchtype=2).Create()
    
    #update the device with the found counter
    Devices[1].Update(nValue=int(counter), sValue=str(counter))
    #Domoticz.Log("RFXMeter/RFXMeter counter ("+Devices[1].Name+") - "+str(counter/1000)+" M3") ## temporarily disabled due to FindModule bug

def Debug(text):
    if (debug):
        Domoticz.Log(text)

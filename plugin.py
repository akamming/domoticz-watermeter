# Basic Python Plugin Example
#
# Author: GizMoCuz
#
"""
<plugin key="WMPS" name="WaterMeter NPN plugin" author="akamming" version="1.0.0" wikilink="http://www.domoticz.com/wiki/plugins/plugin.html" externallink="https://www.google.com/">
    <description>
        <h2>Watermeter</h2><br/>
        Plugin version of the Watermeter python script using a NPN sensor
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
            <li>GPIO Pin Number - The GPIO Pin (BCM!) to which your NPN sensor is connected. To avoid conflicts, make sure the gpio pin is not managed/configured somewhere else on your system to prevent confllicts. You can still use the normal GPIO drivers in domoticz for other pins as long as you don't configure the same pins</li>
            <li>Resistor Type - Configure the correct type of resistor. If the NPN is soldered to the GPIO without any physical resistors in a scheme, you definitely should configure a resistor here. </li>
            <li>Interrupt Mode - Configure if you want the meter to be triggered if the pin goes from 1 to 0 (falling), from 0 to -1 (rising) or on both changes (both). Normally it should be either falling or rising, but not both (both will get you double readings) </li>
            <li>Debounce Time - Configure the cooldown time after the interrupt to prevent interrupt flooding. A high number is recommended, but it should be less then the time it takes to have 1 liter going throught your watermeter, to prevent lost measurements </li> 
            <li>Meter Reading File - The path of the file where you want the actual meter reading to be stored. If you do not specifiy a path, your domoticz working directory will be used</li>
            <li>Default Meter Reading - Will be the initial value when the Meter Reading File is created</li>
        </ul>
    </description>
    <params>
         <param field="Mode1" label="GPIO Pin Number" width="70px">
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
            <option label="GPIO19" value="19" default="true"/>
            <option label="GPIO20" value="20"/>
            <option label="GPIO21" value="21"/>
            <option label="GPIO22" value="22"/>
            <option label="GPIO23" value="23"/>
            <option label="GPIO24" value="24"/>
            <option label="GPIO25" value="25"/>
            <option label="GPIO26" value="26"/>
        </options>
         </param> 
         <param field="Mode2" label="Resistor Type" width="70px">
         <options>
            <option label="PullUp" value="PU" default="true"/>
            <option label="PullDown" value="PD"/>
            <option label="None" value="None"/>
        </options>
         </param> 
         <param field="Mode3" label="Interrupt mode" width="150px" required="true">
         <options>
            <option label="Falling" value="Falling" default="true"/>
            <option label="Rising" value="Rising"/>
        </options>
        </param>
         <param field="Mode4" label="debounce time (ms)" width="150px" required="true">
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
         </options>
         </param>
         <param field="Mode5" label="Meter Reading File" width="150px" required="true" default="meterstand.txt" />
         <param field="Mode6" label="Default Meter Reading" width="70px" default="1468502"/>
         <param field="Mode7" label="Debug" width="150px">
            <options>
                <option label="False" value="0"/>
                <option label="True" value="1"  default="true" />
         </options>
         </param>
     </params>
</plugin>
"""
import Domoticz
import  RPi.GPIO as GPIO

class BasePlugin:


    def Interrupt(channel):
          Domoticz.Log ("Caught interrupt")

    def DumpConfigToLog():
        for x in Parameters:
            if Parameters[x] != "":
                Domoticz.Log( "'" + x + "':'" + str(Parameters[x]) + "'")
                Domoticz.Log("Device count: " + str(len(Devices)))

        for x in Devices:
            Domoticz.Log("Device:           " + str(x) + " - " + str(Devices[x]))
            Domoticz.Log("Device ID:       '" + str(Devices[x].ID) + "'")
            Domoticz.Log("Device Name:     '" + Devices[x].Name + "'")
            Domoticz.Log("Device nValue:    " + str(Devices[x].nValue))
            Domoticz.Log("Device sValue:   '" + Devices[x].sValue + "'")
            Domoticz.Log("Device LastLevel: " + str(Devices[x].LastLevel))
        return



    enabled = False
    def __init__(self):
        #self.var = 123
        return

    def onStart(self):
        Domoticz.Log("onStart called")
        Domoticz.Device(Name="watermeter", Unit=1, Type=113, Subtype=0, Switchtype=2, Image=17).Create()
        Domoticz.Log(str(Parameters["Mode5"]))
        # GPIO.setmode(GPIO.BOARD)
        # GPIO.add_event_detect(12, GPIO.FALLING, callback = self.Interrupt, bouncetime = 350)

    def onStop(self):
        Domoticz.Log("onStop called")

    def onConnect(self, Connection, Status, Description):
        Domoticz.Log("onConnect called")

    def onMessage(self, Connection, Data):
        Domoticz.Log("onMessage called")

    def onCommand(self, Unit, Command, Level, Hue):
        Domoticz.Log("onCommand called for Unit " + str(Unit) + ": Parameter '" + str(Command) + "', Level: " + str(Level))

    def onNotification(self, Name, Subject, Text, Status, Priority, Sound, ImageFile):
        Domoticz.Log("Notification: " + Name + "," + Subject + "," + Text + "," + Status + "," + str(Priority) + "," + Sound + "," + ImageFile)

    def onDisconnect(self, Connection):
        Domoticz.Log("onDisconnect called")

    def onHeartbeat(self):
        Domoticz.Log("onHeartbeat called")

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
            Domoticz.Debug( "'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
    return

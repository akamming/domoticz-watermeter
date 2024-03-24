# domoticz-watermeter
Python plugin for measuring your watermeter with a NPN sensor on a GPIO pin

## why this plugin?
I struggeled with all the manual steps for getting a watermeter in domoticz, using instructions like
https://www.domoticz.com/forum/viewtopic.php?f=28&t=17123
or 
https://ehoco.nl/watermeter-uitlezen-in-domoticz-lua-script/

so i automated the following steps by rewriting the python script i found in the thread above to this plugin
- Pin is automatically exported (no need for exporting the pin in shell scripts before starting domoticz)
- pluging starts and stops with domoticz, so no steps to keep a seperate python script up and running on your system all is handled within domoticz
- Counter is automatically created, so no difficult json commands to create the counter manually

## support
is only tested on  a raspberry pi 3b+

## Installation 
- install the dependency by giving the command "sudo apt-get install python3-gpiozero"
- go to you plugins directory
- give the command "git clone https://github.com/akamming/domoticz-watermeter.git"
- restart domoticz
- add the hardware. In the hardwarepage there is a description on how to configure the plugin
- Make sure your rfxcom divider setting for water (Setup/Settings/Counter settings) in domoticz is set to 1000.
- have fun!

## Debugging
If you feel like debugging, there are 2 settings you can configure
- If you create the file DEBUG in the plugin directory, debug logging will be switched on
- If you create the file TESTPULSE in the plugin directory, the plugin will fake increments on the watermeter. every 10 sec it will act like it got a pulse from the GPIO pin. This can be used for testing purposes

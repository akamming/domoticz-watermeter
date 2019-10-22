# domoticz-watermeter
Python plugin for measuring your watermeter with a NPN sensor on a GPIO pin

##why this plugin?
i struggeled with all the manual steps for getting a watermeter in domoticz, using instructions like
https://www.domoticz.com/forum/viewtopic.php?f=28&t=17123
or 
https://ehoco.nl/watermeter-uitlezen-in-domoticz-lua-script/

so i automated the following steps by rewriting the python script i found in the thread above to this plugin
- No more exporting pins in shell scripts
- No manual steps to keep a python script up and running on your system
- No manual steps to create the counter

## support
is only supported on a raspberry pi (only tested on a 3b+)

## Installation 
- go to you plugins directory
- give the command "git clone https://github.com/akamming/domoticz-watermeter.git"
- restart domoticz
- add the hardware. In the hardwarepage there is a description on how to configure the plugin
- Make sure your rfxcom divider setting for water (Setup/Settings/Counter settings) in domoticz is set to 1000.
- have fun!

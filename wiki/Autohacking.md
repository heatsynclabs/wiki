Some resources so far

- <http://www.geekmyride.org/wiki/index.php/Main_Page>

<!-- -->

- mc33290 is an ISO K Line Serial Link Interface, I think has to do with serial interfacing odbii
- [ELM](http://www.elmelectronics.com/contact.html) seems to make some of the (only?) odb interface chips. They appear to have a software stack they burn onto microchip microcontrollers
- <http://www.scantool.net/parts/> has some promising software, and seems to sell ELM products and a breakout board.

Typically, one finds that the manufacturers use the following standards though most manufactures have adopted ISO15765 CAN for 2006 and newer vehicles:

- J1850-PWM (mainly Ford)
- J1850-VPW (Chrysler, GM, Saturn)
- ISO9141/ISO14230 (Acura, Chrysler, Honda, Subaru, Suzuki, Toyota, Volkswagen)
- ISO15765 (most newer vehicles)

**Open Source Implementations**

- [Vehicle Telemetry Platform](http://www.practicalarduino.com/projects/vehicle-telemetry-platform) from the Practical Arduino book is a derivative of the OBDuino32K using the Arduino Mega
- <http://code.google.com/p/opengauge/> looks like a great open source resource
- [OBDuinoMega](http://github.com/practicalarduino/OBDuinoMega.git)
- [OBDuino32K](http://code.google.com/p/opengauge/wiki/OBDuino32K)
- [MPGuino](http://ecomodder.com/wiki/index.php/MPGuino) Miles Per Gallon monitor using the Arduino

**Commercial Implementations**

These links are basically for commercial versions of the obdII interface. Almost all of them give you a connector with free software that can read the basic trouble codes. Some give you the manufacturer specific "extended" or "enhanced" support codes that allow a person to troubleshoot even more components.

- [AutoEnginuity.com](http://autoenginuity.com/)

**Hardware**

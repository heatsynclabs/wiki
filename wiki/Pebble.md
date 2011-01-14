# Introduction

The pebble is XXX. The hardware files are located at <https://github.com/lukeweston/Pebble/> and the Software is kept at <https://github.com/geekscape/Aiko>

The pebble has a multitude of cool electronics components for you to play with. Our implementation of these boards include a 'standard' set of features and optional addons

## Standard Features

### 8 bit shift register

#### Description

Shift registers take in serial data (one number at a time, 1, 0, 1, 0, 1, 1, 1, 0) and express that data in parallel across 8 pins(10101110). It basically turns one data pin into 8! For some operations you could think of it as a multiplexer. For this example it is important to read up on the [shiftOut](http://www.arduino.cc/en/Tutorial/ShiftOut) arduino function as that does almost all of the hard work for you! This example again repurposes an the \[Hello World <http://arduino.cc/en/Tutorial/ShftOut11>\] example from that page and substitutes our proper pins CLOCK=4, DATA=3, STROBE=2

#### Code

<code>

`int CLOCK=4;`\
`int DATA=3;`\
`int STROBE=2;`

void setup() {

` //set pins to output so you can control the shift register`\
` pinMode(STROBE, OUTPUT);`\
` pinMode(CLOCK, OUTPUT);`\
` pinMode(DATA, OUTPUT);`

}

void loop() {

` // count from 0 to 255 and display the number `\
` // on the LEDs`\
` for (int numberToDisplay = 0; numberToDisplay < 256; numberToDisplay++) {`\
`   // take the latchPin low so `\
`   // the LEDs don't change while you're sending in bits:`\
`   digitalWrite(STROBE, LOW);`\
`   // shift out the bits:`\
`   shiftOut(DATA, CLOCK, MSBFIRST, numberToDisplay);  `

`   //take the latch pin high so the LEDs will light up:`\
`   digitalWrite(STROBE, HIGH);`\
`   // pause before next value:`\
`   delay(500);`\
` }`

} </code>

### Temperature sensor

#### Description

The temperature sensor is the XXX chip and utilizes a library called One Wire. XXX add datasheet link here. The value should generally read 25C indoors. If you squeeze the sensor with your finger that value should rise fairly quickly to 30C.

#### Code

My example crudely combines the Aiko LCD example and the Aiko temperature example to display the temperature to the screen. Note this example requires the One Wire library to be installed to your libraries directory of Arduino, in addition to the Aiko libraries. <code>

1.  include \<AikoEvents.h\>
2.  include \<AikoSExpression.h\>

using namespace Aiko;

1.  define PIN_LCD_STROBE 2 // CD4094 8-bit shift/latch
2.  define PIN_LCD_DATA 3 // CD4094 8-bit shift/latch
3.  define PIN_LCD_CLOCK 4 // CD4094 8-bit shift/latch
4.  define PIN_ONE_WIRE 5

void setup() {

` Events.addHandler(temperatureSensorHandler, 1000);`\
` Events.addHandler(lcdHandler,   1000);`

}

void loop() {

` Events.loop();`

}

1.  include \<OneWire.h\>

OneWire oneWire(PIN_ONE_WIRE); // Maxim DS18B20 temperature sensor

byte oneWireInitialized = false;

1.  define ONE_WIRE_COMMAND_READ_SCRATCHPAD 0xBE
2.  define ONE_WIRE_COMMAND_START_CONVERSION 0x44
3.  define ONE_WIRE_COMMAND_MATCH_ROM 0x55
4.  define ONE_WIRE_COMMAND_SKIP_ROM 0xCC

<!-- -->

1.  define ONE_WIRE_DEVICE_18B20 0x28
2.  define ONE_WIRE_DEVICE_18S20 0x10

int temperature_whole = 0; int temperature_fraction = 0;

void temperatureSensorHandler(void) { // total time: 33 milliseconds

` byte address[8];`\
` byte data[12];`\
` byte index;`

` if (! oneWire.search(address)) {  // time: 14 milliseconds`

// Serial.println("(error 'No more one-wire devices')");

`   oneWire.reset_search();         // time: <1 millisecond`\
`   return;`\
` }`

` if (OneWire::crc8(address, 7) != address[7]) {`

// sendMessage("(error 'Address CRC is not valid')");

`   return;`\
` }`

` if (address[0] != ONE_WIRE_DEVICE_18B20) {`

// sendMessage("(error 'Device is not a DS18B20')");

`   return;`\
` }`

` if (oneWireInitialized) {`\
`   byte present = oneWire.reset();                   // time: 1 millisecond`\
`   oneWire.select(address);                          // time: 5 milliseconds`\
`   oneWire.write(ONE_WIRE_COMMAND_READ_SCRATCHPAD);  // time: 1 millisecond`

`   for (index = 0; index < 9; index++) {             // time: 5 milliseconds`\
`     data[index] = oneWire.read();`\
`   }`

`   if (OneWire::crc8(data, 8) != data[8]) {`

// sendMessage("(error 'Data CRC is not valid')");

`     return;`\
`   }`

`   int temperature = (data[1] << 8) + data[0];`\
`   int signBit     = temperature & 0x8000;`\
`   if (signBit) temperature = (temperature ^ 0xffff) + 1;  // 2's complement`

`   int tc_100 = (6 * temperature) + temperature / 4;  // multiply by 100 * 0.0625`

`   temperature_whole    = tc_100 / 100;`\
`   temperature_fraction = tc_100 % 100;`

` }`

` // Start temperature conversion with parasitic power`\
` oneWire.reset();                                      // time: 1 millisecond`\
` oneWire.select(address);                              // time: 5 milliseconds`\
` oneWire.write(ONE_WIRE_COMMAND_START_CONVERSION, 1);  // time: 1 millisecond`

` // Must wait at least 750 milliseconds for temperature conversion to complete`\
` oneWireInitialized = true;`

}

/\* -------------------------------------------------------------------------- \*/ /\* LCD KS0066 4-bit data interface, 3 Arduino pins and MC14094 8-bit register

`* `[`http://www.datasheetsite.com/datasheet/KS0066`](http://www.datasheetsite.com/datasheet/KS0066)\
`*`\
`* MC14094 input:  Arduino digital pin 2=Clock, pin 4=Data, pin 7=Strobe`\
`* MC14094 output: Q8=DB4, Q7=DB5, Q6=DB6, Q5=DB7, Q4=E, Q3=RW, Q2=RS, Q1=None`\
`* `[`http://www.ee.mut.ac.th/datasheet/MC14094.pdf`](http://www.ee.mut.ac.th/datasheet/MC14094.pdf)\
`*`\
`*   +--------------------------------------------+`\
`*   |    Arduino (ATMega 168 or 328)             |`\
`*   |    D02           D03           D04         |`\
`*   +----+-------------+-------------+-----------+`\
`*        |4            |5            |6`\
`*        |1            |2            |3`\
`*   +----+-------------+-------------+-----------+`\
`*   |    Strobe        Data          Clock       |`\
`*   |    MC14094 8-bit shift/latch register      |`\
`*   |    Q8   Q7   Q6   Q5   Q4   Q3   Q2   Q1   |`\
`*   +----+----+----+----+----+----+----+----+----+`\
`*        |11  |12  |13  |14  |7   |6   |5   |4`\
`*        |11  |12  |13  |14  |6   |5   |4 `\
`*   +----+----+----+----+----+----+----+---------+`\
`*   |    DB4  DB5  DB6  DB7  E    RW   RS        |`\
`*   |               LCD KS0066                   |`\
`*   +--------------------------------------------+`\
`*/`

byte lcdInitialized = false;

// LCD pin bit-patterns, output from MC14094 -\> LCD KS0066 input

1.  define LCD_ENABLE_HIGH 0x10 // MC14094 Q4 -\> LCD E
2.  define LCD_ENABLE_LOW 0xEF // Enable (high) / Disable (low)
3.  define LCD_RW_HIGH 0x20 // MC14094 Q3 -\> LCD RW
4.  define LCD_RW_LOW 0xDF // Read (high) / Write (low)
5.  define LCD_RS_HIGH 0x40 // MC14094 Q2 -\> LCD RS
6.  define LCD_RS_LOW 0xBF // Data (high) / Instruction (low) Select

// LCD Commands

1.  define LCD_COMMAND_CLEAR 0x01 // Clear display
2.  define LCD_COMMAND_HOME 0x02 // Set DD RAM address counter to (0, 0)
3.  define LCD_COMMAND_ENTRY_SET 0x06 // Entry mode set
4.  define LCD_COMMAND_DISPLAY_SET 0x0C // Display on/off control
5.  define LCD_COMMAND_FUNCTION_SET 0x28 // Function set
6.  define LCD_COMMAND_SET_DDRAM_ADDRESS 0x80 // Set DD RAM address counter (row, column)

<!-- -->

1.  define LCD_SECOND_ROW 0x40 // Second row literal

byte lcdSetup\[\] = { // LCD command, delay time in milliseconds

` LCD_COMMAND_HOME,         50,  // wait for LCD controller to be initialized`\
` LCD_COMMAND_HOME,         50,  // ditto`\
` LCD_COMMAND_FUNCTION_SET,  1,  // 4-bit interface, 2 display lines, 5x8 font`\
` LCD_COMMAND_DISPLAY_SET,   1,  // turn display on, cursor off, blinking off`\
` LCD_COMMAND_CLEAR,         2,  // clear display`\
` LCD_COMMAND_ENTRY_SET,     1   // increment mode, display shift off`

};

void lcdInitialize(void) {

` pinMode(PIN_LCD_CLOCK,  OUTPUT);`\
` pinMode(PIN_LCD_DATA,   OUTPUT);`\
` pinMode(PIN_LCD_STROBE, OUTPUT);`

` byte length = sizeof(lcdSetup) / sizeof(*lcdSetup);`\
` byte index = 0;`

` while (index < length) {`\
`   lcdWrite(lcdSetup[index ++], false);`\
`   delay(lcdSetup[index ++]);`\
` }`

` lcdInitialized = true;`

}

void lcdWrite(

` byte value,`\
` byte dataFlag) {`

` digitalWrite(PIN_LCD_STROBE, LOW);`

` byte output = value >> 4;                                    // Most Significant Nibble`\
` if (dataFlag) output = (output | LCD_RS_HIGH) & LCD_RW_LOW;  // Command or Data ?`

` for (byte loop1 = 0; loop1 < 2; loop1 ++) {  // First MSN, then LSN`\
`   for (byte loop2 = 0; loop2 < 3; loop2 ++) {  // LCD ENABLE LOW -> HIGH -> LOW`\
`     output = (loop2 == 1) ? (output | LCD_ENABLE_HIGH) : (output & LCD_ENABLE_LOW);`

`     shiftOut(PIN_LCD_DATA, PIN_LCD_CLOCK, LSBFIRST, output);`\
`     digitalWrite(PIN_LCD_STROBE, HIGH);`\
`     delayMicroseconds(10);`\
`     digitalWrite(PIN_LCD_STROBE,LOW);`\
`   }`

delay(1);

`   output = value & 0x0F;                                       // Least Significant Nibble`\
`   if (dataFlag) output = (output | LCD_RS_HIGH) & LCD_RW_LOW;  // Command or Data ?`\
` }`

}

void lcdClear(void) {

` lcdWrite(LCD_COMMAND_CLEAR, false);`\
` delay(2);`

}

void lcdPosition(

` byte row,        // Must be either 0 (first row) or 1 (second row)`\
` byte column) {   // Must be between 0 and 15`

` if (row == 1) row = LCD_SECOND_ROW;`\
` lcdWrite(LCD_COMMAND_SET_DDRAM_ADDRESS | row | column, false);`\
` delayMicroseconds(40);`

}

void lcdWriteString(

` char message[]) {`

` while (*message) lcdWrite((*message ++), true);`

}

// checks out how many digits there are in a number

int estimateDigits(int nr) {

` int dec = 10;`\
` int temp = 1;`\
` int div = nr/dec;`\
` while (div > 0) {`\
`   dec *= 10;`\
`   div = nr/dec;`\
`   temp++;`\
` }`\
` return temp;`

}

// Raise number to power

int pow(int base, int expo) {

` int temp = 1;`\
` for (int c = 1; c <= expo; c++) {`\
`   temp *= base;`\
` }`\
` return temp;`

}

// this function help us to write numbers // with more than one digit

void lcdWriteNumber(int nr, int digits) {

` for (int i = digits-1; i >= 0; i--) {`\
`   int dec = pow(10,i);`\
`   int div = nr/dec;`\
`   lcdWrite(div+48, true);`\
`   if (div > 0) {`\
`     nr -= div*dec;`\
`   }`\
` }`

}

void lcdWriteNumber(int nr) {

` int value = nr;`

` if (value < 0) {`\
`   lcdWrite('-', true);`\
`   value = - nr;`\
` }`

` int digits = estimateDigits(value);`\
` lcdWriteNumber(value, digits);`

}

void lcdHandler(void) {

` if (lcdInitialized == false) {`\
`   lcdInitialize();`\
`   lcdClear();`\
` }`

` lcdPosition(0, 8);`\
` lcdWriteNumber((int) temperature_whole);`\
` `

} </code>

### Light sensor

#### Description

The light sensor detects light on an anlalog pin and is located on A0.

#### Code

The following code is simply the Aiko LCD code crudely combined with the Aiko Light sensor code to display the light values on the screen. You should expect a value of ~900 for fluorescent lights indoor, and if you press your finger over the top of the sensor that value should fall to ~300. <code>

1.  include \<AikoEvents.h\>
2.  include \<AikoSExpression.h\>

using namespace Aiko;

1.  define PIN_LCD_STROBE 2 // CD4094 8-bit shift/latch
2.  define PIN_LCD_DATA 3 // CD4094 8-bit shift/latch
3.  define PIN_LCD_CLOCK 4 // CD4094 8-bit shift/latch
4.  define PIN_LIGHT_SENSOR 0

void setup() {

` Events.addHandler(ldrHandler, 1000);`\
` Events.addHandler(lcdHandler,   1000);`

}

void loop() {

` Events.loop();`

}

int ldr = 0;

void ldrHandler(void) {

`ldr = analogRead(PIN_LIGHT_SENSOR);`

}

/\* -------------------------------------------------------------------------- \*/ /\* LCD KS0066 4-bit data interface, 3 Arduino pins and MC14094 8-bit register

`* `[`http://www.datasheetsite.com/datasheet/KS0066`](http://www.datasheetsite.com/datasheet/KS0066)\
`*`\
`* MC14094 input:  Arduino digital pin 2=Clock, pin 4=Data, pin 7=Strobe`\
`* MC14094 output: Q8=DB4, Q7=DB5, Q6=DB6, Q5=DB7, Q4=E, Q3=RW, Q2=RS, Q1=None`\
`* `[`http://www.ee.mut.ac.th/datasheet/MC14094.pdf`](http://www.ee.mut.ac.th/datasheet/MC14094.pdf)\
`*`\
`*   +--------------------------------------------+`\
`*   |    Arduino (ATMega 168 or 328)             |`\
`*   |    D02           D03           D04         |`\
`*   +----+-------------+-------------+-----------+`\
`*        |4            |5            |6`\
`*        |1            |2            |3`\
`*   +----+-------------+-------------+-----------+`\
`*   |    Strobe        Data          Clock       |`\
`*   |    MC14094 8-bit shift/latch register      |`\
`*   |    Q8   Q7   Q6   Q5   Q4   Q3   Q2   Q1   |`\
`*   +----+----+----+----+----+----+----+----+----+`\
`*        |11  |12  |13  |14  |7   |6   |5   |4`\
`*        |11  |12  |13  |14  |6   |5   |4 `\
`*   +----+----+----+----+----+----+----+---------+`\
`*   |    DB4  DB5  DB6  DB7  E    RW   RS        |`\
`*   |               LCD KS0066                   |`\
`*   +--------------------------------------------+`\
`*/`

byte lcdInitialized = false;

// LCD pin bit-patterns, output from MC14094 -\> LCD KS0066 input

1.  define LCD_ENABLE_HIGH 0x10 // MC14094 Q4 -\> LCD E
2.  define LCD_ENABLE_LOW 0xEF // Enable (high) / Disable (low)
3.  define LCD_RW_HIGH 0x20 // MC14094 Q3 -\> LCD RW
4.  define LCD_RW_LOW 0xDF // Read (high) / Write (low)
5.  define LCD_RS_HIGH 0x40 // MC14094 Q2 -\> LCD RS
6.  define LCD_RS_LOW 0xBF // Data (high) / Instruction (low) Select

// LCD Commands

1.  define LCD_COMMAND_CLEAR 0x01 // Clear display
2.  define LCD_COMMAND_HOME 0x02 // Set DD RAM address counter to (0, 0)
3.  define LCD_COMMAND_ENTRY_SET 0x06 // Entry mode set
4.  define LCD_COMMAND_DISPLAY_SET 0x0C // Display on/off control
5.  define LCD_COMMAND_FUNCTION_SET 0x28 // Function set
6.  define LCD_COMMAND_SET_DDRAM_ADDRESS 0x80 // Set DD RAM address counter (row, column)

<!-- -->

1.  define LCD_SECOND_ROW 0x40 // Second row literal

byte lcdSetup\[\] = { // LCD command, delay time in milliseconds

` LCD_COMMAND_HOME,         50,  // wait for LCD controller to be initialized`\
` LCD_COMMAND_HOME,         50,  // ditto`\
` LCD_COMMAND_FUNCTION_SET,  1,  // 4-bit interface, 2 display lines, 5x8 font`\
` LCD_COMMAND_DISPLAY_SET,   1,  // turn display on, cursor off, blinking off`\
` LCD_COMMAND_CLEAR,         2,  // clear display`\
` LCD_COMMAND_ENTRY_SET,     1   // increment mode, display shift off`

};

void lcdInitialize(void) {

` pinMode(PIN_LCD_CLOCK,  OUTPUT);`\
` pinMode(PIN_LCD_DATA,   OUTPUT);`\
` pinMode(PIN_LCD_STROBE, OUTPUT);`

` byte length = sizeof(lcdSetup) / sizeof(*lcdSetup);`\
` byte index = 0;`

` while (index < length) {`\
`   lcdWrite(lcdSetup[index ++], false);`\
`   delay(lcdSetup[index ++]);`\
` }`

` lcdInitialized = true;`

}

void lcdWrite(

` byte value,`\
` byte dataFlag) {`

` digitalWrite(PIN_LCD_STROBE, LOW);`

` byte output = value >> 4;                                    // Most Significant Nibble`\
` if (dataFlag) output = (output | LCD_RS_HIGH) & LCD_RW_LOW;  // Command or Data ?`

` for (byte loop1 = 0; loop1 < 2; loop1 ++) {  // First MSN, then LSN`\
`   for (byte loop2 = 0; loop2 < 3; loop2 ++) {  // LCD ENABLE LOW -> HIGH -> LOW`\
`     output = (loop2 == 1) ? (output | LCD_ENABLE_HIGH) : (output & LCD_ENABLE_LOW);`

`     shiftOut(PIN_LCD_DATA, PIN_LCD_CLOCK, LSBFIRST, output);`\
`     digitalWrite(PIN_LCD_STROBE, HIGH);`\
`     delayMicroseconds(10);`\
`     digitalWrite(PIN_LCD_STROBE,LOW);`\
`   }`

delay(1);

`   output = value & 0x0F;                                       // Least Significant Nibble`\
`   if (dataFlag) output = (output | LCD_RS_HIGH) & LCD_RW_LOW;  // Command or Data ?`\
` }`

}

void lcdClear(void) {

` lcdWrite(LCD_COMMAND_CLEAR, false);`\
` delay(2);`

}

void lcdPosition(

` byte row,        // Must be either 0 (first row) or 1 (second row)`\
` byte column) {   // Must be between 0 and 15`

` if (row == 1) row = LCD_SECOND_ROW;`\
` lcdWrite(LCD_COMMAND_SET_DDRAM_ADDRESS | row | column, false);`\
` delayMicroseconds(40);`

}

void lcdWriteString(

` char message[]) {`

` while (*message) lcdWrite((*message ++), true);`

}

// checks out how many digits there are in a number

int estimateDigits(int nr) {

` int dec = 10;`\
` int temp = 1;`\
` int div = nr/dec;`\
` while (div > 0) {`\
`   dec *= 10;`\
`   div = nr/dec;`\
`   temp++;`\
` }`\
` return temp;`

}

// Raise number to power

int pow(int base, int expo) {

` int temp = 1;`\
` for (int c = 1; c <= expo; c++) {`\
`   temp *= base;`\
` }`\
` return temp;`

}

// this function help us to write numbers // with more than one digit

void lcdWriteNumber(int nr, int digits) {

` for (int i = digits-1; i >= 0; i--) {`\
`   int dec = pow(10,i);`\
`   int div = nr/dec;`\
`   lcdWrite(div+48, true);`\
`   if (div > 0) {`\
`     nr -= div*dec;`\
`   }`\
` }`

}

void lcdWriteNumber(int nr) {

` int value = nr;`

` if (value < 0) {`\
`   lcdWrite('-', true);`\
`   value = - nr;`\
` }`

` int digits = estimateDigits(value);`\
` lcdWriteNumber(value, digits);`

}

void lcdHandler(void) {

` if (lcdInitialized == false) {`\
`   lcdInitialize();`\
`   lcdClear();`\
` }`

` lcdPosition(0, 8);`\
` lcdWriteNumber((int) ldr);`

} </code>

### 3 buttons

#### Description

These buttons are in a 'ladder' configuration meaning they only actually use 1 pin, A2, to implement all 3 buttons! Very generally speaking when one button is pressed something like 4/5 of voltage is read across the pin, when a different button is pressed 3/5 of voltage is read across pin, when third 2/5 of voltage is read, if 2 buttons are pressed then some combination of the 2 voltages is read! This means you can not only test for 1 of the 3 buttons to be pressed, but you could check to see if 2 or 3 or all 3 buttons were pressed even though they're connected to one pin!

#### Code

This code is very basic and simply adapts the arduino analog input, analog output, serial output example and changes the Analog input pin to match our pin, A2.

### Potentiometer

#### Description

A potentiometer is simply a resistor that we can manually vary the resistance of. Potentiometers are everywhere. The knob on your stereo is a potentiometer that controls the volume! Our potentiometer is connected internally to A1 of the Arduino.

#### Code

The following code simply adapts the Arduino analog input, analog output, serial output example to use the appropriate analog pin, A1. <code> /\*

` Analog input, analog output, serial output`\
\
`Reads an analog input pin, maps the result to a range from 0 to 255`\
`and uses the result to set the pulsewidth modulation (PWM) of an output pin.`\
`Also prints the results to the serial monitor.`\
\
`The circuit:`\
`* potentiometer connected to analog pin 0.`\
`  Center pin of the potentiometer goes to the analog pin.`\
`  side pins of the potentiometer go to +5V and ground`\
`* LED connected from digital pin 9 to ground`\
\
`created 29 Dec. 2008`\
`Modified 4 Sep 2010`\
`by Tom Igoe`\
\
`This example code is in the public domain.`\
\
`*/`

// These constants won't change. They're used to give names // to the pins used: const int analogInPin = A1; // Analog input pin that the potentiometer is attached to const int analogOutPin = 9; // Analog output pin that the LED is attached to

int sensorValue = 0; // value read from the pot int outputValue = 0; // value output to the PWM (analog out)

void setup() {

` // initialize serial communications at 9600 bps:`\
` Serial.begin(9600); `

}

void loop() {

` // read the analog in value:`\
` sensorValue = analogRead(analogInPin);            `\
` // map it to the range of the analog out:`\
` outputValue = map(sensorValue, 0, 1023, 0, 255);  `\
` // change the analog out value:`\
` analogWrite(analogOutPin, outputValue);           `

` // print the results to the serial monitor:`\
` Serial.print("sensor = " );                       `\
` Serial.print(sensorValue);      `\
` Serial.print("\t output = ");      `\
` Serial.println(outputValue);   `

` // wait 10 milliseconds before the next loop`\
` // for the analog-to-digital converter to settle`\
` // after the last reading:`\
` delay(10);                     `

} </code>

### Relays

#### Description

The relays are model XXX. Relays are used to switch more power hungry things on and off. Small leds can simply be connected up to the arduino pins directly, but rather large LEDS or motors might draw too much current and need to be switched through a relay. These relays are exposed on the 6 pin right angle header in the upper left. The pin closest to the edge of the board is pin 1, and the furthest in is considered pin 6.

- Pin1 - Gnd
- Pin2 - Relay 1 Side 1
- Pin3 - Relay 1 Side 2
- Pin4 - Relay 2 Side 1
- Pin5 - Relay 2 Side 2
- Pin6 - 5V

What you need to understand about these relays is that they are NOT connected to voltage internally by the board. You need to INPUT power(Pin6) to one of the sides of the relay (Pin5), then connect the other side of the relay(Pin4) to your load (a resistor, motor, etc) and then the other side of that load to GND.

`XXX Picture here`

XXX add datasheet and relay image here.

#### Code

The relay code is unchanged and should be found under the pebble examples.

#### Testing and Debugging

When a relay switches it generally makes a little click sound so you should be able to hear that if your relay is working properly.

## Optional Features

### LCD

#### Description

The lcd screen, when plugged in correctly, should hang over and 'block' access to the electronics and board underneath. Also note the potentiometer. The pot controls the contrast of the characters on screen and should generally be set nearly all the way clockwise. The LCD we use is purchased from [Adafruit](http://www.adafruit.com/index.php?main_page=product_info&cPath=37&products_id=181), or you can stop contact us.

Please see pictures below: XXX Insert Picture of pot turned right, XXX insert picture of lcd correct placement

#### Code

The LCD code remains unchanged from the pebble display example.

### Xbee

#### Description

The xbee module allows communication with other devices through the zigbee protocol which is somewhat similar to bluetooth.

#### Code

We currently have no code to show off this device.

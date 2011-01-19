This is code used in teaching an Arduino workshop. It combines a 16x2 character LCD, an IR LED, an IR photodetector, and a piezo speaker to form an electronic "pet" similar to a Tamogachi.

For assistance with this code, please post in the HeatSync Google Group in this thread: [HSL Thread: Arduino IR Pet (workshop code)](http://groups.google.com/group/heatsynclabs/browse_thread/thread/72528934bf0a1662)

## Assembly

(Assembly instructions/photos still being posted here, thanks for your patience.)

Photo: ![Arduino_IR_Pet_Photo.JPG](files/Arduino_IR_Pet_Photo.JPG)

Sorry for the blurriness, but this should give you an idea of how to construct the IR Pet (along with the comments at the top of the code below.)

## Libraries

Download and extract this ZIP into your arduino app's libraries folder-- resulting file structure should look like arduino\libraries\tone\tone.h

[Tone.zip](files/Tone.zip)

*Tone.zip*

## Code

    /*
      HeatSync Labs IR Pet
      
     Demonstrates the use of a 16x2 LCD display, IR emitters and sensors, Piezo 
     
      The circuit:
     * LCD PWR- pin to GND
     * LCD PWR+ pin to +5V
     * LCD RS pin to digital pin 7
     * LCD Enable pin to digital pin 8
     * LCD D4 pin to digital pin 9
     * LCD D5 pin to digital pin 10
     * LCD D6 pin to digital pin 11
     * LCD D7 pin to digital pin 12
     * Potentiometer:
     *  ends to +5V and ground
     *  center ("wiper") to LCD VO pin (LCD pin 3)
     * Photodetector:
     *  connect to digital pin 3 with a resistor in between, and GND 
     * LED: 
     *  connect to digital pin 2 with a resistor in between, and GND
     * Piezo Speaker:
     *  connect to digital pin 5 and GND
     
      Operation: 
     * Once powered on and this code uploaded, the LCD should show a HeatSync Labs splash screen followed by health and happiness gauges.
     * If you can't see anything on the LCD, try adjusting the potentiometer. If you see garbled stuff, press the reset button on the arduino or double-check your wiring.
     * To increase the pet's happiness, "feed" its IR photodetector with infrared light (possibly from its own infrared LED, or a remote control, or another pet's LED.)
     * To increase the pet's health, "clean up" after it by making a loud noise into the piezo (try blowing on the piezo, it can act like a really weak microphone!)
     * If you get continuous heart or smiley animations and noises, some of your sensors may be stuck on (i.e. the IR photodetector) or they might be wired incorrectly (my photodetector produces a 0 when active and 1 when inactive, for example.)
     
     */

    // include the LCD library code:
    #include <LiquidCrystal.h>
    // include the RTTTL Tone (music) library:
    #include <Tone.h>

    /*
     * This section for music settings
     */
    Tone tone1;

    #define OCTAVE_OFFSET 0

    int notes[] = { 0,
    NOTE_C4, NOTE_CS4, NOTE_D4, NOTE_DS4, NOTE_E4, NOTE_F4, NOTE_FS4, NOTE_G4, NOTE_GS4, NOTE_A4, NOTE_AS4, NOTE_B4,
    NOTE_C5, NOTE_CS5, NOTE_D5, NOTE_DS5, NOTE_E5, NOTE_F5, NOTE_FS5, NOTE_G5, NOTE_GS5, NOTE_A5, NOTE_AS5, NOTE_B5,
    NOTE_C6, NOTE_CS6, NOTE_D6, NOTE_DS6, NOTE_E6, NOTE_F6, NOTE_FS6, NOTE_G6, NOTE_GS6, NOTE_A6, NOTE_AS6, NOTE_B6,
    NOTE_C7, NOTE_CS7, NOTE_D7, NOTE_DS7, NOTE_E7, NOTE_F7, NOTE_FS7, NOTE_G7, NOTE_GS7, NOTE_A7, NOTE_AS7, NOTE_B7
    };

      char *songA = "MissionImp:d=16,o=6,b=95:32d,32d#,32d,32d#,32d,32d#,32d,32d#,32d,32d,32d#,32e,32f,32f#,32g,g,8p";
      char *songB = "shorter_r2d2:d=4,o=5,b=450:16c#7,16g#7,16f6,16a#7,16e7,16g#8,16e8,16g#6,16g7,16c#7,16g7,16f#8,16c#7,16f#6,16f8,16g#7,16g6,16a8,16c#8,16g6,16f#8,16g7,16f8,16a#6,16f#8,16d8,16g7,16g8,16c8,16g#6,16a8";

    #define isdigit(n) (n >= '0' && n <= '9')

    /*
     * This section for custom characters on the LCD
     */
     
    // blank 
    byte blank[8] = {   B00000, B00000, B00000, B00000, B00000, B00000, B00000, B00000};
    // smiley
    byte smiley[8] = {  B00000, B01010, B01010, B00000, B10001, B10001, B01110, B00000};
    // heart
    byte heart[8] = {   B00000, B01010, B10101, B10001, B10001, B01010, B00100, B00000};
    // chip
    byte chip[8] = {    B01110, B11111, B01110, B11111, B01110, B11111, B01110, B11111};
    // heatsync logo
    byte hsl_toplft[8] = {  B00000, B00000, B00000, B00011, B00100, B00100, B01001, B01011};
    byte hsl_toprt[8] = {   B00000, B00000, B01010, B11010, B00101, B00111, B00010, B00011};
    byte hsl_btmrt[8] = {   B11010, B10110, B01111, B11001, B01100, B01110, B00000, B00000};
    byte hsl_btmlft[8] = {  B01000, B00100, B01100, B01011, B00010, B00110, B00000, B00000};

    /*
     * This section for public variables used for the program runtime
     */

    LiquidCrystal lcd(7,8,9,10,11,12); // initialize the library with the numbers of the interface pins
    int sensorValue = 0;  // variable to store the value coming from the sensor
    int ledPin = 2;    // select the output pin for the IR LED
    int sensorPin = 3;    // select the input pin for the IR sensor
    int speakerPin = 5;   // select the output pin for the speaker
    int speakerValue = 0;  // variable to store whether the button is currently pushed
    int buttonPin = 4;    // select the input pin for the button
    int health = 50;      // starting "health"
    int happy = 50;       // starting "happiness"
    int loopCounter = 0;  // just a counter to space out events within the loop() below

    void setup() {
      // set up the LCD's number of columns and rows: 
      lcd.begin(16, 2);
      // set up the speaker's pin number
      tone1.begin(speakerPin);
      // set up serial communication (back to the PC via USB for debugging)
      Serial.begin(9600);
      // declare the sensorPin as an INPUT:
      pinMode(sensorPin, INPUT);  
      // write the sensorPin high
      digitalWrite(sensorPin, HIGH); 
      // declare the ledPin as an OUTPUT:
      pinMode(ledPin, OUTPUT); 

      lcd.createChar(0, blank);
      lcd.createChar(1, smiley);
      lcd.createChar(2, heart);
      lcd.createChar(3, chip);
      lcd.createChar(4, hsl_toplft);
      lcd.createChar(5, hsl_toprt);
      lcd.createChar(6, hsl_btmrt);
      lcd.createChar(7, hsl_btmlft);
      lcd.begin(16, 2);

      showBootScreen();
      delay(2000);
      lcd.clear();
    }

    void loop() {
      loopCounter++;
      if(loopCounter > 400)
      {
        adjustHealth(-1);
        loopCounter = 0;
        makeDirty();
      }
      
      if(loopCounter % 100 == 0)
      {
        adjustHappy(-1); 
      }
      
      
      showHealth();
      showHappy();
      
      digitalWrite(ledPin, HIGH); 
      
      // read the value from the sensor:
      sensorValue = digitalRead(sensorPin); 
      if(sensorValue == 0)  // for some reason IR transistors are 0 when light and 1 when dark?
      {
        Serial.println("Sensor");
        feedChips();
      }  
     
      // declare the speakerPin as an INPUT:
      pinMode(speakerPin, INPUT);  
      delay(100);    
      speakerValue = digitalRead(speakerPin);
      if(speakerValue == 1)
      {
        Serial.println("Speaker");
        cleanUp();
      }
      delay(100);    
      
    }

    void makeDirty() {
      lcd.setCursor(random(4, 11) ,random(0, 2));
      lcd.print(".");
      delay(100);
    }

    void cleanUp() {
      play_rtttl(songA);
      
      adjustHealth(6);
      writeAt(2,0,0);
      delay(100);
      writeAt(0,0,0);
      writeAt(2,1,1);
      delay(100);
      writeAt(0,1,1);
      writeAt(2,2,0);
      delay(100);
      writeAt(0,2,0);
      writeAt(2,3,1);
      delay(100);
      writeAt(0,3,1);
      writeAt(0,4,0);
      writeAt(0,5,0);
      writeAt(0,6,0);
      writeAt(0,7,0);
      writeAt(0,8,0);
      writeAt(0,9,0);
      writeAt(0,10,0);
      writeAt(0,11,0);
      writeAt(0,12,0);
      writeAt(0,4,1);
      writeAt(0,5,1);
      writeAt(0,6,1);
      writeAt(0,7,1);
      writeAt(0,8,1);
      writeAt(0,9,1);
      writeAt(0,10,1);
      writeAt(0,11,1);
      writeAt(0,12,1);
    }

    void feedChips() {
      
      play_rtttl(songB);

      adjustHappy(8);
      writeAt(3,0,0);
      delay(100);
      writeAt(0,0,0);
      writeAt(3,1,1);
      delay(100);
      writeAt(0,1,1);
      writeAt(3,2,0);
      delay(100);
      writeAt(0,2,0);
      writeAt(3,3,1);
      delay(100);
      writeAt(0,3,1);
    }

    void writeAt(int character, int x, int y) {
      lcd.setCursor(x, y);
      lcd.write(character); 
    }

    void adjustHealth(int diff){
      if(health > 0)
      {
        health = health + diff;
      }
      if(health > 99)
      {
        health = 99; 
      }
    }

    void adjustHappy(int diff){
      if(happy > 1 || diff > 0)
      {
        happy = happy + diff;
      }
      if(happy > 99)
      {
        happy = 99; 
      }
    }

    void showHappy() {
      lcd.setCursor(13, 1);
      lcd.write(1);
      lcd.print(happy);
      lcd.write(0);
    }

    void showHealth() {
      lcd.setCursor(13, 0);
      lcd.write(2);
      lcd.print(health);
      lcd.write(0);
    }

    void showBootScreen(){
      lcd.setCursor(0, 0);
      lcd.write(4);
      lcd.write(5);
      lcd.setCursor(0, 1);
      lcd.write(7);
      lcd.write(6);

      lcd.setCursor(3, 0);
      lcd.print("HeatSync Labs");
      
      lcd.setCursor(3, 1);
      lcd.print("BootROM v1337"); 
    }

    void play_rtttl(char *p)
    {
      // Absolutely no error checking in here

      byte default_dur = 4;
      byte default_oct = 6;
      int bpm = 63;
      int num;
      long wholenote;
      long duration;
      byte note;
      byte scale;

      // format: d=N,o=N,b=NNN:
      // find the start (skip name, etc)

      while(*p != ':') p++;    // ignore name
      p++;                     // skip ':'

      // get default duration
      if(*p == 'd')
      {
        p++; p++;              // skip "d="
        num = 0;
        while(isdigit(*p))
        {
          num = (num * 10) + (*p++ - '0');
        }
        if(num > 0) default_dur = num;
        p++;                   // skip comma
      }

      //Serial.print("ddur: "); Serial.println(default_dur, 10);

      // get default octave
      if(*p == 'o')
      {
        p++; p++;              // skip "o="
        num = *p++ - '0';
        if(num >= 3 && num <=7) default_oct = num;
        p++;                   // skip comma
      }

      //Serial.print("doct: "); Serial.println(default_oct, 10);

      // get BPM
      if(*p == 'b')
      {
        p++; p++;              // skip "b="
        num = 0;
        while(isdigit(*p))
        {
          num = (num * 10) + (*p++ - '0');
        }
        bpm = num;
        p++;                   // skip colon
      }

      //Serial.print("bpm: "); Serial.println(bpm, 10);

      // BPM usually expresses the number of quarter notes per minute
      wholenote = (60 * 1000L / bpm) * 4;  // this is the time for whole note (in milliseconds)

      //Serial.print("wn: "); Serial.println(wholenote, 10);

      // now begin note loop
      while(*p)
      {
        // first, get note duration, if available
        num = 0;
        while(isdigit(*p))
        {
          num = (num * 10) + (*p++ - '0');
        }
        
        if(num) duration = wholenote / num;
        else duration = wholenote / default_dur;  // we will need to check if we are a dotted note after

        // now get the note
        note = 0;

        switch(*p)
        {
          case 'c':
            note = 1;
            break;
          case 'd':
            note = 3;
            break;
          case 'e':
            note = 5;
            break;
          case 'f':
            note = 6;
            break;
          case 'g':
            note = 8;
            break;
          case 'a':
            note = 10;
            break;
          case 'b':
            note = 12;
            break;
          case 'p':
          default:
            note = 0;
        }
        p++;

        // now, get optional '#' sharp
        if(*p == '#')
        {
          note++;
          p++;
        }

        // now, get optional '.' dotted note
        if(*p == '.')
        {
          duration += duration/2;
          p++;
        }
      
        // now, get scale
        if(isdigit(*p))
        {
          scale = *p - '0';
          p++;
        }
        else
        {
          scale = default_oct;
        }

        scale += OCTAVE_OFFSET;

        if(*p == ',')
          p++;       // skip comma for next note (or we may be at the end)

        // now play the note

        if(note)
        {
         // Serial.print("Playing: ");
          //Serial.print(scale, 10); Serial.print(' ');
          //Serial.print(note, 10); Serial.print(" (");
          //Serial.print(notes[(scale - 4) * 12 + note], 10);
          //Serial.print(") ");
          //Serial.println(duration, 10);
          tone1.play(notes[(scale - 4) * 12 + note]);
          delay(duration);
          tone1.stop();
        }
        else
        {
          //Serial.print("Pausing: ");
          //Serial.println(duration, 10);
          delay(duration);
        }
      }
    }

## Parts List

NPN Transistor:\
<http://www.mouser.com/ProductDetail/Fairchild-Semiconductor/KSC3503DSTU/?qs=sGAEpiMZZMtn7beagP2hIRaqh2YBECe1Yqoz3NTyz48%3d>

IR Emitter:\
<http://mouser.com/search/ProductDetail.aspx?qs=8T8Vkz9kCnmXLF3JXFC7QQ==>

IR Receiver:\
<http://mouser.com/search/ProductDetail.aspx?qs=WxFF5lh7QM1L5Vm%2btOeRTw==>

Standard LCD 16x2 + Extras(White on Blue):\
<http://www.adafruit.com/index.php?main_page=product_info&cPath=37&products_id=181>

Piezo Buzzer - PS1240:\
<http://www.adafruit.com/index.php?main_page=product_info&cPath=35&products_id=160>

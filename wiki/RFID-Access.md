Attempt at creating an RFID access control shield for Arduino, both for doors and for pieces of equipment.

Video of current state: <http://www.twitvid.com/O548T>

Todo:

- piezo/led feedback
- relays for door strike or possible 120v on/off control
- signin/signout with timer for tracking hourly usage
- ethernet/wifi connection to HTTP server
  - authentication using server
  - feedback to HTTP server (signins/signouts, hourly usage?)

<!-- -->

    // RFID Access Control
    // By Will Bradley
    // Work in progress. Currently only reads an RFID card and outputs authorized/unauthorized messages.
    // Uses Parallax RFID unit on pins 2,3,4 and Adafruit 2x16 LCD on pins 7-12.

    // Modified by Worapoht K.
    #include <SoftwareSerial.h>
    // include LCD library code:
    #include <LiquidCrystal.h>

    int  val = 0; 
    String code = ""; 
    int bytesread = 0; 
    String allowed = "0F03039364";
    String allowedName = "Gordon Freeman";
    String strTag = "TAG ";
    String strAuth = "Authorized ";
    String strUnauth = "Unauthorized ";

    // initialized RFID reader
    #define rxPin 4  // RFID reader SOUT pin connected to Serial RX pin at 2400bps 
    #define txPin 3
    #define enablePin 2

    // initialize LCD library with the numbers of the interface pins
    LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

    void setup()
    { 
      Serial.begin(2400);  // Hardware serial for Monitor 2400bps

      pinMode(2,OUTPUT);       // Set digital pin 2 as OUTPUT to connect it to the RFID /ENABLE pin 
      digitalWrite(2, LOW);    // Activate the RFID reader 
      
      // set up the LCD's number of columns and rows: 
      lcd.begin(16, 2);
      // Print a blank message to the LCD.
      lcd.print("");
    }

    void loop()
    { 
      SoftwareSerial RFID = SoftwareSerial(rxPin,txPin); 
      RFID.begin(2400);

      char tempCode[10];
      
      if((val = RFID.read()) == 10)
      {   // check for header 
        bytesread = 0; 
        while(bytesread<10)
        {  // read 10 digit code 
          val = RFID.read(); 
          if((val == 10)||(val == 13))
          {  // if header or stop bytes before the 10 digit reading 
            break;                       // stop reading 
          } 
          tempCode[bytesread]
          = val;      // add the digit    

          bytesread++;                   // ready to read next digit  
        } 
        
        code.concat(tempCode);

        if(bytesread == 10)
        {  // if 10 digit read is complete 
          Serial.print(strTag.concat(code));   // possibly a good TAG 
          
          if(code.substring(0,10) == allowed) {
            lcdPrintln(strAuth, 0);
            lcdPrintln(allowedName, 1);
            Serial.println(code);
            delay(1000);
            lcdClear();
          } else {
            lcdPrintln(strUnauth, 0);
            Serial.println(code);
            delay(1000);
            lcdClear();
          }
              
        }
        
        code = "";
        bytesread = 0; 
        delay(500);                       // wait for a second
      } 
    } 

    void lcdPrintln(String message, int line) {
          Serial.println(message);
            
          // set the cursor to column 0, line 1
          // (note: line 1 is the second row, since counting begins with 0):
          lcd.setCursor(0, line);
          // print the number of seconds since reset:
          lcd.print(message);
    } 

    void lcdClear() {
         lcd.clear(); 
    }

// include libraries
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_PN532.h>

// define I2C communication
#define PN532_IRQ   (2)
#define PN532_RESET (3)

// define the nfc shield
Adafruit_PN532 nfc(PN532_IRQ, PN532_RESET);

void setup() {
  Serial.begin(115200);
//  Serial.println("is this gonna work");                                                                   

  nfc.begin();

// check if shield is properly connected
  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata) {
//    Serial.print("nope");
    while (1); // halt
  }
  
//Serial.println("working!");
}


void loop() {
  uint8_t success;
  uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 };  // Buffer to store the returned UID
  uint8_t uidLength;                        // Length of the UID (4 or 7 bytes depending on ISO14443A card type)
    
  // Wait for an ISO14443A type cards (Mifare, etc.).  When one is found
  // 'uid' will be populated with the UID, and uidLength will indicate
  // if the uid is 4 bytes (Mifare Classic) or 7 bytes (Mifare Ultralight)
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, uid, &uidLength);
  
  if (success) {
    Serial.println("yay");
    delay(5000);
  }
  else
      {
        Serial.println("fuck");
      }
}

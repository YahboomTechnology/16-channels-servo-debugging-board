#include <Wire.h>
#define I2C_ADDR                    0x2D
/****************************
     Register setting function
*****************************/
bool I2CWrite(unsigned char reg_addr,unsigned char date)
{
    Wire.beginTransmission(I2C_ADDR);  //Send Device address
    Wire.write(reg_addr);              
    Wire.write(date);                  //Send the angle to be set
    if(Wire.endTransmission()!=0)      //Send end signal
      {
          delay(10);
          return false;
      }
      delay(10);
      return true;  
}

void setup() {
  // put your setup code here, to run once:
  Wire.begin(); 
}

void loop() {
  // put your main code here, to run repeatedly:
  I2CWrite(1,0);//Set servo S1 to 0
  delay(2000);
  I2CWrite(1,180);//Set servo S1 to 180
  delay(2000);
}

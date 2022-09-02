#include <avr/io.h>
#include <stdbool.h>
#include <util/delay.h>
int main (void)
{

 bool W=0,X=0,Y=0,Z=0,G=0;
 DDRB =  0b00000001;
 DDRD =  0b11000011;
 PORTD = 0b00111100;
while(1){
Z = (PIND & (1 << PIND5)) == (1 << PIND5);
Y = (PIND & (1 << PIND4)) == (1 << PIND4);
X = (PIND & (1 << PIND3)) == (1 << PIND3);
W = (PIND & (1 << PIND2)) == (1 << PIND2);
G = (!Y&&Z)||(!W&&Y&&X)||(W&&Y);
PORTB |= (G << 0);
}
return 0;
}



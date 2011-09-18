/*
 * Firmware running on MSP430 Launchpad.
 * Waits for receipt of a byte over the back-channel UART
 */

#include <msp430.h>

#define RXBIT ((P1IN >> 2) & 1)

void delay()
{
        volatile unsigned int i = 0xffff;
        i = i / 2;
        while(i--);
}

void wait_for_rx_change()
{
        unsigned char b;
        b = RXBIT;
        while(RXBIT == b);
        delay(); // wait for transmission to be over
}

void init()
{
        WDTCTL = WDTPW + WDTHOLD;
        P1DIR = 1; // P1.0 output
        P1OUT = 0;
}
        
main()
{
        init();
        while(1) {
                wait_for_rx_change();
                P1OUT ^= 1;
        }
}

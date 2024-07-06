#include <singleLEDLibrary.h>
#include <IRremote.h>

/*
BIKE LED
This controls 2 relays attached to LEDs. 
It relies on 3 way switch to flicker the left or right LED.
There is a HAZARD state which flickers both LEDS, but disables changing via the switch.

You can change the brightness, frequency and state using an IR remote.

When the sequence LEFT MID LEFT MID RIGHT MID is read within 2.75s, 
it enters HAZARD mode.
*/
enum STATE
{
  ON,
  LEFT,
  RIGHT,
  HAZARD
};

STATE curr_state;
int freq_ind = 5;
STATE state_seq[] = {ON, ON, ON, ON, ON, ON};
unsigned long milli_seq[] = {0, 2500, 5000, 7500, 10000, 12500};
const int freq_arr[] = {5000, 3000, 2000, 1000, 500, 300, 150, 50};
const int IR_PIN = 9;
const int KEY_LEFT_PIN_GND = 11;
const int KEY_RIGHT_PIN_GND = 7;
const int IR_LEFT_PIN = 3;
const int IR_RIGHT_PIN = 5;
const boolean debug_mode = true;
sllib IR_LEFT = sllib(IR_LEFT_PIN);
sllib IR_RIGHT = sllib(IR_RIGHT_PIN);

const unsigned long REMOTE_1 = 0xBA45FF00;
const unsigned long REMOTE_2 = 0xB946FF00;
const unsigned long REMOTE_3 = 0xB847FF00;
const unsigned long REMOTE_4 = 0xBB44FF00;
const unsigned long REMOTE_5 = 0xBF40FF00;
const unsigned long REMOTE_6 = 0xBC43FF00;
const unsigned long REMOTE_7 = 0xF807FF00;
const unsigned long REMOTE_8 = 0xEA15FF00;
const unsigned long REMOTE_9 = 0xF609FF00;
const unsigned long REMOTE_STAR = 0xE916FF00;
const unsigned long REMOTE_0 = 0xE619FF00;
const unsigned long REMOTE_HASHTAG = 0xF20DFF00;
const unsigned long REMOTE_UP = 0xE718FF00;
const unsigned long REMOTE_DOWN = 0xAD52FF00;
const unsigned long REMOTE_LEFT = 0xF708FF00;
const unsigned long REMOTE_RIGHT = 0xA55AFF00;
const unsigned long REMOTE_OK = 0xE31CFF00;

//+=============================================================================
// Configure the Arduino
//
void setup() {
  Serial.begin(9600);
  pinMode(KEY_LEFT_PIN_GND, INPUT_PULLUP);
  pinMode(KEY_RIGHT_PIN_GND, INPUT_PULLUP);
  if (debug_mode) {
    log_debug(String(KEY_LEFT_PIN_GND) + "pin is left indicator\n");
    log_debug(String(KEY_RIGHT_PIN_GND) + "pin is right indicator\n");
    log_debug("Enabling IRin...\n");
  }
  
  // Start the receiver and if not 3. parameter specified, take LED_BUILTIN pin from the internal boards definition as default feedback LED
  IrReceiver.begin(IR_PIN, ENABLE_LED_FEEDBACK);

  Serial.print("Ready to receive IR signals of protocols: \n");
//  printActiveIRProtocols(&Serial);
  log_debug(String(IR_PIN) + "pin receiving IR\n");

  setState(ON);
  IR_LEFT.setOnSingle();
  IR_RIGHT.setOnSingle();
  IR_LEFT.update();
  IR_RIGHT.update();
  log_debug("left right indicator pin on");
}

//+=============================================================================
// Functions
//
void log_debug(String str) {
  if (debug_mode) Serial.print(str);
}

String enumToString(STATE state) {
  if (state == ON) {
    return "ON";
  } else if (state == LEFT) {
    return "LEFT";
  } else if (state == RIGHT) {
    return "RIGHT";
  } else if (state == HAZARD) {
    return "HAZARD";
  }
}

void setBrightnessBothPin(int val) {
  IR_LEFT.setBrightness(val);
  IR_RIGHT.setBrightness(val);
}

void setState(STATE state) {
  curr_state = state;
  log_debug("State to " + enumToString(curr_state) + "\n");
}

void doStateAction() {
  IR_LEFT.update();
  IR_RIGHT.update();
  switch (curr_state) {
    case (LEFT):
      IR_LEFT.setBreathSingle(freq_arr[freq_ind]);
      IR_RIGHT.setOnSingle();
      break;
    case (RIGHT):
      IR_RIGHT.setBreathSingle(freq_arr[freq_ind]);
      IR_LEFT.setOnSingle();
      break;
    case (HAZARD):
      IR_LEFT.setBreathSingle(freq_arr[freq_ind]);
      IR_RIGHT.setBreathSingle(freq_arr[freq_ind]);
      break;
    default:
      IR_LEFT.setOnSingle();
      IR_RIGHT.setOnSingle();
  }
}

void applyHazardState(STATE state) {
  for (int i = 1; i <= 5; i++) {
    state_seq[i-1] = state_seq[i];
    milli_seq[i-1] = milli_seq[i];
  }
  state_seq[5] = state;
  milli_seq[5] = millis();
  if ((milli_seq[5] - milli_seq[0]) <= 2750 && 
    state_seq[0] == LEFT &&
    state_seq[1] == ON &&
    state_seq[2] == LEFT &&
    state_seq[3] == ON &&
    state_seq[4] == RIGHT &&
    state_seq[5] == ON) {
      setState(HAZARD);
  }
}

//+=============================================================================
// The repeating section of the code
//
void loop() {
  if (IrReceiver.decode()) {  // Grab an IR code
    // Print a short summary of received data
    if (IrReceiver.decodedIRData.flags & IRDATA_FLAGS_WAS_OVERFLOW) {
      Serial.println("Overflow detected");
    } else {
      IrReceiver.printIRResultShort(&Serial);
      IrReceiver.resume();                            // Prepare for the next value
      if (IrReceiver.decodedIRData.decodedRawData == REMOTE_1) {
        log_debug("Brightness to 10%\n");
        setBrightnessBothPin(10);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_2) {
        log_debug("Brightness to 20%\n");
        setBrightnessBothPin(20);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_3) {
        log_debug("Brightness to 30%\n");
        setBrightnessBothPin(30);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_4) {
        log_debug("Brightness to 40%\n");
        setBrightnessBothPin(40);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_5) {
        log_debug("Brightness to 50%\n");
        setBrightnessBothPin(50);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_6) {
        log_debug("Brightness to 60%\n");
        setBrightnessBothPin(60);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_7) {
        log_debug("Brightness to 70%\n");
        setBrightnessBothPin(70);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_8) {
        log_debug("Brightness to 80%\n");
        setBrightnessBothPin(80);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_9) {
        log_debug("Brightness to 90%\n");
        setBrightnessBothPin(90);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_0) {
        log_debug("Brightness to 0%\n");
        setBrightnessBothPin(0);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_STAR) {
        log_debug("Brightness to 100%\n");
        setBrightnessBothPin(100);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_HASHTAG) {
        setState(HAZARD);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_OK) {
        setState(ON);
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_UP) {
        int curr_brightness = IR_LEFT.getBrightness();
        if (curr_brightness <= 90) {
          log_debug("Brightness UP to " + String(curr_brightness + 10) + "%\n");
          setBrightnessBothPin(curr_brightness+10);
        }
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_DOWN) {
        int curr_brightness = IR_LEFT.getBrightness();
        if (curr_brightness >= 0) {
          log_debug("Brightness UP to " + String(curr_brightness - 10) + "%\n");
          setBrightnessBothPin(curr_brightness-10);
        }
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_LEFT) {
        if (freq_ind > 0) {
          freq_ind--;
          log_debug("Frequency lowered to " + String(freq_arr[freq_ind]) + "Hz");
        }
      } else if (IrReceiver.decodedIRData.decodedRawData == REMOTE_RIGHT) {
        if (freq_ind < (sizeof(freq_arr) / sizeof(freq_arr[0])) - 1) {
          freq_ind++;
          log_debug("Frequency increased to " + String(freq_arr[freq_ind]) + "Hz");
        }
      }
    }
  }
  if ((LEFT == curr_state || RIGHT == curr_state) && HIGH == digitalRead(KEY_LEFT_PIN_GND) && HIGH == digitalRead(KEY_RIGHT_PIN_GND)) {
    setState(ON);
    applyHazardState(ON);
  } else if (ON == curr_state && LOW == digitalRead(KEY_LEFT_PIN_GND)) {
    setState(LEFT);
    applyHazardState(LEFT);
  } else if (ON == curr_state && LOW == digitalRead(KEY_RIGHT_PIN_GND)) {
    setState(RIGHT);
    applyHazardState(RIGHT);
  }
  doStateAction();
}

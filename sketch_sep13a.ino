
const uint8_t PIN_JOY_Y = A1;
const uint8_t PIN_JOY_SW = 7;

const int DEADZONE = 90;  // <-- put YOUR number from step 2 here
const uint8_t W = 36;
const uint8_t H = 14;          // court height, in rows
const uint8_t PADDLE_H = 3;    // paddle height, in rows
const float PADDLE_SPD = 1.7;  // max rows moved per frame
const unsigned long FRAME_MS = 90;
const float SPIN = 0.8;
const float SPEED_UP = 1.05;
const float BALL_MAX = 1.20;

int joyCenterY = 512;
float padY = (H - PADDLE_H) / 2.0;
int score = 0;
int misses = 0;

unsigned long lastFrame = 0;
bool lastSW = HIGH;
int pressCount = 0;
long loopCount = 0;

float ballX, ballY, ballVX, ballVY;
const float BALL_SPD = 0.55;

unsigned long lastPressMs = 0;

char row[W + 1];

void setup() {
  Serial.begin(250000);
  pinMode(PIN_JOY_SW, INPUT_PULLUP);

  row[W] = '\0';

  Serial.println("Calibrating -- hands OFF the stick...");
  delay(500);
  long sum = 0;
  for (uint8_t i = 0; i < 16; i++) {
    sum += analogRead(PIN_JOY_Y);
    delay(8);
  }
  joyCenterY = sum / 16;
  Serial.print("Center = ");
  Serial.println(joyCenterY);

  randomSeed(analogRead(A5));
  serveBall();
  lastFrame = millis();
}
void serveBall() {
  ballX = W / 2.0;
  ballY = H / 2.0;
  ballVX = (random(0, 2) ? 1 : -1) * BALL_SPD;
  ballVY = (random(0, 2) ? 1 : -1) * BALL_SPD * 0.6;
}

void updateBall() {
  ballX += ballVX;
  ballY += ballVY;

  if (ballY < 0) {
    ballY = 0;
    ballVY = -ballVY;
  }  // top
  if (ballY > H - 1) {
    ballY = H - 1;
    ballVY = -ballVY;
  }  // bottom
  if (ballX < 0) {
    ballX = 0;
    ballVX = -ballVX;
  }  // left (paddle later)
  if (ballX > W - 1) {
    ballX = W - 1;
    ballVX = -ballVX;
  }  // right

  if (ballX < 0) {
    int by = (int)(ballY + 0.5);
    int top = int(padY);

    if (by >= top && by < top + PADDLE_H) {
      ballX = 0;
      ballVX = -ballVX;

      float hit = (float)(by - top) / (float)(PADDLE_H - 1);

      ballVY = (hit - 0.5) * 2.0 * SPIN * fabs(ballVX);

      if (fabs(ballVX) < BALL_MAX) {
        ballVX *= SPEED_UP;
        ballVY *= SPEED_UP;
      }
      score++;
    } else {
      misses++;
      serveBall();
    }
  }
}


void loop() {
  loopCount++;

  bool sw = digitalRead(PIN_JOY_SW);
  if (lastSW == HIGH && sw == LOW) {
    pressCount++;
    serveBall();
  }
  lastSW = sw;

  if (millis() - lastFrame >= FRAME_MS) {
    lastFrame = millis();
    updatePaddle();
    updateBall();
    drawFrame();
  }
  if (lastSW == HIGH && sw == LOW && millis() - lastPressMs > 50) {
    pressCount++;
    lastPressMs = millis();
  }
}

void updatePaddle() {
  int raw = analogRead(PIN_JOY_Y);
  int offset = raw - joyCenterY;

  if (abs(offset) > DEADZONE) {
    // how far can the stick travel on THIS side of center?
    int span = (offset > 0) ? (1023 - joyCenterY) : joyCenterY;

    // turn deflection into a 0.0 - 1.0 amount, then into a speed
    float amount = (float)(abs(offset) - DEADZONE) / (float)(span - DEADZONE);
    if (amount > 1.0) amount = 1.0;

    float step = amount * PADDLE_SPD;
    padY += (offset > 0) ? step : -step;
  }

  if (padY < 0) padY = 0;
  if (padY > H - PADDLE_H) padY = H - PADDLE_H;
}

void drawFrame() {
  int top = (int)padY;

  int bx = (int)(ballX + 0.5);  // round, don't truncate
  int by = (int)(ballY + 0.5);

  if (bx < 0) bx = 0;          // NEVER index an array without
  if (bx > W - 1) bx = W - 1;  // knowing the index is in range
  if (by < 0) by = 0;
  if (by > H - 1) by = H - 1;

  Serial.println();
  Serial.print(" SCORE ");
  Serial.print(score);
  Serial.print(" Misses ");
  Serial.println(misses);

  drawBorder();
  for (uint8_t y = 0; y < H; y++) {
    memset(row, ' ', W);
    if (y >= top && y < top + PADDLE_H) row[0] = '#';
    if (y == by) row[bx] -= '0';
    Serial.print("  |");
    Serial.print(row);
    Serial.println('|');
  }
  drawBorder();
}
void drawBorder() {
  Serial.print(F(" +"));
  for (uint8_t i = 0; i < W; i++) Serial.print('-');
  Serial.println('+');
}
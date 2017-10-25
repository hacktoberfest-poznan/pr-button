# PR button
This repo contains script that was used to fire off lighting and audio effects after submitting a pull request during Hacktoberfest in Poznań.

## Sound effects
It takes all mp3/aif/wav files from sounds dir and plays them randomly.

## Lighting effects
Event held place in [Setapp](https://setapp.pl/) which has couple of smart lights by [FIBARO](https://www.fibaro.com/). Which provide a way to remotely control them through http endpoints. You'll need FIBARO api access with valid credentials. We used 3 lights and a default FIBARO strobe effect.

## Hardware
We used Raspberry Pi, but you can use any internet connected device with GPIO and audio output.

Simply connect a button to pin 18 and ground - that's it.

## Video
[![Example of use](https://img.youtube.com/vi/tBqrBtV4_34/0.jpg)](https://www.youtube.com/watch?v=tBqrBtV4_34)

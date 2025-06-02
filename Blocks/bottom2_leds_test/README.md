# Bottom2 LED Control

This folder contains example code and resources to control the RGB LEDs of the Bottom2 module for the M5Stack Core2.

## 📁 Contents

- `bottom2_led.py`: Python module to control the 10 RGB LEDs using the NeoPixel library.
- `Prova RGB.m5f2`: A UiFlow 2.0 project file for testing LED behavior.

## 🎯 Objective

Provide simple and reusable code to control the RGB LEDs of the Bottom2 module using either Python or UiFlow.

## 🧰 Requirements

- M5Stack Core2
- Bottom2 module (with 10 NeoPixel LEDs)
- Firmware: MicroPython compatible with NeoPixel (e.g., UIFlow firmware or custom MicroPython build)
- For `.m5f2` files: UiFlow 2.0 IDE

## 💡 Usage (Python)

```python
from bottom2_led import set_led, clear_all

# Turn LED 0 to red
set_led(0, 255, 0, 0)

# Clear all LEDs
clear_all()
```

## 🧪 Testing with UiFlow2.0
- Open UiFlow 2.0
-Import the project file Prova RGB.m5f2
-Upload the code to your device
## 📜 License

This project is licensed under the terms of the  
**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

You are free to:
- ✅ **Share** — copy and redistribute the material in any medium or format  
- ✅ **Adapt** — remix, transform, and build upon the material  
  as long as you follow the license terms:

### Conditions:
- 🧾 **Attribution** — You must give appropriate credit (Neus),  
  provide a link to the license, and indicate if changes were made.
- 🚫 **NonCommercial** — You may not use the material for commercial purposes.
- 🔁 **ShareAlike** — If you remix, transform, or build upon the material,  
  you must distribute your contributions under the same license.

🔗 [Read the full license](https://creativecommons.org/licenses/by-nc-sa/4.0/)

![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)

> 📦 This is part of the [neusmstack GitHub](https://github.com/neusmstack) educational projects.

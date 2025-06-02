#  🧩 Bloc personalitzat `GoPlus2 Test` per a UiFlow 2.0

Aquest directori conté un conjunt de fitxers destinats a la creació i prova d’un **bloc personalitzat per a UiFlow 2.0**, dissenyat específicament per controlar **servos i LEDs RGB** mitjançant el mòdul **GoPlus2** de M5Stack.

---

## 🎯 Objectiu del projecte

Aquest projecte té com a finalitat:

- ✅ Validar la comunicació amb el **GoPlus2** mitjançant el bus **I2C**.
- ✅ Controlar servos des de MicroPython o UiFlow.
- ✅ Il·luminar els LEDs del Bottom2 per a usos educatius.
- ✅ Crear una base per a futurs blocs personalitzats adaptats a l’aula.
- 🎓 Formar part d’un projecte didàctic per aplicar tecnologia M5Stack en entorns **STEAM** a secundària.

---

## 📂 Contingut de la carpeta

| Fitxer                      | Descripció                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `block.json`               | Fitxer de definició del bloc per a UiFlow 2.0 (estructura i paràmetres).   |
| `goplus2_block.py`         | Implementació en Python de la funcionalitat del bloc personalitzat.        |
| `icon.png`                 | Icona gràfica que representa el bloc dins UiFlow.                          |
| `move_motor_goplus2.py`    | Mòdul auxiliar per controlar servos via I2C al GoPlus2.                     |
| `test_servos_leds_goplus2.py` | Script de prova que activa servos i LEDs per validar el bloc.           |

---

## 🔧 Requisits de programari

- [UiFlow 2.0 IDE](https://uiflow2.m5stack.com/)
- Visual Studio Code (opcional, per editar fitxers Python)
- Firmware de M5Stack compatible amb UiFlow 2.0

---

## 🧱 Requisits de maquinari

- M5Stack Core2  
- Mòdul GoPlus2  
- Mòdul Bottom2 amb LEDs SK6812  
- Servos connectats als ports A/B/C del GoPlus2  
- Alimentació estable (Base magnètica o Power Bank)

---

## 🚀 Com fer-lo servir

### 1. Carregar el bloc a UiFlow 2.0

1. Entra a [UiFlow 2.0](https://uiflow2.m5stack.com/)
2. A la secció **Custom Blocks**, puja els fitxers:
   - `block.json`
   - `goplus2_block.py`
   - `icon.png`
3. Afegeix el bloc al teu projecte per controlar servos i LEDs.

### 2. Prova directa amb MicroPython

Pots provar el funcionament directament des de Thonny o VS Code:

```python
from move_motor_goplus2 import move_motor
move_motor(1, 90)  # Mou el servo 1 a 90 graus
🧩 Bloc personalitzat `GoPlus2 Test` per a UiFlow 2.0

Aquest directori conté un conjunt de fitxers destinats a la creació i prova d’un **bloc personalitzat per a UiFlow 2.0**, dissenyat específicament per controlar **servos i LEDs RGB** mitjançant el mòdul **GoPlus2** de M5Stack.

## 📂 Contingut de la carpeta

| Fitxer                      | Descripció                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `block.json`               | Fitxer de definició del bloc per a UiFlow 2.0 (estructura i paràmetres).   |
| `goplus2_block.py`         | Implementació en Python de la funcionalitat del bloc personalitzat.        |
| `icon.png`                 | Icona gràfica que representa el bloc dins UiFlow.                          |
| `move_motor_goplus2.py`    | Mòdul auxiliar per controlar servos via I2C al GoPlus2.                     |
| `test_servos_leds_goplus2.py` | Script de prova que activa servos i LEDs per validar el bloc.           |

## 🔧 Programari necessari

- **UiFlow 2.0 IDE** (https://uiflow2.m5stack.com/) per carregar i provar blocs personalitzats.
- **Visual Studio Code** amb extensió Python, per editar els fitxers `.py`.
- **Thonny** (opcional) per fer proves directes en MicroPython al M5Stack Core2.
- **GitHub** per gestionar el projecte i versionar el codi.

## 🚀 Com fer servir aquest projecte

### 1. Importar el bloc a UiFlow 2.0

1. Entra a [UiFlow 2.0](https://uiflow2.m5stack.com/).
2. Ves a la secció **Custom Blocks** i prem **Upload**.
3. Pujar els fitxers següents:
   - `block.json`
   - `goplus2_block.py`
   - `icon.png`
4. Després d'importar, apareixerà un nou bloc anomenat `test_servos_leds_goplus2`.

### 2. Exemple d’ús del bloc

- Arrossega el bloc `test_servos_leds_goplus2` a l’inici del programa.
- Connecta servos als ports A/B/C del **GoPlus2**.
- Els LEDs RGB del **Bottom2** s’activaran amb colors en seqüència.
- El programa mostrarà que el bloc funciona correctament.

### 3. Per a desenvolupadors: edició i proves manuals

- Obre `move_motor_goplus2.py` i `test_servos_leds_goplus2.py` amb **Visual Studio Code**.
- Connecta el **M5Stack Core2** per USB.
- Puja els scripts amb **Thonny** o un altre entorn MicroPython.
- Afegeix:

```python
from move_motor_goplus2 import move_motor
move_motor(1, 90)
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

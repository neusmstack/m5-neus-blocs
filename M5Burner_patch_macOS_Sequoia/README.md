# 🩹 M5Burner Patch for macOS Sequoia 15.5 (MacBook M4 compatibility)

This patch solves compatibility issues when launching **M5Burner** on a **MacBook Air with M4 chip** running **macOS Sequoia 15.5**.

## ⚠️ Problem

M5Burner does not launch correctly or fails to load firmware on systems using the new Apple Silicon M4 chip with macOS Sequoia (15.5 or later).

## ✅ Solution

Use this patch to replace internal configuration files inside the M5Burner app package.  
This fix was tested and confirmed working by Neus on a MacBook Air with the M4 chip.

## 📦 Contents

- `M5Burner_patch_files.zip`: contains the patched files you need to replace inside the M5Burner application.

## 🛠️ Instructions

1. Locate the **M5Burner.app** (usually in `/Applications`).
2. Right-click > **Show Package Contents**.
3. Go to: `Contents/Resources/app/`
4. Replace the existing files with the ones from the `.zip`.
5. Open Terminal and run the following command:
   ```bash
   xattr -cr /Applications/M5Burner.app

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


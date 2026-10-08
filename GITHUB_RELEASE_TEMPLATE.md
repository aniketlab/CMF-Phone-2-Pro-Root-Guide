# 📱 CMF Phone 2 Pro (Galaga) B4.1 Root & Fenrir Toolkit

**Release Version:** `v1.0.0-Galaga-B4.1`

This release contains all the necessary files to flash the supported firmware on your CMF Phone 2 Pro, root it securely via KernelSU/BakaSU, and successfully spoof the unlocked bootloader state using Fenrir.

---

## 📦 What's Included?

### 1. `Galaga_B4.1-260812-1729_FULL.zip` (Split Parts: `.001`, `.002`, etc.)
An easy-to-use, **All-In-One (AIO) Flashable Package** prepared by me. Due to GitHub's 2GB file limit, it has been split into multiple parts.
*   **How to extract:** Download all parts into the same folder. Right-click on the first file (`.zip.001`) and select **Extract Here** using [7-Zip](https://www.7-zip.org/) or WinRAR.
*   **What it does:** Extracts into a folder containing the full firmware and pre-configured flashing scripts (`flash_all.bat`). 
*   **Why use this:** Saves you from manually downloading and arranging split firmware files from the official archive. Just extract, run the script, and your phone will be on the perfectly supported firmware.

### 2. `init_boot.img`
*   **What it is:** The stock `init_boot` image extracted directly from the B4.1 firmware.
*   **Why use this:** If your phone is **already** on the `Galaga-B4.1-260812-1729` build, you do not need to download the massive FULL zip above. Simply download this tiny file, patch it in your Root Manager, and flash it to achieve root!

### 3. `galaga-fenrir.bin`
*   **What it is:** The official Fenrir bootloader spoofing payload specifically compiled for the CMF Phone 2 Pro (Galaga).
*   **Why use this:** Flash this to the `lk` partition (after rooting) to hide the annoying "Unlocked Bootloader" warning and achieve a spoofed `green/locked` verified boot state.

---

## 📖 How to Use
Please follow the comprehensive, step-by-step instructions detailed in the [Main README Guide](https://github.com/aniketlab/CMF-Phone-2-Pro-Root-Guide).

## 🤝 Credits & Alternatives
*   If you prefer downloading the raw, split firmware files yourself, you can find the official archive here: [Nothing Archive by spike0en](https://github.com/spike0en/nothing_archive/releases/tag/Galaga_B4.1-260812-1729).
*   Special thanks to the [Fenrir Project](https://github.com/R0rt1z2/fenrir) for making bootloader spoofing possible.

<div align="center">
  <img src="CMF_Phone_2_Pro_Cover_NoBg.png" width="500" alt="CMF Phone 2 Pro Cover">
  <h1>📱 CMF Phone 2 Pro (Galaga) — Complete Root & Bootloader Spoofing Guide</h1>
  <p>A professional A-to-Z guide for safely rooting your device and spoofing the unlocked bootloader state (using Fenrir).</p>
</div>

---

## 📱 Target Device & Firmware Details

Below is the specific firmware version this guide is built for. You **must** be on this exact build for the Fenrir bootloader spoofing to work flawlessly.

| Feature | Details |
| :--- | :--- |
| **Phone Name** | CMF Phone 2 Pro |
| **Codename** | `Galaga` |
| **Nothing OS** | 4.1 |
| **Android Version** | 16 |
| **Firmware Build** | `Galaga-B4.1-260812-1729` |
| **Kernel Version** | `6.1.162-android14-11-g65896c4edca1-ab15242664` |

---

## 🛑 Step 0: Verify Your Current Build

First, verify what version you are currently on. Connect your phone to your PC and run these commands in CMD/PowerShell:

```bash
adb shell getprop ro.build.display.id
adb shell getprop ro.build.version.incremental
adb shell uname -r
adb shell getprop ro.boot.slot_suffix
```

<details>
  <summary><b>👁️ Click Here to View Expected Output Screenshot</b></summary>
  <br>
  <div align="center">
    <img src="terminal_example.svg" width="600" alt="Terminal Output Example">
  </div>
</details>
<br>

If your output does **not** match the exact versions shown in the screenshot above (meaning you are on an older version), you will need to start from **Step 1** to upgrade properly!

---

## 📥 Required Downloads (All-in-One)

To make things extremely simple, all required files are well organized below:

### 📦 1. Core Files (Firmware & Fenrir)

| File Name | Description | Download Link |
| :--- | :--- | :--- |
| **AIO Firmware (Split Zip)**<br>`Galaga_B4.1-FULL.zip`, `.z01`, `.z02` | **(Recommended)** Custom All-in-One package. Due to GitHub limits, it is split into parts. Download all 3 parts, extract the main `.zip` file, and you have everything ready to go! | [📥 Download from Releases](https://github.com/aniketlab/CMF-Phone-2-Pro-Root-Guide/releases/tag/v1.0.0-Galaga-B4.1) |
| **Standalone `init_boot.img`** | For users *already* on this firmware who only need to patch it for root (saves you downloading the huge firmware files). | [📥 Download from Releases](https://github.com/aniketlab/CMF-Phone-2-Pro-Root-Guide/releases/tag/v1.0.0-Galaga-B4.1) |
| **Fenrir Bin**<br>`galaga-fenrir.bin` | The actual file that hides the bootloader warning. | [📥 Download from Releases](https://github.com/aniketlab/CMF-Phone-2-Pro-Root-Guide/releases/tag/v1.0.0-Galaga-B4.1) |
| **Official Nothing Archive** | *(Alternative)* Official split files. You will have to extract and arrange them manually. | [Link to spike0en repo](https://github.com/spike0en/nothing_archive/releases/tag/Galaga_B4.1-260812-1729) |

### ⚙️ 2. Root Managers (Choose One)
Download **one** Manager APK of your choice. *(Note: Apatch is no longer recommended here; please use BakaSU instead)*:

| Manager Name | Official Repository Link |
| :--- | :--- |
| 🛡️ **KernelSU** | [Download KernelSU APK](https://github.com/tiann/KernelSU/releases) |
| 🚀 **KernelSU Next** | [Download KernelSU Next APK](https://github.com/KernelSU-Next/KernelSU-Next/releases) |
| 🦊 **BakaSU** *(Formerly Resuski)* | [Download BakaSU APK](https://github.com/Baka-SU/BakaSU/releases) |

---

## 🚀 Step 1: PC Setup & Bootloader Unlock

If you are new here, your bootloader is likely locked. You must unlock it to get flashing permissions. 
> [!WARNING]
> **Unlocking the bootloader will COMPLETELY WIPE / DELETE all your data.**

### 1. Download Essential Drivers
First, download and extract the official tools on your computer:
*   **Platform Tools (ADB & Fastboot):** [Official Download Link (Windows, Mac, Linux)](https://developer.android.com/tools/releases/platform-tools)
*   **Google USB Drivers:** [Official Download Link (Windows)](https://developer.android.com/studio/run/win-usb)

### 2. Manual Driver Installation (Important)
Sometimes, Windows fails to recognize the phone in Fastboot mode (you might see a yellow warning triangle in Device Manager). If that happens:
1. Open **Device Manager**.
2. Right-click the Android device with the yellow triangle and select **Update driver**.
3. Click **Browse my computer for drivers** -> **Let me pick from a list of available drivers on my computer**.
4. Select **Android Device** -> **Android Bootloader Interface**, then click Next to install.

### 3. Unlocking the Bootloader
1. On your phone, go to **Settings > About Phone** and tap **Build Number** 7 times.
2. Go back to **Developer Options** and enable both **OEM Unlocking** and **USB Debugging**.
3. Connect your phone to your PC and type:
   ```bash
   adb devices
   adb reboot bootloader
   ```
4. Once your phone is in Fastboot mode, type this command to unlock:
   ```bash
   fastboot flashing unlock
   ```

> [!CAUTION]
> **CRITICAL STEP:** The moment you hit Enter on the unlock command, your phone screen will display a bunch of code. **You only have 2 to 3 seconds to press the VOLUME UP button!** If you miss this tiny window, the command will fail, and you will have to re-enter the `fastboot flashing unlock` command and try again.

5. After pressing Volume Up, select "Unlock the bootloader" using the volume keys and confirm with the **Power button**.
6. Your phone will reset and boot up. You now have permission to flash the new firmware!

---

## ⚡ Step 2: Jump to Supported Firmware

Now that your bootloader is unlocked, let's flash the supported firmware on which Fenrir works flawlessly.

> [!TIP]
> If your device is **already** running the `Galaga-B4.1-260812-1729` build, you can skip this entire step! Just download the standalone `init_boot.img` from the Releases section and jump straight to **Step 3**.

1. Download **all 3 parts** of the AIO Firmware Zip (`.zip`, `.z01`, `.z02`) from the [Releases section](https://github.com/aniketlab/CMF-Phone-2-Pro-Root-Guide/releases/tag/v1.0.0-Galaga-B4.1) and place them in the same folder.
2. Right-click on the main file (`Galaga_B4.1-260812-1729_FULL.zip`) and select **Extract Here** using [7-Zip](https://www.7-zip.org/) or WinRAR. It will automatically combine all parts into a single ready-to-flash folder! *(This saves you the headache of manually assembling individual raw images).*
3. Ensure **USB Debugging** is enabled, then reboot back into Bootloader mode:
   ```bash
   adb reboot bootloader
   ```
3. Inside the extracted folder, double-click the **`flash_all.bat`** script.
4. The script will prompt you with a series of questions. For a successful and clean installation, answer exactly as shown below:

   | Script Prompt / Question | Your Input | Reason / Note |
   | :--- | :---: | :--- |
   | Bootloader unlocked? | **`Y`** | Required to proceed. |
   | Are you in bootloader mode? | **`Y`** | Fastboot mode is required. |
   | Fastboot drivers properly installed? | **`Y`** | Required to proceed. |
   | Begin hash verification? | **`Y`** | Good practice to verify file integrity. |
   | *Hash warning: Some files are invalid...* | **`Y`** | *(Note: The script misreads comment lines as missing files. Actual image files are 100% valid).* |
   | Wipe Data? | **`Y`** | Highly recommended for a clean installation. |
   | Flash images on both slots? | **`N`** | Flashing to the current active slot is sufficient. |
   | Disable Android Verified Boot? | **`N`** | Keep AVB enabled. |
   | Reboot to system? | **`Y`** | Reboots the phone automatically. |

> [!WARNING]
> **Do NOT press `Ctrl+C` or disconnect your phone during the flash!** 
> While flashing the `vendor_a` partition, the process may appear completely frozen for a long time (5 to 10 minutes). This is completely normal. Be patient; the script will eventually resume, complete, and display `"# DONE #"`.

5. Once flashing is finished, the flasher window will close after pressing a key, and the phone will automatically reboot into the fresh `Galaga-B4.1` version.

---

## 🛡️ Step 3: Rooting the Phone (KernelSU / BakaSU)

Now that we are on the correct firmware, we will extract the `init_boot.img` and root the phone.

1. From the extracted AIO folder on your PC, copy `init_boot.img` and paste it into your phone's internal storage (e.g., the `Downloads` folder).
2. Install your preferred Root Manager APK (KernelSU, KernelSU Next, or BakaSU) on your phone.
3. Open the Manager app ➔ tap **Install** ➔ choose **Select and patch a file**.
4. Select the `init_boot.img` from your internal storage and wait for the patching process to finish.
5. A new patched image will be generated in your phone's `Download` folder. Copy this patched file back to your PC and place it inside your `Platform Tools` folder.
6. Boot your phone into Fastboot (Bootloader) mode and run:
   ```bash
   fastboot flash init_boot <name_of_the_patched_file.img>
   fastboot reboot
   ```
7. Once the phone boots up, open the Manager app again. You can also verify root via your PC:
   ```bash
   adb shell su -c id
   ```
   *(If the output shows `uid=0(root)`, Boom! 💥 You are successfully rooted).*

---

## 🦊 Step 4: Flash Fenrir (Bootloader Spoofing)

With root access secured, the final step is to hide the annoying "Unlocked Bootloader" warning by spoofing the system state.

1. Reboot your phone into Fastboot mode:
   ```bash
   adb reboot bootloader
   ```
2. Place the `galaga-fenrir.bin` file into your Platform Tools folder.
3. Run the following command:
   ```bash
   fastboot flash lk galaga-fenrir.bin
   ```
4. Once flashed, you need to boot directly into Recovery:
   ```bash
   fastboot reboot recovery
   ```
   > [!IMPORTANT]
   > *Pro Tip:* Sometimes the command fails to open the recovery screen. If that happens, manually hold down **Volume Up (+)** and the **Power Button** simultaneously until the phone enters Recovery mode.

5. Inside Recovery, select **Format Data / Factory Data Reset** from the menu.
6. After the reset completes, reboot the phone and complete the initial Android setup!

---

## ✅ Step 5: Final Verification

To confirm everything is working perfectly after setup:
1. Re-install the exact same Root Manager APK you used earlier (Root access will automatically be detected because it is patched at the kernel level).
2. On your PC, use ADB to verify the bootloader spoofing state:

```bash
adb shell getprop ro.boot.verifiedbootstate
# Expected Output: green

adb shell getprop ro.boot.flash.locked
# Expected Output: 1

adb shell getprop ro.boot.vbmeta.device_state
# Expected Output: locked
```

**Congratulations! 🎉 Your CMF Phone 2 Pro is now safely rooted and spoofed in the most professional way possible!**

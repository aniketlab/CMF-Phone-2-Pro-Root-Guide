<div align="center">
  <img src="CMF_Phone_2_Pro_Cover_NoBg.png" width="500" alt="CMF Phone 2 Pro Cover">
  <h1>📱 CMF Phone 2 Pro (Galaga) — Complete Root & Bootloader Spoofing Guide</h1>
  <p>Ek A-to-Z Professional Guide aapke phone ko safely Root karne aur Bootloader Warning (Fenrir) ko hide karne ke liye.</p>
</div>

---

> [!NOTE]
> Yeh poori guide shuru se lekar aakhir tak Hindi mein banayi gayi hai taaki kisi ko bhi samajhne mein problem na ho. Agar aap pehli baar root kar rahe hain, toh tension mat lijiye, bas steps ko dhyaan se follow karein!

## 📱 Device & Firmware Details (Target)

Niche ek box diya gaya hai, aapko is tutorial ke zariye exactly is build par aana hai:

| Feature | Details |
| :--- | :--- |
| **Phone Name** | CMF Phone 2 Pro |
| **Codename** | `Galaga` |
| **Nothing OS** | 4.1 |
| **Android Version** | 16 |
| **Firmware Build** | `Galaga-B4.1-260812-1729` |
| **Kernel Version** | `6.1.162-android14-11-g65896c4edca1-ab15242664` |

---

## 🛑 Step 0: Apni Current Details Check Karein

Pehle verify karein ki abhi aap kis version par hain. PC se apne phone ko connect karein aur CMD mein in commands ko run karein:

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

Agar aapka output upar diye gaye box se match **nahi** karta (kyunki aap purane version par hain), toh aapko **Step 1** se start karna hoga!

---

## 📥 Required Downloads (Sab Kuch Ek Jagah)

Bina kisi confusion ke, aapko idhar-udhar bhatakne ki zaroorat nahi hai. Saari zaroori files ko nicely categorize kar diya gaya hai:

### 📦 1. Core Files (Firmware & Fenrir)
*Filhal inke links Release section mein add kiye jayenge. Tab tak aap mere Release page ka wait karein.*

| File Name | Description | Download Link |
| :--- | :--- | :--- |
| **AIO Firmware Zip** | Ek single zip jisme saara extracted firmware aur flashing scripts hain. | [📥 Download from Releases](#) |
| **Fenrir Bin** | Bootloader warning ko hide karne wali file (`galaga-fenrir.bin`). | [📥 Download from Releases](#) |

### ⚙️ 2. Root Managers (Koi Ek Chunein)
Apni pasand ka koi bhi ek **Manager APK** download karein. *(Apatch ab supported nahi hai, uski jagah BakaSU use karein)*:

| Manager Name | Official Repository Link |
| :--- | :--- |
| 🛡️ **KernelSU** | [Download KernelSU APK](https://github.com/tiann/KernelSU/releases) |
| 🚀 **KernelSU Next** | [Download KernelSU Next APK](https://github.com/KernelSU-Next/KernelSU-Next/releases) |
| 🦊 **BakaSU** *(Pehle Resuski tha)* | [Download BakaSU APK](https://github.com/Baka-SU/BakaSU/releases) |

---

## 🚀 Step 1: PC Setup & Bootloader Unlock

Agar aap pehli baar aaye hain, toh aapka bootloader 100% lock hoga. Root aur flashing permissions ke liye usko unlock karna zaroori hai. **(Dhyan rahe: Isse phone ka saara data wipe / delete ho jayega)**

1. **PC Setup:** Apne computer mein `Platform Tools` (ADB & Fastboot) aur `Android Bootloader/Fastboot Drivers` install karein.
2. **USB Debugging:** Phone ki **Settings > About Phone** mein ja kar Build Number par 7 baar tap karein. Phir **Developer Options** mein ja kar **OEM Unlocking** aur **USB Debugging** ko ON karein.
3. Phone ko PC se connect karein aur CMD mein likhein:
   ```bash
   adb reboot bootloader
   ```
4. Phone fastboot mode mein aa jayega. Ab yeh command dalein:
   ```bash
   fastboot flashing unlock
   ```
5. Phone ki screen par ek warning aayegi. **Volume buttons** se "Unlock the bootloader" select karein aur **Power button** dabayein.
6. Phone reset hoga aur on ho jayega. (Ab aapko permission mil chuki hai naya firmware daalne ki!)

---

## ⚡ Step 2: Supported Firmware Par Jana

Ab kyunki phone unlock hai, hum apna supported latest firmware daalenge jispar Fenrir perfectly kaam karega.

1. Meri **Release** section se download ki gayi "AIO Firmware Zip" ko extract karein.
2. Phone ki USB Debugging wapas ON karein aur phone ko wapas Bootloader mode mein dalein (`adb reboot bootloader`).
3. Extracted folder mein ek flash script hogi (jaise `flash_all.bat`), uspe double click karein.
4. Script aapse kuch poochegi, usme apne hisaab se Yes (Y) ya No (N) enter karein aur flashing start hone dein.
5. Flashing khatam hone ke baad phone automatically naye `Galaga-B4.1` version par on ho jayega.

---

## 🛡️ Step 3: Phone Ko Root Karna (KernelSU / Apatch)

Firmware properly install ho gaya, ab hum `init_boot.img` nikal kar phone root karenge.

1. Usi extracted folder se `init_boot.img` copy karke apne phone ki internal storage (Downloads folder) mein daal dein.
2. Phone mein apna manpasand Manager (KernelSU Next, ya Resuski) ka APK install karein.
3. Manager app open karein ➔ **Install** par click karein ➔ **Select and patch a file** par click karein.
4. Apni internal storage se wahi `init_boot.img` select karein aur Patch hone dein.
5. Patch hone ke baad, ek nayi patched image phone ke `Download` folder mein ban jayegi. Us file ko copy karke PC par apne `Platform Tools` wale folder mein rakhein jahan aapka CMD open hai.
6. Phone ko Fastboot (Bootloader) mein dalein aur flash karein:
   ```bash
   fastboot flash init_boot <patched_file_ka_naam.img>
   fastboot reboot
   ```
7. Phone on hone par wapas Manager app check karein. Aap PC se bhi verify kar sakte hain:
   ```bash
   adb shell su -c id
   ```
   *(Agar `uid=0(root)` aaya, matlab Boom! 💥 Root ho gaya).*

---

## 🦊 Step 4: Fenrir Flash Karna (Bootloader Spoofing)

Root ho chuka hai, ab bas wo shuruwaati Unlocked Bootloader wali warning hatani hai aur system ko spoof karna hai.

1. Phone ko fir se Fastboot mode mein dalein (`adb reboot bootloader`).
2. Meri release mein di gayi Fenrir file (`galaga-fenrir.bin`) ko Platform tools wale folder mein rakhein.
3. Yeh command dalein:
   ```bash
   fastboot flash lk galaga-fenrir.bin
   ```
4. Flash hone ke baad, aapko phone ki Recovery mein jana hai:
   ```bash
   fastboot reboot recovery
   ```
   > [!IMPORTANT]
   > *Pro Tip:* Kabhi kabhi command dene ke baad bhi phone recovery open nahi karta. Aise mein **Volume Up (+)** aur **Power Button** ko ek sath daba kar rakhein jab tak phone explicitly Recovery mode mein na chala jaye.

5. Recovery open hone ke baad, menu se **Format Data / Factory Data Reset** select karein.
6. Reset hone ke baad phone on karein, aur apna initial setup complete karein!

---

## ✅ Step 5: Final Verification

Phone pura setup hone ke baad confirm karne ke liye:
1. Apna wahi version wala Root Manager APK dobara install karein (Root wahan apne aap wapas aa jayega, kyunki wo kernel-level par hai).
2. PC par ADB se yeh commands run karke dekhein ki Bootloader spoof chal raha hai ya nahi:

```bash
adb shell getprop ro.boot.verifiedbootstate
# Output aana chahiye: green

adb shell getprop ro.boot.flash.locked
# Output aana chahiye: 1

adb shell getprop ro.boot.vbmeta.device_state
# Output aana chahiye: locked
```

**Congratulations! 🎉 Aapka CMF Phone 2 Pro safely root aur spoof ho chuka hai ekdum professional tarike se!**

# CMF Phone 2 Pro (Galaga) — Complete A-to-Z Root + Fenrir Lab README

> Yeh README hamari CMF Phone 2 Pro / `Galaga` rooting + KernelSU Next LKM + Fenrir journey ka chronological record hai — starting setup se lekar successful final state tak, phir same process dost ke same device par repeat karne ke liye exact checklist tak.

## 0. Current Final State — WORKING ✅

Hamare tested CMF Phone 2 Pro par final setup:

- Device: **CMF Phone 2 Pro**
- Codename: **Galaga**
- Variant discussed: **IND**
- Nothing OS: **4.1**
- Build: **Galaga-B4.1-260812-1729**
- Android: **16**
- Kernel: **6.1.162-android14-11-g65896c4edca1-ab15242664**
- Physical bootloader: **still unlocked**
- KernelSU Next: **LKM root**
- Root modification: patched **`init_boot`**
- Fenrir: flashed to **`lk`**
- Fenrir-spoofed properties observed: `green`, `flash.locked=1`, `vbmeta.device_state=locked`
- Root verification: `uid=0(root)` was confirmed during the process.
- Stock ROM remained in use; no custom ROM was needed.

**Important:** Fenrir's `locked/green` properties are its spoofed integrity/boot-state behavior. We did **not** physically relock the bootloader.

---

# 1. Project Goal

Main goal tha:

1. CMF Phone 2 Pro ko stock Nothing OS par rakhna.
2. Exact compatible firmware use karna.
3. **KernelSU Next LKM** root obtain karna.
4. Uske baad **Fenrir** ko `lk` partition par flash karna.
5. Root ko retain karna.
6. Boot/integrity state ko Fenrir ke through spoofed `green/locked` state mein lana.
7. Final system ko repeatable process banana, taki same kaam dost ke same device par bhi kiya ja sake.

---

# 2. Initial Device Baseline — Before We Started

Initial phone state:

- Device: CMF Phone 2 Pro / Galaga
- Nothing OS: **3.2**
- Build: **Galaga-V3.2-250526-1427-IND**
- Android: **15**
- Kernel: `6.1.112-android14-11-g8961b96ba360-ab12909824`
- Bootloader: **already unlocked**

Initial research mein exact kernel/firmware compatibility important thi, kyunki exploit/root paths version-sensitive the.

---

# 3. Important Projects / Links We Used or Discussed

## Fenrir

Original project:

https://github.com/R0rt1z2/fenrir

Galaga-specific update/instructions:

https://t.me/CMFPhone2GlobalUpdates

Fenrir ka discussed concept:

- unlocked bootloader ko locked state ki tarah spoof karna
- boot warning ko remove karna
- stock/custom ROM par integrity behavior improve karna
- Galaga ke liye `lk` partition flash use karna

## KernelSU Next

Project:

https://github.com/KernelSU-Next/KernelSU-Next/releases

Docs:

https://kernelsu.org/guide/installation.html

Hamne **KernelSU Next LKM** choose kiya tha.

## Nothing Archive

Firmware archive:

https://nothingarchive.tech/docs/firmware

Relevant build:

`Galaga-B4.1-260812-1729`

## Nothing Archive OTA Guide

https://nothingarchive.tech/docs/guides#ota-sideloading

## Other projects discussed during research

- root-my-nothing: https://github.com/ang3lo-azevedo/root-my-nothing
- GhostLock: https://github.com/YuKongA/ghostlock-app
- User's POCO M7 Plus project: https://github.com/aniketlab/POCO-M7-Plus-Jailbreak

These were wider research/context projects. The successful CMF path was:

**KernelSU Next LKM + Fenrir**

---

# 4. Why We Moved to B4.1

Initial kernel:

`6.1.112-android14-11-g8961b96ba360-ab12909824`

After moving to B4.1:

`6.1.162-android14-11-g65896c4edca1-ab15242664`

This exact B4.1 kernel mattered because the exploit/root research was highly version-sensitive.

### Key lesson

Do not assume:

> "Nothing OS 4.1 hai = compatible."

Instead verify the exact build:

`Galaga-B4.1-260812-1729`

---

# 5. Firmware Package We Downloaded

The B4.1 package we worked with contained files similar to:

```text
Galaga_B4.1-260812-1729-image-logical.7z.001
Galaga_B4.1-260812-1729-image-logical.7z.002
Galaga_B4.1-260812-1729-image-logical.7z.003
Galaga_B4.1-260812-1729-image-firmware.7z
Galaga_B4.1-260812-1729-image-boot.7z
<hash file>
flash_all.bat
```

After extraction, many `.img` files were present, including:

```text
boot.img
init_boot.img
vendor_boot.img
dtbo.img
vbmeta.img
vbmeta_system.img
vbmeta_vendor.img
system.img
system_ext.img
system_dlkm.img
vendor.img
vendor_dlkm.img
odm.img
...
```

### Critical KSU image

For our LKM route we specifically needed:

```text
init_boot.img
```

Not simply `boot.img`.

---

# 6. Failed First OTA App Attempt

Before switching to direct fastboot flashing, we tried a Nothing Offline OTA updater APK with the OTA package.

Error:

```text
DOWNLOAD_STATE_INITIALIZATION_ERROR/20
```

### Resolution

We switched to the extracted fastboot image package + flashing script.

---

# 7. Stock B4.1 Fastboot Flash

We used the stock B4.1 image package with a `flash_all.bat` / Nothing Flasher style script.

The tool automatically downloaded platform-tools when required.

## Hash verification behavior

The script printed several `missing` lines. Investigation showed the `.sha256` parser was interpreting comment/header text as image filenames.

Actual image verification result:

```text
Valid images = 35
Invalid images = 0
```

The apparent "missing" entries were parser/header artifacts rather than missing core image files, so we proceeded.

---

# 8. Exact Y/N Choices During Stock Flash

A separate record was made as:

`CMF_Phone_2_Pro_Flash_YN_Record.txt`

The exact sequence:

```text
1. Bootloader unlocked?          Y
2. In bootloader mode?           Y
3. Fastboot drivers installed?   Y
4. Begin hash verification?      Y
5. Proceed despite missing?      Y
6. Wipe Data?                    Y
7. Flash images both slots?      N
8. Disable Android Verified Boot? N
9. Reboot to system?             Y
```

### Result

- Data was wiped.
- Images were flashed to **slot A**.
- AVB disable was **not** selected.
- Device rebooted successfully.
- Final script showed:

```text
# DONE #
Stock firmware restored.
```

---

# 9. Flashing Troubleshooting — `vendor_a` Looked Stuck

During flashing, `vendor_a` appeared stuck for more than ~10 minutes.

At one point `Ctrl+C` was pressed, but the process continued/resumed and eventually completed.

### Lesson

Do not instantly power-cycle a device just because a large partition appears frozen. Large Android partitions can take time depending on USB/storage/tool behavior.

In our actual run, the process eventually completed successfully.

---

# 10. Post-B4.1 Verification

After reboot, ADB detected the phone:

```text
adb devices
```

Detected serial:

```text
00198658R002725
```

### Build

```bash
adb shell getprop ro.build.display.id
```

Output:

```text
B4.1-260812-1729
```

### Incremental

```bash
adb shell getprop ro.build.version.incremental
```

Output:

```text
2608121729
```

### Slot

```bash
adb shell getprop ro.boot.slot_suffix
```

Output:

```text
_a
```

### Verified boot BEFORE Fenrir

```bash
adb shell getprop ro.boot.verifiedbootstate
```

Output:

```text
orange
```

### Android

```text
16
```

### Kernel

```bash
adb shell uname -r
```

Output:

```text
6.1.162-android14-11-g65896c4edca1-ab15242664
```

---

# 11. GhostLock Attempt

GhostLock was tested after the B4.1 update.

It showed unsupported / did not work for this setup.

Therefore the GhostLock route was dropped for the CMF test and we focused on:

```text
KernelSU Next LKM + Fenrir
```

---

# 12. KernelSU Next Strategy

We explicitly chose:

```text
KernelSU Next
    └── LKM
        └── patch init_boot.img
```

### LKM vs GKI decision

- **LKM:** preserve the stock kernel while loading the root module path.
- **GKI:** a different kernel installation/modification route.

For this device and our goal, we chose **LKM** and used the matching `init_boot.img`.

---

# 13. KernelSU Next Patching

We extracted the stock B4.1 `init_boot.img`.

Using KernelSU Next Manager, we patched it.

Patched file used during the session:

```text
kernelsu_next_patched_20260930_182417.img
```

---

# 14. Fastboot State Before KSU Flash

We entered bootloader/fastboot mode and checked:

```bash
fastboot devices
```

Detected:

```text
00198658R002725    fastboot
```

### Current slot

```bash
fastboot getvar current-slot
```

Result:

```text
current-slot: a
```

### Bootloader state

```bash
fastboot getvar unlocked
```

Result:

```text
unlocked: yes
```

---

# 15. Exact KernelSU Next Flash Command

We used:

```bash
fastboot flash init_boot "C:\Nothing 2 Pro\platform-tools\kernelsu_next_patched_20260930_182417.img"
```

Output:

```text
Sending 'init_boot_a' (8192 KB) OKAY
Writing 'init_boot_a' OKAY
Finished. Total time: 0.242s
```

Then:

```bash
fastboot reboot
```

---

# 16. KernelSU Post-Flash Verification

After reboot:

```bash
adb shell uname -r
```

Result:

```text
6.1.162-android14-11-g65896c4edca1-ab15242664
```

Build stayed:

```text
B4.1-260812-1729
```

Root verification command:

```bash
adb shell su -c id
```

Successful state:

```text
uid=0(root)
```

At this point we treated KernelSU Next LKM root as working.

---

# 17. Fenrir Stage

Galaga-specific file:

```text
galaga-fenrir.bin
```

Approximate size discussed:

```text
5.1 MB
```

---

# 18. Fenrir Concept

Fenrir was described as a mechanism that:

- spoofs unlocked bootloader as locked
- changes boot/integrity presentation
- removes the orange boot-state warning
- works only on supported firmware/builds

Again: this is **not the same thing as physically relocking the bootloader**.

---

# 19. Fenrir Flash Procedure We Used

First:

```bash
adb reboot bootloader
```

Then verify:

```bash
fastboot devices
```

Then flash:

```bash
fastboot flash lk galaga-fenrir.bin
```

After that we entered recovery with:

```bash
fastboot reboot recovery
```

---

# 20. Fenrir Recovery / Data Wipe Incident

Recovery showed a red/warning-style data-load message and offered choices similar to:

- Try again
- Factory data reset
- Try to restore

We selected:

```text
Factory data reset
```

The phone then booted successfully and required setup again.

This matched the Fenrir Galaga installation flow we were following: flash `lk`, then format data in recovery.

---

# 21. Fenrir Final Verification

### Verified boot state

```bash
adb shell getprop ro.boot.verifiedbootstate
```

Result:

```text
green
```

### Flash locked property

```bash
adb shell getprop ro.boot.flash.locked
```

Result:

```text
1
```

### VBMeta device state

```bash
adb shell getprop ro.boot.vbmeta.device_state
```

Result:

```text
locked
```

### Kernel stayed unchanged

```bash
adb shell uname -r
```

Result:

```text
6.1.162-android14-11-g65896c4edca1-ab15242664
```

This confirmed the tested setup had KSU + Fenrir coexisting while the stock kernel remained.

---

# 22. Final Architecture

```text
Stock Galaga B4.1
        │
        ├── stock init_boot.img
        │        │
        │        └── KernelSU Next patch
        │                  │
        │                  └── LKM root
        │
        └── stock lk
                 │
                 └── galaga-fenrir.bin
                           │
                           └── spoofed green/locked boot state
```

Practical mapping:

```text
KernelSU Next -> init_boot
Fenrir        -> lk
Stock kernel  -> preserved
Physical BL   -> remains unlocked
```

This separation is why the two modifications worked together in our test.

---

# 23. Important Mistakes / Corrections

## #1 — OTA updater

Tried offline OTA updater APK.

Result:

```text
DOWNLOAD_STATE_INITIALIZATION_ERROR/20
```

Resolution: use the extracted fastboot package.

## #2 — `boot.img` vs `init_boot.img`

For our KSU Next LKM route:

```text
PATCH init_boot.img
```

Use a matching image from the exact build.

## #3 — GhostLock

GhostLock was unsupported for our tested B4.1 state, so we abandoned that route here.

## #4 — `vendor_a` looked frozen

Waited rather than immediately power-cycling. The stock flash completed.

## #5 — Fenrir recovery warning

Selected factory data reset so the device could boot the new Fenrir state.

## #6 — `locked` != physical relock

These:

```text
ro.boot.flash.locked=1
ro.boot.vbmeta.device_state=locked
ro.boot.verifiedbootstate=green
```

must be understood as the Fenrir-spoofed state, not proof of a physical relock.

---

# 24. Critical Firmware Compatibility Rule

Target exact build:

```text
Galaga-B4.1-260812-1729
```

Do not casually flash Galaga Fenrir on:

- older firmware
- different Galaga firmware
- unsupported custom ROMs
- another device/codename

An older Galaga Fenrir post referenced:

```text
Galaga_B4.1-260615-1653
```

Later/current instructions referenced:

```text
Galaga_B4.1-260812-1729
```

So before a future flash, always re-check the current Galaga-specific Fenrir post and use the binary/instructions matched to the current supported build.

---

# 25. Do NOT Confuse Galaga With Other Nothing Devices

CMF Phone 2 Pro codename:

```text
Galaga
```

Other Nothing devices can have different Fenrir requirements.

For this device the Galaga command we used was:

```bash
fastboot flash lk galaga-fenrir.bin
```

Do not import another device's partition flashing instructions into Galaga.

---

# 26. Full Firmware Flash vs KSU Install vs Fenrir

## Full stock firmware flash

Use when the phone is not already on the target build, or when restoring/rebuilding the stock state.

This involved the complete extracted firmware package and `flash_all.bat`.

## KSU only

If the phone already exactly matches:

```text
Galaga-B4.1-260812-1729
```

you do **not** need to reflash the entire firmware just to install KSU.

You need the matching stock:

```text
init_boot.img
```

Patch it and flash the patched image.

## Fenrir only

Once on the supported build:

```bash
fastboot flash lk galaga-fenrir.bin
```

then format data in recovery according to the current Galaga instructions.

---

# 27. Current Friend Situation

Friend's CMF Phone 2 Pro reportedly has:

```text
Nothing OS 4.1
Galaga-B4.1-260812-1729-IND
```

### First conclusion

**Do NOT flash the full firmware just because it says Nothing OS 4.1.**

First verify the exact build and bootloader state.

---

# 28. Friend Phone — STEP 1: ADB

Once friend arrives:

```bash
adb devices
```

Authorize USB debugging on the phone if asked.

---

# 29. Friend Phone — STEP 2: Verify Exact Build

Run:

```bash
adb shell getprop ro.build.display.id
```

Expected:

```text
B4.1-260812-1729
```

Then:

```bash
adb shell getprop ro.build.version.incremental
```

Expected:

```text
2608121729
```

Also:

```bash
adb shell uname -r
```

Record the exact kernel.

And:

```bash
adb shell getprop ro.boot.slot_suffix
```

Record `_a` or `_b`.

---

# 30. Friend Phone — STEP 3: Check Bootloader State

From bootloader:

```bash
fastboot getvar unlocked
```

If:

```text
unlocked: yes
```

continue.

If:

```text
unlocked: no
```

the bootloader must be unlocked before flashing modified images.

### Important

Bootloader unlocking generally wipes userdata, so backup important data first.

---

# 31. Friend Phone — STEP 4: No Full Firmware Flash If Exact Build Matches

Decision:

```text
Exact B4.1-260812-1729?
        │
        ├── YES -> no full firmware flash
        │
        └── NO  -> stop and obtain correct supported firmware
```

Do not move forward until the build is confirmed.

---

# 32. Friend Phone — STEP 5: Get Matching Stock `init_boot.img`

Use the exact B4.1 package corresponding to:

```text
Galaga-B4.1-260812-1729
```

Extract:

```text
init_boot.img
```

### Do not use

- old B3.x `init_boot.img`
- another Galaga build's image
- another device's image
- an arbitrary `boot.img`

---

# 33. Friend Phone — STEP 6: Patch With KernelSU Next

Open KernelSU Next Manager.

Patch the exact stock matching:

```text
init_boot.img
```

Save the resulting patched image somewhere accessible.

Example:

```text
kernelsu_next_patched.img
```

---

# 34. Friend Phone — STEP 7: Bootloader Mode

```bash
adb reboot bootloader
```

Then:

```bash
fastboot devices
```

Confirm the phone appears.

---

# 35. Friend Phone — STEP 8: Check Current Slot

```bash
fastboot getvar current-slot
```

Record:

```text
a
```

or:

```text
b
```

---

# 36. Friend Phone — STEP 9: Flash KSU `init_boot`

Example:

```bash
fastboot flash init_boot "C:\path\to\kernelsu_next_patched.img"
```

Look for successful `Sending` and `Writing` results.

Then:

```bash
fastboot reboot
```

---

# 37. Friend Phone — STEP 10: Verify KSU Before Fenrir

After Android boots:

```bash
adb shell uname -r
```

Confirm expected B4.1 kernel.

Then:

```bash
adb shell getprop ro.build.display.id
```

Expected:

```text
B4.1-260812-1729
```

Then:

```bash
adb shell su -c id
```

Successful root:

```text
uid=0(root)
```

**Do not rush to Fenrir before KSU is working.**

---

# 38. Friend Phone — STEP 11: Flash Fenrir

Once root is confirmed:

```bash
adb reboot bootloader
```

Then:

```bash
fastboot devices
```

Then:

```bash
fastboot flash lk galaga-fenrir.bin
```

---

# 39. Friend Phone — STEP 12: Recovery + Format Data

```bash
fastboot reboot recovery
```

If recovery reports that data cannot be loaded / system data is unavailable, use the factory reset / format-data option required by the current Galaga Fenrir instructions.

Then boot Android.

---

# 40. Friend Phone — STEP 13: Final Verification

After Android boot:

```bash
adb shell getprop ro.boot.verifiedbootstate
```

Expected Fenrir state:

```text
green
```

Then:

```bash
adb shell getprop ro.boot.flash.locked
```

Expected:

```text
1
```

Then:

```bash
adb shell getprop ro.boot.vbmeta.device_state
```

Expected:

```text
locked
```

Then:

```bash
adb shell uname -r
```

Expected B4.1 kernel from the tested device:

```text
6.1.162-android14-11-g65896c4edca1-ab15242664
```

Finally:

```bash
adb shell su -c id
```

Expected:

```text
uid=0(root)
```

---

# 41. Final Friend Workflow — Ultra-Compact

```text
1. Check build
   ↓
2. Check bootloader unlocked
   ↓
3. If exact B4.1-260812-1729 -> skip full firmware flash
   ↓
4. Extract exact stock init_boot.img
   ↓
5. Patch with KernelSU Next Manager (LKM)
   ↓
6. fastboot flash init_boot patched.img
   ↓
7. Reboot + verify su = uid=0(root)
   ↓
8. adb reboot bootloader
   ↓
9. fastboot flash lk galaga-fenrir.bin
   ↓
10. fastboot reboot recovery
   ↓
11. Factory reset / format data
   ↓
12. Boot Android
   ↓
13. Verify green + locked properties
   ↓
14. Verify root again
```

---

# 42. Pre-Flight Checklist

```text
[ ] Backup important data
[ ] USB debugging works
[ ] adb works
[ ] fastboot works
[ ] Platform-tools installed
[ ] Exact build confirmed
[ ] Correct Galaga B4.1 package available
[ ] Matching stock init_boot.img available
[ ] KernelSU Next Manager available
[ ] galaga-fenrir.bin available
[ ] Bootloader state confirmed
[ ] Battery sufficiently charged
[ ] Stable USB cable/port
```

---

# 43. Safety / Recovery Rules

1. Never flash a modified image without first knowing which build it belongs to.
2. Never use a random `init_boot.img`.
3. Never assume "Nothing OS 4.1" is enough; check the exact build.
4. Do not mix Galaga instructions with other Nothing codenames.
5. Fenrir flash is not a physical bootloader relock.
6. Expect data loss when unlocking or formatting data.
7. Do not interrupt long partition flashes just because progress looks slow.
8. Verify KSU **before** applying Fenrir.
9. After major flashing, verify build, slot, kernel, root, and boot/integrity state.
10. Re-check the current Fenrir compatibility notice before future flashes.

---

# 44. Exact Command Cheat Sheet

## ADB

```bash
adb devices
adb reboot bootloader
adb reboot recovery
adb shell getprop ro.build.display.id
adb shell getprop ro.build.version.incremental
adb shell getprop ro.boot.slot_suffix
adb shell getprop ro.boot.verifiedbootstate
adb shell getprop ro.boot.flash.locked
adb shell getprop ro.boot.vbmeta.device_state
adb shell uname -r
adb shell su -c id
```

## Fastboot

```bash
fastboot devices
fastboot getvar current-slot
fastboot getvar unlocked
fastboot flash init_boot "C:\path\to\kernelsu_next_patched.img"
fastboot flash lk galaga-fenrir.bin
fastboot reboot
fastboot reboot recovery
```

---

# 45. Expected Verification Table

| Stage | Property / Command | Expected / Observed |
|---|---|---|
| Build | `getprop ro.build.display.id` | `B4.1-260812-1729` |
| Incremental | `getprop ro.build.version.incremental` | `2608121729` |
| Kernel | `uname -r` | `6.1.162-android14-11-g65896c4edca1-ab15242664` |
| Root | `su -c id` | `uid=0(root)` |
| Slot | `getprop ro.boot.slot_suffix` | `_a` or `_b` |
| Pre-Fenrir VB state | `ro.boot.verifiedbootstate` | `orange` observed |
| Post-Fenrir VB state | `ro.boot.verifiedbootstate` | `green` observed |
| Post-Fenrir flash-lock prop | `ro.boot.flash.locked` | `1` observed |
| Post-Fenrir VBMeta prop | `ro.boot.vbmeta.device_state` | `locked` observed |

---

# 46. What Changed Across the Whole Journey

## Before

```text
B3.x-ish / old state
Android 15
Kernel 6.1.112...
Bootloader unlocked
No final root/Fenrir stack
```

## After stock upgrade

```text
B4.1-260812-1729
Android 16
Kernel 6.1.162...
Bootloader unlocked
```

## After KSU

```text
B4.1-260812-1729
Android 16
Kernel unchanged
KernelSU Next LKM root
```

## After Fenrir

```text
B4.1-260812-1729
Android 16
Kernel unchanged
KernelSU Next LKM root
Fenrir on lk
Spoofed green/locked boot state
Physical bootloader remains unlocked
```

---

# 47. Why the Combination Worked

The two modifications touched different pieces:

```text
KernelSU Next LKM
    -> init_boot

Fenrir
    -> lk
```

So, in our tested setup, they coexisted without replacing the stock kernel.

---

# 48. Platform-Tools Note

Our platform-tools directory was:

```text
C:\Nothing 2 Pro\platform-tools\
```

The friend's PC may use another path.

Use quotes around Windows paths containing spaces:

```bash
fastboot flash init_boot "C:\Some Folder\patched.img"
```

---

# 49. Existing Flash Record

A separate record was generated during the earlier stock-flashing session:

```text
CMF_Phone_2_Pro_Flash_YN_Record.txt
```

It documents the Y/N sequence used during the B4.1 flash.

---

# 50. Current Compatibility Note

At the time this README was created, the current Galaga Fenrir instructions referenced:

```text
Galaga-B4.1-260812-1729
```

and the Galaga command:

```bash
fastboot flash lk galaga-fenrir.bin
```

followed by formatting data in recovery.

Because exploit compatibility can change with new binaries/firmware, re-check the current Galaga-specific instructions before a future flash.

---

# 51. One-Line Mental Model

```text
EXACT STOCK BUILD
      ↓
PATCH MATCHING init_boot WITH KSU NEXT
      ↓
VERIFY ROOT
      ↓
FLASH galaga-fenrir.bin TO lk
      ↓
FORMAT DATA IN RECOVERY
      ↓
VERIFY GREEN/LOCKED PROPERTIES + ROOT
```

---

# 52. Current Status

## OUR DEVICE

```text
✅ Stock B4.1
✅ Android 16
✅ Kernel 6.1.162
✅ KernelSU Next LKM
✅ Root confirmed
✅ Fenrir flashed
✅ Green verified state observed
✅ Locked spoof properties observed
✅ Physical bootloader still unlocked
```

## FRIEND'S DEVICE

```text
⏳ Waiting for friend to arrive
⏳ First task = verify exact build and bootloader state
⏳ If exact B4.1-260812-1729, skip full firmware flash
⏳ Then KSU Next LKM
⏳ Then Fenrir
```

---

# 53. Final Golden Rules

```text
RULE #1  = Exact build first.
RULE #2  = Matching init_boot only.
RULE #3  = KSU LKM before Fenrir in our tested workflow.
RULE #4  = KSU -> init_boot.
RULE #5  = Fenrir -> lk.
RULE #6  = Format data after Fenrir.
RULE #7  = Green/locked props != physical bootloader relock.
RULE #8  = Verify every stage before moving to the next.
RULE #9  = Never mix Galaga instructions with other Nothing devices.
RULE #10 = Re-check current Fenrir compatibility before future flashing.
```

---

## Appendix A — Session Evidence / Exact Values

### Initial

```text
Build:
Galaga-V3.2-250526-1427-IND

Kernel:
6.1.112-android14-11-g8961b96ba360-ab12909824
```

### After B4.1

```text
Build:
B4.1-260812-1729

Incremental:
2608121729

Android:
16

Slot:
_a

Verified boot:
orange

Kernel:
6.1.162-android14-11-g65896c4edca1-ab15242664
```

### After KSU

```text
KernelSU Next:
LKM

Modified image:
init_boot

Root:
uid=0(root)
```

### After Fenrir

```text
ro.boot.verifiedbootstate:
green

ro.boot.flash.locked:
1

ro.boot.vbmeta.device_state:
locked

Kernel:
6.1.162-android14-11-g65896c4edca1-ab15242664
```

---

## Appendix B — Files / Artifacts Mentioned

### Stock firmware package

```text
Galaga_B4.1-260812-1729-...
```

### KSU patched image

```text
kernelsu_next_patched_20260930_182417.img
```

### Fenrir binary

```text
galaga-fenrir.bin
```

### Y/N flash record

```text
CMF_Phone_2_Pro_Flash_YN_Record.txt
```

---

## Appendix C — Source Links

Fenrir original:
https://github.com/R0rt1z2/fenrir

Galaga update channel:
https://t.me/CMFPhone2GlobalUpdates

KernelSU Next:
https://github.com/KernelSU-Next/KernelSU-Next/releases

KernelSU docs:
https://kernelsu.org/guide/installation.html

Nothing Archive firmware:
https://nothingarchive.tech/docs/firmware

Nothing Archive guides:
https://nothingarchive.tech/docs/guides#ota-sideloading

GhostLock:
https://github.com/YuKongA/ghostlock-app

root-my-nothing:
https://github.com/ang3lo-azevedo/root-my-nothing

POCO M7 Plus Jailbreak:
https://github.com/aniketlab/POCO-M7-Plus-Jailbreak

---

# END

## Current winning recipe

```text
Galaga B4.1-260812-1729
        +
KernelSU Next LKM on matching init_boot
        +
Fenrir on lk
        +
Recovery data format
        =
WORKING ROOT + FENRIR SETUP
```

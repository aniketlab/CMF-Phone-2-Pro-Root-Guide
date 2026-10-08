from rich.console import Console
from rich.text import Text
from rich.theme import Theme

# Compact width and custom sleek theme
custom_theme = Theme({
    "prompt": "bold cyan",
    "cmd": "bright_white",
    "out": "bright_green"
})

console = Console(record=True, width=75, theme=custom_theme)

p = Text("PS C:\\> ", style="prompt")

console.print(p + Text("adb shell getprop ro.build.display.id", style="cmd"))
console.print(Text("B4.1-260812-1729", style="out"))

console.print(p + Text("adb shell getprop ro.build.version.incremental", style="cmd"))
console.print(Text("2608121729", style="out"))

console.print(p + Text("adb shell uname -r", style="cmd"))
console.print(Text("6.1.162-android14-11-g65896c4edca1-ab15242664", style="out"))

console.print(p + Text("adb shell getprop ro.boot.slot_suffix", style="cmd"))
console.print(Text("_a", style="out"))

console.save_svg("terminal_example.svg", title="Expected Output")
print("Compact SVG generated successfully!")

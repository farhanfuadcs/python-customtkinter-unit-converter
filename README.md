# Python Unit Converter

A graphical unit conversion application built with Python and CustomTkinter. Users can select a conversion category, choose the source and target units, enter a value, and view the converted result.

## Features

- **Length conversion:** Supports millimeters, centimeters, meters, kilometers, inches, feet, and miles.
- **Weight conversion:** Supports milligrams, grams, kilograms, metric tonnes, ounces, and pounds.
- **Temperature conversion:** Supports Celsius, Fahrenheit, and Kelvin.
- **Dynamic unit selection:** Updates the available units based on the selected category.
- **Graphical interface:** Uses CustomTkinter widgets for a desktop GUI.
- **Input error handling:** Displays an error message when the input value is invalid or a unit selection is unavailable.
- **Separate conversion functions:** Keeps the calculation logic organized by category.

## Technologies Used

- Python
- CustomTkinter
- Tkinter message boxes
- Dictionaries
- Functions
- Exception handling
- GUI event handling

## Installation

Install the required library:

```bash
pip install customtkinter
```

## How to Run

1. Save the program as `unit_converter.py`.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python unit_converter.py
   ```

## How to Use

1. Select Length, Weight, or Temperature.
2. Choose the units in the From and To menus.
3. Enter the value to convert.
4. Click **Convert** to display the result.

## Supported Units

| Category | Units |
|---|---|
| Length | mm, cm, m, km, in, ft, mi |
| Weight | mg, g, kg, t, oz, lb |
| Temperature | C, F, K |

## Conversion Examples

| Conversion | Example result |
|---|---:|
| 1 km to m | 1000 m |
| 1 lb to kg | Approximately 0.4536 kg |
| 0 C to F | 32 F |
| 100 C to K | 373.15 K |

## Project Structure

```text
python-customtkinter-unit-converter/
└── unit_converter.py
```


## Learning Outcomes

This project demonstrates practical Python skills in GUI development, dictionaries, functions, conditional logic, event-driven programming, unit conversion formulas, and input validation.

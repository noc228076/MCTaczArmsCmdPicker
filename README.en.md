

# MC-TACZ Arms CMD Picker

**MC-TACZ Arms CMD Picker** is a command generation tool designed for the TACZ mod in Minecraft, aimed at helping players quickly generate command codes for specific weapons.

## 📌 Project Introduction

This project is written in Python and includes a simple command-line interface for selecting weapons and generating corresponding Minecraft commands. It is suitable for weapon debugging, testing, or server management scenarios within the TACZ mod.

## 📁 File Structure Description

- `main.py`: The main entry point of the program, responsible for weapon selection and command generation.
- `utils.py`: Contains auxiliary functions, such as input validation.
- `data/gun_id.py`: A list of weapon IDs, used to map weapon names to their corresponding IDs.
- `data/cmd_list.py`: A list of command templates, defining the command format for different weapons.
- `data/__init__.py`: Initialization module, used to organize data files.

## 🛠️ How to Use

1. Make sure you have Python 3.x installed.
2. Run the `main.py` file:
   ```bash
   python main.py
   ```
3. Follow the prompts to select a weapon and generate the command.

## 📝 Example Output

After selecting a weapon, the program will output a command in the following format:
```
/give @p tacz:weapon_<gun_id>
```

## 📎 Dependencies

- No third-party libraries required, only the standard library is used.

## 🤝 Contribution Guidelines

PRs or Issues are welcome to improve the project. You can add support for more weapons, optimize the UI, or enhance the documentation.

## 📄 License

This project is licensed under the MIT License. Please refer to the `LICENSE` file for details.

---

If you have any questions or suggestions, please submit an Issue on the project page.
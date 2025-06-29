# 🚀 BanditPassMan

**BanditPassMan** is a Python-based password manager tailored for the [Bandit wargame](https://overthewire.org/wargames/bandit/bandit0.html) from OverTheWire. It helps you securely store, retrieve, and manage passwords for each Bandit level, streamlining your progress through the game.

---

## ✨ Features

- 🔒 Securely store passwords for each Bandit level
- 🔍 Retrieve and update passwords easily
- 💻 Simple command-line interface
- ⚡ Lightweight and easy to use

---

## 🛠️ Installation

1. **Clone this repository:**
    ```bash
    git clone https://github.com/yourusername/banditPassMan.git
    cd banditPassMan
    ```

2. **(Optional) Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **(Optional) Make the script executable (Linux/macOS):**
    ```bash
    chmod +x banditman
    ```

4. **(Optional) Add BanditPassMan to your PATH (Linux/macOS):**
    You can create a symbolic link to `banditman` in a directory that's in your PATH, such as `/usr/local/bin`:
    ```bash
    sudo ln -s "$(pwd)/banditman" /usr/local/bin/banditman
    ```
    Now you can run `banditman` from anywhere.

---

## 🚦 Usage

Run the password manager from the command line:

```bash
python banditman <command> [username]
```
or (if executable):
```bash
./banditman <command> [username]
```

### 📋 Available Commands

| Command(s)         | Description                                                        |
|--------------------|--------------------------------------------------------------------|
| `add`, `a`         | Add a new Bandit level (auto-incremented username).                |
| `edit`, `e` `<username>` | Edit the password, secret, or solve for a specific Bandit level.   |
| `list`, `l`        | List all stored Bandit levels.                                     |
| `show`, `s` `<username>` | Show details for a specific Bandit level.                          |
| `next`, `n`        | Show the SSH command and password for the next Bandit level.        |

> 💡 **Tip:** Follow the on-screen prompts or use the commands above to add, retrieve, update, or view passwords for each Bandit level.

---

## 🤝 Contributing

Contributions are welcome!  
Please open an issue or submit a pull request for any improvements or bug fixes.

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

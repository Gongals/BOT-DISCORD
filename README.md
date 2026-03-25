# 🤖 Discord Bot (Python)

A simple Discord bot built with Python using the `discord.py` library.
This project was created as a learning exercise to understand how Discord bots work, including commands, arguments, and project structure.

---

## 🚀 Features

* `!ping` → replies with "pong"
* `!call @user` → mentions a user
* `!coinflip` → random heads or tails
* `!rate @user` → gives a random "rating"
* `!say <message>` → repeats your message
* `!ball <question>` → magic 8-ball style answers

---

## 🛠️ Technologies Used

* Python 3
* discord.py

---

## 📁 Project Structure

```
.
├── main.py        # Bot initialization and startup
├── controls.py    # Commands and logic
```

---

## ⚙️ Setup & Installation

1. Clone the repository:

```
git clone https://github.com/Gongals/BOT-DISCORD
cd your-repo-name
```

2. Install dependencies:

```
pip install discord.py
```

3. Add your Discord bot token in `main.py`:

```
bot.run('YOUR_TOKEN_HERE')
```

⚠️ Never share your real token publicly.

---

## ▶️ Running the Bot

```
python main.py
```

---

## 📚 What I Learned

* Creating a Discord bot with `discord.py`
* Handling commands and arguments
* Using optional parameters (`None`)
* Capturing full message input with `*`
* Organizing code into multiple files

---

## 🧠 Future Improvements

* Better error handling
* Command cooldowns
* Use environment variables for the token
* Add more features and commands

---

## 📄 License

This project is for learning purposes.

# 🔎 Search Bot

Search Bot is a simple web-based search engine that retrieves information from Wikipedia.  
Users can enter a topic in the search bar, and the application returns the top relevant results along with short summaries. Each result contains a clickable link that directs users to the full Wikipedia page for more detailed information.

---

## 📸 Screenshot

![Search Bot Screenshot](ss/Screenshot 2026-03-14 195450.png)

> Place your screenshot inside a folder named **screenshots** and name it `search_bot.png`.

Example project structure:

```
Search_bot
│
├── app.py
├── templates
│   └── index.html
├── static
│   └── style.css
├── screenshots
│   └── search_bot.png
└── README.md
```

---

## ✨ Features

- Search Wikipedia topics using a simple web interface  
- Retrieves the top 5 relevant search results  
- Displays short summaries for quick understanding  
- Provides clickable links to the full Wikipedia articles  
- Clean and structured display of search results  
- Dynamic content rendering using Flask templates  
- Loading indicator while search results are being fetched  

---

## 🛠 Technologies Used

### Backend
- Python  
- Flask (Web Framework)  
- Wikipedia Python Library  

### Frontend
- HTML  
- CSS  

### Tools
- Visual Studio Code  
- Virtual Environment (.venv)

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Search_bot.git
cd Search_bot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Mac / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install flask wikipedia
```

---

## ▶️ Running the Application

Run the Flask app:

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📖 How to Use

1. Enter a keyword or topic in the search box  
2. Click the **Search** button  
3. The system will display the top Wikipedia results with summaries  
4. Click the result title to open the full Wikipedia page  

---

## 🚀 Future Improvements

- Add search history  
- Improve UI with Bootstrap or Tailwind CSS  
- Add dark mode  
- Support more knowledge sources besides Wikipedia  

---

## 📜 License

This project is open source and available under the **MIT License**.

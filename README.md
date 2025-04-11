# Reverse Image Search App

This project is a **mobile application** that performs **reverse image search across social media platforms** using public sources (Yandex and Bing). It identifies:

- When an image was **first posted**
- The **original uploader**
- All other profiles or users who have posted the same image
- The **platforms** where it was posted
- Date and time of each match

Built with:
- **React Native + Expo** (mobile frontend)
- **Flask** (Python backend)
- **Selenium** and **BeautifulSoup** (for scraping Yandex + Bing)
- **REST API communication** between mobile and server

---

## Features

- Upload or take a photo from your phone
- Runs reverse image search using public platforms
- Automatically scrapes result metadata
- Groups results by user profile
- Displays first appearance (timestamp, source, user)
- Works across Reddit, Facebook, Twitter, blogs, and more

---

## Screenshots

*(Insert screenshots or UI mockup here)*

---

## Installation & Setup

### Backend (Flask)

1. **Clone the repository**
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
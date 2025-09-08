# Playlist-creator-
It instantly creates a playlist for a particular date provided on your spotify account.
This Python project creates a Spotify playlist containing the **Billboard Hot 100 songs** from a specific date in history.  
You provide a date (in `YYYY-MM-DD` format), and the script:

1. Scrapes Billboard’s Hot 100 chart for that day.  
2. Searches Spotify for those songs.  
3. Creates a **private playlist** in your Spotify account.  

---

## 🚀 Features
- Scrapes Billboard Hot 100 songs for any given date.  
- Uses the Spotify API to find songs and create a playlist.  
- Automatically skips songs not available on Spotify.  
- Creates a **private playlist** with the top hits.  

---

## 📦 Requirements

- Python 3.8+
- Spotify Developer Account
- Billboard chart scraping via `requests` + `BeautifulSoup4`
- Spotify API integration via `spotipy`

---

## 🔑 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/billboard-spotify-playlist.git
   cd billboard-spotify-playlist


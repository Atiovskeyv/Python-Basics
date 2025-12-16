import requests
import sqlite3
import json
import tkinter as tk
from tkinter import messagebox

import webbrowser   ## Used to open selected playlists in the web browser




     ## Clears all search results, stored playlists, and input fields
def clear_all():
    listbox.delete(0, tk.END)
    all_playlists.clear()
    artist_id_entry.delete(0, tk.END)


     ## Converts follower count values into integers for sorting and filtering
def convert_followers_to_int(value):
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        value = value.strip().upper()
        if value.endswith('M'):
            try:
                return int(float(value[:-1]) * 1_000_000)
            except:
                return 0
        elif value.endswith('K'):
            try:
                return int(float(value[:-1]) * 1_000)
            except:
                return 0
        else:
            try:
                return int(value.replace(',', ''))
            except:
                return 0
    return 0



     ## Safely converts values to integers
def safe_int(value):
    try:
        return int(value)
    except:
        return 0



     ## Stores all fetched playlist data in memory
all_playlists = []



     ## API configuration for retrieving playlist data related to an artist
       
url = "https://songstats.p.rapidapi.com/artists/top_playlists"
headers = {
    "x-rapidapi-key": "071c9a6de6mshd578656e6bc0e09p18668djsn71c839470074",
    "x-rapidapi-host": "songstats.p.rapidapi.com"
}
querystring = {
    "limit": "20",
    "source": "all",
    "scope": "total"
}

     
     

connection = sqlite3.connect("playlist.db")
cursor_object = connection.cursor()
cursor_object.execute(
    """CREATE TABLE IF NOT EXISTS PlayLists(
        id TEXT PRIMARY KEY,
        name TEXT,
        follower_count TEXT,
        source TEXT,
        artist_id TEXT
    )"""
)
connection.commit()
connection.close()




      ## Fetches playlist data for the given Spotify artist ID

def call_api():
    global all_playlists
    artist_id = artist_id_entry.get().strip()
    if not artist_id:
        messagebox.showwarning("Warning", "Please enter a Spotify Artist ID.")
        return
    
         ## Resets previous results before loading new data
    listbox.delete(0, tk.END)
    all_playlists.clear()


        ## Opens database connection for reading cached data

    with sqlite3.connect("playlist.db") as connection:
        cursor = connection.cursor()

          ## Checks if playlist data for the artist already exists in the database
        cursor.execute(
            "SELECT name, follower_count, id FROM PlayLists WHERE artist_id = ?",
            (artist_id,)
        )
        records = cursor.fetchall()

        if records:
            for name, followers, pid in records:
                all_playlists.append((name, followers, pid))
            filter_playlists()
            return

             ## Prepares API request parameters
        params = querystring.copy()
        params["spotify_artist_id"] = artist_id
        print("API Parameters:", params)

        try:
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            print(json.dumps(data, indent=2, ensure_ascii=False))

             
             ## Extracts playlist information from the API response
            if "top_playlists" in data["data"][0]:
                for playlist in data["data"][0]["top_playlists"]:
                    name = playlist.get("playlist_name")
                    followers = playlist.get("followers_total")
                    source = playlist.get("source", "unknown")
                    pid = playlist.get("playlist_id")
                    all_playlists.append((name, followers, pid)) 
                    cursor.execute(
                        "INSERT OR REPLACE INTO PlayLists (id, name, follower_count, source, artist_id) VALUES (?, ?, ?, ?, ?)",
                        (pid, name, followers, source, artist_id)
                    )

                connection.commit()
                filter_playlists()
            else:
                listbox.insert(tk.END, "No top playlist information available.")
        except Exception as e:
            listbox.insert(tk.END, "Failed to fetch data. An error occurred.")
            print("Error:", e)

   
   ## Displays playlist details and allows opening the playlist in Spotify
def show_details(event):
    selected = listbox.curselection()
    if selected:
        i = selected[0]
        name, followers, pid = all_playlists[i]
        answer = messagebox.askyesno(
            "Playlist Details",
            f"Name: {name}\nFollowers: {followers}\nDo you want to open it on Spotify?"
        )
        if answer:
            webbrowser.open(f"https://open.spotify.com/playlist/{pid}")



     ## Filters and sorts playlists based on follower count and search input
def filter_playlists():
    filter_text = filter_entry.get().lower()
    listbox.delete(0, tk.END)
    sorted_list = sorted(
        all_playlists,
        key=lambda x: convert_followers_to_int(x[1]),
        reverse=True
    )

    for i, (name, followers, pid) in enumerate(sorted_list, start=1):
        if filter_text in name.lower():
            listbox.insert(tk.END, f"{i}. {name} - {followers} followers")


     
     ## User interface configuration and layout

  ## Button hover effects
def on_enter(e):
    button.config(bg='#4CAF50', fg='white')

def on_leave(e):
    button.config(bg='SystemButtonFace', fg='black')

window = tk.Tk()
clear_button = tk.Button(window, text="Clear", command=clear_all, bg="#c0392b", fg="white")
clear_button.pack(pady=(5, 0))
window.title("Playlist Page")
window.geometry("650x500")
window.con

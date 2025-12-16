To use this application, you need to copy a Spotify artist ID and submit it to the program as a query. The application then retrieves and displays playlists that either include the artist’s songs or are closely related to the artist through interaction, genre similarity, or shared musical context (for example, playlists featuring similar artists or the same music genre).

You can search through the retrieved playlists by name, select the ones you want, and clear the search results when needed. For more accurate and relevant results, it is recommended to search for well-known artists from a specific genre. For example, when searching for the technical death metal band Necrophagist, the application directly returns playlists related to metal subgenres such as technical death metal and nu metal.

The application also includes a caching mechanism. If you search for the same artist again, the program does not fetch the data again from the API. Instead, it loads the previously saved data, allowing the results to be displayed much faster.

The application was developed and tested using Python 3.13.2 and works without any issues on this version.
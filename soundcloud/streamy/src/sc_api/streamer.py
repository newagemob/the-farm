import requests
import time

# Your SoundCloud API credentials
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

# SoundCloud track ID of the song you want to stream
TRACK_ID = 'TRACK_ID'

# Function to get the stream URL of a track
def get_stream_url(client_id, track_id):
    url = f'https://api.soundcloud.com/tracks/{track_id}/stream'
    params = {
        'client_id': client_id,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['url']
    else:
        print(f"Failed to retrieve stream URL: {response.status_code}")
        return None

# Function to continuously play the song
def stream_soundcloud_track(client_id, track_id):
    stream_url = get_stream_url(client_id, track_id)
    
    if stream_url:
        print(f"Streaming track: {track_id}")
        while True:
            try:
                response = requests.get(stream_url, stream=True)
                if response.status_code == 200:
                    for chunk in response.iter_content(chunk_size=1024):
                        # Play the audio chunk (you can use a media player library for this)
                        print("Playing audio chunk...")
                        time.sleep(0.1)  # Simulate playback
                else:
                    print(f"Failed to stream track: {response.status_code}")
                    break
            except Exception as e:
                print(f"Error while streaming track: {str(e)}")
                break

if __name__ == '__main__':
    stream_soundcloud_track(CLIENT_ID, TRACK_ID)

# starting sooon


from pyrogram import Client, filters
import requests

# Telegram Bot credentials
api_id = 'your_api_id'
api_hash = 'your_api_hash'
bot_token = 'your_bot_token'

# Initialize the Pyrogram client
app = Client('my_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define Terabox API endpoint and credentials
terabox_api_url = 'https://api.terabox.com/upload'
terabox_username = 'your_terabox_username'
terabox_password = 'your_terabox_password'

# Command handler for /upload_video
@app.on_message(filters.regex(pattern=r'https://'))
async def upload_video(client, message):
    try:
        # Check if message contains a video
        if message.video:
            # Download video
            video_path = await message.download()

            # Upload video to Terabox
            files = {'file': open(video_path, 'rb')}
            data = {'username': terabox_username, 'password': terabox_password}
            response = requests.post(terabox_api_url, files=files, data=data)

            # Check if upload was successful
            if response.status_code == 200:
                await message.reply('Video uploaded successfully to Terabox!')
            else:
                await message.reply('Failed to upload video to Terabox.')
        else:
            await message.reply('Please upload a video.')
    except Exception as e:
        await message.reply(f'An error occurred: {e}')

# Start the bot
app.run()


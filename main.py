import requests
import asyncio
from telethon import TelegramClient, events

# 🔥 Telegram Bot Credentials
BOT_TOKEN = "7570457500:AAFZAJ1jMnwkCG-KnUx4TNjBn2WMLi8e8z8"
BOT_USERNAME = "6698364560"

client = TelegramClient("bot_sesn", api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e").start(bot_token=BOT_TOKEN)

# 📌 Auto Delete After 30 Seconds
async def auto_delete(event, message):
    await asyncio.sleep(30)
    await message.delete()

# 📌 /start Command
@client.on(events.NewMessage(pattern=r'^/start(@Enclvebot)?$'))
async def start_handler(event):
    msg = await event.reply(
        "🎉 **Welcome!**\n"
        "- `/rest <gmail/username>` → Get Instagram reset link\n"
        "- `/insta <username>` → Fetch full Instagram profile\n"
    )
    await auto_delete(event, msg)

# 📌 /rest Command (Password Reset)
@client.on(events.NewMessage(pattern=r'^/rest(@Enclvebot)?(?:\s+(.+))?$'))
@client.on(events.NewMessage(pattern=r'^/rest(@Enclvebot)?(?:\s+(.+))?$'))
async def rest_handler(event):
    username_or_email = event.pattern_match.group(2)

    if not username_or_email:
        if event.is_reply:
            replied = await event.get_reply_message()
            username_or_email = replied.text.strip()
        else:
            msg = await event.reply("📌 **Usage: /rest <username or email>**")
            await auto_delete(event, msg)
            return

    msg = await event.reply(f"🔄 Sending reset request for `{username_or_email}`...")

    try:
        url = "https://www.instagram.com/api/v1/web/accounts/send_password_reset/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Referer": "https://www.instagram.com/",
            "Origin": "https://www.instagram.com",
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": "fjpGbVKIVyVXMaLCwQMGVP",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "sessionid=16829956593%3AAb35PnGyCyyuca%3A24%3AAYdZ5xMFraWXM_4iP-r5ScRO9DRht8yLV2hc5E0rzQ;"
        }
        data = {"email_or_username": username_or_email, "recaptcha_challenge": ""}

        response = requests.post(url, headers=headers, data=data)
        print("Response:", response.text)  # Debugging output

        if response.status_code == 200 and '"status":"ok"' in response.text:
            await msg.edit(f"✅ Reset link sent to `{username_or_email}`.")
        else:
            await msg.edit("❌ **Instagram rejected the request. Try again later!**")

    except Exception as e:
        await msg.edit(f"🛑 Error: {str(e)}")

    await auto_delete(event, msg)

# 📌 /insta Command (Fetch Instagram Profile)
@client.on(events.NewMessage(pattern=r'^/insta(@Enclvebot)?(?:\s+(.+))?$'))
async def insta_handler(event):
    username = event.pattern_match.group(2)
    
    if not username:
        if event.is_reply:
            replied = await event.get_reply_message()
            username = replied.text.strip()
        else:
            msg = await event.reply("📌 **Usage: /insta <username>**")
            await auto_delete(event, msg)
            return

    msg = await event.reply(f"🔍 Fetching details for `{username}`...")

    try:
        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        headers = {
            "User-Agent": "Instagram 123.0.0.0 Android",
            "Referer": "https://www.instagram.com/",
            "Origin": "https://www.instagram.com/",
            "X-CSRFToken": "fjpGbVKIVyVXMaLCwQMGVP",
            "Cookie": "sessionid=16829956593%3AAb35PnGyCyyuca%3A24%3AAYdZ5xMFraWXM_4iP-r5ScRO9DRht8yLV2hc5E0rzQ"
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            await msg.edit(f"🛑 Profile could be banned or doesn't exist.")
            await auto_delete(event, msg)
            return

        user_data = response.json().get("data", {}).get("user", {})
        if not user_data:
            await msg.edit(f"🛑 Profile could be banned or doesn't exist.")
            await auto_delete(event, msg)
            return

        profile_pic = user_data.get("profile_pic_url_hd", "")
        bio = user_data.get("biography", "N/A")
        full_name = user_data.get("full_name", "N/A")
        followers = user_data.get("edge_followed_by", {}).get("count", 0)
        following = user_data.get("edge_follow", {}).get("count", 0)
        posts = user_data.get("edge_owner_to_timeline_media", {}).get("count", 0)
        is_private = user_data.get("is_private", False)
        is_verified = user_data.get("is_verified", False)
        is_business = user_data.get("is_professional", False)
        business_category = user_data.get("business_category_name", "N/A")
        external_url = user_data.get("external_url", "N/A")

        result = (
            f"<b>📸 Instagram Profile Info</b>\n"
            f"<blockquote>"
            f"👤 <b>Name:</b> {full_name}<br>"
            f"🔗 <b>Username:</b> @{username}<br>"
            f"📜 <b>Bio:</b> {bio}<br>"
            f"🔗 <b>Website:</b> {external_url}<br>"
            f"👥 <b>Followers:</b> {followers}<br>"
            f"👥 <b>Following:</b> {following}<br>"
            f"📮 <b>Posts:</b> {posts}<br>"
            f"🔒 <b>Private:</b> {is_private}<br>"
            f"✅ <b>Verified:</b> {is_verified}<br>"
            f"🏢 <b>Business Account:</b> {is_business}<br>"
            f"📂 <b>Business Category:</b> {business_category}"
            f"</blockquote>"
        )

        if profile_pic:
            await client.send_message(event.chat_id, result, file=profile_pic, parse_mode='html')
            await msg.delete()
        else:
            await msg.edit(result, parse_mode='html')

        await auto_delete(event, msg)

    except Exception as e:
        await msg.edit(f"🛑 Error: {str(e)}")
        await auto_delete(event, msg)

print("🚀 Bot is running...")
client.run_until_disconnected()

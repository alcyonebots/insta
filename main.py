import requests
from telethon import TelegramClient, events

# 🔥 Replace with your actual Telegram Bot Token & Username
BOT_TOKEN = "7570457500:AAFZAJ1jMnwkCG-KnUx4TNjBn2WMLi8e8z8"
BOT_USERNAME = "iskdlapaldnskqlpsdlksbot"

# 🔥 Replace with your actual API credentials
API_ID = 6
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

client = TelegramClient("bot_session", api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)

class Reset:
    def __init__(self):
        self.url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
        self.headers = {
            "authority": "www.instagram.com",
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": "csrftoken=BbJnjd.Jnw20VyXU0qSsHLV; mid=ZpZMygABAAH0176Z6fWvYiNly3y2; ig_did=BBBA0292-07BC-49C8-ACF4-AE242AE19E97;",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/accounts/password/reset/?source=fxcal",
            "user-agent": "Mozilla/5.0 (Linux; Android 10)",
            "x-csrftoken": "BbJnjd.Jnw20VyXU0qSsHLV",
            "x-instagram-ajax": "1015181662",
            "x-requested-with": "XMLHttpRequest"
        }

    def send(self, email):
        data = {"email_or_username": email, "flow": "fxcal"}
        response = requests.post(self.url, headers=self.headers, data=data)
        try:
            return response.json()
        except Exception as e:
            return {"error": str(e)}

reset_handler = Reset()

# 📌 /start Command
@client.on(events.NewMessage(pattern=r'^/start(@' + BOT_USERNAME + r')?$'))
async def start_handler(event):
    msg = await event.reply(
        "🎉 **Welcome!**\n"
        "- `/rest <gmail/username>` → Get Instagram reset link\n"
        "- `/insta <username>` → Fetch full Instagram profile\n"
    )

# 📌 /rest Command (Password Reset)
@client.on(events.NewMessage(pattern=r'^/rest(@' + BOT_USERNAME + r')?(?:\s+(.+))?$'))
async def rest_handler(event):
    username_or_email = event.pattern_match.group(2)

    if not username_or_email:
        if event.is_reply:
            replied = await event.get_reply_message()
            username_or_email = replied.text.strip()
        else:
            await event.reply("📌 **Usage: /rest <username or email>**")
            return

    msg = await event.reply(f"🔄 Sending reset request for `{username_or_email}`...")

    try:
        result = reset_handler.send(username_or_email)
        if "status" in result and result["status"] == "ok":
            await msg.edit(f"✅ Reset link sent to `{username_or_email}`.")
        else:
            await msg.edit(f"❌ Instagram rejected the request: {result}")
    except Exception as e:
        await msg.edit(f"🛑 Error: {str(e)}")

# 📌 /insta Command (Fetch Instagram Profile)
@client.on(events.NewMessage(pattern=r'^/insta(@' + BOT_USERNAME + r')?(?:\s+(.+))?$'))
async def insta_handler(event):
    if not await check_membership(event):
        return

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
            f"<b>📸 Instagram Profile Info</b><br>"
            f"<blockquote>"
            f"<b>👤Name:</b> {full_name}<br>\n"
            f"<b>🔗 Username:</b> @{username}<br>\n"
            f"<b>📜 Bio:</b> {bio}<br>\n"
            f"<b>🔗 Website:</b> {external_url}\n<br>"
            f"<b>👥 Followers:</b> {followers}\n<br>"
            f"<b>👥 Following:</b> {following}\n<br>"
            f"<b>📮 Posts:</b> {posts}<br>\n"
            f"<b>🔒 Private:</b> {is_private}<br>\n"
            f"<b>✅ Verified:</b> {is_verified}<br>\n"
            f"<b>🏢 Business Account:</b> {is_business}<br>\n"
            f"<b>📂 Business Category:</b> {business_category}</blockquote>"
        )

        if profile_pic:
            await client.send_file(event.chat_id, profile_pic, caption=result, parse_mode='html')
            await msg.delete()
        else:
            await msg.edit(result, parse_mode='html')

        await auto_delete(event, msg)

    except Exception as e:
        await msg.edit(f"🛑 Error: {str(e)}")
        await auto_delete(event, msg)

print("🚀 Bot is running...")
client.run_until_disconnected()

from telethon import events
from config import ADMINS
from database import get_all_users, total_users

BROADCAST = {}

def setup_admin(client):

    # ===================== STATS =====================
    @client.on(events.NewMessage(pattern=r"^/stats$"))
    async def stats(event):
        if event.sender_id not in ADMINS:
            return
        count = total_users()
        await event.reply(f"📊 **Bot Stats**\n\n👥 Total Users: {count}")

    # ===================== BROADCAST START =====================
    @client.on(events.NewMessage(pattern=r"^/broadcast$"))
    async def broadcast(event):
        if event.sender_id not in ADMINS:
            return

        BROADCAST[event.sender_id] = True
        await event.reply(
            "📢 **Broadcast mode ON**\n"
            "Send your message.\n"
            "Use /cancel to stop."
        )

    # ===================== CANCEL =====================
    @client.on(events.NewMessage(pattern=r"^/cancel$"))
    async def cancel(event):
        if event.sender_id not in ADMINS:
            return

        BROADCAST.pop(event.sender_id, None)
        await event.reply("❌ Broadcast cancelled.")

    # ===================== HANDLE BROADCAST MESSAGE =====================
    @client.on(events.NewMessage(func=lambda e: e.sender_id in ADMINS))
    async def admin_follow(event):
        uid = event.sender_id
        txt = event.raw_text

        if txt.startswith("/"):
            return

        if uid in BROADCAST:
            sent = failed = 0

            for user in get_all_users():
                try:
                    await client.send_message(user, txt)
                    sent += 1
                except:
                    failed += 1

            BROADCAST.pop(uid)

            await event.reply(
                f"📢 **Broadcast Complete**\n"
                f"✅ Sent: {sent}\n"
                f"❌ Failed: {failed}"
            )

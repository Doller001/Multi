from telethon import events, Button
from database import add_user
from config import REQUIRED_CHANNELS

def setup_handlers(client):

    # START COMMAND
    @client.on(events.NewMessage(pattern="/start"))
    async def start(event):
        user = await event.get_sender()
        add_user(user.id, user.first_name)

        btns = []

        for ch in REQUIRED_CHANNELS:
            btns.append([Button.url("📢 Join Channel", ch["link"])])

        btns.append([Button.inline("✅ Joined", b"joined")])

        msg = (
            "✅ **Welcome to the Tool Hub!**\n\n"
            "Press **Joined** to access all tools."
        )

        await event.reply(msg, buttons=btns)

    # JOINED → SHOW STATIC TOOL LINKS
    @client.on(events.CallbackQuery(pattern=b"^joined$"))
    async def joined(event):

        tools = [
            ("🖼️ Undress Images", "https://t.me/Undress_imagesss_bot?start=7764057183"),
            ("🎥 Undress Videos", "https://t.me/Undress_videosss_bot?start=7764057183"),
            ("📞 Number Info", "https://t.me/get_info_number0_bot?start=EvsgKeW"),
            ("ℹ️ Telegram Info", "https://t.me/Tg_apna_haibot?start=_ref_petGrMcsK_zhtQD2DsP"),
            ("📞 Number Info 2", "https://t.me/divine_lookup_rbot?start=7764057183"),
            ("🚗 Vehicle Info", "https://t.me/rtovehicledetailsbot?start=A7B9B57D"),
            ("🔍 Search Tool", "https://t.me/searchanything11_bot?start=REFA82748"),
            ("💻 Hacking Tool", "https://t.me/Kali_Hacking_Bot?start=e1b5a0"),
            ("🖥️ Hacking Tool 2", "https://t.me/KaIi_Linux_BOT?start=10c386b45482476a"),
            ("🔗 CH Link", "https://gplinks.co/UfVcpI"),
            ("🎮 Fax Game", "https://gplinks.co/pHNHOPE"),
            ("📸 Instagram Hacks", "https://gplinks.co/JAEydxk"),
            ("🐍 Python Course", "https://t.me/+D2jcnX6xBYU0NTU1"),
            ("🔥 Horn Videos", "https://t.me/+PAkGTQ7W_zljM2E9"),
            ("☎️ Fake Numbers", "https://t.me/Kali_Number_BOT?start=7764057183")
        ]

        buttons = [[Button.url(title, url)] for title, url in tools]

        await event.edit("✅ **Access Granted**\n👇 Select any tool:", buttons=buttons)

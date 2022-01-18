import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

class Translation(object):
    START_TEXT = f"""<b>Hᴇʟʟᴏ ,</b>
    
<b>I ᴀᴍ ᴀ Mᴇɢᴀ Lɪɴᴋ Dᴏᴡɴʟᴏᴀᴅᴇʀ Bᴏᴛ</b>

<b>𝐉ᴜ𝐬ᴛ 𝐄ɴᴛᴇʀ 𝐘ᴏᴜʀ 𝐌ᴇɢᴀ.𝐍ᴢ 𝐋ɪɴᴋ 𝐀ɴᴅ 𝐈 𝐖ɪʟʟ 𝐑ᴇᴛᴜʀɴ 𝐓ʜᴇ 𝐅ɪʟᴇ/𝐕ɪᴅᴇᴏ 𝐓ᴏ 𝐘ᴏᴜ!😇</b>

<b>💠 𝐈 𝐂ᴀɴ 𝐒ᴇᴛ 𝐂ᴜ𝐬ᴛᴏᴍ 𝐂ᴀᴘᴛɪᴏɴ𝐬 𝐀ɴᴅ 𝐂ᴜ𝐬ᴛᴏᴍ 𝐓ʜᴜᴍʙɴᴀɪʟ𝐬 𝐓ᴏᴏ!</b>

<b>💠 𝐈 𝐂ᴀɴ 𝐃ᴏᴡɴʟᴏᴀᴅ 𝐋ɪɴᴋ𝐬 𝐖ʜɪᴄʜ 𝐀ʀᴇ 𝐁ɪɢɢᴇʀ 𝐓ʜᴀɴ 𝟸𝐆𝐁 𝐓ᴏᴏ! 😍</b>

<b>Pʀᴇss /help Fᴏʀ Mᴏʀᴇ Dᴇᴛɪᴀʟs!</b>

✨ <b>𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗔𝗡𝗗 𝗠𝗔𝗧𝗜𝗡𝗔𝗘𝗗 𝗕𝗬 @KOT_FREE_DE_LA_HOYA_OFF</b>"""
    
    NOT_AUTH_TXT = "<b>⚠️ Unauthorized Access ⚠️</b>\nYou're not Auth User. So You Can't Use the Core " \
                   "components of this Bot. Inconvenience is regretted!"
    DOWNLOAD_START = "<b>Downloading to my server now 📥</b> \n\n<code>Please wait uploading will start as soon as possible😇...</code>"
    UPLOAD_START = "Uploading to Telegram now 📤..."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS =  "Downloaded in <b>{}</b> seconds.\n\nUploaded in <b>{}</b> seconds.\n\n<b>Thanks For Using This Free Service</b>"
    SAVED_CUSTOM_THUMB_NAIL = "𝗖𝘂𝘀𝘁𝗼𝗺 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗜𝘀 𝗦𝗮𝘃𝗲𝗱. 𝗧𝗵𝗶𝘀 𝗜𝗺𝗮𝗴𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗨𝘀𝗲𝗱 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗡𝗲𝘅𝘁 𝗨𝗽𝗹𝗼𝗮𝗱𝘀 📁.\n\nIf you want to delete it send\n /deletethumbnail anytime!"
    DEL_ETED_CUSTOM_THUMB_NAIL = "𝗖𝘂𝘀𝘁𝗼𝗺 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗖𝗹𝗲𝗮𝗿𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ❌.\nYou will now get an auto generated thumbnail for your video uploads!"

    HELP_USER = f"""<b><u>🍁Hi I am a Mega Link Downloader Bot.. 🍁</u></b>
 
<u>How to use me:-</u>

<b>Just Send me a mega.nz file link!</b>

<b>Important:-</b> 

- Folder links are not supported.

- Your link should be valid(not expired or been removed) and should not be password protected or encrypted or private!

❇️ <b>If you want a custom thumbnail for your uploads send a photo before sending the mega link!.</b> <i>(This step is Optional)</i>

💠 It means it is not necessary to send an image to include as an thumbnail.
If you don't send a thumbnail the video/file will be uploaded with an auto genarated thumbnail from the video.
The thumbnail you send will be used for your next uploads!

press /deletethumbnail if you want to delete the previously saved thumbnail.
(Then the video will be uploaded with an auto-genarated thumbnail!)

❇️ <b>Special feature</b> :- <i>Set caption to any file you want!</i>

💠 Select an uploaded file/video or forward me <b>Any Telegram File</b> and Just write the text you want to be on the file as a reply to the File by selecting it (as replying to a message😅) and the text you wrote will be attached as caption!😍

Ex:- <a href="https://telegra.ph/file/ba0abc119d4142ae54111.jpg">Send Like This! It's Easy🥳</a>

<b>Note</b> :- You can download links which are bigger than 2GB from me too! Due to telegram API limits I can't upload files which are bigger than 2GB so I will split such files and upload them to you!

✨ <b>𝗕𝗢𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗔𝗡𝗗 𝗠𝗔𝗧𝗜𝗡𝗔𝗘𝗗 𝗕𝗬 @KOT_FREE_DE_LA_HOYA_OFF</b>"""

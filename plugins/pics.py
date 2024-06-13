import os
from pyrogram import Client,filters
from telegraph import upload_file

@Client.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("**Uploading To Telegraph...**")
    download_location = await client.download_media(
        message=message, file_name='root/Database')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("**Photo Size Should Be Less Than 5mb!**") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)
@Client.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/Database')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)
@Client.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/Database')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}**',
            disable_web_page_preview=False,
                           )

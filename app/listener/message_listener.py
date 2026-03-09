
from app.services.torrent_service import TorrentService
from app.utils.telebot_util import TelebotUtil
from app.services.telebot_service import TelebotService
from telebot.types import Message
from app.settings.config import Config
from app.exceptions.torrent_exception import NoSourceFound, NoMetadataFound

class MessageListener:
    def __init__(self, config: Config):
        self.torrent_service = TorrentService()
        self.telebot_service = TelebotService(api_key=config.tele_api_key)
        self.telebot_service.register(callback= self._handle_start,commands=["hi","start"])
        self.telebot_service.register(callback= self._handle_stop,commands=["stop","exit"])
        self.telebot_service.register(callback= self._handle_torrent_download,commands=["tm","tormirror"])

    def start_polling(self):
        print("Starting polling")
        self.telebot_service.start()

    def _handle_start(self, message: Message):
        if message.reply_to_message:
            self.telebot_service.reply_to(message.reply_to_message,"This is telegram bot for torrent to gdrive")
        else:
            self.telebot_service.reply_to(message,"This is telegram bot for torrent to gdrive")

    def _handle_stop(self, message: Message):
        self.telebot_service.send_message(message.chat.id,"Shutting Down")
        # self.bot.stop_polling()
        self.telebot_service.stop_bot()

    def _handle_torrent_download(self, message: Message):
        text = TelebotUtil.getMessageText(message=message)
        link = TelebotUtil.extractLink(text=text)
        if(link):
            reply = self.telebot_service.reply_to(message=message,reply="Starting")
            try:
                handle = self.torrent_service.download(link=link)
            except NoSourceFound as e:
                self.telebot_service.edit_message(message=reply,edit_text="No download source found")
            except NoMetadataFound as e:
                self.telebot_service.edit_message(message=reply,edit_text="Unable to fetch metadata")
            
            if(handle):
                for status in self.torrent_service.status_handler(handle=handle):
                    self.telebot_service.edit_message(message=reply,edit_text="Downloading {%s}" % status.progress)
                else:
                    self.telebot_service.delete_message(reply)
                    self.telebot_service.send_message(message.chat.id,"Upload COMPLETED\n\n{0}\nCheck Here : {1}\n\n\nReady To Go Again".format(handle.name(), 'gdlink'))
        
        # self.telebot_service.send_message(message.chat.id,"Shutting Down")
from vidstream import AudioSender
from vidstream import AudioReceiver

import threading
import socket

#ip = socket.gethostbyname(socket.gethostname())

receiver = AudioReceiver('ip two', 9090 )
receiver_thread = threading.Thread(target=receiver.start_server)


#sender = AudioSender('ip one', 9999)
#sender_thread = threading.Thread(target=sender.start_stream)


receiver_thread.start()
#sender_thread.start
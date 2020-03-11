#!/usr/bin/env python

import sys
import codecs

# A file to be used to save the message from the app.
f = open("C:/Users/yong wei/Documents/BT garage/Blueprint/host/temp.txt", "w")
# g = open("C:/Users/yong wei/Documents/BT garage/Blueprint/host/temp1.txt", "w")

while 1:
    # # First four bytes from app notify us of the message's length.
    text_length_bytes = sys.stdin.read(4)

    # # # Unpack the text length WITHOUT using struct.unpack.
    text_length = ord(text_length_bytes[0])

    # # # Get the message from the app.
    messFromApp = codecs.decode(sys.stdin.read(text_length), "utf-8")

    # # # Save the message from the app to a file.
    # f.write(messFromApp)
    # f.flush()

#   #We will notify the app of the length of the message sent to the program from the app.
#   returnValue = str(text_length - 11)
#   text = '{"text":" Thanks for the message of ' + returnValue + ' characters."}'

#   #Calculate length of the message you are sending back, and do some formatting.
#   inLength = hex(len(text)).replace('0x','')

#   #Pad with bytes, for little-endian.
#   if len(inLength) < 1.5:
#      inLength = '0'+inLength

#   inLength = inLength + '000000'

#   #Pack the message length WITHOUT using struct.pack.
#   inLength = codecs.decode(inLength, "hex")

#   #Write to the stream the message length and the message contents.
#   sys.stdout.write(inLength)
#   sys.stdout.write(text)
#   sys.stdout.flush()

import pywhatkit as pw
txt="""pywhatkit is a Python library that allows you to perform various fun and practical automation tasks, such as:

    Sending WhatsApp messages

    Performing Google searches

    Playing YouTube videos

    Converting images to ASCII art

    Getting information from Wikipedia

    Taking screenshots

    It's designed to be simple and useful for beginners or small automation scripts. """

pw.text_to_handwriting(txt, "Demo1.png", [0,0,138])
print("End")

import aiml
# membuat kernel dan mempelajari berkas AIML
kernel = aiml.Kernel()
kernel.learn("start.xml")
kernel.respond("aiml a")
while True:
    print(kernel.respond(input("Tuliskan pesan di sini: >> ")).upper())
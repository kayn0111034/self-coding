print("(0) Caesar Cipher")
choose=int(input("Which cipher do you want to use?"))

if choose==0:
    text=input("Please enter text for the encryption: ")
    rotate_num=int(input("How many times would you like to rotate your text?"))
    start = time.time()
    print(caesar_cipher(text,rotate_num))
    end = time.time()
    print(f"It took {end-start} seconds to encrypt your text")
else:
    text=input("Please enter text for the encryption: ")
    rotate_num=int(input("How many times would you like to rotate your text?"))
    start = time.time()
    print(caesar_cipher(text,rotate_num))
    end = time.time()
    print(f"It took {end-start} seconds to encrypt your text")

from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import string
from django.urls import reverse
from time import sleep
import itertools
from Crypto.Cipher import Blowfish
import string




def index(request):
    return render(request, 'Main/index.html', context={})




def rsa_index(request):
    return render(request, 'Main/rsa_index.html', context={})


def encode(request):
    result = ''
    bresult = ''
    if request.method == 'POST':
        form = CipherForm(request.POST)
        if form.is_valid():
            keyPair = RSA.generate(3072)

            pubKey = keyPair.publickey()
            print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
            pubKeyPEM = pubKey.exportKey()
            print(pubKeyPEM.decode('ascii'))

            print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
            privKeyPEM = keyPair.exportKey()
            print(privKeyPEM.decode('ascii'))

            encryptor = PKCS1_OAEP.new(pubKey)
            data = form.cleaned_data["text"]
            print(data)
            encrypted = encryptor.encrypt(data.encode('utf-8'))
            print(binascii.hexlify(encrypted))
            # dec = encryptor.encrypt(data)
            # print(encrypted)
            form.save()
            result = binascii.hexlify(encrypted)
            bresult = encrypted


            # decryptor = PKCS1_OAEP.new(keyPair)
            # decrypted = decryptor.decrypt(dec)
            # print('Decrypted:', decrypted)

    form = CipherForm()
    return render(request, 'Main/rsa_encode.html', context={'form': form, 'result': result, 'bresult': bresult})







def decode(request):
    decrypted = ''
    if request.method == 'POST':
        form = CipherForm(request.POST)
        if form.is_valid():
            keyPair = RSA.generate(3072)

            pubKey = keyPair.publickey()
            print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
            pubKeyPEM = pubKey.exportKey()
            print(pubKeyPEM.decode('ascii'))
            #
            # print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
            # privKeyPEM = keyPair.exportKey()
            # print(privKeyPEM.decode('ascii'))
            #
            # data = form.cleaned_data["text"]
            # print(data)
            # print(binascii.hexlify(encrypted))
            # # dec = encryptor.encrypt(data)
            # # print(encrypted)
            # form.save()
            # result = binascii.hexlify(encrypted)

            data = form.cleaned_data["text"]
            print(data)
            encryptor = PKCS1_OAEP.new(pubKey)
            encrypted = encryptor.encrypt(data.encode('utf-8'))

            decryptor = PKCS1_OAEP.new(keyPair)
            # decrypted = decryptor.decrypt(data)
            print('Decrypted:', decrypted)

    form = CipherForm()
    return render(request, 'Main/rsa_decode.html', context={'form': form, 'result': decrypted})




def caesar_index(request):
    return render(request, 'Main/caesar_index.html', context={})



def caesar_encode(request):
    encrypt = ''
    if request.method == 'POST':
        form = CipherForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["text"]
            print(data)
            s = form.cleaned_data["key"]
            for i in range(len(data)):
                char = data[i]
                if (char.isupper()):
                    encrypt += chr((ord(char) + s-65) % 26 + 65)
                else:
                    encrypt += chr((ord(char) + s - 97) % 26 + 97)
            # return HttpResponseRedirect(reverse('caesar_encode_url'))
            print(encrypt)
    form = CipherForm()
    context = {
        'result': encrypt,
        'form': form
    }
    return render(request, 'Main/caesar_encode.html', context=context)



def caesar_decode(request):
    alphabet = string.ascii_lowercase
    decrypted_message = ''
    if request.method == 'POST':
        form = CipherForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["text"]
            print(data)
            key = form.cleaned_data["key"]
            for c in data:
                if c in alphabet:
                    position = alphabet.find(c)
                    new_position = (position - key) % 26
                    new_character = alphabet[new_position]
                    decrypted_message += new_character
                else:
                    decrypted_message += c

    form = CipherForm()
    return render(request, 'Main/caesar_decode.html', context={'form':form, 'result': decrypted_message})



def vigenere_index(request):
    return render(request, 'Main/vigenere_index.html', context={})



def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))



def vigenere_encode(request):
    result = ''
    if request.method == 'POST':
        form = CipherForm(request.POST)
        if form.is_valid():
            plaintext = form.cleaned_data["text"]
            key = form.cleaned_data["vig_key"]
            key_length = len(key)
            key_as_int = [ord(i) for i in key]
            plaintext_int = [ord(i) for i in plaintext]
            ciphertext = ''
            for i in range(len(plaintext_int)):
                value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
                ciphertext += chr(value + 65)
            print(ciphertext)
            result = ciphertext

    form = CipherForm()
    return render(request, 'Main/vigenere_encode.html', context={'form':form, 'result':result})



def vigenere_decode(request):
    result = ''
    if request.method == 'POST':
        form = CipherForm(request.POST)
        if form.is_valid():
            encrypt_text = form.cleaned_data["text"]
            key = form.cleaned_data["vig_key"]
            orig_text = []
            for i in range(len(encrypt_text)):
                x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
                x += ord('A')
                orig_text.append(chr(x))
            result = "" . join(orig_text)

    form = CipherForm()
    return render(request, 'Main/vigenere_decode.html', context={'form':form, 'result':result})



def blowfish_index(request):
    return render(request, 'Main/blowfish_index.html', context={})





def blowfish_encode(request):
    result = ''
    if request.method == 'POST':
        form = CipherForm(request.POST)
        print("0")
        if form.is_valid():
            s = form.cleaned_data["text"]
            key = form.cleaned_data["key"]
            cipher = Blowfish.new(32, mode)
            print(cipher)
            encrypted_data = cipher.encrypt("0123data")
            print(encrypted_data)
        print(form.errors)
    form = CipherForm()
    return render(request, 'Main/blowfish_encode.html', context={'form':form, 'result':result})



# def playfair_decode(request):
#     result = ''
#     if request.method == 'POST':
#         form = CipherForm(request.POST)
#         if form.is_valid():
#             ciphertext = form.cleaned_data["text"]
#             key = form.cleaned_data["vig_key"]
#             table = generate_table(key)
#             plaintext = ""
#
#             for char1, char2 in chunker(ciphertext, 2):
#                 row1, col1 = divmod(table.index(char1), 5)
#                 row2, col2 = divmod(table.index(char2), 5)
#
#                 if row1 == row2:
#                     ciphertext += table[row1 * 5 + (col1 + 1) % 5]
#                     ciphertext += table[row2 * 5 + (col2 + 1) % 5]
#                 elif col1 == col2:
#                     ciphertext += table[((row1 + 1) % 5) * 5 + col1]
#                     ciphertext += table[((row2 + 1) % 5) * 5 + col2]
#                 else:  # rectangle
#                     ciphertext += table[row1 * 5 + col2]
#                     ciphertext += table[row2 * 5 + col1]
#             print(ciphertext)
#
#
#     form = CipherForm()
#     return render(request, 'Main/playfair_decode.html', context={'form':form, 'result':result})

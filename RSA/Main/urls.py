from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index_url'),
    path('rsa/', rsa_index, name='rsa_index_url'),
    path('rsa/encode/', encode, name='encode_url'),
    path('rsa/decode/', decode, name='decode_url'),
    path('caesar/', caesar_index, name='caesar_index_url'),
    path('caesar/encode/', caesar_encode, name='caesar_encode_url'),
    path('caesar/decode/', caesar_decode, name='caesar_decode_url'),
    path('vigenere/', vigenere_index, name='vigenere_index_url'),
    path('vigenere/encode/', vigenere_encode, name='vigenere_encode_url'),
    path('vigenere/decode/', vigenere_decode, name='vigenere_decode_url'),
    path('blowfish/', blowfish_index, name='blowfish_index_url'),
    path('blowfish/encode/', blowfish_encode, name='blowfish_encode_url'),
    path('blowfish/decode/', blowfish_encode, name='blowfish_decode_url'),


]

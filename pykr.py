"""Copyright (c) 2010, David Peter, Grant Mathews
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list
of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or other
materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

This product uses the Flickr API but is not endorsed or certified by Flickr.
"""
HOST = None

__all__ = [ 'Flickr' ]

class Flickr(object):
    photos = "I'm beautiful."
    def __init__(self, api_key):
        self.api_key = api_key


##################################
# Short URLs
##################################

alphabet = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'

def surl_encode(p_id):
    encoded = ''
    base = 58
    while p_id:
        encoded = alphabet[p_id%base] + encoded
        p_id /= base
    return "http://flic.kr/p/%s"%encoded

def surl_decode(surl):
    p_id = 0
    multi = 1
    base = 58
    index = len(surl) - 1
    while index >= 0:
        p_id += multi * alphabet.find(surl[index])
        multi *= base
        index -= 1
    return p_id

print surl_encode(3707787591)
print surl_decode("6DDo5g")
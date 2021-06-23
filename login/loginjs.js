 newEncrypt = function(l) {
    var n = p.enc.Utf8.parse("pdTY2wfQwiY6iQ6N")
      , t = p.enc.Utf8.parse("pdTY2wfQwiY6iQ6N")
      , e = p.enc.Utf8.parse(l)
      , a = p.AES.encrypt(e, n, {
        iv: t,
        mode: p.mode.CBC,
        padding: p.pad.Pkcs7
    });
    return p.enc.Base64.stringify(a.ciphertext)
}
function getpwd(b){
    return newEncrypt(b);
}

// privaKey:pdTY2wfQwiY6iQ6N
//              Encrypt: function(l) {
//                         var n = p.enc.Utf8.parse("t171420100302rsa")
//                           , t = p.enc.Utf8.parse("t171420100302rsa")
//                           , e = p.enc.Utf8.parse(l)
//                           , a = p.AES.encrypt(e, n, {
//                             iv: t,
//                             mode: p.mode.CBC,
//                             padding: p.pad.Pkcs7
//                         });
//                         return p.enc.Base64.stringify(a.ciphertext)
//                     }
//                 };
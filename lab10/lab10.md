# 1

$p = 14086963408384851001$

$q = 16670813262138239653$

$\phi(n) = (p - 1) (q - 1) = 234841136411758272970005817684311852000$

$e = 65537$

$$Folosind\ proprietatea\ ca\ d = \frac{\phi(n)\times{k} + 1}{e},\ reiese\
d = 131139372709478887666895441874581979136$$

# 2

## a)

```sh
$ openssl genrsa -out alice_sk.pem 2048
```

## b) 

```sh
$ openssl rsa -in alice_sk.pem -text -noout
```

``65537``

## c)

### valoarea modului $N$
```sh
$ openssl rsa -in alice_sk.pem -modulus -noout
```
```
modulus:
    00:b5:93:58:3c:4c:f1:e0:a8:fd:41:91:c0:96:e4:
    31:c7:62:01:70:d7:22:3b:e8:1a:69:c1:77:a5:c2:
    ac:d9:c2:2a:a0:8c:75:4c:d6:3d:38:22:c9:ee:38:
    33:ef:77:76:dd:be:be:8b:c0:a8:56:05:6b:48:a1:
    99:bc:26:81:f4:09:57:c0:e4:31:70:b7:a3:bd:46:
    e4:9d:73:4d:7d:17:33:e7:f8:49:97:7e:10:66:52:
    19:d9:50:18:e3:89:6b:80:ad:97:7b:9c:b7:59:0f:
    0d:5b:13:52:54:71:c8:fb:76:af:89:d8:f3:e8:6d:
    9c:94:0c:ef:23:f9:e6:f0:ee:31:25:8c:ae:90:2c:
    d4:0c:7b:70:c5:8a:f0:fd:08:b3:b6:25:94:a3:90:
    39:19:6c:51:36:bb:1e:86:61:c8:33:1c:ed:e0:81:
    c8:23:33:d6:bd:47:12:98:5d:8e:fc:57:3f:b7:b5:
    3d:d3:7f:8f:7f:1e:c1:11:57:93:78:03:d8:17:e7:
    09:4f:bb:19:83:a0:1b:7c:05:77:55:45:fb:ee:2b:
    f1:9b:29:15:ad:34:ba:be:c8:10:e3:e5:7d:12:35:
    5b:58:1a:20:c2:d9:f8:12:69:40:e3:d1:6f:01:9f:
    af:f2:c1:7a:ae:54:52:aa:46:31:a8:a5:d2:20:07:
    09:67

```

### valoarea numerelor prime
```sh
$ openssl rsa -in alice_sk.pem -noout -text | grep -E 'prime[0-9]+' -A 9
```

```
prime1:
    00:fe:39:3e:a1:7d:4a:7f:50:7b:a6:ee:9c:e0:df:
    80:5d:65:a5:c4:cb:7d:2a:8c:f2:15:7e:b3:ba:d9:
    ca:46:96:05:94:48:82:9e:fb:e3:4d:7a:39:a1:cc:
    25:63:4f:0a:53:ba:f7:57:08:75:a6:23:28:62:ff:
    66:05:08:1e:80:0b:91:e4:a9:fa:a9:e9:d5:62:6f:
    a9:e4:c5:1b:39:45:5b:8c:f5:c8:93:40:82:1b:ee:
    dd:69:4d:8f:b2:0b:79:e9:3b:a8:7f:2e:97:d9:dc:
    78:e9:50:fd:8f:40:8e:e4:36:67:07:0a:76:28:fb:
    c7:62:83:76:5e:5c:60:30:af
prime2:
    00:b6:d8:25:ab:90:53:67:3d:23:da:25:ed:97:64:
    86:8d:0b:ee:a5:d1:d8:7d:d9:28:71:e0:b4:4d:88:
    6b:6f:a0:9a:c2:fa:82:4a:29:b9:06:05:81:14:30:
    c8:c7:f3:81:d3:f9:6e:71:3b:c2:db:f5:96:3a:fa:
    66:b3:94:dd:bc:ea:c5:68:d5:b4:3b:cf:0b:99:8b:
    a7:97:3f:64:2c:9f:45:fa:e2:4d:27:8f:b6:72:4f:
    3f:3e:42:77:26:13:72:54:1a:e1:18:1a:93:12:4a:
    87:fe:59:10:80:65:b1:b2:d4:ab:3a:83:3f:eb:30:
    0f:46:86:c8:3b:7e:a0:30:c9
```


## d)

```sh
$ openssl rsa -aes256 -in alice_sk.pem -out alice_prot_sk.pem
```

## e) 

#### Lungimea cheii protejate este mai mare

```sh
$ openssl rsa -in alice_prot_sk.pem
```

## f) 

#### Poate mitiga accesul neautorizat

```sh
$ openssl rsa -in alice_prot_sk.pem -text -noout
```

``65537``

## g)

```sh
$ openssl rsa -pubin -in alice_pk.pem -modulus -noout
```

```
Modulus:
    00:b5:93:58:3c:4c:f1:e0:a8:fd:41:91:c0:96:e4:
    31:c7:62:01:70:d7:22:3b:e8:1a:69:c1:77:a5:c2:
    ac:d9:c2:2a:a0:8c:75:4c:d6:3d:38:22:c9:ee:38:
    33:ef:77:76:dd:be:be:8b:c0:a8:56:05:6b:48:a1:
    99:bc:26:81:f4:09:57:c0:e4:31:70:b7:a3:bd:46:
    e4:9d:73:4d:7d:17:33:e7:f8:49:97:7e:10:66:52:
    19:d9:50:18:e3:89:6b:80:ad:97:7b:9c:b7:59:0f:
    0d:5b:13:52:54:71:c8:fb:76:af:89:d8:f3:e8:6d:
    9c:94:0c:ef:23:f9:e6:f0:ee:31:25:8c:ae:90:2c:
    d4:0c:7b:70:c5:8a:f0:fd:08:b3:b6:25:94:a3:90:
    39:19:6c:51:36:bb:1e:86:61:c8:33:1c:ed:e0:81:
    c8:23:33:d6:bd:47:12:98:5d:8e:fc:57:3f:b7:b5:
    3d:d3:7f:8f:7f:1e:c1:11:57:93:78:03:d8:17:e7:
    09:4f:bb:19:83:a0:1b:7c:05:77:55:45:fb:ee:2b:
    f1:9b:29:15:ad:34:ba:be:c8:10:e3:e5:7d:12:35:
    5b:58:1a:20:c2:d9:f8:12:69:40:e3:d1:6f:01:9f:
    af:f2:c1:7a:ae:54:52:aa:46:31:a8:a5:d2:20:07:
    09:67
Exponent: 65537 (0x10001)
```

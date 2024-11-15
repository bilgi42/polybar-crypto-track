# polybar-crypto-track
An extension for tracking your own cryptocurreny wallets in polybar

![image](https://github.com/user-attachments/assets/5d9ecfa8-4f4d-4cd2-a78a-c71c5831a7e5)

It can show various cryptocurrencies converted in various currencies.\
For example:\
[ADA/JPY]\
[LTC/EUR]\
[BTC/TRY]

# Installation
```
git clone https://github.com/bilgi42/polybar-crypto-track.git &&
    cd polybar-crypto-track &&
    mkdir -p ~/.config/polybar &&
    cp ./crypto-tracker.py ~/.config/polybar &&
    sudo chmod u+x ~/.config/polybar/crypto-track.py
```

After that, you have to add this module to polybar's config

```

modules-left = crypto-track


[module/crypto-track]
type = custom/script
interval = 300
exec = ~/.config/polybar/crypto-track.py

```

# Post Installation and Config

All the configs can be found in the Python file. Please edit the Python file for coin address, type and pairings.

### Řešení osmého cvičení Základů kryptografie
-------------
## 1
SHA1 = 160 bitů, MD5 = 128 bitů

2<sup>160</sup>/2<sup>128</sup> = 2<sup>32</sup> = 4 294 967 296

## 2
- zpráva je rozdělena do bloků
- každý blok je šifrován samostatně
- možný útok opakováním zprávy (stejné dešifrování pro identické bloky)
<img src="https://i.ibb.co/wgYZn3z/zkr-2.png" alt="zkr-2" border="0">

<img src="https://i.ibb.co/WnQQMwp/zkr-2b.png" alt="zkr-2b" border="0">

<img src="https://i.ibb.co/YXs7HDy/zkr-2c.png" alt="zkr-2c" border="0">

## 3
- server nebude posílat výzvu a klient posílá odpověď a podepsané časové razítko
- razítko podepisuje před sdílením klíče
- server ověřuje časové razítko kvůli aktuálnosti
- server zná předem sdílený klíč

## 4
- **Standardizovaný protokol:** lze jej použít mezi více platformami
- **Založen na tiketech:** po dobu platnosti tiketu není nutno nové spojení znovu ověřovat → zrychlení
- **Ověření klienta i serveru:** obě dvě strany mají tajný klíč k prokázání identity

## 5
- LM hash je omezen na 14 znaků, což odpovídá zhruba 95<sup>14</sup> kombinacím
- slabina tkví v heslech delších, než 7 znaků a oddělením hashování (složitost klesne na 95<sup>7</sup>)
- všechna malá písmena jsou před zašifrováním změněna na velká písmena → snížení výsledného počtu kombinací na 69<sup>7</sup>

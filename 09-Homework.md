### Řešení devátého úkolu pro Základů kryptografie
-------------
## 1
- vutbr.cz - používá TLS 1.3
- sukl.cz - používá TLS 1.2

## 2
- TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8
- TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256

Za bezpečné kryptografické sady můžeme považovat ty, které využívají dočasné verze klíčového ustanovení (ECDHE nebo DHE) a které podepisují data za pomoci RSA/ECDSA. Měly by také používat vhodné technologie (např. AES a vhodnou šifrovací funkci SHA5).

## 3
- **Subjekt**: osoba, pro kterou je certifikát vystaven
- **Platnost certifikátu**: časové rozmezí od/do je certifikát platný
- **Certifikační autorita**: instituce, která vystavila certifikát
- **Veřejný klíč**
- **Použitý hashovací algoritmus**
- **Digitální podpis, shoda klíče, šifrovací klíče a zašifrování dat**

## 4
- **Autentizace**: ověření identity uživatele
- **Autorizace**: určuje práva uživatele v rámci systému
- **Účtování**: uchovává informace pro logování

*příklady protokolů: Diameter, TACACS+, RADIUS*

## 5
- RSA (2048 bitů)
- ECDH (224 bitů)
- AES (128 bitů, 112 bitů není podporováno)

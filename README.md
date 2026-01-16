# 🧾 Projecte 1 — Sistema integral de vendes

Resum
-----
Aquest repositori conté la implementació completa del Projecte 1 — Sistema integral de vendes. Hi ha quatre aplicacions en Python que simulen el flux real d’alta i gestió de clients i productes, assignació de productes amb preus per client i procés de compra amb validació de comandes. El contingut reflecteix el treball acabat i els resultats obtinguts durant la pràctica.

Integrants
- Victor  
- Alejandro  
- Benjaming  
- Erick  
- Nicolas

Què s’inclou al repositori
---------------------------
- alta_clients.py — Aplicació 1: gestió de clients (llegir, crear, esborrar).  
- alta_productes.py — Aplicació 2: gestió de productes (llegir, crear, esborrar).  
- assignacio_productes.py — Aplicació 3: relacions client–producte amb preus.  
- venda_client.py — Aplicació 4: login per NIF, cistell i validació de comanda.  
- data/clients.txt — fitxer de dades de clients utilitzat en les proves.  
- data/productes.txt — fitxer de dades de productes.  
- data/relacions.txt — relacions client;producte;preu.  
- docs/PLA_DE_PROVES.pdf — pla de proves exportat a PDF (un full per aplicació).  
- PLA_DE_PROVES_LINK.txt — enllaç públic al Google Sheets amb el pla de proves.  
- README.md — aquest fitxer.

Comprovacions i execució (resum)
--------------------------------
Per facilitar la comprovació dels resultats, s’inclouen scripts independents que s’executen des de consola. A efectes de revisió, s’hi indiquen les comandes resumides per iniciar cadascuna de les quatre aplicacions:

- Aplicació 1 (clients):
  ```
  python alta_clients.py
  ```
- Aplicació 2 (productes):
  ```
  python alta_productes.py
  ```
- Aplicació 3 (assignacions):
  ```
  python assignacio_productes.py
  ```
- Aplicació 4 (venda / comanda):
  ```
  python venda_client.py
  ```

Fitxers de dades: format
------------------------
- clients.txt — cada línia: `NIF_client;Nom_client`  
  Exemple:
  ```
  12345678A;Joan Garcia
  ```
- productes.txt — cada línia: `Codi_producte;Nom_producte`  
  Exemple:
  ```
  P001;Ratolí USB
  ```
- relacions.txt — cada línia: `NIF_client;Codi_producte;preu`  
  Exemple:
  ```
  12345678A;P001;12.5
  ```
- Comandes validades — fitxer amb nom `<NIF><YYYYMMDD>`, línies `Codi_producte;Quantitat;Preu`

Pla de proves i ubicació
------------------------
- El pla de proves complet (format full de càlcul, exportat a PDF) està a `docs/PLA_DE_PROVES.pdf`.  
- L’enllaç públic al Google Sheets del pla de proves està en `PLA_DE_PROVES_LINK.txt` a l’arrel del repositori.  
- El full de proves inclou un full per aplicació amb casos de prova, passos, resultats esperats i resultats obtinguts.


Limitacions i observacions
-------------------------
- La funcionalitat opcional de multiidioma no s’ha implementat (no inclosa en l’entrega).  
- S’han tingut en compte control d’errors bàsics i gestió d’I/O; la modularització facilita la lectura i les proves.  
- Les dades de mostra s’han deixat a `data/` per facilitar la comprovació del corrector.


Enllaç al pla de proves (Google Sheets)
---------------------------------------
El link públic es troba a `PLA_DE_PROVES_LINK.txt` a l’arrel del repositori. També hi ha una còpia exportada a PDF a `docs/PLA_DE_PROVES.pdf`.

```

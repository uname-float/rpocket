# RPocket CLI

## Scopo del Progetto
RPocket CLI è uno strumento per gestire abbonamenti e sottoscrizioni a servizi vari. Permette agli utenti di memorizzare i dettagli della carta di credito e associarli a servizi con scadenza e note.

## Requisiti
- Python 3.6 o versioni successive
- PostgreSQL

## Installazione
1. Clonare il repository:

   ```bash
   git clone https://github.com/yourusername/rpocket.git
   cd rpocket
   ```

2. Installare le dipendenze con Poetry:

   ```bash
   poetry install
   ```


3. Creare un file `.env` nella root del progetto e impostare le variabili di ambiente necessarie. Ad esempio:

Assicurati di sostituire `username` e `password` con le credenziali del tuo database PostgreSQL.

4. Inizializzare il database eseguendo il file SQL fornito:
###DATABASE_URL=postgresql://username:password@localhost/rpocket

5. Avviare l'applicazione:
./rpocket/cli.py


## Esecuzione dei Test
Per eseguire i test, assicurati di avere Poetry installato e di aver già installato le dipendenze (vedi Installazione sopra). Quindi esegui il seguente comando dalla root del progetto:

## Utilizzo dei Comandi Principali
### Aggiungere una carta di credito
Per aggiungere una nuova carta di credito, esegui il seguente comando:
./rpocket/cli.py add-credit-card [card_number] [expiration_date] [owner_name] [cvv] [notes]


Sostituisci `[card_number]`, `[expiration_date]`, `[owner_name]`, `[cvv]`, e `[notes]` con i dettagli della tua carta di credito.

Esempio:


Questo README fornisce informazioni essenziali su come installare, eseguire test ed utilizzare i comandi principali della tua CLI. Assicurati di personalizzarlo per riflettere al meglio le caratteristiche e le funzionalità specifiche della tua applicazione.













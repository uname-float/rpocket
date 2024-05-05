- **Endpoint per la gestione delle carte di credito:**
  - `GET /credit-cards`: Restituisce tutte le carte di credito associate all'utente.
  - `POST /credit-cards`: Aggiunge una nuova carta di credito per l'utente.
  - `GET /credit-cards/{card_id}`: Restituisce i dettagli di una specifica carta di credito.
  - `PUT /credit-cards/{card_id}`: Aggiorna i dettagli di una carta di credito esistente.
  - `DELETE /credit-cards/{card_id}`: Elimina una carta di credito dall'account dell'utente.

- **Endpoint per la gestione delle sottoscrizioni:**
  - `GET /subscriptions`: Restituisce tutte le sottoscrizioni attive associate all'utente.
  - `POST /subscriptions`: Aggiunge una nuova sottoscrizione per l'utente.
  - `GET /subscriptions/{subscription_id}`: Restituisce i dettagli di una specifica sottoscrizione.
  - `PUT /subscriptions/{subscription_id}`: Aggiorna i dettagli di una sottoscrizione esistente.
  - `DELETE /subscriptions/{subscription_id}`: Annulla una sottoscrizione dell'utente.

- **Endpoint per la generazione di report finanziari:**
  - `GET /financial-reports`: Restituisce report finanziari, ad esempio spese mensili, categorie di spesa, tendenze nel tempo, ecc.
  - `GET /financial-reports/{report_id}`: Restituisce un report finanziario specifico.
  - `POST /financial-reports`: Genera un nuovo report finanziario in base ai parametri specificati dall'utente.

- **Endpoint per l'integrazione con altri servizi:**
  - `POST /payments`: Esegue un pagamento utilizzando una carta di credito associata all'utente.
  - `POST /sync-data`: Sincronizza i dati dell'utente con altre piattaforme o servizi esterni.
  - `GET /recommendations`: Restituisce raccomandazioni personalizzate in base alle abitudini.


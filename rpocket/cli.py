#!/usr/bin/env python

import typer
import psycopg2
from psycopg2 import Error

# Connessione al database PostgreSQL
def connect():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="",
            host="192.168.1.49",
            port="5432",
            database="rpocket",
        )
        return connection
    except (Exception, Error) as error:
        print("Errore durante la connessione al database:", error)


app = typer.Typer()

@app.command()
def add_credit_card(card_number: str, expiration_date: str, owner_name: str, cvv: str, notes: str):

    # Qui inserisci la logica per aggiungere la carta di credito nel database
    connection = connect()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO credit_card (card_number, expiration_date, owner_name, cvv, notes) VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (card_number, expiration_date, owner_name, cvv, notes),
        )
        credit_card_id = cursor.fetchone()[0]
        connection.commit()
        print("Carta di credito aggiunta con successo! ID:", credit_card_id)
        return credit_card_id
    except (Exception, Error) as error:
        print("Errore durante l'inserimento della carta di credito:", error)
    finally:
        cursor.close()
        connection.close()


# Comando per inserire un nuovo abbonamento
@app.command()
def add_subscription(
    service_name: str, credit_card_id: int, expiration_date: str, notes: str
):
    connection = connect()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO subscriptions (service_name, credit_card_id, expiration_date, notes) VALUES (%s, %s, %s, %s)",
            (service_name, credit_card_id, expiration_date, notes),
        )
        connection.commit()
        print("Abbonamento aggiunto con successo!")
    except (Exception, Error) as error:
        print("Errore durante l'inserimento dell'abbonamento:", error)
    finally:
        cursor.close()
        connection.close()


# Comando per visualizzare tutti gli abbonamenti
@app.command()
def list_subscriptions():
    connection = connect()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM subscriptions")
        subscriptions = cursor.fetchall()
        for subscription in subscriptions:
            print(subscription)
    except (Exception, Error) as error:
        print("Errore durante il recupero degli abbonamenti:", error)
    finally:
        cursor.close()
        connection.close()

# Restituisci un dizionario con i dettagli dell'abbonamento trovato
@app.command()
def get_subscription_details(name: str):
    connection = connect()
    cursor = connection.cursor()

    try:
        # Esegui la query per recuperare i dettagli dell'abbonamento basati sul nome
        query = "SELECT * FROM subscriptions WHERE service_name = %s"
        cursor.execute(query, (name,))

        # Ottieni il risultato della query
        subscription_details = cursor.fetchone()

        if subscription_details:
            # Se è stato trovato un abbonamento con il nome specificato, restituisci i dettagli
            return {
                "name": subscription_details[0],
                "card_id": subscription_details[1],
                "expiration_date": subscription_details[2],
                "description": subscription_details[3]
                # Aggiungi altre chiavi se necessario
            }
        else:
            # Se l'abbonamento non è stato trovato, restituisci None o solleva un'eccezione
            return None
    finally:
        # Chiudi la connessione e il cursore
        cursor.close()
        connection.close()

def get_subscriptions(cursor, card_name):
    """
    Ottiene le subscription associate a una carta di credito.
    """
    subscriptions = []
    try:
        # Esecuzione della query per recuperare le subscription associate alla carta di credito
        cursor.execute(
            #"SELECT service_name, expiration_date, notes FROM subscriptions WHERE credit_card_id = %s",
            "SELECT service_name, expiration_date, notes, pay FROM subscriptions WHERE credit_card_id IN (SELECT id FROM credit_card WHERE card_name = %s)",
            (card_name,),
        )

        # Recupero dei risultati
        subscriptions = cursor.fetchall()
    except (Exception, Error) as error:
        typer.echo(f"Si è verificato un errore durante il recupero delle subscription: {error}")
    return subscriptions

# Ricevi informazioni sulla carta seriale numero
@app.command()
def get_card_detail(card_number: str):
    """
    Ottiene i dettagli di una carta di credito dal database.
    """
    try:
        # Connessione al database
        connection = connect()
        cursor = connection.cursor()

        # Esecuzione della query per recuperare i dettagli della carta di credito
        cursor.execute(
            "SELECT card_number, card_name, expiration_date, owner_name, cvv, notes, card_name FROM credit_card WHERE card_number = %s",
            (card_number,),
        )

        # Recupero dei risultati
        card_detail = cursor.fetchone()

        if card_detail:
            typer.echo(f"Dettagli della carta di credito {card_number}:")
            typer.echo(f"Numero della carta: {card_detail[0]}")
            typer.echo(f"Nome della carta: {card_detail[1]}")
            typer.echo(f"Data di scadenza: {card_detail[2]}")
            typer.echo(f"Proprietario: {card_detail[3]}")
            typer.echo(f"CVV: {card_detail[4]}")
            typer.echo(f"Note: {card_detail[5]}")
            typer.echo(f"Nome della carta: {card_detail[6]}")

            # Ottieni le subscription associate alla carta di credito
            subscriptions = get_subscriptions(cursor, card_detail[1])
            if subscriptions:
                typer.echo("\nSubscription associate:")
                for subscription in subscriptions:
                    typer.echo(f"- Nome: {subscription[0]}")
                    typer.echo(f"  Scadenza: {subscription[1]}")
                    typer.echo(f"  Descrizione: {subscription[2]}")
                    typer.echo(f"  Costo: {subscription[3]}")
            else:
                typer.echo("Nessuna subscription associata a questa carta di credito.")
        else:
            typer.echo("Carta di credito non trovata.")
    except (Exception, Error) as error:
        typer.echo(f"Si è verificato un errore durante il recupero dei dettagli della carta di credito: {error}")
    finally:
        # Chiusura della connessione al database
        if connection:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    app()

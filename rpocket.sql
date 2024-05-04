CREATE TABLE credit_card (
    id SERIAL PRIMARY KEY,
    card_number VARCHAR(16),
    card_name VARCHAR(30),
    expiration_date DATE,
    owner_name VARCHAR(255),
    cvv VARCHAR(3),
    notes TEXT
);

CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(255),
    credit_card_id INT REFERENCES credit_card(id),
    expiration_date DATE,
    subscription_cost NUMERIC(10, 2),
    notes TEXT
);


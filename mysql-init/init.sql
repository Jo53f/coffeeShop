CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(30),
    description VARCHAR(30),
    price DECIMAL(6,2),
    author VARCHAR(30)
);

CREATE TABLE foods (
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30),
    description VARCHAR(30),
    price DECIMAL(6,2),
    weight DECIMAL(5,2)
);

CREATE TABLE drinks (
    drink_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30),
    description VARCHAR(30),
    price DECIMAL(6,2),
    hot BOOLEAN,
    amount DECIMAL(5,2)
);
CREATE TABLE Produto(
    sku varchar(30) PRIMARY KEY,
    nome varchar(50) NOT NULL,
    custo FLOAT,
    preco FLOAT,
    estoque INT
);
CREATE TABLE Kit(
    sku varchar(30) PRIMARY KEY,
    nome varchar(50) NOT NULL
);
CREATE TABLE Item(
    id varchar(20) PRIMARY KEY,
    quantidade INT,
    desconto FLOAT,
    /* --- */
    produto varchar(30),
    kit varchar(30), 
    FOREIGN KEY (produto) REFERENCES Produto(sku),
    FOREIGN KEY (kit) REFERENCES Kit(sku)
);

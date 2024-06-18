USE store;

CREATE TABLE store.products (
	id INT NOT NULL AUTO_INCREMENT,
	name varchar(100) NULL,
	sku varchar(15) NULL,
	PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE store.inventories (
	id INT NOT NULL AUTO_INCREMENT,
	product_id INT NOT NULL,
	stock INT NOT NULL,
	price DECIMAL(15,2) NULL,
	PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE store.orders (
	id INT NOT NULL AUTO_INCREMENT,
	fecha DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
	total DECIMAL(15,2) NULL,
	PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE store.products_orders (
	id INT NOT NULL AUTO_INCREMENT,
	product_id INT NOT NULL,
	order_id INT NOT null,
	amount INT NULL,
	subtotal decimal(15,2) NULL,
	PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE store.inventories ADD CONSTRAINT inventories_products_FK FOREIGN KEY (product_id) REFERENCES store.products(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE store.products_orders ADD CONSTRAINT products_orders_products_FK FOREIGN KEY (product_id) REFERENCES store.products(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE store.products_orders ADD CONSTRAINT products_orders_orders_FK FOREIGN KEY (order_id) REFERENCES store.orders(id) ON DELETE CASCADE ON UPDATE CASCADE;


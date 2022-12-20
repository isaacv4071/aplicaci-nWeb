from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(20) NOT NULL UNIQUE,
    `full_name` VARCHAR(50),
    `password` VARCHAR(128),
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `owner` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `document_type` VARCHAR(50) NOT NULL,
    `full_name` VARCHAR(50),
    `address` VARCHAR(50),
    `phone` VARCHAR(50),
    `email` VARCHAR(255),
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `vehicles` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `plate` VARCHAR(50) NOT NULL,
    `brand` VARCHAR(50),
    `model` VARCHAR(50),
    `year` INT,
    `color` VARCHAR(50),
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `modified_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `owner_id` INT NOT NULL,
    CONSTRAINT `fk_vehicles_owner_e6e3b12d` FOREIGN KEY (`owner_id`) REFERENCES `owner` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """

-- MySQL Script generated by MySQL Workbench
-- Fri Dec  8 22:08:15 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`user_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user_info` (
  `id` VARCHAR(45) NOT NULL DEFAULT 'uuid()',
  `username` VARCHAR(45) NULL,
  `avatar` VARCHAR(128) NULL COMMENT '头像地址',
  `passwd` VARCHAR(256) NULL,
  `integration` INT NULL DEFAULT 0 COMMENT '拥有的积分',
  `follower_num` INT NULL DEFAULT 0 COMMENT '关注者，具体关注的用户可以存放到nosql数据库中',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`user_status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user_status` (
  `id` VARCHAR(45) NULL,
  `token` VARCHAR(256) NULL,
  `time` DATETIME NULL,
  `latitude` DOUBLE NULL DEFAULT 0,
  `longitude` DOUBLE NULL DEFAULT 0,
  `role` INT NULL COMMENT '0 是 开拓者，1 是探索者',
  `user_info_id` VARCHAR(45) NOT NULL,
  INDEX `fk_user_status_user_info_idx` (`user_info_id` ASC),
  CONSTRAINT `fk_user_status_user_info`
    FOREIGN KEY (`user_info_id`)
    REFERENCES `mydb`.`user_info` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`user_realeased_activity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`user_realeased_activity` (
  `id` VARCHAR(45) NOT NULL,
  `start_time` DATETIME NULL,
  `end_time` DATETIME NULL,
  `latitude` DOUBLE NULL,
  `longitude` DOUBLE NULL,
  `description` VARCHAR(256) NULL,
  `user_info_id` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_user_realeased_activity_user_info1_idx` (`user_info_id` ASC),
  CONSTRAINT `fk_user_realeased_activity_user_info1`
    FOREIGN KEY (`user_info_id`)
    REFERENCES `mydb`.`user_info` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`order` (
  `id` VARCHAR(45) NOT NULL,
  `type` INT NOT NULL DEFAULT 0 COMMENT '0 即时抢单\n1  预约单\n2 追加单？是否放这还得考虑',
  `order_status` INT NOT NULL DEFAULT 0 COMMENT '订单状态：\n0：还未开始\n1：派单中\n2：进行中\n3：结束\n4：异常',
  `requester_id` VARCHAR(45) NOT NULL DEFAULT 0,
  `responser_id` VARCHAR(45) NOT NULL DEFAULT 0,
  `request_latitude` DOUBLE NULL,
  `request_longitude` DOUBLE NULL,
  `offered_integration` INT NOT NULL DEFAULT 0,
  `order_description` VARCHAR(256) NULL,
  `live_cast_period` INT NULL DEFAULT 0 COMMENT '直播时长',
  `appoint_cast_starttime` DATETIME NULL COMMENT '只有type为预约时才有效',
  `service_star` INT NULL COMMENT '1-5,5个评分星级',
  `service_added_integration` INT NULL,
  `service_comments` VARCHAR(256) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_order_user_info1_idx` (`requester_id` ASC),
  INDEX `fk_order_user_info2_idx` (`responser_id` ASC),
  CONSTRAINT `fk_order_user_info1`
    FOREIGN KEY (`requester_id`)
    REFERENCES `mydb`.`user_info` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_user_info2`
    FOREIGN KEY (`responser_id`)
    REFERENCES `mydb`.`user_info` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

/*
Navicat MySQL Data Transfer

Source Server         : my
Source Server Version : 80018
Source Host           : localhost:3306
Source Database       : fishpond

Target Server Type    : MYSQL
Target Server Version : 80018
File Encoding         : 65001

Date: 2021-05-06 15:45:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for alarm
-- ----------------------------
DROP TABLE IF EXISTS `alarm`;
CREATE TABLE `alarm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `col_time` timestamp(6) NOT NULL,
  `col_value` varchar(20) NOT NULL,
  `sensor_type` int(10) NOT NULL,
  `area` varchar(20) NOT NULL,
  `pond_name` varchar(20) NOT NULL,
  `alarm_type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO `alarm` VALUES ('2', '2021-05-03 16:38:03.000000', '16', '1', '东厂水槽', '养鱼池', 'ph过高');
INSERT INTO `alarm` VALUES ('3', '2021-05-04 16:38:03.000000', '16', '2', '南京', '江宁', '水温过高');
INSERT INTO `alarm` VALUES ('4', '2021-05-05 16:38:03.000000', '16', '1', '北京', '朝阳', 'ph过低');
INSERT INTO `alarm` VALUES ('5', '2020-05-03 16:38:03.000000', '16', '3', '深圳', '南山', '溶解氧过低');
INSERT INTO `alarm` VALUES ('6', '2019-05-03 16:38:03.000000', '16', '2', '上海', '浦东', '水温过低');
INSERT INTO `alarm` VALUES ('7', '2018-05-03 16:38:03.000000', '16', '1', '苏州', '姑苏', 'ph过高');
INSERT INTO `alarm` VALUES ('8', '2021-04-03 16:38:03.000000', '16', '2', '无锡', '养鱼池', '水温过低');
INSERT INTO `alarm` VALUES ('9', '2021-04-13 16:38:03.000000', '16', '1', '常州', '养鱼池', 'ph过低');
INSERT INTO `alarm` VALUES ('10', '2021-05-13 16:38:03.000000', '16', '4', '镇江', '养鱼池', '气温过高');
INSERT INTO `alarm` VALUES ('11', '2021-01-03 16:38:03.000000', '16', '1', '广州', '天河', 'ph过高');
INSERT INTO `alarm` VALUES ('12', '2021-05-04 16:38:03.000000', '16', '1', '扬州', '养鱼池', 'ph过低');
INSERT INTO `alarm` VALUES ('13', '2021-05-09 16:38:03.000000', '16', '3', '南京', '秦淮', '溶解氧过低');
INSERT INTO `alarm` VALUES ('14', '2021-07-03 16:38:03.000000', '16', '1', '北京', '东城', 'ph过低');
INSERT INTO `alarm` VALUES ('15', '2011-05-03 16:38:03.000000', '16', '3', '纽约', '华尔街', '溶解氧过低');
INSERT INTO `alarm` VALUES ('16', '2020-04-03 16:38:03.000000', '16', '1', '东京', '养鱼池', 'ph过高');

-- ----------------------------
-- Records of alarm
-- ----------------------------

-- ----------------------------
-- Table structure for calendar
-- ----------------------------
DROP TABLE IF EXISTS `calendar`;
CREATE TABLE `calendar` (
  `id` int(11) NOT NULL,
  `time` date DEFAULT NULL,
  `food` float(20,0) NOT NULL,
  `pond_id` int(11) NOT NULL,
  `vaccine` int(11) DEFAULT NULL,
  `clean_water` int(11) DEFAULT NULL,
  `add_fish` int(11) DEFAULT NULL,
  `kill_insect` int(11) DEFAULT NULL,
  `disinfect` int(11) DEFAULT NULL,
  `other` text,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of calendar
-- ----------------------------

-- ----------------------------
-- Table structure for device
-- ----------------------------
DROP TABLE IF EXISTS `device`;
CREATE TABLE `device` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `state` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of device
-- ----------------------------
INSERT INTO `device` VALUES ('1', 'PH检测仪', 'AZ8685分辨率0.1PH', '0');
INSERT INTO `device` VALUES ('2', '增氧机', '大焊YTZYB', '0');
INSERT INTO `device` VALUES ('3', '投饲机', 'ZY-120触屏全自动', '0');
INSERT INTO `device` VALUES ('4', '水流控制器', '四氟尘里DN300', '1');
INSERT INTO `device` VALUES ('5', '南天门大棒', '非人类研究所', '0');
INSERT INTO `device` VALUES ('6', '南天门大棒', '非人类研究所', '0');

-- ----------------------------
-- Table structure for pond
-- ----------------------------
DROP TABLE IF EXISTS `pond`;
CREATE TABLE `pond` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pond_name` varchar(20) NOT NULL,
  `fish_type` varchar(20) NOT NULL,
  `area_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of pond
-- ----------------------------
INSERT INTO `pond` VALUES ('1', '池塘代号啊牛', '金鱼', '厂左1');
INSERT INTO `pond` VALUES ('2', '小池塘2号', '鲤鱼', '厂左2');
INSERT INTO `pond` VALUES ('4', '东厂水槽', '金龙鱼', '河海大学');
INSERT INTO `pond` VALUES ('6', '东厂水槽啊', '六眼飞鱼', '纪新元');
INSERT INTO `pond` VALUES ('11', '东厂水槽啊', '六眼飞鱼', '计信院');
INSERT INTO `pond` VALUES ('15', '池塘代号啊', '金鱼', '厂左1');
INSERT INTO `pond` VALUES ('16', '池塘代号啊', '金鱼', '厂左1');
INSERT INTO `pond` VALUES ('17', '西方水塔', '食人鱼', '西北片区');
INSERT INTO `pond` VALUES ('18', '南方水池', '王多鱼', '西南片区');
INSERT INTO `pond` VALUES ('19', '池塘代号啊', '食人鱼', '纪新元');
INSERT INTO `pond` VALUES ('22', '东厂水槽', '金龙鱼', '纪新元');
INSERT INTO `pond` VALUES ('23', '池塘代号啊', '金鱼', '河海大学');
INSERT INTO `pond` VALUES ('25', '东厂水槽啊', '金龙鱼', '计信院');
INSERT INTO `pond` VALUES ('28', '东厂水槽2', '金龙鱼', '河海大学');
INSERT INTO `pond` VALUES ('29', '东厂水槽牛逼', '食人鱼', '计信院112');

-- ----------------------------
-- Table structure for sensor_threshold
-- ----------------------------
DROP TABLE IF EXISTS `sensor_threshold`;
CREATE TABLE `sensor_threshold` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` int(20) NOT NULL,
  `max1` float NOT NULL,
  `min1` float NOT NULL,
  `pond_name` varchar(20) NOT NULL,
  `area_name` varchar(20) NOT NULL,
  `max2` float NOT NULL,
  `min2` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sensor_threshold
-- ----------------------------
INSERT INTO `sensor_threshold` VALUES ('1', '1', '30', '10', '小池塘1号', '厂左1', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('2', '2', '35', '13', '小池塘2号', '厂左2', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('3', '2', '40', '24', '小池塘3号', '厂左3', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('4', '3', '7', '11', '小池塘4号', '厂左1', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('5', '4', '25', '20', '小池塘5号', '厂左2', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('6', '2', '31', '12', '小池塘6号', '厂左3', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('7', '1', '32', '11', '小池塘7号', '厂左1', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('8', '3', '30', '10', '小池塘8号', '厂左1', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('9', '1', '22', '12', '电子信息', '厂左3', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('10', '4', '36', '15', '软件工程', '厂左5', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('11', '3', '30', '20', '太平洋', '厂左4', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('12', '1', '30', '4', '大西洋', '厂左2', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('13', '2', '30', '17', '印度洋', '厂左1', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('14', '2', '55', '26', '北冰洋', '厂左4', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('15', '2', '25', '10', '小池塘1号', '厂左3', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('16', '3', '30', '10', '小池塘1号', '厂左2', '20', '15');
INSERT INTO `sensor_threshold` VALUES ('17', '1', '10', '3', '小池塘1号', '厂左1', '20', '15');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(20) NOT NULL,
  `user_password` varchar(20) NOT NULL,
  `user_type` int(11) NOT NULL,
  `user_phone` varchar(11) DEFAULT NULL,
  `user_wechat` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'spp', '123456', '1', '15951078507', 'wechat');
INSERT INTO `user` VALUES ('2', '张三', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('3', '李四', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('4', '王五', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('5', 'dzy', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('6', 'lili', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('7', 'rose', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('8', 'jack', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('9', 'ly', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('10', '阿三', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('11', '张四', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('12', '张wu', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('13', '张', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('14', 'kkk', 'kaowe174', '2', '15951078507', 'athisnk');
INSERT INTO `user` VALUES ('15', 'lll', 'kaowe174', '2', '15951078507', 'athisnk');

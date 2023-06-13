/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80028 (8.0.28)
 Source Host           : 127.0.0.1:3306
 Source Schema         : ll

 Target Server Type    : MySQL
 Target Server Version : 80028 (8.0.28)
 File Encoding         : 65001

 Date: 13/06/2023 12:57:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book`  (
  `BookName` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `BookId` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Auth` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Category` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Publisher` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `PublishTime` date NULL DEFAULT NULL,
  `NumStorage` int NULL DEFAULT 0,
  `NumCanBorrow` int NULL DEFAULT 0,
  `NumBorrowed` int NULL DEFAULT 0
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES ('力学', 'IS1000', '刘斌', '教育', '中国科学技术大学 ', '1999-01-01', 34, 32, 3);
INSERT INTO `book` VALUES ('微积分', 'IS1001', '牛顿莱布尼兹', '教育', '中国科学技术大学', '1998-01-01', 14, 13, 2);
INSERT INTO `book` VALUES ('电磁场论', 'IS1002', '叶邦角', '教育', '中国科学技术大学', '1997-01-01', 24, 24, 0);
INSERT INTO `book` VALUES ('热学', 'IS1003', '张鹏飞', '教育', '中国科学技术大学', '2002-01-01', 45, 45, 0);
INSERT INTO `book` VALUES ('电动力学', 'IS1004', '叶邦角', '教育', '中国科学技术大学', '2003-01-01', 70, 70, 0);
INSERT INTO `book` VALUES ('数据库', 'IS1006', '袁平波', '教育', '中国科学技术大学', '2010-01-01', 10, 11, 0);
INSERT INTO `book` VALUES ('电磁学', 'IS1005', '叶邦角', '教育', '中国科学技术大学 ', '2012-01-01', 43, 43, 0);
INSERT INTO `book` VALUES ('数学分析', 'IS1007', '陈卿', '教育', '中国科学技术大学', '2013-01-01', 23, 23, 0);
INSERT INTO `book` VALUES ('吉米多维奇题解1', 'IS1008', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('吉米多维奇题解2', 'IS1009', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('吉米多维奇题解3', 'IS1010', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('吉米多维奇题解4', 'IS1011', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 49, 1);
INSERT INTO `book` VALUES ('吉米多维奇题解5', 'IS1012', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('吉米多维奇题解6', 'IS1013', '吉米多维奇', '教育', '俄罗斯出版社', '2010-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('朗道力学', 'IS1014', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 49, 1);
INSERT INTO `book` VALUES ('朗道量子力学', 'IS1016', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('朗道量子电动力学', 'IS1017', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('朗道统计物理学', 'IS1018', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('朗道流体力学', 'IS1019', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('朗道弹性理论力学', 'IS1020', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('朗道物理动力学', 'IS1021', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('植物学', 'IS1022', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0);
INSERT INTO `book` VALUES ('动物学', 'IS1023', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0);
INSERT INTO `book` VALUES ('细胞生物学', 'IS1024', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0);
INSERT INTO `book` VALUES ('动物生理学', 'IS1025', '佚名', '生物学', '高等教育出版社', '2011-05-01', 50, 50, 0);
INSERT INTO `book` VALUES ('古生物学', 'IS1026', '佚名', '生物学', '高等教育出版社', '2011-05-01', 100, 100, 0);
INSERT INTO `book` VALUES ('高等数学', 'IS1027', '佚名', '教育', '高等教育出版社', '2011-05-01', 50, 49, 1);
INSERT INTO `book` VALUES ('线性代数', 'IS1029', '佚名', '教育', '高等教育出版社', '2011-05-01', 50, 50, 0);
INSERT INTO `book` VALUES ('C++程序设计', 'IS1030', '孙广中', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0);
INSERT INTO `book` VALUES ('C程序设计', 'IS1031', '郑重', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0);
INSERT INTO `book` VALUES ('数据结构', 'IS1032', '顾为兵', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0);
INSERT INTO `book` VALUES ('信号与系统', 'IS1033', '李卫平', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0);
INSERT INTO `book` VALUES ('线性电子线路', 'IS1034', '陆伟', '教育', '中国科学技术大学', '2011-05-01', 50, 50, 0);
INSERT INTO `book` VALUES ('朗道电动力学', 'IS1015', '朗道', '教育', '高等教育出版社', '2012-01-01', 50, 50, 0);
INSERT INTO `book` VALUES ('亮剑', 'IS1045', '都梁', '军事', '人民出版社', '1998-01-01', 50, 50, 0);

-- ----------------------------
-- Table structure for buyordrop
-- ----------------------------
DROP TABLE IF EXISTS `buyordrop`;
CREATE TABLE `buyordrop`  (
  `BookId` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Time` date NULL DEFAULT NULL,
  `BuyOrDrop` bit(1) NULL DEFAULT b'0',
  `Number` int NULL DEFAULT 0
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of buyordrop
-- ----------------------------
INSERT INTO `buyordrop` VALUES ('IS1234', '2018-04-18', b'1', 12);
INSERT INTO `buyordrop` VALUES ('IS1234', '2018-04-21', b'0', 2);
INSERT INTO `buyordrop` VALUES ('IS1000', '2018-04-22', b'1', 34);
INSERT INTO `buyordrop` VALUES ('IS1001', '2018-04-22', b'1', 14);
INSERT INTO `buyordrop` VALUES ('IS1002', '2018-04-22', b'1', 24);
INSERT INTO `buyordrop` VALUES ('IS1003', '2018-04-22', b'1', 45);
INSERT INTO `buyordrop` VALUES ('IS1004', '2018-04-22', b'1', 25);
INSERT INTO `buyordrop` VALUES ('IS1004', '2018-04-27', b'1', 45);
INSERT INTO `buyordrop` VALUES ('IS1005', '2018-04-27', b'1', 45);
INSERT INTO `buyordrop` VALUES ('IS1234', '2018-04-28', b'0', 10);
INSERT INTO `buyordrop` VALUES ('IS1234', '2018-04-28', b'0', 10);
INSERT INTO `buyordrop` VALUES ('IS1006', '2018-04-28', b'1', 10);
INSERT INTO `buyordrop` VALUES ('IS1005', '2018-04-28', b'0', 45);
INSERT INTO `buyordrop` VALUES ('IS1005', '2018-04-28', b'1', 43);
INSERT INTO `buyordrop` VALUES ('IS1007', '2018-04-28', b'1', 23);
INSERT INTO `buyordrop` VALUES ('IS1008', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1009', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1010', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1011', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1012', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1013', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1014', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1015', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1016', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1017', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1018', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1019', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1020', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1021', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1022', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1023', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1024', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1025', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1026', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1026', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1027', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1029', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1030', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1031', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1032', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1033', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1034', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1015', '2018-04-28', b'0', 50);
INSERT INTO `buyordrop` VALUES ('IS1015', '2018-04-28', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1035', '2021-05-06', b'1', 60);
INSERT INTO `buyordrop` VALUES ('IS1035', '2021-05-06', b'0', 60);
INSERT INTO `buyordrop` VALUES ('IS1056', '2021-05-06', b'1', 900);
INSERT INTO `buyordrop` VALUES ('is1056', '2021-05-06', b'0', 900);
INSERT INTO `buyordrop` VALUES ('IS1045', '2021-05-08', b'1', 50);
INSERT INTO `buyordrop` VALUES ('IS1036', '2021-05-08', b'0', 50);
INSERT INTO `buyordrop` VALUES ('IS1036', '2021-05-08', b'0', 10);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `StudentId` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Password` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `IsAdmin` int NULL DEFAULT 0,
  `TimesBorrowed` int NULL DEFAULT 0,
  `NumBorrowed` int NULL DEFAULT 0,
  UNIQUE INDEX `StudentId`(`StudentId` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('123', '123', 'e10adc3949ba59abbe56e057f20f883e', 1, 0, 0);
INSERT INTO `user` VALUES ('1234', '1234', 'e10adc3949ba59abbe56e057f20f883e', 0, 2, 1);
INSERT INTO `user` VALUES ('12345', '12345', 'e10adc3949ba59abbe56e057f20f883e', 1, 0, 0);

-- ----------------------------
-- Table structure for user_book
-- ----------------------------
DROP TABLE IF EXISTS `user_book`;
CREATE TABLE `user_book`  (
  `StudentId` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `BookId` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `BorrowTime` date NULL DEFAULT NULL,
  `ReturnTime` date NULL DEFAULT NULL,
  `BorrowState` bit(1) NULL DEFAULT b'0'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user_book
-- ----------------------------
INSERT INTO `user_book` VALUES ('PB15000135', 'IS1000', '2018-04-28', '2018-04-28', b'0');
INSERT INTO `user_book` VALUES ('PB15000135', 'IS1027', '2018-04-28', NULL, b'1');
INSERT INTO `user_book` VALUES ('PB15000135', 'IS1011', '2018-04-28', NULL, b'1');
INSERT INTO `user_book` VALUES ('PB15000135', 'IS1014', '2018-04-28', NULL, b'1');
INSERT INTO `user_book` VALUES ('PB15000135', 'IS1000', '2021-05-06', NULL, b'1');
INSERT INTO `user_book` VALUES ('PB15000135', 'IS1001', '2021-05-06', NULL, b'1');
INSERT INTO `user_book` VALUES ('1234', 'IS1000', '2021-05-08', NULL, b'1');
INSERT INTO `user_book` VALUES ('1234', 'IS1001', '2021-05-08', '2021-05-08', b'0');

SET FOREIGN_KEY_CHECKS = 1;

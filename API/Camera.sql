/*
 Navicat SQLite Data Transfer

 Source Server         : AJackTi
 Source Server Type    : SQLite
 Source Server Version : 3012001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3012001
 File Encoding         : 65001

 Date: 20/04/2019 18:22:55
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for Camera
-- ----------------------------
DROP TABLE IF EXISTS "Camera";
CREATE TABLE "Camera" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"TimeStart"	INTEGER NOT NULL,
	"TimeEnd"	INTEGER NOT NULL,
	"VideoLink"	TEXT,
	"Parameter"	TEXT NOT NULL
);

-- ----------------------------
-- Auto increment value for Camera
-- ----------------------------
UPDATE "main"."sqlite_sequence" SET seq = 12 WHERE name = 'Camera';

PRAGMA foreign_keys = true;

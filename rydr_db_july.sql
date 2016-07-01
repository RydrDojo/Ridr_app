-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: localhost    Database: rydr_db
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `comment_id` int(11) NOT NULL,
  `comment_content` text,
  `comments_created_at` datetime DEFAULT NULL,
  `comments_updated_at` datetime DEFAULT NULL,
  `rides_ride_id` int(11) NOT NULL,
  `users_user_id` int(11) NOT NULL,
  PRIMARY KEY (`comment_id`),
  KEY `fk_comments_rides1_idx` (`rides_ride_id`),
  KEY `fk_comments_users1_idx` (`users_user_id`),
  CONSTRAINT `fk_comments_rides1` FOREIGN KEY (`rides_ride_id`) REFERENCES `rides` (`ride_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`users_user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `friends`
--

DROP TABLE IF EXISTS `friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `friends` (
  `users_user_id` int(11) NOT NULL,
  `users_friend_id` int(11) NOT NULL,
  PRIMARY KEY (`users_user_id`,`users_friend_id`),
  KEY `fk_users_has_users_users2_idx` (`users_friend_id`),
  KEY `fk_users_has_users_users1_idx` (`users_user_id`),
  CONSTRAINT `fk_users_has_users_users1` FOREIGN KEY (`users_user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_users_users2` FOREIGN KEY (`users_friend_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friends`
--

LOCK TABLES `friends` WRITE;
/*!40000 ALTER TABLE `friends` DISABLE KEYS */;
/*!40000 ALTER TABLE `friends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locations` (
  `location_id` int(11) NOT NULL,
  `street_1` varchar(255) DEFAULT NULL,
  `street_2` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(3) DEFAULT NULL,
  `postal_code` varchar(15) DEFAULT NULL,
  `country` varchar(255) DEFAULT 'US',
  `location_created_at` datetime DEFAULT NULL,
  `location_updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `message_content` text,
  `messages_created_at` datetime DEFAULT NULL,
  `messages_updated_at` datetime DEFAULT NULL,
  `recipient_id` int(11) DEFAULT NULL,
  `users_user_id` int(11) NOT NULL,
  PRIMARY KEY (`message_id`),
  KEY `fk_messages_users1_idx` (`users_user_id`),
  CONSTRAINT `fk_messages_users1` FOREIGN KEY (`users_user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ratings`
--

DROP TABLE IF EXISTS `ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ratings` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `star_value` int(11) DEFAULT NULL,
  `user_rating_id` int(11) DEFAULT NULL,
  `ratings_content` text,
  `ratings_created_at` datetime DEFAULT NULL,
  `ratings_updated_at` datetime DEFAULT NULL,
  `users_user_id` int(11) NOT NULL,
  PRIMARY KEY (`rating_id`),
  KEY `fk_ratings_users1_idx` (`users_user_id`),
  CONSTRAINT `fk_ratings_users1` FOREIGN KEY (`users_user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ratings`
--

LOCK TABLES `ratings` WRITE;
/*!40000 ALTER TABLE `ratings` DISABLE KEYS */;
/*!40000 ALTER TABLE `ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rides`
--

DROP TABLE IF EXISTS `rides`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rides` (
  `ride_id` int(11) NOT NULL AUTO_INCREMENT,
  `driver_id` varchar(255) DEFAULT NULL,
  `ride_date` datetime DEFAULT NULL,
  `ride_time` varchar(15) DEFAULT NULL,
  `public` tinyint(1) DEFAULT '1',
  `ride_description` varchar(45) DEFAULT NULL,
  `max_passengers` int(2) DEFAULT NULL,
  `cur_passenger` int(2) DEFAULT '1',
  `ride_image` varchar(45) DEFAULT NULL,
  `origin` text,
  `destination` text,
  `ride_complete` tinyint(1) DEFAULT '0',
  `ride_created_at` datetime DEFAULT NULL,
  `ride_updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`ride_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rides`
--

LOCK TABLES `rides` WRITE;
/*!40000 ALTER TABLE `rides` DISABLE KEYS */;
INSERT INTO `rides` VALUES (16,'10153941387519143','2016-08-18 00:00:00','9:00pm',1,'Hi Google',4,1,NULL,'Google','Microsoft',0,NULL,NULL),(17,'10153941387519143','2016-08-05 00:00:00','9:30pm',1,'This is a drive',5,1,NULL,'San Jose','Las Vegas',0,NULL,NULL),(20,'10153537627565755','2016-08-11 00:00:00','3:00am',1,'Heading home',3,1,NULL,'Las Vegas','Oakland',0,NULL,NULL);
/*!40000 ALTER TABLE `rides` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` int(100) NOT NULL AUTO_INCREMENT,
  `email` varchar(45) DEFAULT NULL,
  `fb_user_id` varchar(255) DEFAULT NULL,
  `first_name` varchar(205) DEFAULT NULL,
  `last_name` varchar(205) DEFAULT NULL,
  `username` varchar(105) DEFAULT NULL,
  `city` text,
  `state` text,
  `profile_pic` varchar(255) DEFAULT NULL,
  `bio` text,
  `carma` varchar(20) DEFAULT NULL,
  `users_created_at` datetime DEFAULT NULL,
  `users_updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `fb_user_id_UNIQUE` (`fb_user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (5,'josiahrooney@gmail.com','10153941387519143','Josiah','Rooney','chaosrock','Santa Rosa','CA',NULL,'I\'m a cool guy!','4.5',NULL,NULL),(6,'tom@gmail.com','1022402214114','Tom','Jones','tommyjones','San Francisco','CA',NULL,'I like cats','3.0',NULL,NULL),(7,'soumyanatural@gmail.com','10154320305784553','Soumya','Gatti','sam_dojo','San Francisco','CA',NULL,'I like dogs','5',NULL,NULL),(8,'carolinedinh@gmail.com','10154445261857590','Caroline','Dinh','care_bear','San Antonio','CA',NULL,'I like pickles','4.5',NULL,NULL),(9,'luis.soccerman@gmail.com','10153537627565755','Luis','Casillas','LLCash','Sunnyvale','CA',NULL,'I like soccer','4',NULL,NULL),(10,'Rohan.shamrock@gmail.com','1794062487479568','Rohan','Sanjay','Rohan.shamrock@gmail.com','San Jose','CA',NULL,'I like food','4.5',NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_rides`
--

DROP TABLE IF EXISTS `users_rides`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_rides` (
  `users_user_id` int(11) NOT NULL,
  `rides_ride_id` int(11) NOT NULL,
  PRIMARY KEY (`users_user_id`,`rides_ride_id`),
  KEY `fk_users_has_rides_rides1_idx` (`rides_ride_id`),
  KEY `fk_users_has_rides_users_idx` (`users_user_id`),
  CONSTRAINT `fk_users_has_rides_rides1` FOREIGN KEY (`rides_ride_id`) REFERENCES `rides` (`ride_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_rides_users` FOREIGN KEY (`users_user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_rides`
--

LOCK TABLES `users_rides` WRITE;
/*!40000 ALTER TABLE `users_rides` DISABLE KEYS */;
INSERT INTO `users_rides` VALUES (5,16),(6,16),(9,16),(5,17),(9,17),(9,20);
/*!40000 ALTER TABLE `users_rides` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-01  3:38:35

-- MySQL dump 10.13  Distrib 8.0.32, for macos13.0 (arm64)
--
-- Host: localhost    Database: RideShare
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Driver`
--

DROP TABLE IF EXISTS `Driver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Driver` (
  `DriverID` int NOT NULL,
  `Driver_mode` tinyint(1) NOT NULL,
  `Rating` float NOT NULL,
  PRIMARY KEY (`DriverID`),
  CONSTRAINT `driver_ibfk_1` FOREIGN KEY (`DriverID`) REFERENCES `User` (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Driver`
--

LOCK TABLES `Driver` WRITE;
/*!40000 ALTER TABLE `Driver` DISABLE KEYS */;
INSERT INTO `Driver` VALUES (3,0,3.7875),(4,0,4.8),(6,0,5),(7,0,5);
/*!40000 ALTER TABLE `Driver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rating`
--

DROP TABLE IF EXISTS `Rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rating` (
  `RatingID` int NOT NULL AUTO_INCREMENT,
  `TripID` int NOT NULL,
  `RiderID` int NOT NULL,
  `DriverID` int NOT NULL,
  `Rating_score` int NOT NULL,
  PRIMARY KEY (`RatingID`),
  KEY `TripID` (`TripID`),
  KEY `RiderID` (`RiderID`),
  KEY `DriverID` (`DriverID`),
  CONSTRAINT `rating_ibfk_1` FOREIGN KEY (`TripID`) REFERENCES `Trip` (`TripID`),
  CONSTRAINT `rating_ibfk_2` FOREIGN KEY (`RiderID`) REFERENCES `User` (`UserID`),
  CONSTRAINT `rating_ibfk_3` FOREIGN KEY (`DriverID`) REFERENCES `Driver` (`DriverID`),
  CONSTRAINT `rating_chk_1` CHECK ((`Rating_score` between 1 and 5))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rating`
--

LOCK TABLES `Rating` WRITE;
/*!40000 ALTER TABLE `Rating` DISABLE KEYS */;
INSERT INTO `Rating` VALUES (1,1,1,3,4),(2,2,2,3,5),(3,3,1,4,4),(4,4,2,4,5),(5,5,5,3,3);
/*!40000 ALTER TABLE `Rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Trip`
--

DROP TABLE IF EXISTS `Trip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Trip` (
  `TripID` int NOT NULL AUTO_INCREMENT,
  `RiderID` int NOT NULL,
  `DriverID` int NOT NULL,
  `Pickup_location` varchar(200) NOT NULL,
  `Dropoff_location` varchar(200) NOT NULL,
  `Fare` decimal(7,2) NOT NULL,
  PRIMARY KEY (`TripID`),
  KEY `RiderID` (`RiderID`),
  KEY `DriverID` (`DriverID`),
  CONSTRAINT `trip_ibfk_1` FOREIGN KEY (`RiderID`) REFERENCES `User` (`UserID`),
  CONSTRAINT `trip_ibfk_2` FOREIGN KEY (`DriverID`) REFERENCES `Driver` (`DriverID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Trip`
--

LOCK TABLES `Trip` WRITE;
/*!40000 ALTER TABLE `Trip` DISABLE KEYS */;
INSERT INTO `Trip` VALUES (1,1,3,'100 Main St','500 Park Ave',12.50),(2,2,3,'150 Main St','400 Park Ave',10.00),(3,1,4,'200 Main St','300 Park Ave',8.50),(4,2,4,'250 Main St','200 Park Ave',7.00),(5,5,3,'300 Main St','100 Park Ave',9.50),(6,1,3,'Richmond','San Francisco',50.00),(7,5,3,'orange','irvine',15.00),(8,5,3,'orange','newport',30.00),(9,1,3,'Orange','Newport',23.00);
/*!40000 ALTER TABLE `Trip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `UserType` enum('Rider','Driver') NOT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'John Doe','Rider'),(2,'Jane Smith','Rider'),(3,'Michael Brown','Driver'),(4,'Emily Johnson','Driver'),(5,'David Wilson','Rider'),(6,'Gilberto','Driver'),(7,'Jose','Driver'),(8,'Luis','Rider');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-06 22:01:18

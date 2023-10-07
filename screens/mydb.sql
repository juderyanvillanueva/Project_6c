-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: loginform
-- ------------------------------------------------------
-- Server version	5.5.62

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
-- Table structure for table `logindata`
--

DROP TABLE IF EXISTS `logindata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logindata` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  `phone_number` varchar(25) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logindata`
--

LOCK TABLES `logindata` WRITE;
/*!40000 ALTER TABLE `logindata` DISABLE KEYS */;
INSERT INTO `logindata` VALUES ('a','a','aaaaaaaaaa','+639751727061','2023-09-01','05:00 PM'),('ar15','09159796119','Jude Ryan Villanueva','09751727061','2023-09-05','06:00 PM'),('arjaymacah','a','Renz Macah','+639751727061',NULL,NULL),('d','a','dt','+639949699752','2023-09-16','05:00 AM'),('jude','09159796119','Jude Ryan Villanueva','09751727061','2023-09-18','07:00 PM'),('jude0419','judepogiaso','Arvin Entienza','09978795680','2023-09-18','12:00 PM'),('jude1111','jude','Jude Ryan','+639751727061','2023-10-29','07:00 AM'),('jude123','arvinpogiaso','benjamin paguyo','09978795680','2023-09-13','06:00 AM'),('jude332','09159796119','J Villa','09751727061','2023-09-22','05:00 PM'),('kljdas123','jude','juderyanv','+639978795680','2023-09-30','12:00 PM'),('wappywuwu','a','wappylakititi','+639751727061','2023-09-15','05:00 AM');
/*!40000 ALTER TABLE `logindata` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-15 13:43:41

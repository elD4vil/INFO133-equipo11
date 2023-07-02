-- MariaDB dump 10.19  Distrib 10.6.12-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: Medios
-- ------------------------------------------------------
-- Server version	10.6.12-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `Medios`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `Medios` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `Medios`;

--
-- Table structure for table `Categoria`
--

DROP TABLE IF EXISTS `Categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Categoria` (
  `Nombre_Categoria` varchar(30) NOT NULL,
  `ID_SitioWeb` int(11) DEFAULT NULL,
  `URL` varchar(200) DEFAULT NULL,
  `Xpath_URL_Noticia` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Nombre_Categoria`),
  KEY `ID_SitioWeb` (`ID_SitioWeb`),
  CONSTRAINT `Categoria_ibfk_1` FOREIGN KEY (`ID_SitioWeb`) REFERENCES `SitioWeb` (`ID_SitioWeb`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Categoria`
--

LOCK TABLES `Categoria` WRITE;
/*!40000 ALTER TABLE `Categoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `Categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Fundador`
--

DROP TABLE IF EXISTS `Fundador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Fundador` (
  `ID_Fundador` int(11) NOT NULL,
  `Nombre_Fundador` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID_Fundador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Fundador`
--

LOCK TABLES `Fundador` WRITE;
/*!40000 ALTER TABLE `Fundador` DISABLE KEYS */;
/*!40000 ALTER TABLE `Fundador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Fundar`
--

DROP TABLE IF EXISTS `Fundar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Fundar` (
  `ID_Medio` int(11) NOT NULL,
  `ID_Fundador` int(11) NOT NULL,
  PRIMARY KEY (`ID_Medio`,`ID_Fundador`),
  KEY `ID_Fundador` (`ID_Fundador`),
  CONSTRAINT `Fundar_ibfk_1` FOREIGN KEY (`ID_Medio`) REFERENCES `Medio` (`ID_Medio`),
  CONSTRAINT `Fundar_ibfk_2` FOREIGN KEY (`ID_Fundador`) REFERENCES `Fundador` (`ID_Fundador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Fundar`
--

LOCK TABLES `Fundar` WRITE;
/*!40000 ALTER TABLE `Fundar` DISABLE KEYS */;
/*!40000 ALTER TABLE `Fundar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medio`
--

DROP TABLE IF EXISTS `Medio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Medio` (
  `ID_Medio` int(11) NOT NULL,
  `Comuna` varchar(20) DEFAULT NULL,
  `Region` varchar(20) DEFAULT NULL,
  `Pais` varchar(30) DEFAULT NULL,
  `Nombre_Medio` varchar(30) DEFAULT NULL,
  `Cobertura` varchar(30) DEFAULT NULL,
  `Continente` varchar(10) DEFAULT NULL,
  `Año_Fundacion` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_Medio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medio`
--

LOCK TABLES `Medio` WRITE;
/*!40000 ALTER TABLE `Medio` DISABLE KEYS */;
/*!40000 ALTER TABLE `Medio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Noticia`
--

DROP TABLE IF EXISTS `Noticia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Noticia` (
  `ID_Noticia` int(11) NOT NULL,
  `URL` varchar(200) DEFAULT NULL,
  `ID_SitioWeb` int(11) DEFAULT NULL,
  `Xpath_Titulo` varchar(200) DEFAULT NULL,
  `Xpath_Contenido` varchar(200) DEFAULT NULL,
  `Xpath_URL_Fecha` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID_Noticia`),
  KEY `ID_SitioWeb` (`ID_SitioWeb`),
  CONSTRAINT `Noticia_ibfk_1` FOREIGN KEY (`ID_SitioWeb`) REFERENCES `SitioWeb` (`ID_SitioWeb`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Noticia`
--

LOCK TABLES `Noticia` WRITE;
/*!40000 ALTER TABLE `Noticia` DISABLE KEYS */;
/*!40000 ALTER TABLE `Noticia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RedSocial`
--

DROP TABLE IF EXISTS `RedSocial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RedSocial` (
  `Nombre_Usuario` varchar(30) NOT NULL,
  `ID_Medio` int(11) DEFAULT NULL,
  `Nombre_Red` varchar(20) DEFAULT NULL,
  `N_Seguidores` int(11) DEFAULT NULL,
  `Fecha_Actualizacion` date DEFAULT NULL,
  PRIMARY KEY (`Nombre_Usuario`),
  KEY `ID_Medio` (`ID_Medio`),
  CONSTRAINT `RedSocial_ibfk_1` FOREIGN KEY (`ID_Medio`) REFERENCES `Medio` (`ID_Medio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RedSocial`
--

LOCK TABLES `RedSocial` WRITE;
/*!40000 ALTER TABLE `RedSocial` DISABLE KEYS */;
/*!40000 ALTER TABLE `RedSocial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SitioWeb`
--

DROP TABLE IF EXISTS `SitioWeb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SitioWeb` (
  `ID_SitioWeb` int(11) NOT NULL,
  `ID_Medio` int(11) DEFAULT NULL,
  `Nombre_SitioWeb` varchar(30) DEFAULT NULL,
  `URL` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID_SitioWeb`),
  KEY `ID_Medio` (`ID_Medio`),
  CONSTRAINT `SitioWeb_ibfk_1` FOREIGN KEY (`ID_Medio`) REFERENCES `Medio` (`ID_Medio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SitioWeb`
--

LOCK TABLES `SitioWeb` WRITE;
/*!40000 ALTER TABLE `SitioWeb` DISABLE KEYS */;
/*!40000 ALTER TABLE `SitioWeb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-17 21:08:48

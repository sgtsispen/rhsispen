-- MySQL dump 10.18  Distrib 10.3.27-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: rhsispen
-- ------------------------------------------------------
-- Server version	10.3.27-MariaDB-0+deb10u1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Afastamento',7,'add_afastamento'),(26,'Can change Afastamento',7,'change_afastamento'),(27,'Can delete Afastamento',7,'delete_afastamento'),(28,'Can view Afastamento',7,'view_afastamento'),(29,'Can add Endereço do Servidor',8,'add_enderecoserv'),(30,'Can change Endereço do Servidor',8,'change_enderecoserv'),(31,'Can delete Endereço do Servidor',8,'delete_enderecoserv'),(32,'Can view Endereço do Servidor',8,'view_enderecoserv'),(33,'Can add Endereço do Setor',9,'add_enderecosetor'),(34,'Can change Endereço do Setor',9,'change_enderecosetor'),(35,'Can delete Endereço do Setor',9,'delete_enderecosetor'),(36,'Can view Endereço do Setor',9,'view_enderecosetor'),(37,'Can add Equipe',10,'add_equipe'),(38,'Can change Equipe',10,'change_equipe'),(39,'Can delete Equipe',10,'delete_equipe'),(40,'Can view Equipe',10,'view_equipe'),(41,'Can add Função',11,'add_funcao'),(42,'Can change Função',11,'change_funcao'),(43,'Can delete Função',11,'delete_funcao'),(44,'Can view Função',11,'view_funcao'),(45,'Can add Região',12,'add_regiao'),(46,'Can change Região',12,'change_regiao'),(47,'Can delete Região',12,'delete_regiao'),(48,'Can view Região',12,'view_regiao'),(49,'Can add Status Funcional',13,'add_statusfuncional'),(50,'Can change Status Funcional',13,'change_statusfuncional'),(51,'Can delete Status Funcional',13,'delete_statusfuncional'),(52,'Can view Status Funcional',13,'view_statusfuncional'),(53,'Can add Tipo de Jornada',14,'add_tipojornada'),(54,'Can change Tipo de Jornada',14,'change_tipojornada'),(55,'Can delete Tipo de Jornada',14,'delete_tipojornada'),(56,'Can view Tipo de Jornada',14,'view_tipojornada'),(57,'Can add Setor',15,'add_setor'),(58,'Can change Setor',15,'change_setor'),(59,'Can delete Setor',15,'delete_setor'),(60,'Can view Setor',15,'view_setor'),(61,'Can add Servidor',16,'add_servidor'),(62,'Can change Servidor',16,'change_servidor'),(63,'Can delete Servidor',16,'delete_servidor'),(64,'Can view Servidor',16,'view_servidor'),(65,'Can add Jornada',17,'add_jornada'),(66,'Can change Jornada',17,'change_jornada'),(67,'Can delete Jornada',17,'delete_jornada'),(68,'Can view Jornada',17,'view_jornada'),(69,'Can add Histórico de Status Funcional',18,'add_histstatusfuncional'),(70,'Can change Histórico de Status Funcional',18,'change_histstatusfuncional'),(71,'Can delete Histórico de Status Funcional',18,'delete_histstatusfuncional'),(72,'Can view Histórico de Status Funcional',18,'view_histstatusfuncional'),(73,'Can add Histórico de Lotação',19,'add_histlotacao'),(74,'Can change Histórico de Lotação',19,'change_histlotacao'),(75,'Can delete Histórico de Lotação',19,'delete_histlotacao'),(76,'Can view Histórico de Lotação',19,'view_histlotacao'),(77,'Can add Histórico de Função',20,'add_histfuncao'),(78,'Can change Histórico de Função',20,'change_histfuncao'),(79,'Can delete Histórico de Função',20,'delete_histfuncao'),(80,'Can view Histórico de Função',20,'view_histfuncao'),(81,'Can add Histório de Afastamento',21,'add_histafastamento'),(82,'Can change Histório de Afastamento',21,'change_histafastamento'),(83,'Can delete Histório de Afastamento',21,'delete_histafastamento'),(84,'Can view Histório de Afastamento',21,'view_histafastamento'),(85,'Can add Contato do Servidor',22,'add_contatoserv'),(86,'Can change Contato do Servidor',22,'change_contatoserv'),(87,'Can delete Contato do Servidor',22,'delete_contatoserv'),(88,'Can view Contato do Servidor',22,'view_contatoserv'),(89,'Can add Contato da Equipe',23,'add_contatoequipe'),(90,'Can change Contato da Equipe',23,'change_contatoequipe'),(91,'Can delete Contato da Equipe',23,'delete_contatoequipe'),(92,'Can view Contato da Equipe',23,'view_contatoequipe');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$88DK0mkpDfZn$z7jz2lM1A1nXLC6b+qRCzWl4PdP2cBu+jK6PLa8t06Y=','2021-02-23 23:08:33.431301',1,'leonardo','','','',1,1,'2021-02-23 23:08:08.583872');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=151 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-02-23 23:34:59.337716','1','1',1,'[{\"added\": {}}]',12,1),(2,'2021-02-23 23:35:04.552799','2','2',1,'[{\"added\": {}}]',12,1),(3,'2021-02-23 23:35:09.212321','3','3',1,'[{\"added\": {}}]',12,1),(4,'2021-02-23 23:35:13.091603','4','4',1,'[{\"added\": {}}]',12,1),(5,'2021-02-23 23:35:17.188669','5','5',1,'[{\"added\": {}}]',12,1),(6,'2021-02-23 23:35:28.977485','6','6',1,'[{\"added\": {}}]',12,1),(7,'2021-02-23 23:35:36.691129','7','7',1,'[{\"added\": {}}]',12,1),(8,'2021-02-23 23:35:40.584106','8','8',1,'[{\"added\": {}}]',12,1),(9,'2021-02-24 00:39:28.915803','1','Palmas - Q. 103 sul rua SO 5',1,'[{\"added\": {}}]',9,1),(10,'2021-02-24 00:44:32.815428','040.CMEPMW','Central de Monitoramento Eletrônico de Pessoas de Palmas',1,'[{\"added\": {}}]',15,1),(11,'2021-02-24 01:24:18.016931','2','Augustinópolis - Rua Eva Carreiro Nogueira',1,'[{\"added\": {}}]',9,1),(12,'2021-02-24 01:25:06.432381','040.UPAUG','Unidade Penal de Augustinópolis',1,'[{\"added\": {}}]',15,1),(13,'2021-02-24 01:30:17.581641','3','Ananás - Rua dos Buritis',1,'[{\"added\": {}}]',9,1),(14,'2021-02-24 01:32:42.688128','040.UPANA','Unidade Penal de Ananás',1,'[{\"added\": {}}]',15,1),(15,'2021-02-24 01:36:14.735231','4','Araguacema - Rua dos estrangeiros',1,'[{\"added\": {}}]',9,1),(16,'2021-02-24 01:36:19.177684','040.UPAGC','Unidade Penal de Araguacema',1,'[{\"added\": {}}]',15,1),(17,'2021-02-24 01:42:04.870842','5','Araguaçu - Rua 27',1,'[{\"added\": {}}]',9,1),(18,'2021-02-24 01:42:38.966446','040.UPAGU','Unidade Penal de Araguaçu',1,'[{\"added\": {}}]',15,1),(19,'2021-02-24 01:45:21.073562','6','Araguaína - Rua Belo Horizonte',1,'[{\"added\": {}}]',9,1),(20,'2021-02-24 01:45:23.813777','040.UPARN','Unidade Penal de Araguaína',1,'[{\"added\": {}}]',15,1),(21,'2021-02-24 01:48:12.972902','7','Araguatins - Rua Siqueira Campos esquina com a rua “D”',1,'[{\"added\": {}}]',9,1),(22,'2021-02-24 01:48:23.729759','040.UPAGN','Unidade Penal de Araguatins',1,'[{\"added\": {}}]',15,1),(23,'2021-02-24 01:50:51.480593','8','Arapoema - Rua dos Garimpeiros',1,'[{\"added\": {}}]',9,1),(24,'2021-02-24 01:50:55.303333','040.UPAPO','Unidade Penal de Arapoema',1,'[{\"added\": {}}]',15,1),(25,'2021-02-24 01:53:43.096330','9','Arraias - Rua 02',1,'[{\"added\": {}}]',9,1),(26,'2021-02-24 01:53:48.492444','040.UPARS','Unidade Penal de Arraias',1,'[{\"added\": {}}]',15,1),(27,'2021-02-24 01:55:28.847193','7','Araguatins - Rua Siqueira Campos',2,'[{\"changed\": {\"fields\": [\"Endereco\", \"Complemento\"]}}]',9,1),(28,'2021-02-24 01:59:15.973634','10','Babaçulândia - Rodovia Trans Dias',1,'[{\"added\": {}}]',9,1),(29,'2021-02-24 01:59:51.684937','040.UPFBA','Unidade Penal Feminina de Babaçulândia',1,'[{\"added\": {}}]',15,1),(30,'2021-02-24 02:05:33.575030','11','Araguaína - Rodovia TO-222, KM 07',1,'[{\"added\": {}}]',9,1),(31,'2021-02-24 02:05:48.059339','040.UNTRAPENAL','Unidade de Tratamento Penal Barra da Grota',1,'[{\"added\": {}}]',15,1),(32,'2021-02-24 02:06:00.897482','040.UPARN','Unidade Penal de Araguaína',2,'[{\"changed\": {\"fields\": [\"Setor sede\"]}}]',15,1),(33,'2021-02-24 02:23:11.511535','12','Barrolândia - Av Bernardo Sayão',1,'[{\"added\": {}}]',9,1),(34,'2021-02-24 02:23:16.966473','040.UPBRD','Unidade Penal de Barrolândia',1,'[{\"added\": {}}]',15,1),(35,'2021-02-24 02:26:12.514049','13','Bernardo Sayão - Segunda Avenida',1,'[{\"added\": {}}]',9,1),(36,'2021-02-24 02:26:43.219762','040.UPBSY','Unidade Penal de Bernardo Sayão',1,'[{\"added\": {}}]',15,1),(37,'2021-02-24 02:32:52.136269','14','Gurupi - Não registrado',1,'[{\"added\": {}}]',9,1),(38,'2021-02-24 02:33:12.079829','040.CMEPGPI','Central de Monitoramento Eletrônico de Pessoas de Gurupi',1,'[{\"added\": {}}]',15,1),(39,'2021-02-24 02:35:12.432967','15','Colinas do Tocantins - Avenida Anhanguera',1,'[{\"added\": {}}]',9,1),(40,'2021-02-24 02:35:57.022636','040.UPCOTO','Unidade Penal de Colinas do Tocantins',1,'[{\"added\": {}}]',15,1),(41,'2021-02-24 02:36:56.325760','16','Colméia - Rua Couto Magalhães',1,'[{\"added\": {}}]',9,1),(42,'2021-02-24 02:37:09.193394','040.UPCLM','Unidade Penal de Colméia',1,'[{\"added\": {}}]',15,1),(43,'2021-02-24 02:40:39.925959','17','Gurupi - Rua A, 281, Quadra 06',1,'[{\"added\": {}}]',9,1),(44,'2021-02-24 02:40:43.186715','040.UPGPI','Unidade Penal de Gurupi',1,'[{\"added\": {}}]',15,1),(45,'2021-02-24 02:44:56.819328','18','Palmas - Rod-TO 020 KM 02',1,'[{\"added\": {}}]',9,1),(46,'2021-02-24 02:45:05.275927','040.UPPMW','Unidade Penal de Palmas',1,'[{\"added\": {}}]',15,1),(47,'2021-02-24 02:54:03.508223','19','Cristalândia - Avenida Dom Jayme',1,'[{\"added\": {}}]',9,1),(48,'2021-02-24 02:54:11.172231','040.UPCRIS','Unidade Penal de Cristalândia',1,'[{\"added\": {}}]',15,1),(49,'2021-02-24 02:56:33.349961','20','Dianópolis - Rua C, Quadra 8, Lote 12',1,'[{\"added\": {}}]',9,1),(50,'2021-02-24 02:56:39.695342','040.UPDNO','Unidade Penal de Dianópolis',1,'[{\"added\": {}}]',15,1),(51,'2021-02-24 02:58:28.847301','21','Formoso do Araguaia - Avenida Dom Pedro II, Quadra 266, Lote 26-A',1,'[{\"added\": {}}]',9,1),(52,'2021-02-24 02:58:49.812902','040.UPFA','Unidade Penal de Formoso do Araguaia',1,'[{\"added\": {}}]',15,1),(53,'2021-02-24 03:00:07.077834','22','Guaraí - Rua Pernambuco, Quadra 05, Lote 01',1,'[{\"added\": {}}]',9,1),(54,'2021-02-24 03:00:10.275965','040.UPGUA','Unidade Penal de Guaraí',1,'[{\"added\": {}}]',15,1),(55,'2021-02-24 03:04:58.515874','23','Lajeado - Rodovia TO-050',1,'[{\"added\": {}}]',9,1),(56,'2021-02-24 03:05:04.364982','040.UPFLAJ','Unidade Penal Feminina de Lajeado',1,'[{\"added\": {}}]',15,1),(57,'2021-02-24 03:08:47.957828','24','Cariri - BR 153, KM 684',1,'[{\"added\": {}}]',9,1),(58,'2021-02-24 03:09:39.137962','040.UPCAR','Unidade Penal do Cariri',1,'[{\"added\": {}}]',15,1),(59,'2021-02-24 03:11:07.311312','25','Miracema do Tocantins - Avenida Industrial',1,'[{\"added\": {}}]',9,1),(60,'2021-02-24 03:11:15.230927','040.UPMIRTO','Unidade Penal de Miracema do Tocantins',1,'[{\"added\": {}}]',15,1),(61,'2021-02-24 03:14:09.478468','26','Miranorte - Avenida Castelo Branco',1,'[{\"added\": {}}]',9,1),(62,'2021-02-24 03:14:26.414973','040.UPMIR','Unidade Penal de Miranorte',1,'[{\"added\": {}}]',15,1),(63,'2021-02-24 03:15:26.407214','27','Natividade - Rua E',1,'[{\"added\": {}}]',9,1),(64,'2021-02-24 03:15:32.626731','040.UPNTV','Unidade Penal de Natividade',1,'[{\"added\": {}}]',15,1),(65,'2021-02-24 03:17:27.854835','28','Palmeirópolis - Rua 5',1,'[{\"added\": {}}]',9,1),(66,'2021-02-24 03:17:53.749754','040.UPPML','Unidade Penal de Palmeirópolis',1,'[{\"added\": {}}]',15,1),(67,'2021-02-24 03:19:58.393358','29','Paraíso do Tocantins - Rua 15',1,'[{\"added\": {}}]',9,1),(68,'2021-02-24 03:20:00.836654','040.UPPSO','Unidade Penal de Paraíso do Tocantins',1,'[{\"added\": {}}]',15,1),(69,'2021-02-24 03:21:26.772689','30','Paranã - Não registrado',1,'[{\"added\": {}}]',9,1),(70,'2021-02-24 03:22:04.419575','040.UPPRN','Unidade Penal de Paranã',1,'[{\"added\": {}}]',15,1),(71,'2021-02-24 03:23:21.479098','31','Pedro Afonso - Avenida João Damasceno',1,'[{\"added\": {}}]',9,1),(72,'2021-02-24 03:24:01.354359','040.UPFPA','Unidade Penal Feminina de Pedro Afonso',1,'[{\"added\": {}}]',15,1),(73,'2021-02-24 03:28:11.633695','32','Peixe - Avenida João Visconde de Queiroz, Quadra 67, Lote 5 a 8',1,'[{\"added\": {}}]',9,1),(74,'2021-02-24 03:28:20.271975','040.UPPXE','Unidade Penal de Peixe',1,'[{\"added\": {}}]',15,1),(75,'2021-02-24 03:30:37.116813','33','Pium - Rua 02',1,'[{\"added\": {}}]',9,1),(76,'2021-02-24 03:30:42.887396','040.UPPM','Unidade Penal de Pium',1,'[{\"added\": {}}]',15,1),(77,'2021-02-24 03:34:40.162005','34','Porto Nacional - Rua Professor Felizmino Ayres Fernandes',1,'[{\"added\": {}}]',9,1),(78,'2021-02-24 03:34:42.972923','040.UPPTN','Unidade Penal de Porto Nacional',1,'[{\"added\": {}}]',15,1),(79,'2021-02-24 03:36:20.610779','35','Talismã - Não registrado',1,'[{\"added\": {}}]',9,1),(80,'2021-02-24 03:41:00.526480','36','Talismã - Não registrado',1,'[{\"added\": {}}]',9,1),(81,'2021-02-24 03:41:27.141114','040.UPTLA','Unidade Penal Feminina de Talismã',1,'[{\"added\": {}}]',15,1),(82,'2021-02-24 03:42:34.045030','37','Taguatinga - Avenida Jose Joaquim de Almeida',1,'[{\"added\": {}}]',9,1),(83,'2021-02-24 03:42:37.692134','040.UPTGA','Unidade Penal de Taguatinga',1,'[{\"added\": {}}]',15,1),(84,'2021-02-24 03:50:44.158106','38','Tocantinópolis - Rua Cruzeiro do Sul',1,'[{\"added\": {}}]',9,1),(85,'2021-02-24 03:51:09.960219','040.UPTOC','Unidade Penal de Tocantinópolis',1,'[{\"added\": {}}]',15,1),(86,'2021-02-24 03:52:59.516881','39','Palmas - Rua Castro Alves, Quadra 4-A, Lote 1 a 6',1,'[{\"added\": {}}]',9,1),(87,'2021-02-24 03:53:18.645123','040.UPFPMW','Unidade Penal Feminina de Palmas',1,'[{\"added\": {}}]',15,1),(88,'2021-02-24 03:54:38.989845','40','Xambioá - Avenida Juarez Forte',1,'[{\"added\": {}}]',9,1),(89,'2021-02-24 03:54:48.004725','040.UPXAM','Unidade Penal de Xambioá',1,'[{\"added\": {}}]',15,1),(90,'2021-02-24 03:55:50.525820','41','Araguaína - Não registrado',1,'[{\"added\": {}}]',9,1),(91,'2021-02-24 03:56:09.817500','040.CMEPARG','Central de Monitoramento Eletrônico de Pessoas de Araguaína',1,'[{\"added\": {}}]',15,1),(92,'2021-02-24 03:59:26.975332','42','Palmas - Rod-TO 020 KM 02',1,'[{\"added\": {}}]',9,1),(93,'2021-02-24 03:59:29.407335','040.GIR','Grupo de Intervenção Rápida',1,'[{\"added\": {}}]',15,1),(94,'2021-02-24 04:01:38.401070','43','Cariri - BR 153, KM 684',1,'[{\"added\": {}}]',9,1),(95,'2021-02-24 04:01:41.017552','040.USMC','Unidade de Segurança Máxima do Cariri',1,'[{\"added\": {}}]',15,1),(96,'2021-02-24 04:03:21.722761','44','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(97,'2021-02-24 04:03:23.679874','040.ESCSOC','Escritório Social',1,'[{\"added\": {}}]',15,1),(98,'2021-02-24 04:04:29.929753','45','Cariri - BR 153, KM 684',1,'[{\"added\": {}}]',9,1),(99,'2021-02-24 04:05:05.821486','040.FAACR','Fazenda Agrícola e Agropecuária do Cariri',1,'[{\"added\": {}}]',15,1),(100,'2021-02-24 04:08:05.028395','46','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(101,'2021-02-24 04:08:11.599751','000.COEP','Coordenação de Operações de Escolta Penal',1,'[{\"added\": {}}]',15,1),(102,'2021-02-24 04:09:54.127580','47','Araguaína - Não registrado',1,'[{\"added\": {}}]',9,1),(103,'2021-02-24 04:09:56.169700','000.GTE2R','Grupo Tático de Escolda da 2º Regional',1,'[{\"added\": {}}]',15,1),(104,'2021-02-24 04:10:31.793500','48','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(105,'2021-02-24 04:10:33.426143','000.GTE5R','Grupo Tático de Escolda da 5º Regional',1,'[{\"added\": {}}]',15,1),(106,'2021-02-24 04:11:16.745924','49','Cariri - Não registrado',1,'[{\"added\": {}}]',9,1),(107,'2021-02-24 04:11:20.490040','000.GTE6R','Grupo Tático de Escolda da 6º Regional',1,'[{\"added\": {}}]',15,1),(108,'2021-02-24 04:12:20.427373','50','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(109,'2021-02-24 04:12:22.244163','040.CEPEMA','Central de Penas e Medidas Alternativas de Palmas',1,'[{\"added\": {}}]',15,1),(110,'2021-02-24 04:12:58.855328','51','Araguaína - Não registrado',1,'[{\"added\": {}}]',9,1),(111,'2021-02-24 04:13:01.163268','040.CEPEMARA','Central de Penas e Medidas Alternativas de Araguaína',1,'[{\"added\": {}}]',15,1),(112,'2021-02-24 04:14:07.260302','52','Cariri - Não registrado',1,'[{\"added\": {}}]',9,1),(113,'2021-02-24 04:15:33.283392','040.CEPEMAGU','Central de Penas e Medidas Alternativas de Gurupi',1,'[{\"added\": {}}]',15,1),(114,'2021-02-24 04:16:09.163751','53','Paraíso do Tocantins - Não registrado',1,'[{\"added\": {}}]',9,1),(115,'2021-02-24 04:16:23.860403','040.CEPEMAPSO','Central de Penas e Medidas Alternativas de Paraíso do Tocantins',1,'[{\"added\": {}}]',15,1),(116,'2021-02-24 04:16:58.214098','54','Porto Nacional - Não registrado',1,'[{\"added\": {}}]',9,1),(117,'2021-02-24 04:17:00.262731','040.CEPEMAPTN','Central de Penas e Medidas Alternativas de Porto Nacional',1,'[{\"added\": {}}]',15,1),(118,'2021-02-24 04:17:46.218011','55','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(119,'2021-02-24 04:17:49.100340','040.NOC','Núcleo de Operações com Cães - NOC',1,'[{\"added\": {}}]',15,1),(120,'2021-02-24 04:23:16.254113','56','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(121,'2021-02-24 04:23:19.133786','040.GOI','Grupo de Operações de Inteligência',1,'[{\"added\": {}}]',15,1),(122,'2021-02-24 04:24:23.917738','57','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(123,'2021-02-24 04:24:25.782601','040.GESINSPS','Gerência dos Serviços de Inteligência dos Sistemas Prisional e Socioeducativo',1,'[{\"added\": {}}]',15,1),(124,'2021-02-24 04:25:00.841580','58','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(125,'2021-02-24 04:25:02.184726','040.GPALP','Gerência de Políticas de Alternativas Penais',1,'[{\"added\": {}}]',15,1),(126,'2021-02-24 04:25:56.654119','59','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(127,'2021-02-24 04:26:04.935373','040.GAOSISPENP','Gerência de Administração e Operações do Sistema Penitenciário e Pricional',1,'[{\"added\": {}}]',15,1),(128,'2021-02-24 04:27:12.511587','60','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(129,'2021-02-24 04:27:13.238953','040.GESUP','Gerência da Escola Superior de Gestão dos Sistemas Penitenciário e Prisional - ESGEPEN',1,'[{\"added\": {}}]',15,1),(130,'2021-02-24 04:27:34.146157','61','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(131,'2021-02-24 04:27:53.767585','040.GEREIS','Gerência de Reintegração Social',1,'[{\"added\": {}}]',15,1),(132,'2021-02-24 04:28:19.611090','62','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(133,'2021-02-24 04:28:21.627731','040.GASEC','Gabinete do Secretário',1,'[{\"added\": {}}]',15,1),(134,'2021-02-24 04:29:28.412270','63','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(135,'2021-02-24 04:29:30.114062','040.GASSESPE','Gerência de Assistência Educacional e Saúde ao Preso e Egresso',1,'[{\"added\": {}}]',15,1),(136,'2021-02-24 04:30:31.927807','64','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(137,'2021-02-24 04:30:35.318007','040.GICRESP','Gerência de Inclusão, Classificação e Remoção do Sistema Penitenciário e Prisional',1,'[{\"added\": {}}]',15,1),(138,'2021-02-24 04:31:15.579972','65','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(139,'2021-02-24 04:31:16.331783','040.GMONEP','Gerência de Monitoramento Eletrônico de Pessoas',1,'[{\"added\": {}}]',15,1),(140,'2021-02-24 04:34:39.772252','66','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(141,'2021-02-24 04:34:40.965512','040.GEGRISP','Gerência de Procedimentos de Grupo de Risco do Sistemas Penitenciário',1,'[{\"added\": {}}]',15,1),(142,'2021-02-24 04:35:56.035221','67','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(143,'2021-02-24 04:35:58.757197','040.GERSINDPRS','Gerência de Sindicância Disciplinar dos Sistemas Prisional e Socioeducativo',1,'[{\"added\": {}}]',15,1),(144,'2021-02-24 04:39:39.821574','040.GEGRISP','Gerência de Procedimentos de Grupo de Risco dos Sistemas Penitenciário',2,'[{\"changed\": {\"fields\": [\"Nome\"]}}]',15,1),(145,'2021-02-24 04:43:22.835020','68','Araguaína - Não registrado',1,'[{\"added\": {}}]',9,1),(146,'2021-02-24 04:43:25.247032','040.DOC2','Divisão de Operações com Cães 2º Regional',1,'[{\"added\": {}}]',15,1),(147,'2021-02-24 04:44:01.025313','69','Cariri - Não registrado',1,'[{\"added\": {}}]',9,1),(148,'2021-02-24 04:44:05.312682','040.DOC6','Divisão de Operações com Cães 6º Regional',1,'[{\"added\": {}}]',15,1),(149,'2021-02-24 04:47:12.819706','70','Palmas - Não registrado',1,'[{\"added\": {}}]',9,1),(150,'2021-02-24 04:47:14.308560','040.SUPASPEN','Superintendência de Administração dos Sistemas Penitenciário e Prisional',1,'[{\"added\": {}}]',15,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'namp','afastamento'),(23,'namp','contatoequipe'),(22,'namp','contatoserv'),(8,'namp','enderecoserv'),(9,'namp','enderecosetor'),(10,'namp','equipe'),(11,'namp','funcao'),(21,'namp','histafastamento'),(20,'namp','histfuncao'),(19,'namp','histlotacao'),(18,'namp','histstatusfuncional'),(17,'namp','jornada'),(12,'namp','regiao'),(16,'namp','servidor'),(15,'namp','setor'),(13,'namp','statusfuncional'),(14,'namp','tipojornada'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-02-23 23:05:47.962579'),(2,'auth','0001_initial','2021-02-23 23:05:50.475586'),(3,'admin','0001_initial','2021-02-23 23:06:00.284032'),(4,'admin','0002_logentry_remove_auto_add','2021-02-23 23:06:02.607932'),(5,'admin','0003_logentry_add_action_flag_choices','2021-02-23 23:06:02.667644'),(6,'contenttypes','0002_remove_content_type_name','2021-02-23 23:06:04.648275'),(7,'auth','0002_alter_permission_name_max_length','2021-02-23 23:06:06.455812'),(8,'auth','0003_alter_user_email_max_length','2021-02-23 23:06:06.645116'),(9,'auth','0004_alter_user_username_opts','2021-02-23 23:06:06.742107'),(10,'auth','0005_alter_user_last_login_null','2021-02-23 23:06:07.594987'),(11,'auth','0006_require_contenttypes_0002','2021-02-23 23:06:07.650013'),(12,'auth','0007_alter_validators_add_error_messages','2021-02-23 23:06:07.712900'),(13,'auth','0008_alter_user_username_max_length','2021-02-23 23:06:08.978380'),(14,'auth','0009_alter_user_last_name_max_length','2021-02-23 23:06:10.629127'),(15,'auth','0010_alter_group_name_max_length','2021-02-23 23:06:10.785277'),(16,'auth','0011_update_proxy_permissions','2021-02-23 23:06:10.861077'),(17,'auth','0012_alter_user_first_name_max_length','2021-02-23 23:06:12.347328'),(18,'namp','0001_initial','2021-02-23 23:06:19.641573'),(19,'sessions','0001_initial','2021-02-23 23:06:43.901679');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('7ojw0vk2hm21qfe1ilxh1re715omwqtr','.eJxVjDsOwjAQRO_iGlnrrwwlPWewdu01DiBbipMKcXcSKQV0o3lv5i0irkuN6-A5TllchBKn344wPbntID-w3btMvS3zRHJX5EGHvPXMr-vh_h1UHHVbM1qvQSUItvA5b1E5g0SKAYoz2QKXUkJ2mlRA7ww4pxOA92SST0F8vtn6N3w:1lEgnB:w3UIlyzsQuq_C4sNsbRWW5lUXjhUptF3FbSDA7wKedc','2021-03-09 23:08:33.476541');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_afastamento`
--

DROP TABLE IF EXISTS `namp_afastamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_afastamento` (
  `id_afastamento` varchar(25) NOT NULL,
  `tipificacao` varchar(50) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  PRIMARY KEY (`id_afastamento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_afastamento`
--

LOCK TABLES `namp_afastamento` WRITE;
/*!40000 ALTER TABLE `namp_afastamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_afastamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_contatoequipe`
--

DROP TABLE IF EXISTS `namp_contatoequipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_contatoequipe` (
  `id_contato_equipe` int(11) NOT NULL AUTO_INCREMENT,
  `tipificacao` varchar(50) NOT NULL,
  `contato` varchar(50) NOT NULL,
  `fk_equipe_id` int(11) NOT NULL,
  PRIMARY KEY (`id_contato_equipe`),
  KEY `namp_contatoequipe_fk_equipe_id_50fcc1f5_fk_namp_equi` (`fk_equipe_id`),
  CONSTRAINT `namp_contatoequipe_fk_equipe_id_50fcc1f5_fk_namp_equi` FOREIGN KEY (`fk_equipe_id`) REFERENCES `namp_equipe` (`id_equipe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_contatoequipe`
--

LOCK TABLES `namp_contatoequipe` WRITE;
/*!40000 ALTER TABLE `namp_contatoequipe` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_contatoequipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_contatoserv`
--

DROP TABLE IF EXISTS `namp_contatoserv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_contatoserv` (
  `id_contato_serv` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_contato` varchar(100) NOT NULL,
  `contato` varchar(100) NOT NULL,
  `fk_servidor_id` varchar(30) NOT NULL,
  PRIMARY KEY (`id_contato_serv`),
  KEY `namp_contatoserv_fk_servidor_id_6d709b58_fk_namp_serv` (`fk_servidor_id`),
  CONSTRAINT `namp_contatoserv_fk_servidor_id_6d709b58_fk_namp_serv` FOREIGN KEY (`fk_servidor_id`) REFERENCES `namp_servidor` (`id_matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_contatoserv`
--

LOCK TABLES `namp_contatoserv` WRITE;
/*!40000 ALTER TABLE `namp_contatoserv` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_contatoserv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_enderecoserv`
--

DROP TABLE IF EXISTS `namp_enderecoserv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_enderecoserv` (
  `id_endereco_serv` int(11) NOT NULL AUTO_INCREMENT,
  `uf` varchar(2) NOT NULL,
  `cep` varchar(8) NOT NULL,
  `municipio` varchar(100) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `numero` varchar(10) NOT NULL,
  `bairro` varchar(100) NOT NULL,
  `complemento` varchar(100) NOT NULL,
  PRIMARY KEY (`id_endereco_serv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_enderecoserv`
--

LOCK TABLES `namp_enderecoserv` WRITE;
/*!40000 ALTER TABLE `namp_enderecoserv` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_enderecoserv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_enderecosetor`
--

DROP TABLE IF EXISTS `namp_enderecosetor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_enderecosetor` (
  `id_endereco_setor` int(11) NOT NULL AUTO_INCREMENT,
  `uf` varchar(2) NOT NULL,
  `cep` varchar(8) NOT NULL,
  `municipio` varchar(100) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `numero` varchar(10) NOT NULL,
  `bairro` varchar(100) NOT NULL,
  `complemento` varchar(100) NOT NULL,
  PRIMARY KEY (`id_endereco_setor`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_enderecosetor`
--

LOCK TABLES `namp_enderecosetor` WRITE;
/*!40000 ALTER TABLE `namp_enderecosetor` DISABLE KEYS */;
INSERT INTO `namp_enderecosetor` VALUES (1,'TO','77015018','Palmas','Q. 103 sul rua SO 5','22','Plano diretor sul','Ao lado do Hotel Castro'),(2,'TO','77960000','Augustinópolis','Rua Eva Carreiro Nogueira','s/n','Bairro São Pedro',''),(3,'TO','77890000','Ananás','Rua dos Buritis','s/n','Bairro Chapadinha I',''),(4,'TO','77690000','Araguacema','Rua dos estrangeiros','s/n','Cidade alta',''),(5,'TO','77475000','Araguaçu','Rua 27','627','Centro',''),(6,'TO','77800000','Araguaína','Rua Belo Horizonte','38','Setor Urbano',''),(7,'TO','77950000','Araguatins','Rua Siqueira Campos','s/n','Centro','Esquina com a rua “D”'),(8,'TO','77801000','Arapoema','Rua dos Garimpeiros','646','Centro',''),(9,'TO','77330000','Arraias','Rua 02','s/n','Parque das Colinas',''),(10,'TO','77870000','Babaçulândia','Rodovia Trans Dias','s/n','Centro',''),(11,'TO','77835640','Araguaína','Rodovia TO-222, KM 07','s/n','','Povoado Barra da Grota'),(12,'TO','77665000','Barrolândia','Av Bernardo Sayão','s/n','Centro',''),(13,'TO','77755000','Bernardo Sayão','Segunda Avenida','s/n','Centro',''),(14,'TO','77415370','Gurupi','Não registrado','s/n','',''),(15,'TO','77760000','Colinas do Tocantins','Avenida Anhanguera','1073','Centro',''),(16,'TO','77725000','Colméia','Rua Couto Magalhães','595','Centro',''),(17,'TO','77402080','Gurupi','Rua A, 281, Quadra 06','s/n','Setor Cruzeiro',''),(18,'TO','77000000','Palmas','Rod-TO 020 KM 02','s/n','','Saída para Aparecida do Rio Negro'),(19,'TO','77490000','Cristalândia','Avenida Dom Jayme','2845','Centro',''),(20,'TO','77300000','Dianópolis','Rua C, Quadra 8, Lote 12','12','Setor Nova Cidade',''),(21,'TO','77470000','Formoso do Araguaia','Avenida Dom Pedro II, Quadra 266, Lote 26-A','26-A','Setor São Jose II',''),(22,'TO','77700000','Guaraí','Rua Pernambuco, Quadra 05, Lote 01','1','Setor Canaã',''),(23,'TO','77655000','Lajeado','Rodovia TO-050','s/n','Zona Urbana',''),(24,'TO','77453000','Cariri','BR 153, KM 684','s/n','Zona Rural','Cariri'),(25,'TO','77650000','Miracema do Tocantins','Avenida Industrial','1097','Bairro Vila Maria',''),(26,'TO','77660000','Miranorte','Avenida Castelo Branco','2438','Centro',''),(27,'TO','77370000','Natividade','Rua E','s/n','Setor Ginasial',''),(28,'TO','77365000','Palmeirópolis','Rua 5','471','Centro',''),(29,'TO','77600000','Paraíso do Tocantins','Rua 15','800','Setor Oeste',''),(30,'TO','77360000','Paranã','Não registrado','','',''),(31,'TO','77710000','Pedro Afonso','Avenida João Damasceno','','Aeroporto',''),(32,'TO','77460000','Peixe','Avenida João Visconde de Queiroz, Quadra 67, Lote 5 a 8','5','Setor Sul',''),(33,'TO','77570000','Pium','Rua 02','306','','Praça da Matriz'),(34,'TO','77500000','Porto Nacional','Rua Professor Felizmino Ayres Fernandes','s/n','Setor Nova Capital',''),(35,'TO','77483000','Talismã','Não registrado','','',''),(36,'TO','','Talismã','Não registrado','','',''),(37,'TO','77320000','Taguatinga','Avenida Jose Joaquim de Almeida','s/n','',''),(38,'TO','77900000','Tocantinópolis','Rua Cruzeiro do Sul','s/n','Setor Rodoviário',''),(39,'TO','77270000','Palmas','Rua Castro Alves, Quadra 4-A, Lote 1 a 6','1','Setor Bela Vista',''),(40,'TO','77880000','Xambioá','Avenida Juarez Forte','1437','Setor trecho seco',''),(41,'TO','','Araguaína','Não registrado','','',''),(42,'TO','77000000','Palmas','Rod-TO 020 KM 02','','','Saída para Aparecida do Rio Negro'),(43,'TO','77453000','Cariri','BR 153, KM 684','','Zona Rural','Cariri'),(44,'TO','77000000','Palmas','Não registrado','','',''),(45,'TO','77453000','Cariri','BR 153, KM 684','','Zona Rural','Cariri'),(46,'TO','77000000','Palmas','Não registrado','','',''),(47,'TO','','Araguaína','Não registrado','','',''),(48,'TO','77000000','Palmas','Não registrado','','',''),(49,'TO','','Cariri','Não registrado','','',''),(50,'TO','','Palmas','Não registrado','','',''),(51,'TO','','Araguaína','Não registrado','','',''),(52,'TO','','Cariri','Não registrado','','',''),(53,'TO','','Paraíso do Tocantins','Não registrado','','',''),(54,'TO','','Porto Nacional','Não registrado','','',''),(55,'TO','','Palmas','Não registrado','','',''),(56,'TO','77000000','Palmas','Não registrado','','',''),(57,'TO','77000000','Palmas','Não registrado','','',''),(58,'TO','77000000','Palmas','Não registrado','','',''),(59,'TO','77000000','Palmas','Não registrado','','',''),(60,'TO','77000000','Palmas','Não registrado','','',''),(61,'TO','77000000','Palmas','Não registrado','','',''),(62,'TO','77000000','Palmas','Não registrado','','',''),(63,'TO','77000000','Palmas','Não registrado','','',''),(64,'TO','77000000','Palmas','Não registrado','','',''),(65,'TO','77000000','Palmas','Não registrado','','',''),(66,'TO','77000000','Palmas','Não registrado','','',''),(67,'TO','77000000','Palmas','Não registrado','','',''),(68,'TO','','Araguaína','Não registrado','','',''),(69,'TO','','Cariri','Não registrado','','',''),(70,'TO','77000000','Palmas','Não registrado','','','');
/*!40000 ALTER TABLE `namp_enderecosetor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_equipe`
--

DROP TABLE IF EXISTS `namp_equipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_equipe` (
  `id_equipe` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `hora_inicial` time(6) NOT NULL,
  `categoria` varchar(50) NOT NULL,
  `fk_setor_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id_equipe`),
  KEY `namp_equipe_fk_setor_id_29f766c2_fk_namp_setor_id_setor` (`fk_setor_id`),
  CONSTRAINT `namp_equipe_fk_setor_id_29f766c2_fk_namp_setor_id_setor` FOREIGN KEY (`fk_setor_id`) REFERENCES `namp_setor` (`id_setor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_equipe`
--

LOCK TABLES `namp_equipe` WRITE;
/*!40000 ALTER TABLE `namp_equipe` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_equipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_funcao`
--

DROP TABLE IF EXISTS `namp_funcao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_funcao` (
  `id_funcao` varchar(25) NOT NULL,
  `nome` varchar(100) NOT NULL,
  PRIMARY KEY (`id_funcao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_funcao`
--

LOCK TABLES `namp_funcao` WRITE;
/*!40000 ALTER TABLE `namp_funcao` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_funcao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_histafastamento`
--

DROP TABLE IF EXISTS `namp_histafastamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_histafastamento` (
  `id_hist_afastamento` int(11) NOT NULL AUTO_INCREMENT,
  `data_inicial` date NOT NULL,
  `duracao` int(10) unsigned NOT NULL CHECK (`duracao` >= 0),
  `fk_afastamento_id` varchar(25) NOT NULL,
  `fk_servidor_id` varchar(30) NOT NULL,
  PRIMARY KEY (`id_hist_afastamento`),
  KEY `namp_histafastamento_fk_afastamento_id_d86ceb63_fk_namp_afas` (`fk_afastamento_id`),
  KEY `namp_histafastamento_fk_servidor_id_16028649_fk_namp_serv` (`fk_servidor_id`),
  CONSTRAINT `namp_histafastamento_fk_afastamento_id_d86ceb63_fk_namp_afas` FOREIGN KEY (`fk_afastamento_id`) REFERENCES `namp_afastamento` (`id_afastamento`),
  CONSTRAINT `namp_histafastamento_fk_servidor_id_16028649_fk_namp_serv` FOREIGN KEY (`fk_servidor_id`) REFERENCES `namp_servidor` (`id_matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_histafastamento`
--

LOCK TABLES `namp_histafastamento` WRITE;
/*!40000 ALTER TABLE `namp_histafastamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_histafastamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_histfuncao`
--

DROP TABLE IF EXISTS `namp_histfuncao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_histfuncao` (
  `id_hist_funcao` int(11) NOT NULL AUTO_INCREMENT,
  `data_inicio` date NOT NULL,
  `data_final` date NOT NULL,
  `fk_funcao_id` varchar(25) NOT NULL,
  `fk_servidor_id` varchar(30) NOT NULL,
  PRIMARY KEY (`id_hist_funcao`),
  KEY `namp_histfuncao_fk_funcao_id_fb386d82_fk_namp_funcao_id_funcao` (`fk_funcao_id`),
  KEY `namp_histfuncao_fk_servidor_id_6c23d507_fk_namp_serv` (`fk_servidor_id`),
  CONSTRAINT `namp_histfuncao_fk_funcao_id_fb386d82_fk_namp_funcao_id_funcao` FOREIGN KEY (`fk_funcao_id`) REFERENCES `namp_funcao` (`id_funcao`),
  CONSTRAINT `namp_histfuncao_fk_servidor_id_6c23d507_fk_namp_serv` FOREIGN KEY (`fk_servidor_id`) REFERENCES `namp_servidor` (`id_matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_histfuncao`
--

LOCK TABLES `namp_histfuncao` WRITE;
/*!40000 ALTER TABLE `namp_histfuncao` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_histfuncao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_histlotacao`
--

DROP TABLE IF EXISTS `namp_histlotacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_histlotacao` (
  `id_hist_lotacao` int(11) NOT NULL AUTO_INCREMENT,
  `data_inicial` date NOT NULL,
  `data_final` date NOT NULL,
  `fk_equipe_id` int(11) NOT NULL,
  `fk_servidor_id` varchar(30) NOT NULL,
  PRIMARY KEY (`id_hist_lotacao`),
  KEY `namp_histlotacao_fk_equipe_id_ba29e270_fk_namp_equipe_id_equipe` (`fk_equipe_id`),
  KEY `namp_histlotacao_fk_servidor_id_2b863bb6_fk_namp_serv` (`fk_servidor_id`),
  CONSTRAINT `namp_histlotacao_fk_equipe_id_ba29e270_fk_namp_equipe_id_equipe` FOREIGN KEY (`fk_equipe_id`) REFERENCES `namp_equipe` (`id_equipe`),
  CONSTRAINT `namp_histlotacao_fk_servidor_id_2b863bb6_fk_namp_serv` FOREIGN KEY (`fk_servidor_id`) REFERENCES `namp_servidor` (`id_matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_histlotacao`
--

LOCK TABLES `namp_histlotacao` WRITE;
/*!40000 ALTER TABLE `namp_histlotacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_histlotacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_histstatusfuncional`
--

DROP TABLE IF EXISTS `namp_histstatusfuncional`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_histstatusfuncional` (
  `id_hist_funcional` int(11) NOT NULL AUTO_INCREMENT,
  `data_inicial` date NOT NULL,
  `data_final` date NOT NULL,
  `fk_servidor_id` varchar(30) NOT NULL,
  `fk_status_funcional_id` int(11) NOT NULL,
  PRIMARY KEY (`id_hist_funcional`),
  KEY `namp_histstatusfunci_fk_servidor_id_37d67170_fk_namp_serv` (`fk_servidor_id`),
  KEY `namp_histstatusfunci_fk_status_funcional__19b63cb9_fk_namp_stat` (`fk_status_funcional_id`),
  CONSTRAINT `namp_histstatusfunci_fk_servidor_id_37d67170_fk_namp_serv` FOREIGN KEY (`fk_servidor_id`) REFERENCES `namp_servidor` (`id_matricula`),
  CONSTRAINT `namp_histstatusfunci_fk_status_funcional__19b63cb9_fk_namp_stat` FOREIGN KEY (`fk_status_funcional_id`) REFERENCES `namp_statusfuncional` (`id_status_funcional`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_histstatusfuncional`
--

LOCK TABLES `namp_histstatusfuncional` WRITE;
/*!40000 ALTER TABLE `namp_histstatusfuncional` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_histstatusfuncional` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_jornada`
--

DROP TABLE IF EXISTS `namp_jornada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_jornada` (
  `id_jornada` int(11) NOT NULL AUTO_INCREMENT,
  `data_jornada` date NOT NULL,
  `assiduidade` tinyint(1) NOT NULL,
  `fk_equipe_id` int(11) NOT NULL,
  `fk_servidor_id` varchar(30) NOT NULL,
  `fk_tipo_jornada_id` int(11) NOT NULL,
  PRIMARY KEY (`id_jornada`),
  KEY `namp_jornada_fk_equipe_id_80e1e00c_fk_namp_equipe_id_equipe` (`fk_equipe_id`),
  KEY `namp_jornada_fk_servidor_id_6b15c827_fk_namp_serv` (`fk_servidor_id`),
  KEY `namp_jornada_fk_tipo_jornada_id_b44f655e_fk_namp_tipo` (`fk_tipo_jornada_id`),
  CONSTRAINT `namp_jornada_fk_equipe_id_80e1e00c_fk_namp_equipe_id_equipe` FOREIGN KEY (`fk_equipe_id`) REFERENCES `namp_equipe` (`id_equipe`),
  CONSTRAINT `namp_jornada_fk_servidor_id_6b15c827_fk_namp_serv` FOREIGN KEY (`fk_servidor_id`) REFERENCES `namp_servidor` (`id_matricula`),
  CONSTRAINT `namp_jornada_fk_tipo_jornada_id_b44f655e_fk_namp_tipo` FOREIGN KEY (`fk_tipo_jornada_id`) REFERENCES `namp_tipojornada` (`id_tipo_jornada`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_jornada`
--

LOCK TABLES `namp_jornada` WRITE;
/*!40000 ALTER TABLE `namp_jornada` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_jornada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_regiao`
--

DROP TABLE IF EXISTS `namp_regiao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_regiao` (
  `id_regiao` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  PRIMARY KEY (`id_regiao`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_regiao`
--

LOCK TABLES `namp_regiao` WRITE;
/*!40000 ALTER TABLE `namp_regiao` DISABLE KEYS */;
INSERT INTO `namp_regiao` VALUES (1,'Região Operacional Administrativa I'),(2,'Região Operacional Administrativa II'),(3,'Região Operacional Administrativa III'),(4,'Região Operacional Administrativa IV'),(5,'Região Operacional Administrativa V'),(6,'Região Operacional Administrativa VI'),(7,'Região Operacional Administrativa VII'),(8,'Região Operacional Administrativa VIII');
/*!40000 ALTER TABLE `namp_regiao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_servidor`
--

DROP TABLE IF EXISTS `namp_servidor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_servidor` (
  `id_matricula` varchar(30) NOT NULL,
  `vinculo` varchar(3) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `sexo` varchar(1) NOT NULL,
  `dt_nasc` date NOT NULL,
  `cargo` varchar(50) NOT NULL,
  `tipo_vinculo` varchar(50) NOT NULL,
  `regime_juridico` varchar(50) NOT NULL,
  `situacao` tinyint(1) NOT NULL,
  `fk_endereco_serv_id` int(11) NOT NULL,
  `fk_equipe_id` int(11) NOT NULL,
  PRIMARY KEY (`id_matricula`),
  UNIQUE KEY `fk_endereco_serv_id` (`fk_endereco_serv_id`),
  KEY `namp_servidor_fk_equipe_id_352fffb3_fk_namp_equipe_id_equipe` (`fk_equipe_id`),
  CONSTRAINT `namp_servidor_fk_endereco_serv_id_0ec09cf8_fk_namp_ende` FOREIGN KEY (`fk_endereco_serv_id`) REFERENCES `namp_enderecoserv` (`id_endereco_serv`),
  CONSTRAINT `namp_servidor_fk_equipe_id_352fffb3_fk_namp_equipe_id_equipe` FOREIGN KEY (`fk_equipe_id`) REFERENCES `namp_equipe` (`id_equipe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_servidor`
--

LOCK TABLES `namp_servidor` WRITE;
/*!40000 ALTER TABLE `namp_servidor` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_servidor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_setor`
--

DROP TABLE IF EXISTS `namp_setor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_setor` (
  `id_setor` varchar(50) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `setor_sede` tinyint(1) NOT NULL,
  `fk_endereco_setor_id` int(11) NOT NULL,
  `fk_regiao_id` int(11) NOT NULL,
  PRIMARY KEY (`id_setor`),
  UNIQUE KEY `fk_endereco_setor_id` (`fk_endereco_setor_id`),
  KEY `namp_setor_fk_regiao_id_a3c40670_fk_namp_regiao_id_regiao` (`fk_regiao_id`),
  CONSTRAINT `namp_setor_fk_endereco_setor_id_2d39fe17_fk_namp_ende` FOREIGN KEY (`fk_endereco_setor_id`) REFERENCES `namp_enderecosetor` (`id_endereco_setor`),
  CONSTRAINT `namp_setor_fk_regiao_id_a3c40670_fk_namp_regiao_id_regiao` FOREIGN KEY (`fk_regiao_id`) REFERENCES `namp_regiao` (`id_regiao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_setor`
--

LOCK TABLES `namp_setor` WRITE;
/*!40000 ALTER TABLE `namp_setor` DISABLE KEYS */;
INSERT INTO `namp_setor` VALUES ('000.COEP','Coordenação de Operações de Escolta Penal',1,0,46,5),('000.GTE2R','Grupo Tático de Escolda da 2º Regional',1,0,47,2),('000.GTE5R','Grupo Tático de Escolda da 5º Regional',1,0,48,5),('000.GTE6R','Grupo Tático de Escolda da 6º Regional',1,0,49,6),('040.CEPEMA','Central de Penas e Medidas Alternativas de Palmas',1,0,50,5),('040.CEPEMAGU','Central de Penas e Medidas Alternativas de Gurupi',1,0,52,6),('040.CEPEMAPSO','Central de Penas e Medidas Alternativas de Paraíso do Tocantins',1,0,53,4),('040.CEPEMAPTN','Central de Penas e Medidas Alternativas de Porto Nacional',1,0,54,5),('040.CEPEMARA','Central de Penas e Medidas Alternativas de Araguaína',1,0,51,2),('040.CMEPARG','Central de Monitoramento Eletrônico de Pessoas de Araguaína',1,0,41,2),('040.CMEPGPI','Central de Monitoramento Eletrônico de Pessoas de Gurupi',1,0,14,6),('040.CMEPMW','Central de Monitoramento Eletrônico de Pessoas de Palmas',1,0,1,5),('040.DOC2','Divisão de Operações com Cães 2º Regional',1,0,68,2),('040.DOC6','Divisão de Operações com Cães 6º Regional',1,0,69,6),('040.ESCSOC','Escritório Social',1,0,44,5),('040.FAACR','Fazenda Agrícola e Agropecuária do Cariri',1,0,45,6),('040.GAOSISPENP','Gerência de Administração e Operações do Sistema Penitenciário e Pricional',1,0,59,5),('040.GASEC','Gabinete do Secretário',1,0,62,5),('040.GASSESPE','Gerência de Assistência Educacional e Saúde ao Preso e Egresso',1,0,63,5),('040.GEGRISP','Gerência de Procedimentos de Grupo de Risco dos Sistemas Penitenciário',1,0,66,5),('040.GEREIS','Gerência de Reintegração Social',1,0,61,5),('040.GERSINDPRS','Gerência de Sindicância Disciplinar dos Sistemas Prisional e Socioeducativo',1,0,67,5),('040.GESINSPS','Gerência dos Serviços de Inteligência dos Sistemas Prisional e Socioeducativo',1,0,57,5),('040.GESUP','Gerência da Escola Superior de Gestão dos Sistemas Penitenciário e Prisional - ESGEPEN',1,0,60,5),('040.GICRESP','Gerência de Inclusão, Classificação e Remoção do Sistema Penitenciário e Prisional',1,0,64,5),('040.GIR','Grupo de Intervenção Rápida',1,0,42,5),('040.GMONEP','Gerência de Monitoramento Eletrônico de Pessoas',1,0,65,5),('040.GOI','Grupo de Operações de Inteligência',1,0,56,5),('040.GPALP','Gerência de Políticas de Alternativas Penais',1,0,58,5),('040.NOC','Núcleo de Operações com Cães - NOC',1,0,55,5),('040.SUPASPEN','Superintendência de Administração dos Sistemas Penitenciário e Prisional',1,0,70,5),('040.UNTRAPENAL','Unidade de Tratamento Penal Barra da Grota',1,1,11,2),('040.UPAGC','Unidade Penal de Araguacema',1,0,4,4),('040.UPAGN','Unidade Penal de Araguatins',1,1,7,1),('040.UPAGU','Unidade Penal de Araguaçu',1,0,5,6),('040.UPANA','Unidade Penal de Ananás',1,0,3,2),('040.UPAPO','Unidade Penal de Arapoema',1,0,8,3),('040.UPARN','Unidade Penal de Araguaína',1,0,6,2),('040.UPARS','Unidade Penal de Arraias',1,1,9,8),('040.UPAUG','Unidade Penal de Augustinópolis',1,0,2,1),('040.UPBRD','Unidade Penal de Barrolândia',1,0,12,4),('040.UPBSY','Unidade Penal de Bernardo Sayão',0,0,13,3),('040.UPCAR','Unidade Penal do Cariri',0,0,24,6),('040.UPCLM','Unidade Penal de Colméia',1,0,16,3),('040.UPCOTO','Unidade Penal de Colinas do Tocantins',1,0,15,3),('040.UPCRIS','Unidade Penal de Cristalândia',1,0,19,4),('040.UPDNO','Unidade Penal de Dianópolis',1,1,20,7),('040.UPFA','Unidade Penal de Formoso do Araguaia',1,0,21,6),('040.UPFBA','Unidade Penal Feminina de Babaçulândia',1,0,10,2),('040.UPFLAJ','Unidade Penal Feminina de Lajeado',1,0,23,5),('040.UPFPA','Unidade Penal Feminina de Pedro Afonso',1,0,31,3),('040.UPFPMW','Unidade Penal Feminina de Palmas',1,0,39,5),('040.UPGPI','Unidade Penal de Gurupi',1,0,17,6),('040.UPGUA','Unidade Penal de Guaraí',1,1,22,3),('040.UPMIR','Unidade Penal de Miranorte',1,0,26,5),('040.UPMIRTO','Unidade Penal de Miracema do Tocantins',1,0,25,5),('040.UPNTV','Unidade Penal de Natividade',1,0,27,7),('040.UPPM','Unidade Penal de Pium',1,0,33,4),('040.UPPML','Unidade Penal de Palmeirópolis',1,0,28,8),('040.UPPMW','Unidade Penal de Palmas',1,1,18,5),('040.UPPRN','Unidade Penal de Paranã',0,0,30,8),('040.UPPSO','Unidade Penal de Paraíso do Tocantins',1,1,29,4),('040.UPPTN','Unidade Penal de Porto Nacional',1,0,34,5),('040.UPPXE','Unidade Penal de Peixe',1,0,32,6),('040.UPTGA','Unidade Penal de Taguatinga',1,0,37,7),('040.UPTLA','Unidade Penal Feminina de Talismã',1,0,36,6),('040.UPTOC','Unidade Penal de Tocantinópolis',1,0,38,1),('040.UPXAM','Unidade Penal de Xambioá',1,0,40,2),('040.USMC','Unidade de Segurança Máxima do Cariri',1,1,43,6);
/*!40000 ALTER TABLE `namp_setor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_statusfuncional`
--

DROP TABLE IF EXISTS `namp_statusfuncional`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_statusfuncional` (
  `id_status_funcional` int(11) NOT NULL AUTO_INCREMENT,
  `nome_status` varchar(50) NOT NULL,
  `descricao_status` varchar(100) NOT NULL,
  PRIMARY KEY (`id_status_funcional`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_statusfuncional`
--

LOCK TABLES `namp_statusfuncional` WRITE;
/*!40000 ALTER TABLE `namp_statusfuncional` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_statusfuncional` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `namp_tipojornada`
--

DROP TABLE IF EXISTS `namp_tipojornada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `namp_tipojornada` (
  `id_tipo_jornada` int(11) NOT NULL AUTO_INCREMENT,
  `carga_horaria` int(10) unsigned NOT NULL CHECK (`carga_horaria` >= 0),
  `tipificacao` varchar(100) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  PRIMARY KEY (`id_tipo_jornada`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `namp_tipojornada`
--

LOCK TABLES `namp_tipojornada` WRITE;
/*!40000 ALTER TABLE `namp_tipojornada` DISABLE KEYS */;
/*!40000 ALTER TABLE `namp_tipojornada` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-24  2:00:49
